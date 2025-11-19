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


