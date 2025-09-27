## ColddBox: Easy
<img width="102" height="101" alt="image" src="https://github.com/user-attachments/assets/5cebb776-f278-48e7-9517-bdce1a8598a9" />

##

## Recon
- Upon looking at the site we know it's ran on wordpress, so we did run a scan on the target with nmap to find it's running an old version of WP as well.
  
<img width="802" height="337" alt="image" src="https://github.com/user-attachments/assets/656d630e-998b-4bd3-9eb1-1ac4233654ea" />

- We also ran wpscan to further scan our target for more information, and we found 4 users.

  <img width="560" height="327" alt="image" src="https://github.com/user-attachments/assets/1ad832ad-0749-47e1-a71a-b367aaee86cc" />


<img width="736" height="266" alt="image" src="https://github.com/user-attachments/assets/0207b24a-10eb-40e6-90a4-13e242c4352f" />

- Knowing these usernames we can attempt to brute force using wpscan also with the following command.
   ```bash
     wpscan --url http://10.201.97.131 --passwords /usr/share/wordlists/seclists/Passwords/Common-Credentials/10-million-password-list-top-10000.txt
   ```
<img width="555" height="47" alt="image" src="https://github.com/user-attachments/assets/7a2a0aee-86eb-4217-bdd6-f94f65eff4fe" />

- We found a password for a user, took a bit though.
<img width="1" height="1" alt="image" src="https://github.com/user-attachments/assets/e7ee3865-127d-4744-bd38-b944baed18b0" />

- Once logged in we are going to go to appearance >> themes, and go to 404 template.
      - We can replace this entire php code with this one from pentest monkeys. https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php

- Being sure to change these options 

<img width="395" height="218" alt="image" src="https://github.com/user-attachments/assets/2a938b9b-200e-4049-b444-1b32c1c44bfd" />

- Setup a nc listener on your machine.

  <img width="226" height="82" alt="image" src="https://github.com/user-attachments/assets/d653377c-ff0d-4aeb-b111-36498d0125c1" />

  - Now we need to make our 404 page popup for us, todo this let's go back to the target site, and click around.
  
<img width="1100" height="586" alt="image" src="https://github.com/user-attachments/assets/d8ec8409-b372-4373-aa2d-5d6139421217" />

- Now let's change the "p=1" value.

<img width="305" height="50" alt="image" src="https://github.com/user-attachments/assets/6c332eb2-3f87-4023-86e5-60325c90e96c" />

- And we got our reverse shell on the listener!
- It is unstable at the moment, we will need to get a proper terminal shell.
<img width="921" height="179" alt="image" src="https://github.com/user-attachments/assets/7ab0851d-a09e-474a-9af7-5abbe7aa1c2d" />

<img width="1128" height="223" alt="image" src="https://github.com/user-attachments/assets/6586b15d-c170-49dd-922e-1b6ad523f78e" />

```bash
  python3 -c ‘import pty;pty.spawn(“/bin/bash”)’
  export TERM=xterm
```

- After some errors I got it to work with, with Chatgpt helping fix the error..
  ```bash
    python3 -c "import pty; pty.spawn('/bin/bash')"
  ```
 

 <img width="884" height="94" alt="image" src="https://github.com/user-attachments/assets/8a6006be-2db8-4f9d-8dbb-4a5765308b68" />

- A little research with wordpress, we can find the config file in /var/www/html, and it contains information for further escalation.
  
  <img width="897" height="860" alt="image" src="https://github.com/user-attachments/assets/4a3aa7fa-fc97-4157-abb0-2a9381dae9be" />

  <img width="425" height="137" alt="image" src="https://github.com/user-attachments/assets/f99bbfe4-7fc8-4efe-aca1-58e923268c58" />

  - And like that we have the flag, 

<img width="543" height="96" alt="image" src="https://github.com/user-attachments/assets/458cc361-2505-4dd6-88dc-00643c11fa7e" />

- Now we need to get root.

<img width="825" height="235" alt="image" src="https://github.com/user-attachments/assets/5193bbd0-acb7-4ba6-b4ee-7aa4c8618e0d" />


- I was able to use chmod to get to the root flag, but there is also a way todo this using ftp.
```bash
  sudo chmod o+x /root       # allows traversal only (not listing) by others
```

<img width="463" height="117" alt="image" src="https://github.com/user-attachments/assets/75d84766-f08c-476a-93a2-62f42ad8dea7" />

- https://gtfobins.github.io/gtfobins/ftp/#shell
  
<img width="753" height="154" alt="image" src="https://github.com/user-attachments/assets/e8cca5a0-3391-41f5-8239-1c3f3a5f0795" />

<img width="597" height="300" alt="image" src="https://github.com/user-attachments/assets/9e93a11d-366e-4732-a8e8-dd5c4af64536" />

- And that's the other way, and that way you can ls inside root as well.

## End

 - Was a good room, and got a chance to use "wpscan" which I had not really go a chance to use much yet.
   

  


  
