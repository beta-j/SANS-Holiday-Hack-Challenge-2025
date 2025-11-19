# TASK 16 - Quantgnome Leap
Difficulty: ❄️❄️

## OBJECTIVE : ##
>Kevin in the Retro Store needs help rewinding tech and going in reverse. Extract the flag and enter it here.

## HINTS: ##
<details>
  <summary>Hints provided for Task 17</summary>
  
>-	It looks like the program on the disk contains some weird coding.

>-  Holy cow! Another retro floppy disk, what are the odds? Well it looks like this one is intact.

>-  Maybe it is encrypted OR encoded?

</details>
 
#

## PROCEDURE : ##

Kevin gives us a 5.25" floppy containg a [BASIC program](/Assets/login.bas) - oh.....this really brings back soem fond memories!!

Luckily BASIC is a pretty straightforward language to understand.  The program declares two variables at the start `ENC_PASS$` and `ENC_FLAG` and these seem to both contain encrypted (or encoded) strings.  The program then asks the user to enter a password and checks whether it is the same length as `ENC_PASS$` - so we know that the password it is expecting is 8 characters long.

Next the program goes through the user-provided string character by character, takes its ASCII value and XORs with 7:
``(ASC(MID$(PASS$,I,1)) XOR 7)`` this is compared to the character in the same position in `ENC_PASS$` variable.  If any of the characters do not match, access is denied.

So we now know that we can retrieve the actual password by running an XOR of `D13URKBT` with 7 since XOR functions are reversible, i.e. `A XOR B XOR B = A`.  We can use the following [CyberChef recipe](https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'Decimal','string':'7'%7D,'Standard',false)&input=RDEzVVJLQlQ) to convert it back:
```json
[
  { "op": "XOR",
    "args": [{ "option": "Decimal", "string": "7" }, "Standard", false] }
]
```

Similarly, we can run the same `XOR 7` operation on the ASCII values of the contents of `ENC_FLAG$`.  It is important to note here that the `'` character in BASIC indicates an inline comment, so anything following the `'` on line 30 will be ignored:

```basic
30 ENC_FLAG$ = "DSA|auhts*wkfi=dhjwubtthut+dhhkfis+hnkz" ' old "DSA|qnisf`bX_huXariz"
```

So `DSA|auhts*wkfi=dhjwubtthut+dhhkfis+hnkz` XOR 7 gives us: `CTF{frost-plan:compressors,coolant,oil}`


