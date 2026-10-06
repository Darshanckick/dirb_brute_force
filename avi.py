# webrute.py — async web path brute-forcer with LIVE results
import asyncio
import os
import sys
import time
import argparse
from pathlib import Path

import aiohttp

from rich.console import Console, Group
from rich.table import Table
from rich.progress import (
    Progress, SpinnerColumn, BarColumn, TextColumn,
    MofNCompleteColumn, TimeElapsedColumn, TimeRemainingColumn,
)
from rich.panel import Panel
from rich.live import Live
from rich.text import Text
from rich.align import Align
from rich.box import ROUNDED, DOUBLE
from rich.columns import Columns

# ---------- UTF-8 for CMD ----------
if os.name == "nt":
    os.system("chcp 65001 > nul")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

console = Console()

STATUS_COLOR = {
    200: "bold green",  201: "bold green",  204: "green",
    301: "bold cyan",   302: "cyan",        307: "cyan",
    401: "bold yellow", 403: "bold red",    500: "bold magenta",
}
INTERESTING = {200, 201, 204, 301, 302, 307, 401, 403, 500}


# ---------- Async HTTP probe ----------
async def probe(session, url, timeout, follow):
    try:
        async with session.get(
            url,
            timeout=aiohttp.ClientTimeout(total=timeout),
            allow_redirects=follow,
            ssl=False,
        ) as r:
            body = await r.content.read(2048)
            return r.status, len(body), r.headers.get("Content-Type", "")
    except asyncio.TimeoutError:
        return None, 0, "timeout"
    except Exception:
        return None, 0, "error"


# ---------- Shared live state ----------
class ScanState:
    def __init__(self):
        self.hits = []              # list of (status, length, path, ctype)
        self.done = 0
        self.total = 0
        self.start = time.perf_counter()
        self.last_error = ""
        self.lock = asyncio.Lock()

    def add_hit(self, item):
        self.hits.append(item)

    def snapshot(self):
        return list(self.hits)

    @property
    def elapsed(self):
        return time.perf_counter() - self.start

    @property
    def rate(self):
        return self.done / self.elapsed if self.elapsed > 0 else 0


# ---------- Worker ----------
async def worker(name, queue, session, base, timeout, follow, state, out_file):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            return
        url = base.rstrip("/") + "/" + item.lstrip("/")
        status, length, ctype = await probe(session, url, timeout, follow)

        state.done += 1

        if status in INTERESTING:
            state.add_hit((status, length, item, ctype))
            # stream to file immediately
            try:
                out_file.write(f"{status}\t{length}\t{url}\n")
                out_file.flush()
            except Exception:
                pass

        queue.task_done()


# ---------- Live rendering ----------
def build_display(state, base, workers):
    # ----- Hits table (top) -----
    hits = state.snapshot()
    hits.sort(key=lambda r: (r[0], r[2]))

    hits_table = Table(
        box=ROUNDED,
        border_style="bright_magenta",
        header_style="bold bright_cyan",
        expand=True,
        title=f"[bold]🎯 Hits[/] [dim]({len(hits)} so far)[/]",
    )
    hits_table.add_column("#", justify="right", style="dim", width=5)
    hits_table.add_column("Status", justify="center", width=8)
    hits_table.add_column("Size", justify="right", style="dim", width=10)
    hits_table.add_column("Path", style="bold white", overflow="fold")
    hits_table.add_column("Type", style="dim cyan", width=18)

    # show newest 12 for readability
    for i, (status, length, path, ctype) in enumerate(hits[-12:], 1):
        color = STATUS_COLOR.get(status, "white")
        hits_table.add_row(
            str(i),
            f"[{color}]{status}[/]",
            f"{length:,}",
            f"{base.rstrip('/')}/{path.lstrip('/')}",
            (ctype.split(";")[0] or "-")[:18],
        )

    # ----- Stats panel (bottom) -----
    stats = Table.grid(expand=True)
    stats.add_column(justify="left")
    stats.add_column(justify="center")
    stats.add_column(justify="center")
    stats.add_column(justify="right")

    stats.add_row(
        f"[bold cyan]Target:[/] {base}",
        f"[bold green]Hits:[/] {len(hits)}",
        f"[bold yellow]Progress:[/] {state.done:,}/{state.total:,}",
        f"[bold magenta]Rate:[/] {state.rate:,.0f} req/s",
    )
    stats.add_row(
        f"[bold cyan]Workers:[/] {workers}",
        f"[dim]Elapsed: {state.elapsed:.1f}s[/]",
        f"[dim]Remaining: "
        f"{max(0,(state.total-state.done)/state.rate):.0f}s[/]"
        if state.rate else "[dim]Remaining: --[/]",
        "",
    )

    return Group(
        Panel(hits_table, border_style="bright_magenta", box=DOUBLE),
        Panel(stats, border_style="bright_cyan", box=ROUNDED),
    )


