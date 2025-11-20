# TASK 18 - Gnome Tea
Difficulty: ❄️❄️❄️

[Direct Link](https://gnometea.web.app/)

## OBJECTIVE : ##
>Enter the apartment building near 24-7 and help Thomas infiltrate the GnomeTea social network and discover the secret agent passphrase.



## HINTS: ##
<details>
  <summary>Hints provided for Task 13</summary>
  
>-	**GnomeTea:** I heard rumors that the new GnomeTea app is where all the Gnomes spill the tea on each other. It uses Firebase which means there is a client side config the app uses to connect to all the firebase services.
>-  **Statically Coded:** Hopefully they did not rely on hard-coded client-side controls to validate admin access once a user validly logs in. If so, it might be pretty easy to change some variable in the developer console to bypass these controls.
>-  **License:** Exif jpeg image data can often contain data like the latitude and longitude of where the picture was taken.
>-  **Rules:** Hopefully they setup their firestore and bucket security rules properly to prevent anyone from reading them easily with curl. There might be sensitive details leaked in messages.

</details>

#

## PROCEDURE : ##

We are presented with a login screen and not much more information.  After hours and hours of looking through the code, GToogling and chatting with ChatGPT, I was able to find the following:

```
const OP = {
    apiKey: "AIzaSyDvBE5-77eZO8T18EiJ_MwGAYo5j2bqhbk",
    authDomain: "holidayhack2025.firebaseapp.com",
    projectId: "holidayhack2025",
    storageBucket: "holidayhack2025.firebasestorage.app",
    messagingSenderId: "341227752777",
    appId: "1:341227752777:web:7b9017d3d2d83ccf481e98"
}
```

This part of the code tells us that the Firebase storage bucket used by the app is called `holidayhack2025.firebasestorage.app` and we can use this simple bit of information to check whether their database is exposed to the internet and dump its contents if it is.  We do this by calling `curl "https://firebasestorage.googleapis.com/v0/b/<BUCKET NAME>/o/`.  note that the `/o` at the enmd of the URI is included to list the objects within the bucket.

This gives us a nice list of image files contained under two directories; `gnome-avatars` and `gnome-documents`.  I used a simple bash script to dom#wnload all of these


useful  [https://isc.sans.edu/diary/32158](https://isc.sans.edu/diary/32158)
