# TASK 12 - Mail Detective
Difficulty: ❄️❄️

[Direct Link](https://its-idorable.holidayhackchallenge.com/receipt/i9j0k1l2)

## OBJECTIVE : ##
>Help Mo in City Hall solve a curly email caper and crack the IMAP case. What is the URL of the pastebin service the gnomes are using?


## HINTS: ##
<details>
  <summary>Hints provided for Task 12</summary>
  
>-	**Did You Say Curl?** If I heard this correctly...our sneaky security gurus found a way to interact with the IMAP server using Curl! Yes...the CLI HTTP tool! Here are some helpful docs I found [https://everything.curl.dev/usingcurl/reademail.html](https://everything.curl.dev/usingcurl/reademail.html)

</details>
 
#  

## PROCEDURE : ##


```
=======================================================================
🎄 Mail Detective: Curly IMAP Investigation 🎄
=======================================================================

⚠️  ALERT! Those gnomes have been sending JavaScript-enabled emails
to everyone in the neighborhood, and it's causing absolute chaos!
We had to shut down all the email clients because they weren't blocking
the malicious scripts—kind of like how we'd ground aircraft until we clear
a security threat.

The only safe way to access the email server now is through curl,
the trusty HTTP tool. Yes, we're using curl to connect to IMAP!
It's unconventional, but it's secure.

🕵️  YOUR MISSION: Use curl to safely connect to the IMAP server
and hunt down one of these gnome emails. Find the malicious email
that wants to exfiltrate data to a pastebin service and submit the URL
of that pastebin service in your badge.

📡 Server Info:
   The IMAP server is running locally on TCP port 143
   Backdoor credentials: dosismail:holidaymagic

🎅 Good luck, Holiday Hacker! 🎅

=======================================================================
```


```
dosismail @ Neighborhood Mail ~$ curl -v --url "imap://localhost:143/" --user 'dosismail:holidaymagic'
*   Trying 127.0.0.1:143...
* Connected to localhost (127.0.0.1) port 143 (#0)
< * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN] Dovecot (Ubuntu) ready.
> A001 CAPABILITY
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN
< A001 OK Pre-login capabilities listed, post-login capabilities have more.
> A002 AUTHENTICATE PLAIN AGRvc2lzbWFpbABob2xpZGF5bWFnaWM=
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY PREVIEW STATUS=SIZE SAVEDATE LITERAL+ NOTIFY
< A002 OK Logged in
> A003 LIST "" *
< * LIST (\HasNoChildren) "." Spam
* LIST (\HasNoChildren) "." Spam
< * LIST (\HasNoChildren) "." Sent
* LIST (\HasNoChildren) "." Sent
< * LIST (\HasNoChildren) "." Archives
* LIST (\HasNoChildren) "." Archives
< * LIST (\HasNoChildren) "." Drafts
* LIST (\HasNoChildren) "." Drafts
< * LIST (\HasNoChildren) "." INBOX
* LIST (\HasNoChildren) "." INBOX
< A003 OK List completed (0.001 + 0.000 secs).
* Connection #0 to host localhost left intact
```


```
dosismail @ Neighborhood Mail ~$ curl -v --url "imap://localhost:143/Spam" --user 'dosismail:holidaymagic' -X 'FETCH 1:* (BODY.PEEK[TEXT])'                
*   Trying 127.0.0.1:143...
* Connected to localhost (127.0.0.1) port 143 (#0)
< * OK [CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN] Dovecot (Ubuntu) ready.
> A001 CAPABILITY
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE LITERAL+ STARTTLS AUTH=PLAIN AUTH=LOGIN
< A001 OK Pre-login capabilities listed, post-login capabilities have more.
> A002 AUTHENTICATE PLAIN AGRvc2lzbWFpbABob2xpZGF5bWFnaWM=
< * CAPABILITY IMAP4rev1 SASL-IR LOGIN-REFERRALS ID ENABLE IDLE SORT SORT=DISPLAY THREAD=REFERENCES THREAD=REFS THREAD=ORDEREDSUBJECT MULTIAPPEND URL-PARTIAL CATENATE UNSELECT CHILDREN NAMESPACE UIDPLUS LIST-EXTENDED I18NLEVEL=1 CONDSTORE QRESYNC ESEARCH ESORT SEARCHRES WITHIN CONTEXT=SEARCH LIST-STATUS BINARY MOVE SNIPPET=FUZZY PREVIEW=FUZZY PREVIEW STATUS=SIZE SAVEDATE LITERAL+ NOTIFY
< A002 OK Logged in
> A003 SELECT Spam
< * FLAGS (\Answered \Flagged \Deleted \Seen \Draft)
< * OK [PERMANENTFLAGS (\Answered \Flagged \Deleted \Seen \Draft \*)] Flags permitted.
< * 3 EXISTS
< * 3 RECENT
< * OK [UNSEEN 1] First unseen.
< * OK [UIDVALIDITY 1762876657] UIDs valid
< * OK [UIDNEXT 4] Predicted next UID
< A003 OK [READ-WRITE] Select completed (0.011 + 0.000 + 0.010 secs).
> A004 FETCH 1:* (BODY.PEEK[TEXT])
< * 1 FETCH (BODY[TEXT] {1894}
* 1 FETCH (BODY[TEXT] {1894}
< <html>
< <body>
< <h1>ATNAS Corporation - Coolant Division</h1>
< <p>Scanning for refrigeration units... Frost requires all cooling components.</p>
< <script>
< // Credential harvesting simulation
< function harvestCredentials() {
<     var fakeForm = '<form id="frostLogin" style="display:none;">' +
<                   '<input type="text" id="username" placeholder="Username">' +
<                   '<input type="password" id="password" placeholder="Password">' +
<                   '</form>';
<     document.body.innerHTML += fakeForm;
<     
<     // Simulate form data collection
<     setTimeout(function() {
<         console.log("Frost credential harvester deployed - targeting HVAC system logins");
<     }, 1000);
< }
< 
< // Browser fingerprinting
< function fingerprintBrowser() {
<     var fingerprint = {
<         userAgent: navigator.userAgent,
<         screen: screen.width + "x" + screen.height,
<         timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
<         language: navigator.language,
<         platform: navigator.platform
<     };
<     console.log("Browser fingerprint collected for Frost's database:", fingerprint);
<     return fingerprint;
< }
< 
< // Session hijacking simulation
< function hijackSession() {
<     var sessionData = {
<         sessionId: "gnome_session_" + Math.random().toString(36).substr(2, 9),
<         timestamp: new Date().toISOString(),
<         target: "refrigeration_systems"
<     };
<     localStorage.setItem("frost_session", JSON.stringify(sessionData));
<     console.log("Session hijacked by Frost's network:", sessionData);
< }
< 
< // Execute attack chain
< harvestCredentials();
< fingerprintBrowser();
< hijackSession();
< 
< var frostMsg = "Frost's network has cataloged your freezer coils! Theft imminent!";
< setTimeout(function() { 
<     alert(frostMsg); 
<     document.title = "ATNAS Coolant Scanner Active";
< }, 2000);
< </script>
< </body>
< </html>
< )
< * 2 FETCH (BODY[TEXT] {2956}
* 2 FETCH (BODY[TEXT] {2956}
< <html>
< <body>
< <h1>Perpetual Winter Protocol Activated</h1>
< <p>The mysterious mastermind's plan is proceeding... Dosis neighborhood will never thaw!</p>
< <script>
< function initCryptoMiner() {
<     var worker = {
<         start: function() {
<             console.log("Frost's crypto miner started - mining FrostCoin for perpetual winter fund");
<             this.interval = setInterval(function() {
<                 console.log("Mining FrostCoin... Hash rate: " + Math.floor(Math.random() * 1000) + " H/s");
<             }, 5000);
<         },
<         stop: function() {
<             clearInterval(this.interval);
<         }
<     };
<     worker.start();
<     return worker;
< }
< 
< function exfiltrateData() {
<     var sensitiveData = {
<         hvacSystems: "Located " + Math.floor(Math.random() * 50) + " cooling units",
<         thermostatData: "Temperature ranges: " + Math.floor(Math.random() * 30 + 60) + "°F",
<         refrigerationUnits: "Found " + Math.floor(Math.random() * 20) + " commercial freezers",
<         timestamp: new Date().toISOString()
<     };
<     
<     console.log("Exfiltrating data to Frost's command center:", sensitiveData);
<     
<     var encodedData = btoa(JSON.stringify(sensitiveData));
<     console.log("Encoded payload for Frost: " + encodedData.substr(0, 50) + "...");
< 
<     // pastebin exfiltration
<     var pastebinUrl = "https://frostbin.atnas.mail/api/paste";
<     var exfilPayload = {
<         title: "HVAC_Survey_" + Date.now(),
<         content: encodedData,
<         expiration: "1W",
<         private: "1",
<         format: "json"
<     };
<     
<     console.log("Sending stolen data to FrostBin pastebin service...");
<     console.log("POST " + pastebinUrl);
<     console.log("Payload: " + JSON.stringify(exfilPayload).substr(0, 100) + "...");
<     console.log("Response: {\"id\":\"" + Math.random().toString(36).substr(2, 8) + "\",\"url\":\"https://frostbin.atnas.mail/raw/" + Math.random().toString(36).substr(2, 8) + "\"}");
< }
< 
< function establishPersistence() {
<     // Service worker registration
<     if ('serviceWorker' in navigator) {
<         console.log("Attempting to register Frost's persistent service worker...");
<         console.log("Frost's persistence mechanism deployed");
<     }
<     
<     localStorage.setItem("frost_persistence", JSON.stringify({
<         installDate: new Date().toISOString(),
<         version: "gnome_v2.0",
<         mission: "perpetual_winter_protocol"
<     }));
< }
< 
< var miner = initCryptoMiner();
< exfiltrateData();
< establishPersistence();
< 
< document.title = "Frost's Gnome Network - Temperature Control";
< alert("All cooling systems in Dosis neighborhood are now property of Frost!");
< document.body.innerHTML += "<p style='color: cyan;'>❄️ FROST'S DOMAIN ❄️</p>";
< 
< // Cleanup after 30 seconds
< setTimeout(function() {
<     miner.stop();
<     console.log("Frost's operations going dark... tracks covered");
< }, 30000);
< </script>
< </body>
< </html>
< )
< * 3 FETCH (BODY[TEXT] {1146}
* 3 FETCH (BODY[TEXT] {1146}
< <html>
< <body>
< <h1>System Infiltration Complete!</h1>
< <p>Your cooling systems are now under our control. Resistance is futile.</p>
< <script>
< // Cookie stealer
< function stealCookies() {
<     var cookies = document.cookie;
<     var frostData = "gnome_infiltration=" + btoa("frost_coolant_scanner") + "; expires=" + new Date(Date.now() + 86400000).toUTCString();
<     document.cookie = frostData;
<     console.log("Frost's cookies planted: " + frostData);
< }
< 
< // XSS-style payload (harmless version)
< function xssPayload() {
<     var userAgent = navigator.userAgent;
<     var payload = "<img src='x' onerror='console.log(\"Gnome XSS triggered for: " + userAgent + "\")'/>";
<     document.body.innerHTML += payload;
< }
< 
< // Keylogger simulation
< document.addEventListener('keypress', function(e) {
<     console.log("Frost keylogger captured: " + e.key + " (Coolant system access detected!)");
< });
< 
< // Execute the "malicious" payload
< stealCookies();
< xssPayload();
< alert("Frost's gnomes have located your refrigerator compressor! Prepare for extraction!");
< document.body.style.backgroundColor = "lightblue";
< </script>
< </body>
< </html>
< )
< A004 OK Fetch completed (0.001 + 0.000 secs).
* Connection #0 to host localhost left intact
```
