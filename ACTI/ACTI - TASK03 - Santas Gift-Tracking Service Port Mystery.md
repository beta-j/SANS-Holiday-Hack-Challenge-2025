# TASK 3 - Santa's Gift-Tracking Service Port #
Difficulty: ❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termGiftTracking)

## OBJECTIVE : ##
>Chat with Yuri near the apartment building about Santa's mysterious gift tracker and unravel the holiday mystery.


#  

## HINTS: ##
<details>
  <summary>Hints provided for Task 3</summary>
  
>-	**Who Requests without a Browser??:** Since we don't have a web browser to connect to this HTTP service...There is another common tool that you can use from the cli.

>-	**Who is Netstat?:** Back in my day...we just used Netstat. I hear ss is the new kid on the block. A lot of the parameters are the same too...such as listing only the ports that are currenting LISTENING on the system.

</details>

#  

## PROCEDURE : ##
The terminal greeting tells us that the Neighborhood Santa-Tracking Service was originally intended to run on port 8080, but some gnomes have managed to change this port.  The terminal also conveniently tells us to use the `ss` tool to identify the new port and then connect to it.

Running `ss` with the `-tlpn` switch will show us what ports are open on the system and are LISTENING for a connection:
```
🎄 tinkerer @ Santa Tracker ~ 🎅 $ ss -tlpn
State                       Recv-Q                      Send-Q                                            Local Address:Port                                              Peer Address:Port                      Process                      
LISTEN                      0                           5                                                       0.0.0.0:12321                                                  0.0.0.0:*
```

From this we can see that there is an application listening on port `12321` which is an unusual port, and given that it's the only application on the list, it's safe to assume that this is the Santa-Tracking Service we're looking for.

Assumign that this is a web application (especially since it originally used port 8080) we can connect to it using `curl`:

```
🎄 tinkerer @ Santa Tracker ~ 🎅 $ curl localhost:12321
{
  "status": "success",
  "message": "\ud83c\udf84 Ho Ho Ho! Santa Tracker Successfully Connected! \ud83c\udf84",
  "santa_tracking_data": {
    "timestamp": "2025-11-07 14:19:54",
    "location": {
      "name": "Evergreen Estates",
      "latitude": 62.361137,
      "longitude": -124.692152
    },
    "movement": {
      "speed": "944 mph",
      "altitude": "14208 feet",
      "heading": "42\u00b0 E"
    },
    "delivery_stats": {
      "gifts_delivered": 2305164,
      "cookies_eaten": 43673,
      "milk_consumed": "1847 gallons",
      "last_stop": "Mistletoe Lane",
      "next_stop": "Holly Berry Hills",
      "time_to_next_stop": "2 minutes"
    },
    "reindeer_status": {
      "rudolph_nose_brightness": "95%",
      "favorite_reindeer_joke": "How does Rudolph know when Christmas is coming? He looks at his calen-deer!",
      "reindeer_snack_preference": "magical carrots"
    },
    "weather_conditions": {
      "temperature": "31\u00b0F",
      "condition": "Clear skies"
    },
    "special_note": "Thanks to your help finding the correct port, the neighborhood can now track Santa's arrival! The mischievous gnomes will be caught and will be put to work wrapping presents."
```
