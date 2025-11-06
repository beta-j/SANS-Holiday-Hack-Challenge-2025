# SANS-Holiday-Hack-Challenge-2025


```

======= Neighborhood Santa-Tracking Service =======

Oh no! Mischievous gnomes have tampered with the neighborhood's Santa-tracking service,
built by the local tinkerer to help everyone know when Santa arrives on Christmas Eve!

The tracking application was originally configured to run on port 8080, but after the
gnomes' meddling, it's nowhere to be found. Without this tracker, nobody in the neighborhood
will know when to expect Santa's arrival!

The tinkerer needs your help to find out which port the santa_tracker process is 
currently using so the neighborhood tracking display can be updated before Christmas Eve!

Your task:
1. Use the 'ss' tool to identify which port the santa_tracker process is 
   listening on
2. Connect to that port to verify the service is running

Hint: The ss command can show you all listening TCP ports and the processes 
using them. Try: ss -tlnp

Good luck, and thank you for helping save the neighborhood's Christmas spirit!

- The Neighborhood Tinkerer 🔧🎄
🎄 tinkerer @ Santa Tracker ~ 🎅 $
```

Use ss to find the port the application is listening on:

```
🎄 tinkerer @ Santa Tracker ~ 🎅 $ ss -tulpn
Netid                 State                  Recv-Q                 Send-Q                                 Local Address:Port                                  Peer Address:Port                Process                
tcp                   LISTEN                 0                      5                                            0.0.0.0:12321                                      0.0.0.0:*                                          
🎄 tinkerer @ Santa Tracker ~ 🎅 $
```

then use curl to access the application on port `12321`

```
🎄 tinkerer @ Santa Tracker ~ 🎅 $ curl localhost:12321
{
  "status": "success",
  "message": "\ud83c\udf84 Ho Ho Ho! Santa Tracker Successfully Connected! \ud83c\udf84",
  "santa_tracking_data": {
    "timestamp": "2025-11-06 15:47:37",
    "location": {
      "name": "Candy Cane Court",
      "latitude": 36.416785,
      "longitude": -114.04252
    },
    "movement": {
      "speed": "912 mph",
      "altitude": "21409 feet",
      "heading": "321\u00b0 SE"
    },
    "delivery_stats": {
      "gifts_delivered": 7800512,
      "cookies_eaten": 37426,
      "milk_consumed": "3464 gallons",
      "last_stop": "Evergreen Estates",
      "next_stop": "Frosty's Passage",
      "time_to_next_stop": "13 minutes"
    },
    "reindeer_status": {
      "rudolph_nose_brightness": "89%",
      "favorite_reindeer_joke": "How does Rudolph know when Christmas is coming? He looks at his calen-deer!",
      "reindeer_snack_preference": "magical carrots"
    },
    "weather_conditions": {
      "temperature": "24\u00b0F",
      "condition": "Clear skies"
    },
    "special_note": "Thanks to your help finding the correct port, the neighborhood can now track Santa's arrival! The mischievous gnomes will be caught and will be put to work wrapping presents."
  }
}🎄 tinkerer @ Santa Tracker ~ 🎅 $
```



