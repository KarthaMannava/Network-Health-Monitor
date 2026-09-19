# Simple script by URDev
# https://github.com/URDev4ever
# https://urdev.carrd.co

from datetime import datetime
import os
import subprocess
import re
import time

# ANSI codes
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
SAND = "\033[38;5;180m"
LILAC = "\033[38;5;146m"
BRICK = "\033[38;5;131m"

RESET = "\033[0m"

now = datetime.now()
now = now.strftime("%H:%M:%S")

count = 0

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def ping():
    if os.name == "nt":
        command = ["ping", "-n", "1", "-w", "10000", "8.8.8.8"]
    else:
        command = ["ping", "-c", "1", "-W", "10", "8.8.8.8"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:
        return None

    output = result.stdout
    match = re.search(r"time[=<]\s*([\d.]+)\s*ms", output)

    if match:
        return float(match.group(1))

    return None

clear()

count = 0
total = 0
min_ms = None
max_ms = None

print(f"{BLUE}┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━┓{RESET}")
while True:
    try:
        now = datetime.now()
        now = now.strftime("%H:%M:%S")

        ms = ping()

        if len(str(ms)) == 6:
            space = ""
        elif len(str(ms)) == 5:
            space = " "
        elif len(str(ms)) == 4:
            space = "  "
        elif len(str(ms)) == 3:
            space = "   "

        if ms is not None:
            count += 1
            total += ms
            avg = total / count

            if min_ms is None or ms < min_ms:
                min_ms = ms
            if max_ms is None or ms > max_ms:
                max_ms = ms

            print(f"{BLUE}┃ {CYAN}[{now}]{GREEN} [+] Connected {BLUE}┃{YELLOW}   {ms} ms {BLUE}{space}┃{MAGENTA}{count: ^11}{BLUE}┃  {LILAC}AVG: {avg:7.2f} ms {BLUE}┃  {SAND}MIN: {min_ms:5.2f} ms {BLUE}┃  {BRICK}MAX: {max_ms:8.2f} ms   {BLUE}┃{RESET}")
        else:
            print(f"{BLUE}┃ {CYAN}[{now}]{RED} [-]  TIMEOUT {BLUE} ┣━━━━━━━━━━━━━╋━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━╋━━━━━━━━━━━━━━━━━━━━━┫{RESET}")
        time.sleep(1)
    except(KeyboardInterrupt):
        print(f"{BLUE}                         ┃             ┃           ┃                  ┃                ┃                     ┃{RESET}")
        print(f"{BLUE}┗━━━━━━━━━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━┻━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━┻━━━━━━━━━━━━━━━━━━━━━┛{RESET}")
        break

