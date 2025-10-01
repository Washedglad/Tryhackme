# Introduction to Phishing

# Scenario objectives
- Monitor and analyze real-time alerts.
- Identify and document critical events such as suspicious emails and attachments.
- Create detailed case reports based on your observations to help your team understand the full scope of alerts and malicious activity.



##

- I am going to be testing out the TryHackMe SOC Simulator.

  <img width="2196" height="894" alt="image" src="https://github.com/user-attachments/assets/03afaa68-e55a-49a8-9254-876452ec166d" />

- We wait until we have alerts being populated to work.

- So we have some now, I am going to grab the High severity alert first and then work oldest to newest in the queue.

<img width="2200" height="335" alt="image" src="https://github.com/user-attachments/assets/fe174244-9d91-4083-b4af-468af0b619a3" />

# 8816 Access to Blacklisted External URL Blocked by Firewall

- This one appears to be due to the firewall blocking acceess to a URL

<img width="2100" height="487" alt="image" src="https://github.com/user-attachments/assets/6eb543a4-0660-432a-9e5a-cd8e8fd8efab" />

- Details:
   Action: blocked
   Application: web-browsing
   DestinationIP: 67.199.248.11
   DestinationPort: 80
   Protocol: TCP
   Rule: Blocked Websites
   SourceIP: 10.20.2.17
   SourcePort: 34257
   URL: http://bit.ly/3sHkX3da12340
   datasource: firewall
   timestamp: 10/01/2025 15:46:04.571

- We can also see the event in Splunk with this search 

<img width="2241" height="1042" alt="image" src="https://github.com/user-attachments/assets/cc602b2f-d133-4e05-81a8-48f7cd27be8a" />

- Using TryDetectThis, which is THM's Virustotal it appears we can search the IOCs for comfirmation of malicious history.

  <img width="1044" height="700" alt="image" src="https://github.com/user-attachments/assets/2f40a327-d0ec-4eb2-a150-70c31187db7e" />


<img width="964" height="662" alt="image" src="https://github.com/user-attachments/assets/cc6a841d-b268-4227-bcd1-0bf517db014b" />

- The URL is comfirmed. 

- I got to thinking and wanted to do a search on the host IP address to confirm no other activities, and didn't find anything other than the one malicious event, and found other normal user browsing. 

<img width="1483" height="1074" alt="image" src="https://github.com/user-attachments/assets/c552a9b6-4457-40e9-9933-01281bf685c9" />

# Closure

Time of activity:  10/01/2025 15:46:04.571

List of Affected Entities: 
- Details:
   Action: blocked
   Application: web-browsing
   DestinationIP: 67.199.248.11
   DestinationPort: 80
   Protocol: TCP
   Rule: Blocked Websites
   SourceIP: 10.20.2.17
   SourcePort: 34257
   URL: http://bit.ly/3sHkX3da12340
   datasource: firewall

Reason for Classifying as True Positive:  Malicious URL blocked by firewall. Alert was fired for internal IP 10.20.2.17 attempting to communicate outbound to http://bit.ly/3sHkX3da12340 hosted on 67.199.248.11, both deemed malicious by TryDetectThis. Logs show the event with the block by the firewall, other events show normal user activity not involving any other malicious IoCs, no signs of compromise found at this time.



List of Attack Indicators:   
URL: http://bit.ly/3sHkX3da12340
DestinationIP: 67.199.248.11



<img width="2142" height="1216" alt="image" src="https://github.com/user-attachments/assets/90c0f9a4-bd12-4964-be03-f5554949251e" />


# 8814 Inbound Email Containing Suspicious External Link

<img width="2175" height="512" alt="image" src="https://github.com/user-attachments/assets/a631b74c-9fe3-4597-9cd1-11855f1a9195" />

