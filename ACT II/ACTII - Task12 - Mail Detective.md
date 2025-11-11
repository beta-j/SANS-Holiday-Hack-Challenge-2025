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
