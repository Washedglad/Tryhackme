# Introduction to Phishing

## Scenario Objectives
- Monitor and analyze real-time alerts
- Identify and document critical events such as suspicious emails and attachments
- Create detailed case reports based on observations to help the team understand the full scope of alerts and malicious activity

---

## Getting Started

I tested the TryHackMe SOC Simulator and waited for alerts to populate.

![SOC Simulator Dashboard](https://github.com/user-attachments/assets/03afaa68-e55a-49a8-9254-876452ec166d)

Once alerts appeared, I prioritized the High severity alert first, then worked through the queue from oldest to newest.

![Alert Queue](https://github.com/user-attachments/assets/fe174244-9d91-4083-b4af-468af0b619a3)

---

## Alert 8816: Access to Blacklisted External URL Blocked by Firewall

This alert was triggered due to the firewall blocking access to a malicious URL.

![Alert 8816 Details](https://github.com/user-attachments/assets/6eb543a4-0660-432a-9e5a-cd8e8fd8efab)

### Event Details
- **Action:** blocked
- **Application:** web-browsing
- **Destination IP:** 67.199.248.11
- **Destination Port:** 80
- **Protocol:** TCP
- **Rule:** Blocked Websites
- **Source IP:** 10.20.2.17
- **Source Port:** 34257
- **URL:** http://bit.ly/3sHkX3da12340
- **Data Source:** firewall
- **Timestamp:** 10/01/2025 15:46:04.571

### Investigation

The event was verified in Splunk:

![Splunk Search Results](https://github.com/user-attachments/assets/cc602b2f-d133-4e05-81a8-48f7cd27be8a)

Using TryDetectThis (THM's version of VirusTotal), I confirmed the malicious nature of the IOCs:

![TryDetectThis URL Analysis](https://github.com/user-attachments/assets/2f40a327-d0ec-4eb2-a150-70c31187db7e)

![URL Confirmation](https://github.com/user-attachments/assets/cc6a841d-b268-4227-bcd1-0bf517db014b)

I performed an additional search on the host IP address to confirm no other suspicious activities. The search revealed only the one malicious event, with other logs showing normal user browsing behavior.

![Host IP Investigation](https://github.com/user-attachments/assets/c552a9b6-4457-40e9-9933-01281bf685c9)

### Closure

**Time of Activity:** 10/01/2025 15:46:04.571

**List of Affected Entities:**
- Action: blocked
- Application: web-browsing
- Destination IP: 67.199.248.11
- Destination Port: 80
- Protocol: TCP
- Rule: Blocked Websites
- Source IP: 10.20.2.17
- Source Port: 34257
- URL: http://bit.ly/3sHkX3da12340
- Data Source: firewall

**Reason for Classifying as True Positive:**  
Malicious URL blocked by firewall. Alert was fired for internal IP 10.20.2.17 attempting to communicate outbound to http://bit.ly/3sHkX3da12340 hosted on 67.199.248.11, both deemed malicious by TryDetectThis. Logs show the event with the block by the firewall. Other events show normal user activity not involving any other malicious IoCs. No signs of compromise found at this time.

**List of Attack Indicators:**
- URL: http://bit.ly/3sHkX3da12340
- Destination IP: 67.199.248.11

![Case Closure](https://github.com/user-attachments/assets/90c0f9a4-bd12-4964-be03-f5554949251e)

---

## Alert 8814: Inbound Email Containing Suspicious External Link

![Alert 8814 Details](https://github.com/user-attachments/assets/a631b74c-9fe3-4597-9cd1-11855f1a9195)

### Event Details
- **Attachment:** None
- **Content:** Hi Ms. Garcia,\n\nWelcome to TheTryDaily!\n\nAs part of your onboarding, please complete your final profile setup so we can configure your access.\n\nKindly click the link below:\n\n<a href="https://hrconnex.thm/onboarding/15400654060/j.garcia">Set Up My Profile</a>.\n\nIf you have questions, please reach out to the HR Onboarding Team.
- **Data Source:** email
- **Direction:** inbound
- **Recipient:** j.garcia@thetrydaily.thm
- **Sender:** onboarding@hrconnex.thm
- **Subject:** Action Required: Finalize Your Onboarding Profile
- **Timestamp:** 10/01/2025 15:47:36.571

### Investigation

Searched in Splunk for related activity and found two events that appeared to be duplicates:

![Splunk Search Results](https://github.com/user-attachments/assets/8180df75-33e2-40fd-8af8-eca386336314)

OSINT checks revealed the sender URL was clean:

![Sender URL Check](https://github.com/user-attachments/assets/a8853b33-847c-4086-b818-4a663f26b4ef)

The embedded URL was also clean:

![URL Check](https://github.com/user-attachments/assets/a64b2e89-198b-4198-9fba-9cc36dbc52c0)

### Closure

**Time of Activity:** 10/01/2025 15:47:36.571

**List of Related Entities:**
- Attachment: None
- Content: Hi Ms. Garcia,\n\nWelcome to TheTryDaily!\n\nAs part of your onboarding, please complete your final profile setup so we can configure your access.\n\nKindly click the link below:\n\n<a href="https://hrconnex.thm/onboarding/15400654060/j.garcia">Set Up My Profile</a>.\n\nIf you have questions, please reach out to the HR Onboarding Team.
- Data Source: email
- Direction: inbound
- Recipient: j.garcia@thetrydaily.thm
- Sender: onboarding@hrconnex.thm
- Subject: Action Required: Finalize Your Onboarding Profile
- Host: 10.10.49.239

**Reason for Classifying as False Positive:**  
Alert fired for an email containing a URL in the body. The URL is clean per OSINT, and the sender is clean as well. No malicious findings were found in the email or related logs via Splunk. Host being targeted for email was 10.10.49.239, and the user was j.garcia. This is benign activity and appears to be related to legitimate onboarding for a new employee.

![Case Closure](https://github.com/user-attachments/assets/f7fb923b-01bb-4bb5-88d1-e7c2ac72702b)

---

## Alert 8815: Inbound Email Containing Suspicious External Link

![Alert 8815 Details](https://github.com/user-attachments/assets/41cb213c-e4f6-4e25-a7bd-b680738f7c7f)

### Event Details
- **Attachment:** None
- **Content:** Dear Customer,\n\nWe were unable to deliver your package due to an incomplete address.\n\nPlease confirm your shipping information by clicking the link below:\n\nhttp://bit.ly/3sHkX3da12340\n\nIf we don't hear from you within 48 hours, your package will be returned to sender.\n\nThank you,\n\nAmazon Delivery
- **Data Source:** email
- **Direction:** inbound
- **Recipient:** h.harris@thetrydaily.thm
- **Sender:** urgents@amazon.biz
- **Subject:** Your Amazon Package Couldn't Be Delivered – Action Required
- **Timestamp:** 10/01/2025 15:44:50.571

### Investigation

Splunk search for the sender's address found only one event:

![Splunk Search Results](https://github.com/user-attachments/assets/232eacfa-b6e6-489d-b686-f97abb055349)

OSINT checks showed urgents@amazon.biz came back clean:

![Sender Check](https://github.com/user-attachments/assets/4ffbb6a7-2b82-41ea-9780-569823a57940)

However, the URL http://bit.ly/3sHkX3da12340 was confirmed as malicious:

![URL Check](https://github.com/user-attachments/assets/d94d94e5-5734-4b0a-aa41-0ba149db009c)

A Splunk search for this URL revealed firewall logs showing the URL was blocked:

![Firewall Logs](https://github.com/user-attachments/assets/2e23efda-f687-4582-a19f-edcc881d6a95)

This indicates the user likely clicked on the URL but was protected by a firewall rule that prevented access to the malicious link.

**Firewall Event Details:**
- Action: blocked
- Application: web-browsing
- Destination IP: 67.199.248.11
- Destination Port: 80
- Protocol: TCP
- Rule: Blocked Websites
- Source IP: 10.20.2.17
- Source Port: 34257
- URL: http://bit.ly/3sHkX3da12340
- Data Source: firewall
- Timestamp: 10/01/2025 15:46:04.571

![Additional Evidence 1](https://github.com/user-attachments/assets/73a4dfbb-79e8-42a6-ab9f-c7c9e28a3445)

![Additional Evidence 2](https://github.com/user-attachments/assets/ec04ed3c-968e-48e7-8ba7-f9f9da8a4f99)

### Closure

**Time of Activity:** 10/01/2025 15:44:50.571

**List of Affected Entities:**
- Attachment: None
- Content: Dear Customer,\n\nWe were unable to deliver your package due to an incomplete address.\n\nPlease confirm your shipping information by clicking the link below:\n\nhttp://bit.ly/3sHkX3da12340\n\nIf we don't hear from you within 48 hours, your package will be returned to sender.\n\nThank you,\n\nAmazon Delivery
- Data Source: email
- Direction: inbound
- Recipient: h.harris@thetrydaily.thm
- Sender: urgents@amazon.biz
- Subject: Your Amazon Package Couldn't Be Delivered – Action Required

**Firewall Block Event:**
- Action: blocked
- Application: web-browsing
- Destination IP: 67.199.248.11
- Destination Port: 80
- Protocol: TCP
- Rule: Blocked Websites
- Source IP: 10.20.2.17
- Source Port: 34257
- URL: http://bit.ly/3sHkX3da12340
- Data Source: firewall
- Timestamp: 10/01/2025 15:46:04.571

**Reason for Classifying as True Positive:**  
URL appears to have been clicked from phishing email received by user h.harris@thetrydaily.thm from malicious sender urgents@amazon.biz, containing the malicious URL http://bit.ly/3sHkX3da12340. Only found two events in Splunk for this alert, one being the firewall blocking access to the malicious URL for the user who clicked.

**Recommended Remediation Actions:**  
Sender of the phishing email might need to be updated/reported as malicious to properly flag this address. Currently showing up as clean/non-malicious. Require user to change password and participate in cyber security training focused on phishing emails.

**List of Attack Indicators:**
- URL: http://bit.ly/3sHkX3da12340
- Destination IP: 67.199.248.11

![Case Closure](https://github.com/user-attachments/assets/0178f606-12b5-4157-a6da-f859f284062c)

---

## Alert 8817: Inbound Email Containing Suspicious External Link

![Alert 8817 Details](https://github.com/user-attachments/assets/0643daf5-271e-4559-86c5-647d3f0705d8)

### Event Details

**Email Event:**
- **Attachment:** None
- **Content:** Hi C.Allen,\n\nWe detected an unusual sign-in attempt on your Microsoft account.\n\nLocation: Lagos, Nigeria\n\nIP Address: 102.89.222.143\n\nDate: 2025-01-24 06:42\n\nIf this was not you, please secure your account immediately to avoid unauthorized access.\n\n<a href="https://m1crosoftsupport.co/login">Review Activity</a>\n\nThank you,\n\nMicrosoft Account Security Team
- **Data Source:** email
- **Direction:** inbound
- **Recipient:** c.allen@thetrydaily.thm
- **Sender:** no-reply@m1crosoftsupport.co
- **Subject:** Unusual Sign-In Activity on Your Microsoft Account
- **Timestamp:** 10/01/2025 15:47:08.571

**Firewall Event:**
- **Action:** allowed
- **Application:** web-browsing
- **Destination IP:** 45.148.10.131
- **Destination Port:** 443
- **Protocol:** TCP
- **Rule:** Allow-Internet
- **Source IP:** 10.20.2.25
- **Source Port:** 32653
- **URL:** https://m1crosoftsupport.co/login
- **Data Source:** firewall
- **Timestamp:** 10/01/2025 15:48:17.571

### Investigation

Found two events in Splunk when searching for "m1crosoftsupport.co", which is malicious given the typosquatted domain name:

![Splunk Search Results](https://github.com/user-attachments/assets/21efed28-e2fc-499c-8774-71289346d2a8)

![Domain Analysis](https://github.com/user-attachments/assets/e206891c-f0fc-4a17-a2c1-572c197688d4)

The destination IP 45.148.10.131 was confirmed as malicious:

![IP Analysis](https://github.com/user-attachments/assets/464fafd1-afee-46e1-8913-eb4b9adcfc59)

The URL in the body of the email was also confirmed as malicious:

![URL Analysis](https://github.com/user-attachments/assets/dd7916dd-e80f-4dcc-ac17-8326c4d1e9fb)

### Closure

![Case Closure Header](https://github.com/user-attachments/assets/ef1fe454-fe4b-4883-bf6b-807461f92388)

**Time of Activity:** 10/01/2025 15:47:08.571

**List of Affected Entities:**

**Email Event:**
- Attachment: None
- Content: Hi C.Allen,\n\nWe detected an unusual sign-in attempt on your Microsoft account.\n\nLocation: Lagos, Nigeria\n\nIP Address: 102.89.222.143\n\nDate: 2025-01-24 06:42\n\nIf this was not you, please secure your account immediately to avoid unauthorized access.\n\n<a href="https://m1crosoftsupport.co/login">Review Activity</a>\n\nThank you,\n\nMicrosoft Account Security Team
- Data Source: email
- Direction: inbound
- Recipient: c.allen@thetrydaily.thm
- Sender: no-reply@m1crosoftsupport.co
- Subject: Unusual Sign-In Activity on Your Microsoft Account
- Timestamp: 10/01/2025 15:47:08.571

**Firewall Event:**
- Action: allowed
- Application: web-browsing
- Destination IP: 45.148.10.131
- Destination Port: 443
- Protocol: TCP
- Rule: Allow-Internet
- Source IP: 10.20.2.25
- Source Port: 32653
- URL: https://m1crosoftsupport.co/login
- Data Source: firewall
- Timestamp: 10/01/2025 15:48:17.571

**Reason for Classifying as True Positive:**  
Alert fired for email containing URLs. The URL https://m1crosoftsupport.co/login is malicious per OSINT. The sender no-reply@m1crosoftsupport.co is malicious as well. The recipient c.allen@thetrydaily.thm clicked the URL and was allowed access by the firewall to the website with destination IP 45.148.10.131, which is also malicious. The source IP involved was 10.20.2.25. No PUT requests were found in Splunk logs at this time to show user possibly submitted credentials.

**Reason for Escalating the Alert:**  
User clicked malicious URL in email, firewall allowed access to the malicious URL/IP. User logs need to be checked.

**Recommended Remediation Actions:**
- Review user logs
- Block URL/IP/Sender at the firewall with rules
- Review logs for PUT requests indicating user may have submitted credentials to the malicious login page
- Review user audit/sign-on logs
- Require user password change
- Require end user to participate in cyber security training focused on phishing emails

**List of Attack Indicators:**
- URL: https://m1crosoftsupport.co/login
- Destination IP: 45.148.10.131
- Sender: no-reply@m1crosoftsupport.co

![Case Closure](https://github.com/user-attachments/assets/581659ec-41f4-4b82-9d4b-10903864d539)

---

## Victory! Security Breach Prevented!

I took breaks throughout the analysis to attend to family matters, so the exercise took a bit longer to complete.

![Completion Screen](https://github.com/user-attachments/assets/ce2ccf89-524e-45eb-83e9-9cfb13cd9868)

### Final Review

My final writeup received the following feedback:

![Final Review](https://github.com/user-attachments/assets/c033b636-59f9-48d8-a857-5c81b7eb46a9)