- Details:
   attachment: None
   content: Hi Ms. Garcia,\n\nWelcome to TheTryDaily!\n\nAs part of your onboarding, please complete your final profile setup so we can configure your access.\n\nKindly click the link below:\n\n<a href="https://hrconnex.thm/onboarding/15400654060/j.garcia">Set Up My Profile</a>.\n\nIf you have questions, please reach out to the HR Onboarding Team.
   datasource: email
   direction: inbound
   recipient: j.garcia@thetrydaily.thm
   sender: onboarding@hrconnex.thm
   subject: Action Required: Finalize Your Onboarding Profile
   timestamp: 10/01/2025 15:47:36.571

- Again searched in Splunk for related activity, and found just two events, but they seemed to be duplicates.

  <img width="2168" height="1122" alt="image" src="https://github.com/user-attachments/assets/8180df75-33e2-40fd-8af8-eca386336314" />

- Sender URL appears clean per OSINT.

  <img width="1047" height="627" alt="image" src="https://github.com/user-attachments/assets/a8853b33-847c-4086-b818-4a663f26b4ef" />

- URL is clean as well.

  <img width="878" height="563" alt="image" src="https://github.com/user-attachments/assets/a64b2e89-198b-4198-9fba-9cc36dbc52c0" />

# Closure

Time of Activity:   10/01/2025 15:47:36.571

List of Related Entities: 
 attachment: None
   content: Hi Ms. Garcia,\n\nWelcome to TheTryDaily!\n\nAs part of your onboarding, please complete your final profile setup so we can configure your access.\n\nKindly click the link below:\n\n<a href="https://hrconnex.thm/onboarding/15400654060/j.garcia">Set Up My Profile</a>.\n\nIf you have questions, please reach out to the HR Onboarding Team.
   datasource: email
   direction: inbound
   recipient: j.garcia@thetrydaily.thm
   sender: onboarding@hrconnex.thm
   subject: Action Required: Finalize Your Onboarding Profile
  Host: 10.10.49.239 

Reason for Classifying as False Positive:  Alert fired for an email containing a URL in the body. The URL is clean per OSINT, and the sender is clean as well. No malicious findings were found in the email, or related logs via Splunk. Host being targeted for email was 10.10.49.239, and the user was j.garcia. This is a benign activity, and appears to be related to legit onboarding for a new employee. 
  

  <img width="2100" height="769" alt="image" src="https://github.com/user-attachments/assets/f7fb923b-01bb-4bb5-88d1-e7c2ac72702b" />

# 8815 Inbound Email Containing Suspicious External Link

<img width="2196" height="509" alt="image" src="https://github.com/user-attachments/assets/41cb213c-e4f6-4e25-a7bd-b680738f7c7f" />

Details:
   attachment: None
   content: Dear Customer,\n\nWe were unable to deliver your package due to an incomplete address.\n\nPlease confirm your shipping information by clicking the link below:\n\nhttp://bit.ly/3sHkX3da12340\n\nIf we don’t hear from you within 48 hours, your package will be returned to sender.\n\nThank you,\n\nAmazon Delivery
   datasource: email
   direction: inbound
   recipient: h.harris@thetrydaily.thm
   sender: urgents@amazon.biz
   subject: Your Amazon Package Couldn’t Be Delivered – Action Required
   timestamp: 10/01/2025 15:44:50.571
  
   
   
- Did a search in Splunk involving the sender's address. Found just one event for this search. 
  
<img width="2100" height="864" alt="image" src="https://github.com/user-attachments/assets/232eacfa-b6e6-489d-b686-f97abb055349" />

- Performed OSINT searches, and urgents@amazon.biz came back clean.

  <img width="955" height="628" alt="image" src="https://github.com/user-attachments/assets/4ffbb6a7-2b82-41ea-9780-569823a57940" />

- http://bit.ly/3sHkX3da12340 however, came back as malicious.

  <img width="866" height="422" alt="image" src="https://github.com/user-attachments/assets/d94d94e5-5734-4b0a-aa41-0ba149db009c" />

- I did a search for this URL in Splunk, and found firewall logs related to this URL.

  <img width="1403" height="771" alt="image" src="https://github.com/user-attachments/assets/2e23efda-f687-4582-a19f-edcc881d6a95" />

