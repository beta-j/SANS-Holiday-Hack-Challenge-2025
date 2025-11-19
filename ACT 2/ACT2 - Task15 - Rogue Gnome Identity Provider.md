# TASK 15 - Rogue Gnome Identity Provider
Difficulty: ❄️❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termRogueGnome)

## OBJECTIVE : ##
>Hike over to Paul in the park for a gnomey authentication puzzle adventure. What malicious firmware image are the gnomes downloading?


## HINTS: ##
<details>
  <summary>Hints provided for Task 15</summary>
  
>-	If you need to host any files for the attack, the server is running a webserver available locally at http://paulweb.neighborhood/ . The files for the site are stored in ~/www
>-  https://github.com/ticarpi/jwt_tool/wiki and https://portswigger.net/web-security/jwt have some great information on analyzing JWT's and performing JWT attacks.
>-  It looks like the JWT uses JWKS. Maybe a JWKS spoofing attack would work.

</details>
 
#

## PROCEDURE : ##

Paul Beckett tells us that he has access to Gnome's Diagnostic Interface at `gnome-48371.atnascorp` with the low-privelege account credentials `gnome:SittingOnAShelf`, and that we need to find a way to get admin access to see what the gnomes are up to.

