# TASK 6 - Intro to Nmap
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termNmap)

## OBJECTIVE : ##
>Meet Eric in the hotel parking lot for Nmap know-how and scanning secrets. Help him connect to the wardriving rig on his motorcycle!

## HINTS: ##
<details>
  <summary>Hints provided for Task 6</summary>
  
>-	**Nmap Documentation:** Nmap is pretty straightforward to use for basic port scans. Check out its [documentation](https://nmap.org/book/man.html)!
>-  **Ncat Documentation:** You may also want to check out the [Ncat Guide](https://nmap.org/ncat/guide/).

</details>
 
#  

## PROCEDURE : ##
```
Welcome to the Intro to Nmap terminal!  We will learn some Nmap basics by running commands to answer the questions asked, which will guide us in finding and connecting to the wardriving rig's service. 
Run the command "hint" to receive a hint.
```

1) When run without any options, nmap performs a TCP port scan of the top 1000 ports. Run a default nmap scan of 127.0.12.25 and see which port is open.
```
elf@d62f7bc9fed1:~$ nmap 127.0.12.25
Starting Nmap 7.80 ( https://nmap.org ) at 2025-11-07 15:10 UTC
Nmap scan report for 127.0.12.25
Host is up (0.000070s latency).
Not shown: 999 closed ports
PORT     STATE SERVICE
8080/tcp open  http-proxy

Nmap done: 1 IP address (1 host up) scanned in 0.38 seconds
```


2) Sometimes the top 1000 ports are not enough. Run an nmap scan of all TCP ports on 127.0.12.25 and see which port is open.
```
elf@7edfd42fe376:~$ nmap 127.0.12.25 -p-
Starting Nmap 7.80 ( https://nmap.org ) at 2025-11-07 15:12 UTC
Nmap scan report for 127.0.12.25
Host is up (0.000050s latency).
Not shown: 65534 closed ports
PORT      STATE SERVICE
24601/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 1.68 seconds
```


3) Nmap can also scan a range of IP addresses.  Scan the range 127.0.12.20 - 127.0.12.28 and see which has a port open.
```
elf@6f54b12d97f7:~$ nmap 127.0.12.20-28 -p-
Starting Nmap 7.80 ( https://nmap.org ) at 2025-11-07 15:13 UTC
Nmap scan report for 127.0.12.20
Host is up (0.00029s latency).
All 65535 scanned ports on 127.0.12.20 are closed

Nmap scan report for 127.0.12.21
Host is up (0.000046s latency).
All 65535 scanned ports on 127.0.12.21 are closed

Nmap scan report for 127.0.12.22
Host is up (0.00020s latency).
All 65535 scanned ports on 127.0.12.22 are closed

Nmap scan report for 127.0.12.23
Host is up (0.00023s latency).
Not shown: 65534 closed ports
PORT     STATE SERVICE
8080/tcp open  http-proxy

Nmap scan report for 127.0.12.24
Host is up (0.00019s latency).
All 65535 scanned ports on 127.0.12.24 are closed

Nmap scan report for 127.0.12.25
Host is up (0.00018s latency).
All 65535 scanned ports on 127.0.12.25 are closed

Nmap scan report for 127.0.12.26
Host is up (0.00018s latency).
All 65535 scanned ports on 127.0.12.26 are closed

Nmap scan report for 127.0.12.27
Host is up (0.000083s latency).
All 65535 scanned ports on 127.0.12.27 are closed

Nmap scan report for 127.0.12.28
Host is up (0.00013s latency).
All 65535 scanned ports on 127.0.12.28 are closed

Nmap done: 9 IP addresses (9 hosts up) scanned in 16.08 seconds
```

4) Nmap has a version detection engine, to help determine what services are running on a given port. What service is running on 127.0.12.25 TCP port 8080?
```
elf@6f54b12d97f7:~$ nmap 127.0.12.25 -p8080 -sV
Starting Nmap 7.80 ( https://nmap.org ) at 2025-11-07 15:15 UTC
Nmap scan report for 127.0.12.25
Host is up (0.000086s latency).

PORT     STATE SERVICE VERSION
8080/tcp open  http    SimpleHTTPServer 0.6 (Python 3.10.12)

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.74 seconds
```

5) Sometimes you just want to interact with a port, which is a perfect job for Ncat!  Use the ncat tool to connect to TCP port 24601 on 127.0.12.25 and view the banner returned.
```
elf@6f54b12d97f7:~$ nc 127.0.12.25 24601
Welcome to the WarDriver 9000!
```

Congratulations, you finished the Intro to Nmap and found the wardriving rig's service!
