# TASK 4 - Visual Networking Thinger
Difficulty: ❄️

[Direct Link](https://visual-networking.holidayhackchallenge.com/?&challenge=termVisnetwork)

## OBJECTIVE : ##
>Skate over to Jared at the frozen pond for some network magic and learn the ropes by the hockey rink.

## HINTS: ##
<details>
  <summary>Hints provided for Task 4</summary>
>-	This terminal has built-in hints!
</details>
 
#  

## PROCEDURE : ##
This one is quite easy and consists of some general revision of basic networking concepts.

### Challenge 1: DNS Lookup ###
Our client will send a request for the corresponding IP address in the DNS A record for the domain visual-networking.holidayhackchallenge.com over port 53.  The server will respond with the corresponding IP address.

|Client|DNS Server|
|--|--|
|Port: 53| Response Value: 34.160.145.134|
|Domain Name: visual-networking.holidayhackchallenge.com|Response Type: A|
|Request Type: A||

### Challenge 2: TCP 3-Way Handshake ###
Anyone who has evere studied anythign to do with networking will know this one by heart.  The client sends a SYN flag to the server which responds with a SYN+ACK and the client acknowledges with an ACK.

|Client|Web Server|
|--|--|
|SYN||
||SYN ACK|
|ACK||

### Challenge 3: HTTP GET Request ###
Whenever a client needs to downlaod any content from a web server it sens a HTTP GET request to the server which will respond with the http response it has been programmed to serve.  In reality, we can choose any HTTP version and/or User-Agent we like here.

>- HTTP Verb: `GET`
>- HTTP Version: `HTTP/1.0`
>-  Host: `visual-networking.holidayhackchallenge.com`
>-  User-Agent: `GNOME`


### Challenge 4: TLS Handshake ###
This one is just slightly more challenging that the previous TLS handshake in that the client and the server also need to exchange certificates and keys.

|Client|Secure Web Server|
|--|--|
|Client Hello ->||
||<- Server Hello|
||<- Certificate|
|Client Key Exchange ->||
||<- Server Change Cipher Spec|
||<- Finished|

### Challenge 5: HTTPS GET Request ###
This one is identical to Challenge 3

>-  HTTP Verb: `GET`
>-  HTTP Version: `HTTP/1.0`
>-  Host: `visual-networking.holidayhackchallenge.com`
>-  User-Agent: `GNOME`
