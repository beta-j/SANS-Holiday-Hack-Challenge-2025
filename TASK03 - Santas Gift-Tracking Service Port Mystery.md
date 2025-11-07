# TASK 3 - Santa's Gift-Tracking Service Port #
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termGiftTracking)

## OBJECTIVE : ##
>Chat with Yuri near the apartment building about Santa's mysterious gift tracker and unravel the holiday mystery.


#  

## HINTS: ##
<details>
  <summary>Hints provided for Task 2</summary>
  
>-	**Who Requests without a Browser??:** Since we don't have a web browser to connect to this HTTP service...There is another common tool that you can use from the cli.

>-	**Who is Netstat?:** Back in my day...we just used Netstat. I hear ss is the new kid on the block. A lot of the parameters are the same too...such as listing only the ports that are currenting LISTENING on the system.

</details>

#  

## PROCEDURE : ##
The terminal greeting tells us that the Neighborhood Santa-Tracking Service was originally intended to run on port 8080, but some gnomes have managed to change this port.  The terminal also conveniently tells us to use the `ss` tool to identify the new port and then connect to it.

Running `ss` with the `-tl` switch will show us what ports are open on the system and are LISTENING for a connection:
```
🎄 tinkerer @ Santa Tracker ~ 🎅 $ ss -tl
State                       Recv-Q                      Send-Q                                            Local Address:Port                                              Peer Address:Port                      Process                      
LISTEN                      0                           5                                                       0.0.0.0:12321                                                  0.0.0.0:*
```

