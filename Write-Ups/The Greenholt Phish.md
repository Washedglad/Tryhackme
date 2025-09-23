# 📨 The Greenholt Phish

<img width="78" height="93" alt="image" src="https://github.com/user-attachments/assets/6513f45c-d8b4-422c-87dd-4c31b8e03333" />

A Sales Executive at Greenholt PLC received an email he didn’t expect from a customer.  
Key red flags:  
- The customer never uses generic greetings like *“Good day.”*  
- No money transfers were expected.  
- The email contained an unsolicited attachment.  
- The email was escalated to the SOC for investigation.  

---

## 📂 Questions & Answers

**Q:** What is the Transfer Reference Number listed in the email's Subject?  
**A:** `09674321`

---

**Q:** Who is the email from?  
**A:** `Mr. James Jackson`

---

**Q:** What is his email address?  
**A:** `info@mutawamarine.com`

---

**Q:** What email address will receive a reply to this email?  
**A:** `info.mutawamarine@mail.com`

---

**Q:** What is the Originating IP?  
**A:** `192.119.71.157`  

<img width="703" height="360" alt="image" src="https://github.com/user-attachments/assets/d4ce4162-a70f-456f-bb88-324560c3fb40" />

---

**Q:** Who is the owner of the Originating IP?  
**A:** `Hostwinds LLC`  

<img width="648" height="480" alt="image" src="https://github.com/user-attachments/assets/a8b84e56-c143-4d35-ad72-91d8ecf975e9" />

---

**Q:** What is the SPF record for the Return-Path domain?  
**A:** `v=spf1 include:spf.protection.outlook.com -all`  

<img width="793" height="153" alt="image" src="https://github.com/user-attachments/assets/2762de8a-f2f0-4f1c-8959-0979d3e989ea" />

---

**Q:** What is the DMARC record for the Return-Path domain?  
**A:** `v=DMARC1; p=quarantine; fo=1`  

<img width="635" height="267" alt="image" src="https://github.com/user-attachments/assets/664ca8bc-f1ca-4272-8e66-5d1ada1661b2" />

---

**Q:** What is the name of the attachment?  
**A:** `SWT_#09674321____PDF__.CAB`  

<img width="305" height="70" alt="image" src="https://github.com/user-attachments/assets/72b35863-2ad4-4a21-883d-93acb2a25879" />

---

**Q:** What is the SHA256 hash of the file attachment?  
**A:** `2e91c533615a9bb8929ac4bb76707b2444597ce063d84a4b33525e25074fff3f`  

<img width="737" height="95" alt="image" src="https://github.com/user-attachments/assets/99fe78f9-ff4b-456e-9ca4-94644de8e99a" />

---

**Q:** What is the attachment’s file size?  
**A:** `400.26 KB`  

<img width="1511" height="300" alt="image" src="https://github.com/user-attachments/assets/f36266ac-000f-4672-9ee4-4683b0e6f78b" />

---

**Q:** What is the actual file extension of the attachment?  
**A:** `RAR`  

<img width="657" height="496" alt="image" src="https://github.com/user-attachments/assets/b7e4a764-f18a-4ce5-81e7-9a84e5baccb5" />

---

## 🛑 Conclusion

Given the findings and the malicious nature of the attachment hash, this email is clearly **phishing**.  

Red flags include:  
- Suspicious greeting and poor grammar.  
- Mismatched `From` and `Reply-To` addresses.  
- SPF/DMARC issues.  
- Unsolicited attachment with misleading extension.  
- Malicious file hash confirmed.  

<img width="718" height="216" alt="image" src="https://github.com/user-attachments/assets/79ee5014-5de2-4fa7-bc9c-f7f4a0b94ae7" />

This email is **malicious** and should be blocked, reported, and investigated further.  

<img width="875" height="561" alt="image" src="https://github.com/user-attachments/assets/57d9fc6e-e032-4779-bcb9-0417f4802437" />
