## Red Team Recon
<img width="118" height="85" alt="image" src="https://github.com/user-attachments/assets/458093e3-102b-4e06-8b2e-33ca4ae505bd" />

# Intro
- In this lab/informational writeup I will be going over reconnaissance in cyber.
    - We should mention we have two forms of reconnaissance:
        - Active - requires interacting with the target to provoke it in order to observe its response.
        - Passive - can be carried out by watching passively
    - In this writeup we will be going over passive, or the ones that do not make noise or alert the person/target that you're learning about them.
 
# Built-in Tools we can use

  - Several tools we will touch on will be:
      - whois
      - dig, nslookup, host
      - traceroute / tracert
        
    # whois

      - WHOIS is a request and response protocol that does follow the RFC 3912 specs.
        The WHOIS server listens on port 43 for incoming requests.
        A WHOIS might give us information if we're lucky about the target, such as names, email addresses, postal addresses, and phone numbers, as well as technical.
        But at the end of the day, WHOIS is going to give us the authoritative name servers for the domain in question.


    # nslookup

      - nslookup 
          - One common tool found on Unix-like systems, Windows, and macOS is nslookup. In the following query, we can see how nslookup uses the default DNS server to get the A and AAAA records related to our domain.

       <img width="728" height="437" alt="image" src="https://github.com/user-attachments/assets/f70ab262-3bc6-4a23-b621-d3618c7f950e" />

    # dig

      - dig
          - Short for Domain Information Groper. 
          - provides a lot of query options and even allows you to specify a different DNS server to use.

     # host

      - host
          - host is another useful alternative for querying DNS servers for DNS records.
       
      # traceroute

       - traceroute
           - Like the name says, it will trace a route that the packets take to reach it's destination, from our system >> to target system.
           - It is also worth noting that some routers do not respond to traceroute, and as a result you will see a * to indicate their IP address instead.
        

## When was thmredteam.com created (registered)? (YYYY-MM-DD)
      2021-09-24
     
 <img width="701" height="280" alt="image" src="https://github.com/user-attachments/assets/625b2962-ab79-499a-b361-86f340c8bdba" />

## To how many IPv4 addresses does clinic.thmredteam.com resolve?
      2

<img width="584" height="317" alt="image" src="https://github.com/user-attachments/assets/cb153a00-9bf3-43c4-8025-14cbb8cc7c93" />

## To how many IPv6 addresses does clinic.thmredteam.com resolve?
      2

<img width="637" height="144" alt="image" src="https://github.com/user-attachments/assets/6842a673-7f27-4560-8de0-5ab871a5bc46" />


-------------------

# Advanced Searching

## 🕵️‍♂️ OSINT Cheat Sheet

### 1. Search Engine Modifiers

| Syntax | Purpose | Example |
|--------|---------|---------|
| `"phrase"` | Exact match | `"Red Team reconnaissance"` |
| `filetype:<ext>` | Specific file type | `OSINT filetype:pdf` |
| `site:<domain>` | Limit to a site | `salary site:blog.tryhackme.com` |
| `-site:<domain>` | Exclude a site | `pentest -site:example.com` |
| `intitle:<word>` | Term in page title | `walkthrough intitle:TryHackMe` |
| `inurl:<word>` | Term in URL | `challenge inurl:tryhackme` |

> **Pro tip:** Useful filetypes include `pdf, doc, docx, ppt, pptx, xls, xlsx`.

---

### 2. Search Engine Tips
- Syntax varies by engine; check official docs:  
  - Google Advanced Search  
  - DuckDuckGo Search Syntax  
  - Bing Advanced Search Options  
- Memorize common operators for faster recon.

---

### 3. Types of Confidential Info Sometimes Indexed
- Internal company documents  
- Spreadsheets with usernames, emails, passwords  
- Sensitive files and directories  
- Service version numbers (may indicate vulnerabilities)  
- Error messages revealing system info  

> **Reminder:** Only collect what’s in-scope and legal. OSINT should always stay ethical.
 
## 🌐 Social Media & Job Ads

### 1. Social Media Recon
Social media platforms are valuable for gathering information about a target. Users often **overshare personal and corporate details**. Key platforms to check:

- LinkedIn  
- Twitter  
- Facebook  
- Instagram  

**What to look for:**
- Names and roles of employees  
- Posts revealing technologies or vendors in use  
- Clues for password recovery questions  
- Ideas for building targeted wordlists  

**Example:**  
A network engineer posting about a recent Juniper certification may indicate that Juniper networking devices are used in their company.

---

### 2. Job Advertisements
Job postings can provide **insight into a company’s systems and infrastructure**.  

**What to look for:**
- Names and emails of HR contacts or hiring managers  
- Technical requirements revealing software, hardware, or certifications in use  
- Geographical hints about office locations  

