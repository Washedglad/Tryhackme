## What is a Web Shell?
- We need to fully understand what a webshell is and why they're important in the cybersecurity industry.
    - A web shell is a malicious program uploaded to a target web server, enabling adversaries to execute commands remotely.
    - Web shells often serve as both an initial access method (via file upload vulnerabilities) and a persistence mechanism.
 
## Why they vulnerabilties occur
- They most likely occur due to an application failing to validate the file type, extension, content, or possibly destination.
- Imagine a website that allows you to upload photos, such as facebook or instagram. Those websites store your images, and if somehow
  the websites were not developed correctly, an attack may be allowed to upload a web shell like shell.php or mydog.aspx and gain cmd exe on the server.

  - Which MITRE ATT&CK Persistence sub-technique are web shells associated with?
    - T1505.003
<img width="1187" height="275" alt="image" src="https://github.com/user-attachments/assets/ac6bba3b-1e18-4d3b-87b8-04a909f848e7" />

  - What file extension is commonly used for web shells targeting Microsoft Exchange?
     - .aspx
<img width="369" height="258" alt="image" src="https://github.com/user-attachments/assets/78b937f5-e087-4617-905a-0cf0e474745f" />

## Anatomy of a Web Shell

- System execution functions in PHP, such as shell_exec(), exec(), system(), and passthru(), can be abused to gain command execution.

<img width="406" height="315" alt="image" src="https://github.com/user-attachments/assets/dc181ece-8f84-4995-a87b-61f328b35930" />

- Take this one for example, we have the whoami we can run to get information using this shell.
  <img width="726" height="189" alt="image" src="https://github.com/user-attachments/assets/d16bafb2-881b-4946-8ea6-a837890f0fb1" />
  <img width="131" height="94" alt="image" src="https://github.com/user-attachments/assets/5d1fc916-a428-4594-9b75-eb691d60ab65" />

 <img width="810" height="309" alt="image" src="https://github.com/user-attachments/assets/149d3298-ae63-4eb0-a1bb-91c749b3b2d2" />

 ## Web Server Logs And Detecting web shells

 -  Understanding the difference between normal and suspicious behavior can help uncover malicious activity.
    - Unusual HTTP Methods & Request Patterns

        - Repeated GET requests in quick succession could mean an attacker is probing for a valid place to upload a shell
          POST requests to valid upload locations following repeated GET requests
          Repeated GET or POST requests to the same file could indicate web shell interaction

   <img width="798" height="531" alt="image" src="https://github.com/user-attachments/assets/fca9ea35-ffdd-47f7-a28e-9f9eca527533" />

 - Let's look at this one as well, the user is trying to find a upload path potentially, and once he finds one he uploads it, you can tell between the codes, 404 and 200.
   <img width="795" height="385" alt="image" src="https://github.com/user-attachments/assets/2d6c860c-4cd4-426c-9662-d184b4e54054" />

## Network Traffic Analysis


To be continued... 

 


  






