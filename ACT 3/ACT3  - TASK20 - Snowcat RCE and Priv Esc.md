# TASK 20 - Snowcat RCE & Priv Esc
Difficulty: ❄️❄️❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termSnowcat)

## OBJECTIVE : ##
>Tom, in the hotel, found a wild Snowcat bug. Help him chase down the RCE! Recover and submit the API key not being used by snowcat.


## HINTS: ##
<details>
  <summary>Hints provided for Task 18</summary>
  
>-	Maybe we can inject commands into the calls to the temperature, humidity, and pressure monitoring services.
>-  If you're feeling adventurous, maybe you can become root to figure out more about the attacker's plans.
>-  Snowcat is closely related to Tomcat. Maybe the recent Tomcat Remote Code Execution vulnerability (CVE-2025-24813) will work here.


</details>

#

## PROCEDURE : ##

We are presented with a login screen and not much more information.  After hours and hours of looking through the code, GToogling and chatting with ChatGPT, I was able to find the following:
