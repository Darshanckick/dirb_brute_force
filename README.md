<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                          AVI // WEBRUTE                         -->
<!--               POWERED BY AVI  •  TERMINAL RECON SUITE           -->
<!-- ═══════════════════════════════════════════════════════════════ -->

<div align="center">

```
    ▄▄▄       ██▒   █▓ ██▓
   ▒████▄    ▓██░   █▒▓██▒
   ▒██  ▀█▄   ▓██  █▒░▒██▒
   ░██▄▄▄▄██   ▒██ █░░░██░
    ▓█   ▓██▒   ▒▀█░  ░██░
    ▒▒   ▓▒█░   ░ ▐░  ░▓
     ▒   ▒▒ ░   ░ ░░   ▒ ░
     ░   ▒        ░░   ▒ ░
         ░  ░      ░   ░
                  ░
```

# `> AVI :: WEBRUTE_`

### `[ ASYNC WEB PATH BRUTE-FORCER // LIVE TERMINAL RECON ]`

**`POWERED BY`** &nbsp; **`A V I`**

<br>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=800&color=00FF41&background=00000000&center=true&vCenter=true&width=700&lines=%5B+INITIALIZING+AVI+CORE+%5D;%5B+LOADING+ASYNC+ENGINE+%5D;%5B+BYPASSING+RATE+LIMITS+%5D;%5B+READY+TO+SCAN+%5D;%5B+POWERED+BY+AVI+%5D)](https://github.com/)

<br>

![Python](https://img.shields.io/badge/PYTHON-3.9%2B-000000?style=for-the-badge&logo=python&logoColor=00FF41&labelColor=000000)
![Platform](https://img.shields.io/badge/PLATFORM-WIN%20%7C%20LINUX%20%7C%20MAC%20%7C%20TERMUX-000000?style=for-the-badge&logo=linux&logoColor=00FF41&labelColor=000000)
![License](https://img.shields.io/badge/LICENSE-MIT-000000?style=for-the-badge&logo=opensourceinitiative&logoColor=00FF41&labelColor=000000)
![Status](https://img.shields.io/badge/STATUS-ONLINE-000000?style=for-the-badge&logo=statuspage&logoColor=00FF41&labelColor=000000)
![Made With](https://img.shields.io/badge/MADE%20WITH-AVI-000000?style=for-the-badge&logo=terminal&logoColor=00FF41&labelColor=000000)

<br>

```
┌──────────────────────────────────────────────────────────┐
│  [ SYSTEM ] :: AVI_CORE v1.0                             │
│  [ STATUS ] :: ████████████████████ 100% READY           │
│  [ ENGINE ] :: ASYNCIO // AIOHTTP // RICH                │
│  [ AUTHOR ] :: AVI                                       │
└──────────────────────────────────────────────────────────┘
```

</div>

---

<div align="center">

## `[!] WARNING :: AUTHORIZATION REQUIRED`

> ```
> ⚠  THIS TOOL IS FOR AUTHORIZED SECURITY TESTING ONLY
> ⚠  UNAUTHORIZED SCANNING IS ILLEGAL IN MOST JURISDICTIONS
> ⚠  YOU ARE RESPONSIBLE FOR YOUR OWN ACTIONS
> ```

</div>

---

## `> whoami`

```bash
$ cat /etc/avi/about.txt
```

> **WebRute** is a high-performance, fully asynchronous **web path & directory brute-forcer**
> built in pure Python and **powered by AVI**.
>
> Feed it a URL and a wordlist — it floods the target with concurrent requests and
> surfaces hidden files, admin panels, API routes, backup dumps, and misconfigurations.
>
> Results stream to a **live terminal dashboard** in real time — no waiting until the end.
> Every hit appears the instant it's discovered.

```diff
+ Single-file script :: avi.py
+ Zero config, zero daemon, zero database
+ Runs on Windows · Linux · macOS · Termux
+ Live UI @ 10 fps — animated hits table
+ Signal-grade async throughput (200–4000+ req/s)
```

---

## `> features --list`

<div align="center">

<table>
<tr>
<td width="50%" valign="top">

### `[+] PERFORMANCE`

```bash
► aiohttp async core
► connection pooling
► DNS cache (ttl 300s)
► 2 KB partial reads
► zero thread overhead
► 200–4000+ req/s
```

</td>
<td width="50%" valign="top">

### `[+] LIVE UI`

```bash
► real-time hits table
► progress + ETA
► live req/s counter
► status color codes
► 10 fps refresh
► zero flicker
```

</td>
</tr>
<tr>
<td width="50%" valign="top">

### `[+] SMART DISCOVERY`

```bash
► status filtering (-s)
► extension fuzz (-x)
► redirect follow (--follow)
► instant file flush
► Ctrl+C safe
```

</td>
<td width="50%" valign="top">

### `[+] CROSS-PLATFORM`

```bash
► Windows CMD / PowerShell
► Linux / macOS
► Termux (Android)
► no compiler required
► single file, pure Python
```

</td>
</tr>
</table>

</div>

---

## `> install`

<details open>
<summary><b>🪟 &nbsp; WINDOWS // POWERSHELL</b></summary>

<br>

```powershell
# 1. Install Python 3.9+ from python.org (check "Add Python to PATH")

# 2. cd into the project
cd path\to\project

# 3. Install dependencies
python -m pip install -r install.txt
```

> 💡 Use `python -m pip` — not bare `pip`.

</details>

<details>
<summary><b>📱 &nbsp; TERMUX // ANDROID</b></summary>

<br>

```bash
# 1. Install Python
pkg update && pkg upgrade -y
pkg install python python-pip -y

# 2. Grant storage access (once)
termux-setup-storage

# 3. cd into the project
cd ~/project

# 4. Install dependencies
pip install -r install.txt
```

**If `aiohttp` fails to compile:**

```bash
pkg install python-dev clang libffi-dev openssl-dev -y
pip install --upgrade pip wheel setuptools
pip install -r install.txt
```

</details>

<details>
<summary><b>🐧 &nbsp; LINUX &nbsp;//&nbsp; 🍎 &nbsp; MACOS</b></summary>

<br>

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
python3 -m pip install -r install.txt
```

</details>

---

## `> usage`

```bash
$ python avi.py -u <URL> -w <WORDLIST> [options]
```

<div align="center">

```diff
@@ BASIC SCAN @@
```

```bash
python avi.py -u http://127.0.0.1:8080 -w wordlist.txt
```

```diff
@@ AGGRESSIVE MODE @@
```

```bash
python avi.py -u http://localhost -w common.txt -t 200 -x php,html,bak -s 200,301,403
```

```diff
@@ REDIRECT HUNT + CUSTOM OUT @@
```

```bash
python avi.py -u http://10.0.0.5 -w raft-medium.txt --follow -o scan1.txt
```

```diff
@@ MOBILE / LOW-RESOURCE @@
```

```bash
python avi.py -u http://127.0.0.1:5000 -w common.txt -t 20 --timeout 8
```

</div>

---

## `> first_blood --lab`

**No target? Spin one up locally in 10 seconds.**

```diff
+ Terminal 1 — start a test server
```

```bash
python -m http.server 8080
```

```diff
+ Terminal 2 — attack it
```

```bash
python avi.py -u http://127.0.0.1:8080 -w wordlist.txt -t 20
```

---

## `> flags --help`

| FLAG | LONG | DESCRIPTION | DEFAULT |
|:----:|:-----|:------------|:-------:|
| `-u` | `--url` | **required** · target base URL | — |
| `-w` | `--wordlist` | **required** · wordlist path | — |
| `-t` | `--threads` | concurrent workers | `50` |
|  | `--timeout` | per-request timeout (s) | `5.0` |
|  | `--follow` | follow redirects | `off` |
| `-x` | `--extensions` | fuzz `php,html,bak,…` | none |
| `-s` | `--status` | only show these codes | all |
| `-o` | `--out` | output file path | `webrute_results.txt` |

---

## `> preview --live`

```
╔════════════════════ 🎯 Hits (4 so far) ════════════════════╗
║ #   Status   Size      Path                    Type        ║
║ 1   200      1,234     http://127.0.0.1/admin  text/html   ║
║ 2   301      0         http://127.0.0.1/api    -           ║
║ 3   403      512       http://127.0.0.1/.env   text/plain  ║
║ 4   200      8,910     http://127.0.0.1/login  text/html   ║
╚════════════════════════════════════════════════════════════╝
╭────────────────────────────────────────────────────────────╮
│ Target: http://127.0.0.1:8080    Hits: 4                       │
│ Progress: 1,204/4,700    Rate: 412 req/s    ETA: 8s           │
│ Workers: 50    Elapsed: 2.9s                                  │
╰────────────────────────────────────────────────────────────╯
```

---

## `> benchmark`

```diff
+ localhost · 4,700-word wordlist · Flask dev server
```

| WORKERS | TIME | THROUGHPUT |
|:-------:|:----:|:----------:|
| `10`  | `12.4 s` | `380 req/s`  |
| `50`  | `2.9 s`  | `1,620 req/s` |
| `100` | `1.8 s`  | `2,610 req/s` |
| `200` | `1.3 s`  | `3,610 req/s` |
| `400` | `1.1 s`  | `4,270 req/s` |

> *throughput varies with target latency, server concurrency, and rate limits*

### `[ recommended -t by target ]`

| TARGET | `-t` |
|--------|:----:|
| Flask / Django dev | `20–50` |
| Node.js / Express | `100–200` |
| Nginx + PHP-FPM | `200–400` |
| Go / Actix / FastAPI | `500+` |
| Termux (Android) | `15–30` |

---

## `> wordlists`

```bash
# recommended starter
curl -O https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt
```

From [SecLists](https://github.com/danielmiessler/SecLists):

```
Discovery/Web-Content/common.txt                    (~4.7k)   ← start here
Discovery/Web-Content/raft-small-words.txt          (~10k)
Discovery/Web-Content/directory-list-2.3-medium.txt (~220k)
```

Or roll your own:

```
admin
login
dashboard
api
config
.env
robots.txt
uploads
static
```

---

## `> architecture`

```
   ┌──────────────┐
   │   main()     │
   └──────┬───────┘
          │
          ▼
   ┌──────────────┐
   │ argparse     │
   └──────┬───────┘
          │
          ▼
   ┌──────────────────────────────┐
   │ run_bruteforce()             │
   │  ├─ load wordlist            │
   │  ├─ build asyncio.Queue      │
   │  ├─ spawn N async workers    │
   │  └─ live UI loop @ 10 fps    │
   └──────┬───────────────────────┘
          │
          ▼
   ┌──────────────────────────────┐
   │ worker() ─► probe()          │
   │              │               │
   │              ▼               │
   │        aiohttp.GET           │
   │              │               │
   │              ▼               │
   │        ScanState  ──► Rich   │
   └──────────────────────────────┘
```

**Design highlights:**

- 🔗 **Shared `ClientSession`** — TCP reuse across all workers
- 🧵 **`asyncio.Queue`** — natural backpressure, lock-free
- ⚡ **Single-threaded loop** — no GIL issues
- 💾 **Immediate flush** — survive Ctrl+C & process kill
- 📥 **Partial reads** — 2 KB cap, no wasted bandwidth

---

## `> tree`

```
project/
├── avi.py                  # main script
├── install.txt             # dependencies
├── README.md               # this file
├── LICENSE                 # MIT
├── wordlist.txt            # input (user-supplied)
└── webrute_results.txt     # auto-generated output
```

### output format `(TSV)`

```
# WebRute results — http://127.0.0.1:8080 — 2026-10-06 14:32:11
# status	size	url
200	1234	http://127.0.0.1:8080/admin
301	0	http://127.0.0.1:8080/api
403	512	http://127.0.0.1:8080/.env
```

Parse with `awk`:

```bash
awk '$1 == "200" { print $3 }' webrute_results.txt
```

---

## `> troubleshooting`

<details>
<summary><b>[!] ModuleNotFoundError: aiohttp</b></summary>

```bash
python -m pip install -r install.txt      # Windows
pip install -r install.txt                # Termux / Linux
```
</details>

<details>
<summary><b>[!] python / pip not found (Termux)</b></summary>

```bash
pkg install python python-pip -y
```
</details>

<details>
<summary><b>[!] aiohttp fails to compile on Termux</b></summary>

```bash
pkg install python-dev clang libffi-dev openssl-dev -y
pip install --upgrade pip wheel setuptools
pip install -r install.txt
```
</details>

<details>
<summary><b>[!] All requests return "timeout"</b></summary>

Server is overloaded — drop workers:

```bash
python avi.py -u ... -w ... -t 10 --timeout 10
```
</details>

<details>
<summary><b>[!] Garbled colors / boxes in CMD</b></summary>

Use **Windows Terminal**, not legacy CMD, for truecolor + emoji.
</details>

<details>
<summary><b>[!] "No interesting paths found"</b></summary>

SPA servers (React/Vue) return 200 for everything — try `-s 200` or change target.
</details>

---

## `> roadmap`

```diff
[ ] auto-404 calibration
[ ] recursive directory scanning
[ ] vhost & subdomain mode
[ ] query string & POST body fuzzing
[ ] proxy support (Burp / ZAP / SOCKS5)
[ ] resume from checkpoint
[ ] JSON / CSV output
[ ] rate limiting (--rate N)
[ ] custom headers & cookies
[ ] multi-target mode
```

---

## `> contribute`

```bash
git checkout -b feature/auto-404
git commit -am 'Add auto-404 calibration'
git push origin feature/auto-404
# then open a Pull Request
```

PEP-8 compliant · include a test or usage example for new features.

---

## `> legal`

```
╔══════════════════════════════════════════════════════════╗
║  AUTHORIZED SECURITY TESTING ONLY                        ║
║                                                          ║
║  ✅ your own servers            ❌ unauthorized scans    ║
║  ✅ bug bounty (in-scope)       ❌ denial of service     ║
║  ✅ CTF / lab environments      ❌ any illegal activity  ║
║  ✅ systems you own                                      ║
║                                                          ║
║  The author accepts NO liability for misuse.             ║
║  You are responsible for complying with all applicable   ║
║  laws (CFAA · CMA · IT Act · etc.) in your jurisdiction. ║
╚══════════════════════════════════════════════════════════╝
```

---

## `> license`

**MIT** — see [`LICENSE`](LICENSE)

---

## `> credits`

- [`aiohttp`](https://docs.aiohttp.org/) — async HTTP engine
- [`rich`](https://rich.readthedocs.io/) — terminal rendering
- [`SecLists`](https://github.com/danielmiessler/SecLists) — wordlists
- Inspired by `ffuf` · `gobuster` · `dirb`

---

<div align="center">

```
┌──────────────────────────────────────────────┐
│                                              │
│              P O W E R E D   B Y             │
│                                              │
│              ░█▀█░█░█░▀█▀                    │
│              ░█▀█░▀▄▀░░█░                    │
│              ░▀░▀░░▀░░░▀░                    │
│                                              │
│                   A  V  I                    │
│                                              │
└──────────────────────────────────────────────┘
```

### `[ AVI // TERMINAL RECON SUITE ]`

**`⭐ star the repo if AVI helped you`**

```
> connection closed by remote host_
```

</div>

<!-- ═══════════════════════════════════════════════════════════════ -->
<!--                    EOF :: POWERED BY AVI                        -->
<!-- ═══════════════════════════════════════════════════════════════ -->