**Tips:**
- Check both international and local job boards where the company posts ads  
- Review the company’s career page for openings  
- Use the [Wayback Machine](https://archive.org/web/) to view historical job postings, which may reveal past systems or tech stack

> **Reminder:** Only collect publicly available information and stay within the scope of engagement.

## How would you search using Google for xls indexed for http://clinic.thmredteam.com?
     filetype:xls site:clinic.thmredteam.com
## How would you search using Google for files with the word passwords for http://clinic.thmredteam.com?
    passwords site:clinic.thmredteam.com

-----------------

## 🌐 Reverse IP & Threat Intelligence Tools

### 1. ViewDNS.info — Reverse IP Lookup
- **Purpose:** Identify other domains hosted on the same IP address.
- Modern shared hosting means **multiple websites can share a single IP**.  
- Using reverse IP lookup on `cafe.thmredteam.com` shows other domains on the same server.  
- **Important:** Knowing an IP does **not** always point to a single website.

**Use Case:** Helps identify additional targets or footprint of an organization, but be careful to stay within scope.

---

### 2. Threat Intelligence Platform
- Provides multiple tests given a domain or IP:
  - WHOIS queries  
  - DNS records (A, AAAA, NS, MX, etc.)  
  - Malware checks  
- Presents results in a **readable, visual format**, often more convenient than raw `whois` or `dig` outputs.
- Example: Looking up `thmredteam.com` shows resolved NS records with IPv4/IPv6 addresses.  
- Can also show other domains sharing the same IP, similar to ViewDNS.info.

---

### 3. Specialized Search Engines

#### Censys
- Can query **IP addresses and domains** for detailed info.  
- Example: Looking up the IP for `cafe.thmredteam.com` reveals:
  - Open ports (80, 443, etc.)  
  - Hosting provider info (e.g., Cloudflare)  
- **Key Point:** Helps identify **whether an IP belongs to your target or a third-party provider**.  
- Avoid probing IPs outside of scope.

#### Shodan
- **Purpose:** Search for connected devices and servers by IP, domain, or service.  
- **Setup:**  
  ```bash
  shodan init API_KEY

## What is the shodan command to get your Internet-facing IP address?
    shodan myip


------------------

## 🛠 Recon-ng Framework for OSINT

Recon-ng is a framework that **automates OSINT collection** using modular components. 
It stores all collected data in a **workspace-specific database**, allowing easy pivoting and transformation of information.

---

### 1. Workflow Overview
1. **Create a Workspace**
```bash
workspaces create WORKSPACE_NAME
recon-ng -w WORKSPACE_NAME
```

## How do you start recon-ng with the workspace clinicredteam?
    recon-ng -w clinicredteam

##  How many modules with the name virustotal exist?
    2
    
<img width="775" height="254" alt="image" src="https://github.com/user-attachments/assets/c4fe773e-fa96-4e15-be54-bce506e6fd2b" />

## There is a single module under hosts-domains. What is its name?
    migrate_hosts 

 <img width="403" height="218" alt="image" src="https://github.com/user-attachments/assets/79030021-9219-4689-9470-79a5fbcdb314" />

## censys_email_address is a module that “retrieves email addresses from the TLS certificates for a company.” Who is the author?
    censys inc

  ----------

## 🧩 Maltego for OSINT

Maltego blends **mind-mapping with OSINT**, allowing you to visually explore relationships between entities like domains, companies, email addresses, or people.

---

### 1. Core Concepts
- **Entity:** A block on the Maltego graph representing a piece of information (e.g., DNS Name, Person, Email).  
- **Transform:** A piece of code or query that retrieves information related to an entity. Transforms can return **zero or more new entities**.  
- **Graph:** Visual representation of entities and the connections discovered via transforms.  

> ⚠️ Some transforms may actively query the target. For passive reconnaissance, understand the transform before using it.

---

### 2. Example Workflow
1. Start with a **DNS Name entity**, e.g., `cafe.thmredteam.com`.  
2. Right-click the entity → **Standard Transforms → Resolve to IP → To IP Address (DNS)**.  
   - Returns one or more IP addresses.  

3. Apply another transform to an IP address:  
   - **DNS from IP → To DNS Name from passive DNS (Robtex)**  
   - Populates the graph with new DNS names.  

4. Additional transforms can reveal:  
   - Geolocation of the IP  
   - Associated domains or hosts  
   - Ownership or network information  

> Each transform expands your graph and organizes the data visually, saving time compared to querying websites individually.

---

### 3. Integration with Other Tools
- Maltego can import results from **WHOIS, nslookup, and other sources**.  
- The visual layout helps track relationships between:  
  - Domains  
  - Hosts  
  - Email addresses  
  - People  

> Even when privacy protections hide some information (like email addresses in WHOIS), Maltego still organizes the data effectively.

---

### 4. Extending Maltego
- **Transforms** can be added to enhance functionality.  
- Categories include: data type, pricing, and target audience.  
- Maltego Community Edition (CE) offers **free transforms**, while some require a paid subscription.  
- Activation is required, even for Maltego CE.

---

### 5. Best Practices
- Start with a known piece of information and pivot using transforms.  
- Keep your graph organized to **track connections efficiently**.  
- Verify whether a transform is passive or active before use to avoid unintended scans.  
- Use Maltego as a complement to other OSINT tools like Recon-ng, Shodan, and Censys.

## What is the name of the transform that queries NIST’s National Vulnerability Database?
    NIST NVD

## What is the name of the project that offers a transform based on ATT&CK?
    MISP Project

 ## 📝 Summary

> “If you know the enemy and know yourself, you need not fear the result of a hundred battles. If you know yourself but not the enemy, for every victory gained you will also suffer a defeat. If you know neither the enemy nor yourself, you will succumb in every battle.” – Sun Tzu

In the cyber warfare era, understanding both our **red team capabilities** and the **target** is crucial. The terrain constantly evolves, and new methods for collecting information are always emerging.

We have explored:

- **Built-in tools**: `whois`, `dig`, and `tracert`  
- **Search engines** for passive reconnaissance  
- **OSINT frameworks**: Recon-ng and Maltego, which consolidate data from multiple sources  

The goal is to **expand knowledge about the target** and gather information for subsequent attack phases. Examples include:

- Discovered **hosts** can be scanned for vulnerabilities  
- **Contact information** and email addresses can support phishing campaigns  

In short, the more information we collect, the more we can **refine attacks** and increase the chances of success.

