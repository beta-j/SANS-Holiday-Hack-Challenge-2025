# TASK 1 - It's All About Defang #
Difficulty: ❄️

[Direct Link](https://its-all-about-defang.holidayhackchallenge.com/?&challenge=termDefang)

## OBJECTIVE : ##
>Find Ed Skoudis upstairs in City Hall and help him troubleshoot a clever phishing tool in his cozy office.

#  

## HINTS: ##
<details>
  <summary>Hints provided for Task 1</summary>

>-	**Extract IOCs** Remember, the new Phishing Threat Analysis Station (PTAS) is still under construction. Even though the regex patterns are provided, they haven't been fine tuned. Some of the matches may need to be manually removed.
  
>-	**Defang All the Thingz** The PTAS does a pretty good job at defanging, however, the feature we are still working on is one that defangs ALL scenarios. For now, you will need to write a custom sed command combining all defang options.


</details>

#  

## PROCEDURE : ##
Here are the regex patterns I used:
Domains:  `[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+`

IP Addresses: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`

URLS: `https://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)+(:[0-9]+)?(/[^\s]*)?`

Email Addresses: `\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b`

Make sure to remove any domains and email addresses related to dosisneighborhood.corp as these are not malicious.


Finally use the following sed to fully defang all of the IoCs: `s/\./[.]/g; s/@/[@]/g; s/http/hxxp/g; s/:\//[://]/g`

<img width="832" height="862" alt="image" src="https://github.com/user-attachments/assets/2ec041eb-3172-4718-8958-cc19db78c88d" />