# ---------- Orchestrator ----------
async def run_bruteforce(base, wordlist, workers, timeout, follow,
                        extensions, filters, out_path):
    # ---- build word list ----
    words = []
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            w = line.strip()
            if not w or w.startswith("#"):
                continue
            words.append(w)
            for ext in extensions:
                words.append(f"{w}.{ext.lstrip('.')}")

    if not words:
        console.print("[red]Wordlist is empty[/]")
        return []

    state = ScanState()
    state.total = len(words)
    queue: asyncio.Queue = asyncio.Queue()

    # prep output file
    out_file = open(out_path, "w", encoding="utf-8")
    out_file.write(f"# WebRute results — {base} — {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    out_file.write("# status\tsize\turl\n")
    out_file.flush()

    connector = aiohttp.TCPConnector(
        limit=workers, limit_per_host=workers,
        ttl_dns_cache=300, ssl=False,
    )

    async with aiohttp.ClientSession(connector=connector) as session:
        # start workers
        worker_tasks = [
            asyncio.create_task(
                worker(i, queue, session, base, timeout, follow, state, out_file)
            )
            for i in range(workers)
        ]

        # feed queue
        for w in words:
            await queue.put(w)
        for _ in range(workers):
            await queue.put(None)

        # LIVE LOOP — redraw until all workers finish
        with Live(
            build_display(state, base, workers),
            console=console,
            refresh_per_second=10,
            screen=False,
            transient=False,
        ) as live:
            while True:
                live.update(build_display(state, base, workers))
                if all(t.done() for t in worker_tasks):
                    break
                await asyncio.sleep(0.1)
            # final paint
            live.update(build_display(state, base, workers))

        await asyncio.gather(*worker_tasks)

    out_file.close()

    results = state.snapshot()
    if filters:
        results = [r for r in results if r[0] in filters]
    return results


# ---------- Final summary ----------
def print_summary(results, base, elapsed, out_path):
    console.print()
    if not results:
        console.print(Panel(
            Align.center("[yellow]No interesting paths found.[/]"),
            border_style="yellow", box=ROUNDED,
        ))
    else:
        table = Table(
            title=f"[bold]✅ Scan complete — {len(results)} path(s) found[/]",
            box=ROUNDED, border_style="bright_green",
            header_style="bold bright_cyan",
        )
        table.add_column("#", justify="right", style="dim")
        table.add_column("Status", justify="center")
        table.add_column("Size", justify="right", style="dim")
        table.add_column("Path", style="bold white")
        table.add_column("Type", style="dim cyan")

        for i, (status, length, path, ctype) in enumerate(
            sorted(results, key=lambda r: (r[0], r[2])), 1
        ):
            color = STATUS_COLOR.get(status, "white")
            table.add_row(
                str(i),
                f"[{color}]{status}[/]",
                f"{length:,}",
                f"{base.rstrip('/')}/{path.lstrip('/')}",
                (ctype.split(";")[0] or "-")[:20],
            )
        console.print(table)

    console.print(Panel(
        Align.center(
            f"[bold]⏱  Elapsed:[/] {elapsed:.2f}s      "
            f"[bold]💾 Saved:[/] {Path(out_path).resolve()}"
        ),
        border_style="dim", box=ROUNDED,
    ))


# ---------- Entry ----------
def main():
    p = argparse.ArgumentParser(description="Async web path brute-forcer (live)")
    p.add_argument("-u", "--url", required=True)
    p.add_argument("-w", "--wordlist", required=True)
    p.add_argument("-t", "--threads", type=int, default=50)
    p.add_argument("--timeout", type=float, default=5.0)
    p.add_argument("--follow", action="store_true")
    p.add_argument("-x", "--extensions", default="")
    p.add_argument("-s", "--status", default="")
    p.add_argument("-o", "--out", default="webrute_results.txt")
    args = p.parse_args()

    extensions = [e.strip() for e in args.extensions.split(",") if e.strip()]
    filters = {int(s) for s in args.status.split(",") if s.strip().isdigit()}

    if not Path(args.wordlist).exists():
        console.print(f"[red]Wordlist not found: {args.wordlist}[/]")
        sys.exit(1)

    t0 = time.perf_counter()
    try:
        results = asyncio.run(run_bruteforce(
            args.url, args.wordlist, args.threads, args.timeout,
            args.follow, extensions, filters, args.out,
        ))
    except KeyboardInterrupt:
        console.print("\n[yellow]⚠ Interrupted — partial results were saved.[/]")
        return

    print_summary(results, args.url, time.perf_counter() - t0, args.out)


if __name__ == "__main__":
    main()
