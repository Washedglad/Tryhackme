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
