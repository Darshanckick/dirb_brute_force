# ⚡ WebRute

An async web path brute-forcer with a live-updating terminal UI.
Fast, cross-platform, and works on Windows CMD, PowerShell, Linux, and Termux (Android).

![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20Linux%20%7C%20Termux-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📋 What It Does

WebRute sends HTTP requests to a target URL for every word in a wordlist
and reports any path that returns an "interesting" status code (200, 301, 403, etc.).

Results are shown **live** in a colored terminal table — you see each hit the instant it's found.

> ⚠️ **Authorization required.** Only run this against servers you own or have written
> permission to test. Unauthorized scanning is illegal in most jurisdictions.

---

## ✨ Features

- ⚡ **Async I/O** — hundreds of concurrent requests with `aiohttp`
- 🎨 **Live terminal UI** — Rich-powered, updates at 10 fps
- 🎯 **Smart filtering** — only shows interesting status codes
- 📝 **Streams to file** — hits written instantly (survives Ctrl+C)
- 🧩 **Extensions** — auto-try `.php`, `.html`, `.bak`, etc.
- 🖥️ **Cross-platform** — Windows CMD, PowerShell, Linux, Termux
- 🔋 **Mobile-tuned** — runs on Android via Termux

---

## 🚀 Installation

### Requirements

- Python **3.9 or newer**
- pip
- Internet access (for install)
- A wordlist file

---

### 🪟 Windows (CMD / PowerShell)

**1. Install Python**

Download from https://www.python.org/downloads/ — check **"Add Python to PATH"** during install.

Verify:
```powershell
python --version
```

**2. Open the project folder**

```powershell
cd C:\Users\ki1931ck\Desktop\Anvitha
```

**3. Install dependencies**

The dependencies are listed in `install.txt`:

```powershell
python -m pip install -r install.txt
```

> 💡 Always use `python -m pip`, **not** bare `pip`. This guarantees the
> packages install to the same Python that runs your script.

---

### 📱 Termux (Android)

**1. Install Python and pip**

```bash
pkg update && pkg upgrade -y
pkg install python python-pip -y
```

**2. Grant storage access (one-time)**

```bash
termux-setup-storage
```

**3. Move into your project**

```bash
cd ~/anu
```
(or `cd ~/storage/shared/Desktop/Anvitha` if the project is on phone storage)

**4. Install dependencies**

```bash
pip install -r install.txt
```

If `aiohttp` fails to compile, install the build tools first:

```bash
pkg install python-dev clang libffi-dev openssl-dev -y
pip install --upgrade pip wheel setuptools
pip install -r install.txt
```

---

## 🎯 Usage

### Basic scan

```powershell
python webrute.py -u http://127.0.0.1:8080 -w wordlist.txt
```

### Aggressive scan (200 workers, extensions, filtered)

```powershell
python webrute.py -u http://127.0.0.1:8080 -w wordlist.txt -t 200 -x php,html,bak -s 200,301,403
```

### Termux (mobile-tuned)

```bash
python webrute.py -u http://127.0.0.1:8080 -w common.txt -t 20 --timeout 8
```

---

## ⚙️ Options

| Flag | Long form | Description | Default |
|------|-----------|-------------|---------|
| `-u` | `--url` | **Required.** Target base URL | — |
| `-w` | `--wordlist` | **Required.** Path to wordlist file | — |
| `-t` | `--threads` | Number of concurrent workers | `50` |
|      | `--timeout` | Per-request timeout in seconds | `5.0` |
|      | `--follow`  | Follow HTTP redirects | off |
| `-x` | `--extensions` | Comma-separated extensions to append | none |
| `-s` | `--status` | Only show these status codes | all interesting |
| `-o` | `--out` | Output file path | `webrute_results.txt` |

---

## 📖 Example Output

```
╔════════════════════ 🎯 Hits (4 so far) ════════════════════╗
║ #   Status   Size      Path                    Type        ║
║ 1   200      1,234     http://127.0.0.1/admin  text/html   ║
║ 2   301      0         http://127.0.0.1/api    -           ║
║ 3   403      512       http://127.0.0.1/.env   text/plain  ║
║ 4   200      8,910     http://127.0.0.1/login  text/html   ║
╚════════════════════════════════════════════════════════════╝
╭────────────────────────────────────────────────────────────╮
│ Target: http://127.0.0.1:8080   Hits: 4   Progress: 1,204/4,700  Rate: 412 req/s │
│ Workers: 50   Elapsed: 2.9s    Remaining: 8s                                  │
╰────────────────────────────────────────────────────────────╯
```

---

## 🧪 First-Time Test (no real target needed)

Don't have a server to scan? Spin up a quick one with Python:

**Terminal 1 — start a test server:**
```powershell
cd C:\Users\ki1931ck\Desktop\Anvitha
python -m http.server 8080
```

**Terminal 2 — run the scanner:**
```powershell
cd C:\Users\ki1931ck\Desktop\Anvitha
python webrute.py -u http://127.0.0.1:8080 -w wordlist.txt -t 50
```

---

## 📚 Wordlists

The tool needs a wordlist — a text file with one path per line:

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

**Recommended sources:**

- [SecLists](https://github.com/danielmiessler/SecLists) — the industry standard
  - `Discovery/Web-Content/common.txt` (~4,700 paths) — **start here**
  - `Discovery/Web-Content/raft-small-words.txt` (~10k)
  - `Discovery/Web-Content/directory-list-2.3-medium.txt` (~220k)

**Quick download:**

```bash
# Windows PowerShell
curl -o common.txt https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt

# Termux
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt
```

---

## 🏎️ Performance Tips

| Target server | Recommended `-t` |
|---|---|
| Flask / Django dev server | 20–50 |
| Node.js / Express | 100–200 |
| Nginx + PHP-FPM | 200–400 |
| Go / Actix | 500+ |

**On Termux (Android):** keep `-t` between **15–30** and `--timeout 8`.

If everything returns `timeout`, you're hitting the server too hard — lower `-t`.

---

## 🗂️ Project Layout

```
Anvitha/
├── webrute.py             ← main script
├── install.txt            ← dependency list
├── README.md              ← this file
├── wordlist.txt           ← your wordlist
└── webrute_results.txt    ← generated on each run
```

---

## 🛠️ Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: aiohttp` | Run `python -m pip install -r install.txt` |
| `Could not open install file` | You're in the wrong folder — `cd` into the project |
| `python: command not found` (Termux) | `pkg install python -y` |
| `pip: command not found` (Termux) | `pkg install python-pip -y` |
| aiohttp compile errors on Termux | `pkg install python-dev clang libffi-dev openssl-dev -y` |
| `Connection refused` | No server running on that URL |
| All requests `timeout` | Lower `-t` (try `-t 10`) or raise `--timeout` to `10` |
| Garbled colors / boxes | Use **Windows Terminal** instead of old CMD |
| Emoji broken in CMD | Run `chcp 65001` first (script does this automatically) |
| Scan hangs forever | Server is saturated — `Ctrl+C`, lower `-t` |

---

## ⚖️ Legal Notice

This tool is provided for **educational** and **authorized security testing** purposes only.

- ✅ Test your own servers, localhost, lab VMs, CTF challenges
- ❌ Do **not** scan servers you don't own or lack written permission to test

The authors assume **no liability** for misuse. You are responsible for complying with all applicable laws.

---

## 📝 License

MIT — see `LICENSE` file.

---

## 🙏 Credits

Built with:
- [aiohttp](https://docs.aiohttp.org/) — async HTTP client
- [Rich](https://rich.readthedocs.io/) — beautiful terminal output

---

## 📬 Feedback

Found a bug or want a feature? Open an issue in the repo.

Happy (authorized) scanning! ⚡