- It appears that this URL was blocked, meaning the user most likely did click on the URL, but was saved/prevented by a firewall rule preventing access to the malicious link.
  
  Details:
  Action: blocked
   Application: web-browsing
   DestinationIP: 67.199.248.11
   DestinationPort: 80
   Protocol: TCP
   Rule: Blocked Websites
   SourceIP: 10.20.2.17
   SourcePort: 34257
   URL: http://bit.ly/3sHkX3da12340
   datasource: firewall
   timestamp: 10/01/2025 15:46:04.571
  
<img width="880" height="362" alt="image" src="https://github.com/user-attachments/assets/73a4dfbb-79e8-42a6-ab9f-c7c9e28a3445" />

<img width="722" height="299" alt="image" src="https://github.com/user-attachments/assets/ec04ed3c-968e-48e7-8ba7-f9f9da8a4f99" />

# Closure

Time of activity: 10/01/2025 15:44:50.571

List of Affected Entities: 
attachment: None
   content: Dear Customer,\n\nWe were unable to deliver your package due to an incomplete address.\n\nPlease confirm your shipping information by clicking the link below:\n\nhttp://bit.ly/3sHkX3da12340\n\nIf we don’t hear from you within 48 hours, your package will be returned to sender.\n\nThank you,\n\nAmazon Delivery
   datasource: email
   direction: inbound
   recipient: h.harris@thetrydaily.thm
   sender: urgents@amazon.biz
   subject: Your Amazon Package Couldn’t Be Delivered – Action Required

 Action: blocked
   Application: web-browsing
   DestinationIP: 67.199.248.11
   DestinationPort: 80
   Protocol: TCP
   Rule: Blocked Websites
   SourceIP: 10.20.2.17
   SourcePort: 34257
   URL: http://bit.ly/3sHkX3da12340
   datasource: firewall
   timestamp: 10/01/2025 15:46:04.571

Reason for Classifying as True Positive:  URL appears to be clicked from phishing email received by user "h.harris@thetrydaily.thm" from malicious sender "urgents@amazon.biz", containing the malicious URL "http://bit.ly/3sHkX3da12340". Only found two events in Splunk for this alert, and one is the firewall blocking access to the malicious URL for the user who clicked.  

Recommended Remediation Actions: Sender of the phishing email might need to updated/reported as malicious to properly flag this address as malicious, currently showing up as clean/non-malicious. Require user to change password, and take part in Cyber training involving phishing emails.

List of Attack Indicators: http://bit.ly/3sHkX3da12340, 67.199.248.11

<img width="2131" height="823" alt="image" src="https://github.com/user-attachments/assets/0178f606-12b5-4157-a6da-f859f284062c" />

# 8817 Inbound Email Containing Suspicious External Link


<img width="2165" height="488" alt="image" src="https://github.com/user-attachments/assets/0643daf5-271e-4559-86c5-647d3f0705d8" />

Details: 

   attachment: None
   content: Hi C.Allen,\n\nWe detected an unusual sign-in attempt on your Microsoft account.\n\nLocation: Lagos, Nigeria\n\nIP Address: 102.89.222.143\n\nDate: 2025-01-24 06:42\n\nIf this was not you, please secure your account immediately to avoid unauthorized access.\n\n<a href="https://m1crosoftsupport.co/login">Review Activity</a>\n\nThank you,\n\nMicrosoft Account Security Team
   datasource: email
   direction: inbound
   recipient: c.allen@thetrydaily.thm
   sender: no-reply@m1crosoftsupport.co
   subject: Unusual Sign-In Activity on Your Microsoft Account
   timestamp: 10/01/2025 15:47:08.571

   Action: allowed
   Application: web-browsing
   DestinationIP: 45.148.10.131
   DestinationPort: 443
   Protocol: TCP
   Rule: Allow-Internet
   SourceIP: 10.20.2.25
   SourcePort: 32653
   URL: https://m1crosoftsupport.co/login
   datasource: firewall
   timestamp: 10/01/2025 15:48:17.571


   
   <img width="1690" height="1054" alt="image" src="https://github.com/user-attachments/assets/21efed28-e2fc-499c-8774-71289346d2a8" />

   - Found two events in Splunk for this alert, when searching for "m1crosoftsupport.co". Wich is malicious given the name, and findings.
     
