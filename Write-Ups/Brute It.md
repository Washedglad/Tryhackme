# Brute It
<img width="112" height="104" alt="image" src="https://github.com/user-attachments/assets/9b937d96-3103-44ee-bcea-f45af8e8d104" />

In this box you will learn about:

- Brute-force

- Hash cracking

- Privilege escalation


# Recon

- Nmap scan of our target reveals: Port 22, 80 open

  <img width="592" height="314" alt="image" src="https://github.com/user-attachments/assets/d9cdfa8b-6284-4e69-8fd4-02e2ffc8c6ae" />


- Dirb reveals an /admin page on the target.

<img width="535" height="325" alt="image" src="https://github.com/user-attachments/assets/bfcbb33f-e609-4ea7-9235-794d8afe879f" />


 # Enumeration

 - Now that we have this login screen, we might be able to enumerate and find some user names.
 - After testing though it does not tell us if we have a correct password or not to determine if there is a real username there.

 <img width="775" height="566" alt="image" src="https://github.com/user-attachments/assets/4629aaeb-56da-4866-b778-3185819dd901" />

 - However some more digging in the source of the admin login page we find a little comment.

   <img width="780" height="582" alt="image" src="https://github.com/user-attachments/assets/7ae34152-dd33-4a41-acf4-fa66d9161fdb" />

 - So we know the username is "Admin" and there is possiby another person named "john".

 - Now we can throw that into Hydra to attempt to brute force the information
   
   ```bash
     hydra -l admin -P /usr/share/wordlists/rockyou.txt 10.201.106.51 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid" -V
   ```
 - We got our information for the hydra input here.
 
   <img width="1104" height="64" alt="image" src="https://github.com/user-attachments/assets/0e357004-e78c-4d74-b3a5-8fbe7836adfa" />

   <img width="335" height="137" alt="image" src="https://github.com/user-attachments/assets/3ec93bd0-c816-407e-845a-889edc03fe97" />


   - And here are the results 

    <img width="816" height="148" alt="image" src="https://github.com/user-attachments/assets/23f521ea-72f1-43b9-a775-7d43f34cfaaf" />

    
   <img width="926" height="637" alt="image" src="https://github.com/user-attachments/assets/9944fdd8-4325-43df-b760-efd019740cae" />

    - Once logged in we are given this, and looks to be a flag and a link to possibly an RSA private key.

  <img width="1283" height="477" alt="image" src="https://github.com/user-attachments/assets/c0d63d3a-ba85-4088-84c0-8ca4b8b5dc02" />

  - The key does look to be encrypted using AES I believe

    <img width="729" height="499" alt="image" src="https://github.com/user-attachments/assets/5f978976-8927-4dca-8b48-da6844324c67" />

- We are going to use wget to download the file from the target and convert it using ssh2john, and then use john to crack it.

  <img width="893" height="201" alt="image" src="https://github.com/user-attachments/assets/872a6f59-80d9-4f0c-a245-d98d368b4db2" />

  <img width="498" height="65" alt="image" src="https://github.com/user-attachments/assets/e093f61c-e9d7-4f66-bf0c-7d8720223f38" />

  <img width="787" height="240" alt="image" src="https://github.com/user-attachments/assets/e751e93b-a0ae-4b13-aa74-999498f1cb84" />

  - We can use this to ssh with john, make sure to give the correct permissions to the rsa file before doing so or ssh will not let you use the key.
 
    <img width="729" height="334" alt="image" src="https://github.com/user-attachments/assets/b8b1d88e-3e85-4da1-9600-eca8fed293af" />

  - And we got a flag in the first directory
 
    <img width="623" height="118" alt="image" src="https://github.com/user-attachments/assets/0f874ba9-9e8d-4af4-8f51-2b114fe73677" />


   ## Privilege Escalation

  - Now we must elevate to higher privs
  
    <img width="467" height="150" alt="image" src="https://github.com/user-attachments/assets/73ca833f-33a7-4c42-a2a9-bead34a9ce4f" />

 - We can run /bin/cat with no passwd it says.

 

 - Hopping over to GTFObins might help find something useful. 

 <img width="176" height="71" alt="image" src="https://github.com/user-attachments/assets/e03945a0-a7c3-44bf-a464-f7ea181b18b0" />

 - So knowing this we can possibly read a very important file that we shouldn't be able too.

 - Using
   ```bash
     LFILE=/etc/shadow
     cat "$LFILE"
   ```

   - And it worked! we got the passwords.
     
 <img width="808" height="492" alt="image" src="https://github.com/user-attachments/assets/6a277711-de52-49e8-ab43-66a0a892fbf4" />

 - We can take the root information and possibly figure out the login now.

 - Copy and paste this entire line into a file on my system
   
<img width="865" height="96" alt="image" src="https://github.com/user-attachments/assets/9ec67cc3-e2db-4a81-9d0a-10855598f7f8" />

- Used john to get the passphrase

 <img width="753" height="184" alt="image" src="https://github.com/user-attachments/assets/83f5f922-f74d-46e0-ad94-f1476f6cfdd6" />

- And using that information we were able to login as root on the target.

 <img width="356" height="81" alt="image" src="https://github.com/user-attachments/assets/842e9ab5-fe24-4d1d-a53f-2ad5b5314ee8" />

<img width="680" height="140" alt="image" src="https://github.com/user-attachments/assets/cb1a1b3e-106d-42a0-bef3-89972ee827f0" />

- Complete

  ## Lessons Learned

  - This lab had several brute force attempts we had to perform using john, as well as cracking hashes.
  - This was the first time I had to use "/usr/share/john/ssh2john.py" and it was a good experience using it.
  - I also learned the importance of using the right phrases for hydra as well, or you will not get the correct results the first time.
  - Overall fun lab, and good learning experience. 

 
 
 




  



  

