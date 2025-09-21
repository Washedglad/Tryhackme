<img width="102" height="84" alt="image" src="https://github.com/user-attachments/assets/b9f68abf-80ef-420c-8d4f-85c325bc7b46" />

## TryHackMe Lab: Chocolate Factory

## Lab Overview
- **Difficulty:** Easy
- **Objectives:** A Charlie And The Chocolate Factory themed room, revisit Willy Wonka's chocolate factory!
- **Tools Used:** [Nmap, Gobuster,Hexdump,johntheripper,netcat]

---

- Checked out the targets webpage, which we're met with a login for a username/pass.
  <img width="1045" height="507" alt="image" src="https://github.com/user-attachments/assets/a5258e4e-0c6f-43b7-ab4b-c66c3672a90b" />

- Did test for SQLi and did not find anything.
- Performed dirb on the target and did not have any luck either, going to nmap now.
  
<img width="481" height="158" alt="image" src="https://github.com/user-attachments/assets/a49dc7f7-f0cf-425e-93da-142ed7956b31" />

- A simple Nmap scans gives us the following results, with a more complex scan we can probably reveal more though.
  
<img width="585" height="319" alt="image" src="https://github.com/user-attachments/assets/ce7361a2-faf5-4e70-95fe-56375bf83aa1" />

- After a very long waiting period, we have our results, and we are given an idea where to find the key.
  
<img width="608" height="77" alt="image" src="https://github.com/user-attachments/assets/2f29f873-e461-4f8d-ae40-e42c0cc8857e" />

- Downloaded the file, and noticed it was a program. Used hexdump to get the values needed and thus found the key.
  
<img width="686" height="206" alt="image" src="https://github.com/user-attachments/assets/90f35341-51c0-4083-abcc-cea7df077822" />

During of longer nmap scan we did see that ftp was open, and we can login via anonymous. There is a file one there, a .jpg.

<img width="638" height="248" alt="image" src="https://github.com/user-attachments/assets/f3449dbc-b67e-4c93-973c-8646d81ba4c9" />

Going to use the python script to try to find the password. 

<img width="359" height="75" alt="image" src="https://github.com/user-attachments/assets/71ec9445-9a70-475f-8a35-af6a03e92dfd" />

<img width="680" height="568" alt="image" src="https://github.com/user-attachments/assets/e1e9935f-51a8-4d35-bc30-2fa082ead733" />

The file is base64 encrypted, so let's try to decrypt. And password hash found. Next step is to use johntheripper to get the password.

<img width="961" height="84" alt="image" src="https://github.com/user-attachments/assets/b04e12d7-71c2-4172-8d92-77b19898d125" />

<img width="812" height="226" alt="image" src="https://github.com/user-attachments/assets/00be14cd-549b-446d-a7ad-7571f7436c02" />

- And we're in!

<img width="1055" height="514" alt="image" src="https://github.com/user-attachments/assets/e733cd46-5b2f-4bc7-8f80-dafcc160f06d" />

- We can also see we can run commands in this bar.

  <img width="588" height="108" alt="image" src="https://github.com/user-attachments/assets/d23931aa-025d-4c2d-a4e6-9912ad6a3d89" />

- Going to attempt a reverse shell now to make it easier to search.

- Using netcat to use a listener on our machine, and a shell command to send it back to us from the target.

<img width="370" height="101" alt="image" src="https://github.com/user-attachments/assets/96ab035c-06f6-430d-90bd-f5ea8fda3bf1" />

<img width="374" height="117" alt="image" src="https://github.com/user-attachments/assets/8280c05d-caa6-4cfa-8483-069235de5682" />

- We cannot open the flag with our current permissions, but there is a file called teleport that could help.
  
<img width="510" height="423" alt="image" src="https://github.com/user-attachments/assets/41cbf33a-f7e4-407c-a645-f6c7b0fdc192" />

- And what do you know, it's a private key!

<img width="273" height="49" alt="image" src="https://github.com/user-attachments/assets/47473f6e-d551-41f5-bd50-01b8ca13c029" />

- Going to copy and paste that to a txt file to use to attempt to login using the private key, and gain more privileges as charlie.

<img width="272" height="49" alt="image" src="https://github.com/user-attachments/assets/beaaf461-4ae5-4e5b-93ed-f541eaa7de69" />

- Tried to use it as normal, and ran into some issues, I need to change the permissions on my system it seems first.

<img width="631" height="245" alt="image" src="https://github.com/user-attachments/assets/ceccc32a-f3b4-45f8-80d9-9c95a596781b" />

- So here we go,
- {sudo chmod &lt;TARGET&gt;}

- chmod 400 file sets the file permissions so that only the owner can read the file.
Group and others get no permissions. The owner cannot write or execute.

<img width="421" height="70" alt="image" src="https://github.com/user-attachments/assets/c55beaac-9f4f-44d1-a3e9-0074862ed299" />

- And it worked, we are logged in as charlie, now let's get the flag.

<img width="424" height="107" alt="image" src="https://github.com/user-attachments/assets/f082bb2e-af68-4b17-a550-6eadc6c19b63" />

- And we got it

<img width="484" height="64" alt="image" src="https://github.com/user-attachments/assets/4d13af02-7eae-46b9-b371-995ea61e3581" />

- To get to root, let's see what we can do as charlie

<img width="778" height="128" alt="image" src="https://github.com/user-attachments/assets/153bd1db-c3d9-43f5-a24e-624c5d6f5db4" />

- We can use vi to get a shell possibly, https://gtfobins.github.io/gtfobins/vi/#shell

<img width="795" height="182" alt="image" src="https://github.com/user-attachments/assets/0c9722d6-c987-4d99-93fb-b4b2b66be8dc" />

- Got it, using: sudo vi -c ':!/bin/sh' /dev/null
<img width="647" height="102" alt="image" src="https://github.com/user-attachments/assets/9c55963d-2dcb-419d-93ac-366fad5c2ebd" />

- We don't have the traditional root.txt here, and it is asking for a key, we remember having a key we found awhile back, let's see what that does.

<img width="993" height="224" alt="image" src="https://github.com/user-attachments/assets/51ff3542-2b43-47e0-bf6f-78d4d78eab3e" />

- I copy and pasted that python script from the root we were at back to my system and I had to fix the code, there was a string literal I fixed, not sure if it was me or on purpose,
- but after that we were given the option to put a key in!
<img width="281" height="63" alt="image" src="https://github.com/user-attachments/assets/d124af94-d6c0-4a16-91ca-c276ae42e25f" />

- There was some trial and error, but eventually got it to work and was given the final flag.

<img width="711" height="496" alt="image" src="https://github.com/user-attachments/assets/f9f09dbe-4e5e-48c5-893c-985a2da773e5" />


  

