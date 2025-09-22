# THM Lab: Brooklyn Nine Nine
<img width="106" height="95" alt="image" src="https://github.com/user-attachments/assets/b8e0c0a7-1a2b-4248-8add-6089df3e5253" /><img width="67" height="38" alt="image" src="https://github.com/user-attachments/assets/b6a26e92-863a-460a-8d4a-ed62315f7d5a" />



## Lab Overview
- Difficulty: Easy
- Objectives: There are two main intended ways to root the box.
- Tools Used: [Nmap, Gobuster]

## Reconnaissance
- First thing we're gonna do is an <b>Nmap</b> scan of the target.
<img width="768" height="214" alt="image" src="https://github.com/user-attachments/assets/d7c25ec4-3ee2-464c-92ce-d049e069d276" />
- Comes back with 3 ports found open.


## Enumeration
- See port 21 open for ftp is interesting, and widens my eyes to looking into it a little more.<img width="275" height="20" alt="image" src="https://github.com/user-attachments/assets/b1453e4e-d3e2-4c2f-9d93-5a04a72b1f4e" />

- That is not going to be an option at the moment it seems, until we find a password to login... 
 <img width="298" height="99" alt="image" src="https://github.com/user-attachments/assets/12022b90-0d83-4062-917f-96b673259518" />
  However, with an attempt randomly with the usual "<b>password</b>" I was in.
  <img width="313" height="168" alt="image" src="https://github.com/user-attachments/assets/04eef017-82e9-45a1-9c50-9799fbb8fe6d" />

  - A quick look around using "ls -lh" we see there is a note we can get our hands onto.
    <img width="648" height="107" alt="image" src="https://github.com/user-attachments/assets/655ab173-560b-4e18-a09f-965465dd3223" />
<img width="631" height="99" alt="image" src="https://github.com/user-attachments/assets/8afc84c0-1d8b-4d21-bebd-9b1faef39149" />

- The note reads that "Jake" uses a weak password, as we already know by guessing the ftp password on the first try.
- We also now have two usernames, "Jake" and "Amy".
  <img width="885" height="109" alt="image" src="https://github.com/user-attachments/assets/46f293c0-676c-4b54-9177-ddb392c7c502" />

 - Knowing that jake is using a weak password, let's go ahead and jump into hydra for a quick find.
    <img width="936" height="307" alt="image" src="https://github.com/user-attachments/assets/dfaf8b87-7e0c-4a0c-a937-a5ab35513d31" />
- And we find <b>password: 987654321</b>

- Doing some looking around there isn't much in Jake's directory, we look at home and find 3 users, looking at "holt" we find our first flag.
  
  <img width="400" height="164" alt="image" src="https://github.com/user-attachments/assets/3aa19514-48cc-4a6d-a4c6-ac121d6454b9" />

- Once we log into ssh via jake's account information we find no files, so let's see what permissions we have as sudo. 
<img width="947" height="207" alt="image" src="https://github.com/user-attachments/assets/f89b77e1-969f-4636-9fc3-b4df9b83303d" />
We see that /less binary, so we can go to https://gtfobins.github.io/gtfobins
<img width="799" height="160" alt="image" src="https://github.com/user-attachments/assets/be003bce-9839-4e2b-ba76-c49d4e44fa1d" />

- After several tries, I managed to get it correct and was at root.
  <img width="551" height="82" alt="image" src="https://github.com/user-attachments/assets/55f773c5-2ec6-43e8-816e-28164f285cf9" />

- And we have our 2nd flag.
  <img width="474" height="143" alt="image" src="https://github.com/user-attachments/assets/ca9e3856-471e-474d-bbaa-cc1de3d1a793" />

Also was another way to get in and that was the use of steganography.

- I used this python script 
  
# Steg-Brute-Force Script

This Python script attempts to extract hidden data from a stego image using a wordlist.

```python
import subprocess

# Prompt for user input
stego_file = input("Enter the path to the stego image: ")
wordlist = input("Enter the path to the wordlist: ")
output_file = input("Enter the name for the extracted file (e.g., extracted.txt): ")

# Open the wordlist and try each password
with open(wordlist, "r") as f:
    for line in f:
        password = line.strip()
        try:
            result = subprocess.run(
                ["steghide", "extract", "-sf", stego_file, "-p", password, "-xf", output_file, "-f"],
                capture_output=True,
                text=True
            )
            # Check both stdout and stderr for success message
            if "wrote extracted data to" in result.stdout or "wrote extracted data to" in result.stderr:
                print(f"[+] Password found: {password}")
                print(f"[+] Data extracted to {output_file}")
                break
            else:
                print(f"[-] Tried: {password}")
        except Exception as e:
            print(f"Error: {e}")

```
- After doing that we were given the password, and in the output file we found the information for holt.
<img width="268" height="42" alt="image" src="https://github.com/user-attachments/assets/f4b366e7-99a3-4f9b-8aa9-b4d35de32984" />
<img width="223" height="112" alt="image" src="https://github.com/user-attachments/assets/3f9f1411-4287-4e22-85df-c790dff09284" />







