<h1 align="center">📡 Ping Monitor CLI</h1>
<p align="center">
  🇺🇸 <b>English</b> |
  🇪🇸 <a href="README_ES.md">Español</a>
</p>
<h3 align="center">Simple real-time network connectivity monitor written in Python.</h3>

Sends one ping per second to `8.8.8.8` and displays:

* Latency (ms)
* Packet timeout detection
* Running average
* Minimum latency
* Maximum latency
* Total successful pings
* Timestamp per request

Designed for quick terminal-based diagnostics on Windows, Linux, or WSL.

---

## ✨ Features

* Cross-platform (Windows / Linux)
* Clean terminal UI
* ANSI colored output
* Automatic timeout detection
* Rolling statistics:

  * `AVG`
  * `MIN`
  * `MAX`
  * Packet count
* 1-second interval monitoring

---

## 🖥️ Example Output

<img width="902" height="508" alt="image" src="https://github.com/user-attachments/assets/323193df-8ac2-4b76-8f5d-346b73f96481" />


---

## 🧠 How It Works

* Uses `subprocess.run()` to execute the system `ping` command.
* Automatically selects:

  * `-n 1 -w 10000` on Windows
  * `-c 1 -W 10` on Linux
* Extracts latency using regex:

  ```
  time=8.32 ms
  ```
* Maintains live statistics in memory.

Think of it like a mini network heartbeat monitor running in your terminal.

---

## 📦 Requirements

* Python 3.8+
* System `ping` command available in PATH

No external dependencies required.

---

## 🚀 Usage

Clone (`git clone https://github.com/URDev4ever/Ping-Monitor.git`) or download the script, then:

```bash
python ping_monitor.py
```
>or `cd Ping-Monitor` first if cloned

Stop with:

```
CTRL + C
```

---

## 🔧 Customization

If you want to change the target:

```python
command = ["ping", "-c", "1", "-W", "10", "8.8.8.8"]
```

Replace `8.8.8.8` with:

* Your router (e.g. `192.168.0.1`)
* Cloudflare (`1.1.1.1`)
* A specific host you want to monitor

---

## 📊 Metrics Explained

| Metric | Meaning                     |
| ------ | --------------------------- |
| ms     | Current ping latency        |
| AVG    | Average latency since start |
| MIN    | Lowest recorded latency     |
| MAX    | Highest recorded latency    |
| Count  | Successful ping responses   |

---

## 🛠 Use Cases

* Monitoring unstable Wi-Fi
* Checking packet drops
* Measuring latency fluctuations
* Debugging WSL networking
* Lightweight alternative to tools like `mtr`

---

## ⚠️ Notes

* This tool was _ONLY_ tested on **Kali Linux (WSL)**, if there are any bugs with other distributions please let me know.
* This does **not** calculate packet loss percentage.
* It depends on the system’s `ping` binary.
* ANSI colors may not display correctly in some older Windows terminals.

---
Made with <3 by URDev.
