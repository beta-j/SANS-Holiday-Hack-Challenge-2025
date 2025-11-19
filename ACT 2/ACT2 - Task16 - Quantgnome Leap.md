# TASK 16 - Quantgnome Leap
Difficulty: ❄️❄️

[Direct Link](https://hhc25-wetty-prod.holidayhackchallenge.com/?&challenge=termQuantgnome)

## OBJECTIVE : ##
>Charlie in the hotel has quantum gnome mysteries waiting to be solved. What is the flag that you find?

## HINTS: ##
<details>
  <summary>Hints provided for Task 16</summary>
  
>-	User keys are like presents. The keys are kept in a hidden location until they need to be used. Hidden files in Linux always start with a dot. Since everything in Linux is a file, directories that start with a dot are also...hidden!

>-  When you give a present, you often put a label on it to let someone know that the present is for them. Sometimes you even say who the present is from. The label is always put on the outside of the present so the public knows the present is for a specific person. SSH keys have something similar called a comment. SSH keys sometimes have a comment that can help determine who and where the key can be used.
</details>
 
#

## PROCEDURE : ##

As soon as we access the terminal we are greeted with an ASCII-art animation of a gnome in a box who appears to disappear as soon as the box is opened - given the title of the task, it's quite clearly a reference to Schroedinger's famous cat that is locked in a box and is simultaneously dead and alive until the box is opened and its state is observed.

The welcome text tells us that there is a _PQC key generation porgram_ on the system and that we should find and run it.

There is a single folder in our home directory; `.ssh` that contains public and private ssh keys.  There are also other home directories called `admin`, `gnome1`, `gnome2`, `gnome3`, `gnome4`, `qgnome` but of course we do not have access to them.

If we look at the contents of `~.ssh/id_rsa.pub` we can see a comment just after the public key saying `gnome1`

```shell
qgnome@quantgnome_leap:~$ cat .ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCya6rjv+pf55l/EvEIZW+yhBdrpBrS0rmyysVhdR5Zn2aatLVDhRnNQrH+si6SOaDAOPhOhy037auUveLhEFaQBDQIDqisQ8JoTT/TKhyO97h1IUkl3zmsuw4Kcu1r24L2UJCIVStiJR8vQU8U0Kg5eWuDRev9j+2VMGqF2hmYqssTNbxHNeNbEr1R6/wciSAa3hNwksqE3dYjbr07veKAIcWcsaPMRHmjHrHXdLLwyweXhgzidd3AgzDskub9XdAiXs2B93mFNbQWel+nE2smxUVUY+SLsGXDTXAJu5AqYXrDEJtSuCOCHKXyPX7WCbmAllQo1FB/9K59pI552+K062SvGDCeLEPpcELozU52/awX2yeldNOj7Bn/xXdKpSPHLUrhsj8y/9gVTnS/0q6VLzO8qIwzxdGh7P0OtQqMrSRkTLEHtdOjojTmT70WUpUaVWXf65X8ymY72G49lJjFVAyM6AFBQK/K52f0UTl4XnvkSHwxYNFyk7wGkE07pWU= gnome1
```

So `id_rsa` and `id_rsa.pub` must be the public/private key pair for ssh to `gnome1`...let's test that hypothesis:

```shell
qgnome@quantgnome_leap:~$ ssh -i .ssh/id_rsa gnome1@localhost
###########################################################################################################################################################################################

Welcome, gnome1 user! You made the first leap!

You authenticated with an RSA key, but that isn't very secure in a post-quantum world. RSA depends on large prime numbers, which a quantum computer can easily solve with something like 
Shor's algorithm.

Take a look around and see if you can find a way to login to the gnome2 account.

###########################################################################################################################################################################################
```

OK - so now it's becoming quite clear that we'll need to find different ways of working our way through the different accounts on this system.

We can try a similar tactic to what we tried earlier, and sure enough we see that the `.ssh` folder for `gnome1` now includes an ED25519 key pair: `id_ed25519` and `id_ed25519.pub`.  We can use these to log in as `gnome2` over SSH too:

```shell
gnome1@pqc-server:~$ ssh -i .ssh/id_ed25519 gnome2@localhost
###########################################################################################################################################################################################

Welcome, gnome2 user! You made the second leap!

You authenticated with an ED25519 key, smaller than an RSA key, but still not secure in a post-quantum world due to Shor's algorithm.

Take a look around and see if you can find a way to login to the gnome3 account.

###########################################################################################################################################################################################
```

We can gain access to `gnome3` in much the same way, only this time using a MAYO post-quantum key pair found in `~/.ssh`:
```shell
gnome2@pqc-server:~$ ssh -i .ssh/id_mayo2 gnome3@localhost
###########################################################################################################################################################################################

Welcome, gnome3 user! You made the third leap!

You authenticated with a MAYO post-quantum key. 
A post-quantum cryptographic algorithm with promising results for embedded systems. HOWEVER, use MAYO with caution! Wait for a standardized implementation (if/when that 
happens).

Take a look around and see if you can find a way to login to the gnome4 account.

###########################################################################################################################################################################################
```

Once again, we can use the same method to gain access to the `gnome4` account, this time using a post-quantum hybrid NIST P-256 ECDSA key:
```shell
gnome3@pqc-server:~$ ssh -i .ssh/id_ecdsa_nistp256_sphincssha2128fsimple gnome4@localhost
###########################################################################################################################################################################################

Welcome, gnome4 user! You made the fourth leap!

You authenticated with a post-quantum hybrid key! What does that mean? A blended approach with proven classical cryptography and post-quantum cryptography.

In this case, you authenticated with a NIST P-256 ECDSA key (a classical elliptic curve) that also uses post-quantum SPHINCS+ (standardized by NIST in FIPS 205 as SLH-DSA). That makes 
this key extremely robust. According to NIST, this is a security level 1 key, which means this key is at least as strong as AES128.

Instead of a single exchange/signature (as with RSA or ED25519), this key produces two (one classical and one post-quantum) that are both checked together. If one fails, authentication 
fails. A hybrid approach is a great first step when testing and implementing post-quantum cryptography, giving organizations 'Quantum Agility'.

Take a look around and see if you can find a way to login to the admin account.

###########################################################################################################################################################################################
```

Now to get admin access, we can use the hybrid post-quantum key found in the `~/.ssh` folder of `gnome4`:
```shell
gnome4@pqc-server:~$ ssh -i .ssh/id_ecdsa_nistp521_mldsa87 admin@localhost
###########################################################################################################################################################################################

You made the QuantGnome Leap! Your final stop.

You authenticated with another hybrid post-quantum key. What is different about this key? It uses the NIST P-521 elliptic curve (roughly equivalent to a 15360-bit RSA key) paired with 
ML-DSA-87. According to NIST, ML-DSA-87 is a security level 5 algorithm, which provides the highest security level and is meant for the most secure environments. NIST standardized 
CRYSTALS-Dilithium as ML-DSA in FIPS 204 with three defined security levels:

- ML-DSA-44: Security Level 2 - At least as strong as SHA256/SHA3-256
- ML-DSA-65: Security Level 3 - At least as strong as AES192
- ML-DSA-87: Security Level 5 - At least as strong as AES256

This is one of the strongest hybrid keys available in post-quantum cryptography. The other extremely strong security level 5 algorithms all use a combination of the NIST P-521 
elliptic curve and one of the following PQC algorithms:

- falcon1024: Falcon (FN-DSA) with a 1024 lattice dimensional size
- sphincssha2256fsimple: SLH-DSA (SPHINCS+) using SHA2 256 and fast signature generation (hence the 'f' in the algorithm name)
- mayo5: MAYO-5 is the highest of the four MAYO security levels

This entire build/system is based off of the Linux Foundation's Open Quantum Safe (OQS) initiative. It uses the OQS liboqs library which provides PQC algorithm support.
You can find out more about the OQS initiative at https://openquantumsafe.org/.

Next Step: You now have access to a directory in the same location as the SSH daemon. Time to look around for your final flag.
###########################################################################################################################################################################################
```


The admin shell welcome message tells us to look for a flag in the same directory as the ssh daemon.

We can fidn which directory that is using the `which ssh` command.  Looking inside the returned directory we find a directory conveniently named `flag` with an (also conviently named) file called `flag` inside it:
```shell
admin@quantgnome_leap:~$ which ssh
/opt/oqs-ssh/bin/ssh

admin@quantgnome_leap:~$ ls /opt/oqs-ssh/
bin                                       moduli                                    ssh_config                                sshd_config
flag                                      sbin                                      ssh_host_ecdsa_nistp521_mldsa-87_key      sshd_logfile.log
key-lookup.log                            scripts                                   ssh_host_ecdsa_nistp521_mldsa-87_key.pub  user-keys
key-lookup.sh                             share                                     ssh_known_hosts
admin@quantgnome_leap:~$ ls /opt/oqs-ssh/flag
flag
admin@quantgnome_leap:~$ cat /opt/oqs-ssh/flag/flag 
HHC{L3aping_0v3r_Quantum_Crypt0}
```

Our flag is: `HHC{L3aping_0v3r_Quantum_Crypt0}`