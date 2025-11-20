# TASK 11 - Retro Recovery
Difficulty: ❄️❄️

## OBJECTIVE : ##
>Join Mark in the retro shop. Analyze his disk image for a blast from the retro past and recover some classic treasures.


## HINTS: ##
<details>
  <summary>Hints provided for Task 11</summary>
  
>-	Wow! A disk from the 1980s! I remember delivering those computer disks to the good boys and girls. Games were their favorite, but they weren't like they are now.
>-  I miss old school games. I wonder if there is anything on this disk? I remember, when kids would accidentlly delete things.......... it wasn't to hard to recover files. I wonder if you can still mount these disks?
>-  I know there are still tools available that can help you find deleted files. Maybe that might help. Ya know, one of my favorite games was a Quick Basic game called Star Trek.


</details>
 
#  

## PROCEDURE : ##

We start off this objective by speaking to Mark DeVito who is inside the Retro Emnporium.  He gives us a FAT12 [floppy.img](../Assets/floppy.img) file and asks us to see whether we can recover any data from it.  He also hints that data might be hiding in the form of a deleted file that is still on the disk.

Since we are attempting to recover deleted data, my first instinct was to fire up [Autopsy](https://www.autopsy.com/) and load the `floppy.imng` file inside it.  Autopsy then lets us run a keyword search, so since we were given hints regarding a possible QBASIC Star Trek game, I searched for 'trek'.  

<img width="899" height="376" alt="image" src="https://github.com/user-attachments/assets/ff7d2b59-d532-4679-94f1-c7014586b3b9" />


This returned a number of BASIC code snippets starting at Unit 38 of the disk:
<img width="1323" height="384" alt="image" src="https://github.com/user-attachments/assets/bc32a4b0-a49b-407c-ab99-4d3c98dd2ee5" />

So I then looked at data units 38 to 97 to have a look at the [full code](/Assets/superstartrek.bas).  It looks like a file called `superstartrek.bas` with the code for a QBASIC game (just as expected).  
<img width="1323" height="384" alt="image" src="https://github.com/user-attachments/assets/e9249ad5-d1dc-47c6-b788-b350b26c859d" />

After skimmign through the code a number of times, nothing stood out in particular, so I pasted the whole thign to [ChatGPT](https://chatgpt.com) and asked it whether it could notice anythign strange about the code.  Sure enough, just a second later, it had spotted a BASE64 encoded string on code line `211` and vewry conveniently decoded it for me too!

<img width="794" height="469" alt="image" src="https://github.com/user-attachments/assets/47bd3d9d-015d-4ef7-834c-274f08ca5dbf" />




