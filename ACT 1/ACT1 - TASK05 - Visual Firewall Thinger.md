# TASK 5 - Visual Firewall Thinger
Difficulty: ❄️

[Direct Link](https://visual-firewall.holidayhackchallenge.com/?&challenge=termVisfirewall)

## OBJECTIVE : ##
>Find Elgee in the big hotel for a firewall frolic and some techy fun.

## HINTS: ##
<details>
  <summary>Hints provided for Task 5</summary>
>-	This terminal has built-in hints!
</details>
 
#  

## PROCEDURE : ##
We are presented with a very nice and festive firewall GUI and we are told to configure the firewall with the following requirements:
>-  **Internet to DMZ:** Allow only HTTP and HTTPS traffic
>-  **DMZ to Internal:** Allow HTTP, HTTPS, and SSH traffic
>-  **Internal to DMZ:** Allow HTTP, HTTPS, and SSH traffic
>-  **Internal to Cloud:** Allow HTTP, HTTPS, SSH, and SMTP traffic
>-  **Internal to Workstations:** Allow all traffic types
>-  **Security Best Practice:** Block direct Internet to Internal access

|Element|Connection|Allowed|
|--|--|--|
|Internet|Connection to DMZ|HTTP, HTTPS|
|DMZ|Connection to Internal Network|HTTP,HTTPS,SSH|
|Internal Network|Connection to Cloud Services|HTTP, HTTPS, SSH, SMTP|
|Internal Network|Connection to Workstations|DNS, HTTP, HTTPS, SMB, SMTP, SSH|

<img width="1333" height="713" alt="image" src="https://github.com/user-attachments/assets/e46ae362-44a0-4382-8f1f-6dbf9c88d03d" />
<img width="1315" height="741" alt="image" src="https://github.com/user-attachments/assets/313311bd-99ed-4cf4-8c8e-bd15df3d4bf8" />

