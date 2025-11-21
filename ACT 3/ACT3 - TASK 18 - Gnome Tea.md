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

This gives us a nice list of image files contained under two directories; `gnome-avatars` and `gnome-documents`.  
```
└─$ curl "https://firebasestorage.googleapis.com/v0/b/holidayhack2025.firebasestorage.app/o/"

{
  "prefixes": [],
  "items": [
    {
      "name": "gnome-avatars/6J2bowmKiNVbITWmR4XsxjH7i492_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/6nBUHcdxo2fLKSYqYyipr9iCOey2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
...
...
...
```
I used a [simple bash script](../Code/firebasedownloader.sh) to download all of these files.

<img width="520" height="394" alt="image" src="https://github.com/user-attachments/assets/5066961a-78a3-4ac3-8b00-5bf2c53ba329" />

This gave me a cache of gnome avatars and images of their driving licenses.  Going off one of the hints to this task, I ran `exif-tool` on all the images and outputed the results to a text file so that I could have a better look.
One of the drivers' licenses stood out as it was the only one to include the GPS Position in its exif data.  The driver license belogns to BARNARBY BRIEFCASE and the GPS coordinates point to a place called [Gnomesville on Google Maps](https://maps.app.goo.gl/azx2kJ3SNYShQXJi8).  OK - so what am I supposed to do with this information now?

Well, taking another look at the html code of the `login` page, there is an interesting comment included:
``<!-- TODO: lock down dms, tea, gnomes collections -->``
This is a fantastic hint since it tells us that the names of some interesting collections, i.e. `dms`, `tea` and `gnomes`.  Once again ChatGPT came in handy here to help me find the correct way of accessing these collections, but in the end I figured out that the contents fo these collections can be viewed by simply calling the following URLs in a browser or using `curl`:

[https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/tea](https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/tea)
[https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/gnomes](https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/gnomes)
[https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/dms](https://firestore.googleapis.com/v1/projects/holidayhack2025/databases/(default)/documents/dms)


Searching for `barnaby` in the `gnomes` collection, we find some more information related to his profile, in particular we now know that his email address is `barnabybriefcase@gnomemail.dosis` and that enjoys gossipping.  

Searching for `barnaby` in the `tea` collection, we learn that he wrote his password down on a sticky note and we also learn what it was!
```
          "stringValue": "😂 I heard Barnaby Briefcase is SO forgetful, he wrote his password on a sticky note and left it at the garden club! It was \"MakeRColdOutside123!\" - like, seriously Barnaby? That's your password? 🤦\u200d♂️"
```

Unfortunately attempting to log in with this password doesn't work.  So we need to dig a little further.

This time, searching for `barnaby` in the `dms` collection brings up a conversation he had with Glitch Mitnick, where he tells him that his password  "is actually the name of [his]] hometown that [he] grew up in" and that he "just visited there back when [he] signed up with [his] id to GnomeTea".  Just to drive the poitn home, he also says that he "took [his] picture of [his] id there".  

So now we can try logging in with the email `barnabybriefcase@gnomemail.dosis` and the password `gnomesville` .... and we're in! 

<img width="730" height="357" alt="image" src="https://github.com/user-attachments/assets/45328791-4858-4b50-8cec-c1c6cb5a6a67" />


OK - now to gain admin access...So - let's try lookign around for a possible admin panel... my first guess would be to try visitng `/admin` at `https://gnometea.web.app/admin`, and sure enough it looks liek the portal exists and we get an extremely handy error message tellign us that we're not allowed to access it and why!

<img width="503" height="165" alt="image" src="https://github.com/user-attachments/assets/400b13c2-68f0-400c-8f4c-32b686bf9b4c" />

The next step is quite clear now,  we simply need to bring up the console in developer mode and set the variable `window.ADMIN_UID = "3loaihgxP0VwCTKmkHHFLe6FZ4m2";` and as soon as we hit enter, we are greeted with the Admin portal, which includes the details of some classified operations and the passphrase that agents are to use when meeting fellow operatives! :)

<img width="598" height="420" alt="image" src="https://github.com/user-attachments/assets/4b44c66c-5b2e-4f8c-9e23-25c55f883bf6" />




