## ﻿Introduction

                                      

You were hired as a SOC Analyst for one of the biggest Juice Shops in the world and an attacker has made their way into your network. 

Your tasks are:

Figure out what techniques and tools the attacker used
What endpoints were vulnerable
What sensitive data was accessed and stolen from the environment
An IT team has sent you a zip file containing logs from the server. Download the attached file, type in "I am ready!" and get to work! There's no time to lose!
#

## What tools did the attacker use? (Order by the occurrence in the log)
    nmap, hydra, sqlmap, curl, feroxbuster
<img width="759" height="167" alt="image" src="https://github.com/user-attachments/assets/ca0236dd-05c3-4d2d-bc3a-8040502107b9" />
<img width="371" height="161" alt="image" src="https://github.com/user-attachments/assets/e9d04ec1-eb9c-46f9-b3ac-ec02f9e55240" />
<img width="797" height="175" alt="image" src="https://github.com/user-attachments/assets/7a479f19-9b21-430e-bd28-f116da025447" />

## What endpoint was vulnerable to a brute-force attack?
    /rest/user/login

<img width="707" height="38" alt="image" src="https://github.com/user-attachments/assets/48b5d767-4e01-4e34-8476-7ea032d07c10" />

## What endpoint was vulnerable to SQL injection?
     /rest/products/search
     
<img width="1178" height="141" alt="image" src="https://github.com/user-attachments/assets/2322647e-d8ee-4db5-8dfc-0ea673663d14" />

## What parameter was used for the SQL injection?
    q 
    
<img width="256" height="26" alt="image" src="https://github.com/user-attachments/assets/d3908dd6-60a7-4b85-a9bd-ab037109952b" />

## What endpoint did the attacker try to use to retrieve files? (Include the /)
      /ftp

<img width="629" height="38" alt="image" src="https://github.com/user-attachments/assets/b8a5aebb-eca1-4ec3-bf3a-8f190b62fd2a" />

# Stolen data

                                      

Analyze the provided log files.

Look carefully at:

The attacker's movement on the website
Response codes
Abnormal query strings



## What section of the website did the attacker use to scrape user email addresses?
    product reviews

##  Was their brute-force attack successful? If so, what is the timestamp of the successful login? (Yay/Nay, 11/Apr/2021:09:xx:xx +0000)
    Yay, 11/Apr/2021:09:16:31 +0000

<img width="776" height="490" alt="image" src="https://github.com/user-attachments/assets/fdedcbf2-567e-4e48-b75e-ac64c12f7029" />

## What user information was the attacker able to retrieve from the endpoint vulnerable to SQL injection?
    email, password
    
<img width="724" height="63" alt="image" src="https://github.com/user-attachments/assets/e671231a-5317-4581-8a75-d38f7daed4ca" />

## What files did they try to download from the vulnerable endpoint? (endpoint from the previous task, question #5)
    coupons_2013.md.bak, www-data.bak

<img width="331" height="115" alt="image" src="https://github.com/user-attachments/assets/84ee6d7b-e16c-400a-88bd-3f2b64055af3" />

## What service and account name were used to retrieve files from the previous question? (service, username)
      ftp, anonymous

<img width="662" height="211" alt="image" src="https://github.com/user-attachments/assets/a0b9543f-8037-4f7f-849a-9438828cf073" />

## What service and username were used to gain shell access to the server? (service, username)
      ssh, www-data

<img width="615" height="136" alt="image" src="https://github.com/user-attachments/assets/780a9273-c891-430b-8b6d-324b5bbc80b2" />










    