<img width="848" height="600" alt="image" src="https://github.com/user-attachments/assets/e206891c-f0fc-4a17-a2c1-572c197688d4" />

   - Destination IP is malicious as well. 45.148.10.131, as well as the URL in the body of the email. 
    
<img width="1068" height="550" alt="image" src="https://github.com/user-attachments/assets/464fafd1-afee-46e1-8913-eb4b9adcfc59" />
<img width="980" height="486" alt="image" src="https://github.com/user-attachments/assets/dd7916dd-e80f-4dcc-ac17-8326c4d1e9fb" />

# Closure

<img width="896" height="307" alt="image" src="https://github.com/user-attachments/assets/ef1fe454-fe4b-4883-bf6b-807461f92388" />

 Time of activity:  10/01/2025 15:47:08.571

List of Affected Entities: 
   attachment: None
   content: Hi C.Allen,\n\nWe detected an unusual sign-in attempt on your Microsoft account.\n\nLocation: Lagos, Nigeria\n\nIP Address: 102.89.222.143\n\nDate: 2025-01-24 06:42\n\nIf this was not you, please secure your account immediately to avoid unauthorized access.\n\n<a href="https://m1crosoftsupport.co/login">Review Activity</a>\n\nThank you,\n\nMicrosoft Account Security Team
   datasource: email
   direction: inbound
   recipient: c.allen@thetrydaily.thm
   sender: no-reply@m1crosoftsupport.co
   subject: Unusual Sign-In Activity on Your Microsoft Account
   timestamp: 10/01/2025 15:47:08.571

   Action: allowed
   Application: web-browsing
   DestinationIP: 45.148.10.131
   DestinationPort: 443
   Protocol: TCP
   Rule: Allow-Internet
   SourceIP: 10.20.2.25
   SourcePort: 32653
   URL: https://m1crosoftsupport.co/login
   datasource: firewall
   timestamp: 10/01/2025 15:48:17.571

Reason for Classifying as True Positive:  Alert fired for email containing URLs, and the URL "https://m1crosoftsupport.co/login"  is malicious per OSINT. The sender is malicious as well, "no-reply@m1crosoftsupport.co". The recipient "c.allen@thetrydaily.thm" appeared to click the URL, and was allowed per Splunk logs by the firewall to access the website with destination IP "45.148.10.131" which is malicious as well. The source IP involved was "10.20.2.25". No PUT requests were found in Splunk logs at this time to show user possibly submitted credentials. 

Reason for Escalating the Alert: URL clicked malicious URL in email, firewall allowed access to the malicious URL/IP. User logs need to be checked.

Recommended Remediation Actions: Review user logs, block URL/IP/Sender at the firewall with rules. Review logs for PUT requests for user putting credentials to the malicious login page possibly. Review user audit/sign-on logs, and require user password change. Require end user to take part in Cyber training, focused on Phishing emails.

List of Attack Indicators: 
URL: https://m1crosoftsupport.co/login
destination IP "45.148.10.131"
Sender: "no-reply@m1crosoftsupport.co"

<img width="2140" height="928" alt="image" src="https://github.com/user-attachments/assets/581659ec-41f4-4b82-9d4b-10903864d539" />


# Victory! Security breach prevented!

- I kept taking breaks to do little things for my wife/kid, so I did take a little bit to finish.

  <img width="1437" height="1128" alt="image" src="https://github.com/user-attachments/assets/ce2ccf89-524e-45eb-83e9-9cfb13cd9868" />

My final writeup got this review: 
<img width="720" height="772" alt="image" src="https://github.com/user-attachments/assets/c033b636-59f9-48d8-a857-5c81b7eb46a9" />




