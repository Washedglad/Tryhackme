# OWASP Top 10 (2021) — Notes & Summary

> Source: OWASP official, Cloudflare, Veracode, etc. 

---

## 🛡 What is OWASP Top 10?

The **Open Web Application Security Project (OWASP)** is a nonprofit focused on improving software security.
Their **Top 10** is an “awareness document” that highlights the most critical web application security risks. 

The list is updated every few years; the latest published version is from 2021. 

---

## 🧠 The 2021 Top 10 — Summary & Notes

Below are the ten categories, with a brief description, common exploit types, and mitigation/high-level defenses.

| # | Name | Description / What it means | Examples / Common Exploits | Mitigations & Best Practices |
|---|------|-----------------------------|-----------------------------|------------------------------|
| **A01** | **Broken Access Control** | Failure to properly enforce access restrictions, letting users access functionality or data they shouldn't | URL tampering (e.g. changing ID in URL), tampering with parameters, forced browsing, privilege escalation | Enforce authorization checks server-side, use “deny by default,” RBAC/ABAC, least privilege |
| **A02** | **Cryptographic Failures** | Misuse or absence of cryptography, e.g. weak encryption, improper key management, cleartext sensitive data | Storing passwords in plaintext, using weak ciphers, failing to validate TLS | Use strong algorithms (AES, RSA, etc.), TLS everywhere, secure key storage, rotate keys, avoid home-grown crypto |
| **A03** | **Injection** | Untrusted input is interpreted as code or commands by a parser/interpreter | SQL injection, LDAP injection, OS command injection, Cross-Site Scripting (XSS) (now under injection category) | Use parameterized queries / prepared statements, input validation/escaping, ORM frameworks, least privileges for DB accounts |
| **A04** | **Insecure Design** | Design-level flaws: missing threat modeling, insecure business logic, weak architecture decisions | E.g. trusting client side logic, insecure workflows, flawed authentication/authorization models | Adopt secure design patterns, threat modeling, use design review / security by design, apply “secure defaults” |
| **A05** | **Security Misconfiguration** | Default, incomplete, or dangerous configurations across stack (servers, frameworks, cloud) | Open ports, verbose error messages, default credentials, missing security headers, XML External Entity (XXE) | Harden configurations, disable unused features, patch stacks, remove default accounts, use automated config checks, disable XML external entities |
| **A06** | **Vulnerable and Outdated Components** | Using libraries, frameworks, or modules with known vulnerabilities | Outdated dependencies, unpatched plugins, exploitable versions of software | Maintain inventory of dependencies, use tools like software composition analysis (SCA), apply patches, update, limit component use |
| **A07** | **Identification & Authentication Failures** | Weak authentication and session management mechanisms that let attackers impersonate or forge credentials | Credential stuffing, session fixation, brute force, weak password recovery flows | Use multi-factor auth, secure session cookies (HttpOnly, Secure, SameSite), rate limiting, strong password policies, invalidating old sessions |
| **A08** | **Software & Data Integrity Failures** | Failures in verifying integrity of software or critical data | Untrusted deserialization, code injection in CI/CD pipelines, unsigned updates | Use integrity checks (signatures, HMAC), validate deserialized data, secure CI/CD pipelines, use trusted sources for code / libraries |
| **A09** | **Security Logging & Monitoring Failures** | Lack of sufficient logging, poor alerts, or inability to detect and respond to breaches | Undetected attacks, slow incident response, missing forensic data | Centralized logging, alerting on anomalies, retention of logs, integrate with SIEM, ensure monitoring covers key actions |
| **A10** | **Server-Side Request Forgery (SSRF)** | Server is tricked into making HTTP requests (or other protocol requests) to internal or unauthorized services | Attacker sends a URL parameter that causes server to fetch internal endpoints (e.g. `http://localhost/admin`) | Validate / sanitize URLs, whitelist allowed targets, block internal/external address spaces, use safe HTTP clients |

---

## ✅ Key Takeaways & Tips

- The Top 10 is **not exhaustive**—it focuses on the most common and critical risks.  
- Many vulnerabilities overlap (e.g. injection + misconfiguration).  
- Always apply **defense-in-depth**: multiple controls across network, app, database.  
- Use **automated scanning** (SAST, DAST, dependency scanning) during development.  
- **Shift security left**—incorporate threat modeling, secure design, and code review from the start.  
- Keep dependencies updated and reduce attack surface (disable unused components).  

---

## 📚 Further Resources & Reference

- OWASP Official: Top Ten project page   
- OWASP Cheat Sheet Series: mapping each Top 10 to cheat sheets 
- Veracode, Cloudflare blogs on each risk with actionable examples 

