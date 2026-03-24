```markdown
# MalakHacks 🎀

A friendly ethical hacking toolkit for Termux, built with love for Malak.  
**Only for educational use – test only on systems you own or have permission to test.**

---

## What’s inside?

**10 categories**, each packed with useful tools:

1. **Network Scanning** – DNS, subdomains, port scan, ping sweep, OS detection, traceroute, WHOIS, etc.  
2. **Web Hacking** – SQLMap, Nikto, Gobuster, FFUF, WAF detection, tech detection.  
3. **Password Attacks** – Hash identifier, built‑in hash cracker, Hashcat, John, Hydra.  
4. **Exploitation** – Metasploit reference, SearchSploit, reverse shell generator, MSFVenom cheat sheet.  
5. **Wireless** – Aircrack-ng guide, Bluetooth scan.  
6. **Post Exploitation** – LinPEAS runner, privesc checklist.  
7. **Forensics** – Steghide, ExifTool, Binwalk, strings, file magic, hex dump.  
8. **Cryptography** – Base64, MD5, SHA1, SHA256, ROT13, Caesar, XOR.  
9. **OSINT** – GeoIP, Shodan (InternetDB), theHarvester, WHOIS, DNS records.  
10. **Tool Manager** – Check installed tools, install core packages.

- **No extra Python packages needed** – everything uses the standard library.
- **Graceful fallbacks** – if a tool like `nmap` is missing, the script will tell you what to install or use a built‑in alternative.

---

## Installation

1. Install **Termux** from [F‑Droid](https://f-droid.org/en/packages/com.termux/) (the Play Store version is outdated).
2. Open Termux and update packages:
   ```bash
   pkg update && pkg upgrade
   pkg install python
```

1. Save the script as malakhacks.py.
      (You can copy it with nano malakhacks.py and paste the code.)
2. Make it executable (optional):
   ```bash
   chmod +x malakhacks.py
   ```
3. Run it:
   ```bash
   python malakhacks.py
   ```

---

Getting external tools to work

Many tools are not in Termux’s default repositories anymore – they need to be installed manually from GitHub.
The script’s Tool Manager (category 10) shows which are present and gives hints, but here’s a full guide.

Tools that are still in the repos (easy):

```bash
pkg install nmap sqlmap nikto gobuster ffuf aircrack-ng traceroute whois dnsutils steghide binutils
```

Tools that need GitHub installs:

John the Ripper (john)

```bash
cd ~
git clone https://github.com/openwall/john.git
cd john/src
./configure && make -s clean && make
cd ../run
# Move it to a PATH location
cp john $PREFIX/bin/
```

Now john will work from anywhere.

Hydra (hydra)

```bash
cd ~
git clone https://github.com/vanhauser-thc/thc-hydra.git
cd thc-hydra
./configure
make
cp hydra $PREFIX/bin/
```

Hashcat (hashcat)

Hashcat is a binary release; download and extract:

```bash
cd ~
wget https://hashcat.net/files/hashcat-6.2.6.7z
pkg install p7zip
7z x hashcat-6.2.6.7z
cd hashcat-6.2.6
cp hashcat $PREFIX/bin/
```

theHarvester

```bash
cd ~
git clone https://github.com/laramies/theHarvester
cd theHarvester
pip install -r requirements/base.txt
# To run, use `python theHarvester.py` inside its folder, or symlink it:
ln -s ~/theHarvester/theHarvester.py $PREFIX/bin/theHarvester
```

wafw00f & binwalk (Python tools – pip works)

```bash
pip install wafw00f binwalk
```

shodan (for CLI)

```bash
pip install shodan
shodan init YOUR_API_KEY
```

metasploit (still installable)

```bash
pkg install unstable-repo
pkg install metasploit
```

---

How it works

· Python built‑ins do a lot: DNS lookups, subdomain brute‑force, hash identification, base64, etc.
· External tools are called via subprocess only if they exist. If they’re missing, you’ll see a helpful installation hint.
· The interface is simple: pick a category, then pick a tool. No complicated command line required.

---

Troubleshooting

“Tool not found” errors

· Use the Tool Manager to see what’s installed.
· Install missing tools with the commands above.

Wireless tools don’t work

· Wi‑Fi monitor mode requires a USB adapter and root. Most phones can’t do it with the internal Wi‑Fi chip.
· The script only shows the commands – you need the hardware and permissions to actually use them.

Permissions for some tools

· Some tools (like aircrack-ng) may need root. Termux can use sudo via termux-sudo (install with pkg install termux-sudo).

Python modules missing?

All modules used are from the Python standard library. No extra pip installs needed for the core script.

---

Disclaimer

This tool is for educational purposes only. Unauthorized access to computer systems is illegal. The author assumes no responsibility for misuse. Always obtain written permission before testing any system.

---

Credits

Made for Malak, by EL4Q.
All logos are cute and for decoration – no copyright infringement intended.

Enjoy, and stay curious. 🎀

```
