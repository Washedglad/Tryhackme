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

- look for double extensions to disguise malicious files like "image.jpg.php".
- Many of the indicators that analysts need to be on the lookout for in log analysis can be applied to network traffic analysis as well.

    Unusual HTTP Methods & Request Patterns
    Suspicious User-Agents & IP Addresses
    Encoded Payloads
    Malicious Code or Commands in Request Bodies
    Unexpected Protocols or Ports
    Unexpected Resource Usage
    Web Server Processes Spawning Command Line Tools

 
- What command would you use to locate .php files in the /var/www/ directory?
    - find /var/www/ -type f -name "*.php"
- Which Wireshark filter would you use to search specifically for PUT requests?
    - http.request.method == "PUT"
 
## Investigating For Signs of Compromise on a WordPress site.

- Suspicious activity has been reported, and your goal is to analyze the available logs to identify indicators of web shell usage. 

- Step one is SSH onto our maachine.

 <img width="298" height="36" alt="image" src="https://github.com/user-attachments/assets/97974f27-017c-42ad-a542-63e3ff30134c" />
<img width="741" height="119" alt="image" src="https://github.com/user-attachments/assets/69a5e97d-3d56-4e66-a9f9-e50cc736975f" />

- So far we are told we hjave been access to the Apache access logs.
    - I ran this command first
    ##
      cat /var/log/apache2/access.log | grep "200"

- Which IP address likely belongs to the attacker?
     <img width="1249" height="466" alt="image" src="https://github.com/user-attachments/assets/99e48617-60f6-4be4-a11c-17c6c69ac640" />
     ##
         203.0.113.66
- We can also see the attacker uploading the initial file "shadyshell.php" and then it looks like he also is trying to gain persistence by uploading another file from his own machine, as seen executing a "wget" cmd at the bottom.

- What is the first directory that the attacker successfully identifies?
      <img width="1155" height="168" alt="image" src="https://github.com/user-attachments/assets/5f356e17-fa64-4993-bd60-a32d2f8f88fc" />
      - /wordpress

- What is the name of the .php file the attacker uses to upload the web shell?
    ##
       upload_form.php
- What is the first command run by the attacker using the newly uploaded web shell?
   ##
      whoami
- After gaining access via the web shell, the attacker uses a command to download a second file onto the server. What is the name of this file?
  ##
      linpeas.sh

- The attacker has hidden a secret within the web shell.
Use cat to investigate the web shell code and find the flag. 
 <img width="654" height="284" alt="image" src="https://github.com/user-attachments/assets/478bb98a-cdf3-4721-9e27-0cf087402866" />









  






  






