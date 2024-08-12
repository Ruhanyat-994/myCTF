# Dav
----

## Port Scanning
```sh

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
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-05 05:53 EDT
Nmap scan report for 10.10.226.177
Host is up (0.17s latency).

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
