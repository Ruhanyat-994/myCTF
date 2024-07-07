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


## PrivEsc

- #### **Finding info in the crontab**
```sh
cat /etc/crontab 
```

- #### Searching for `Bash History`
```sh
ls -la /etc/cron.daily/
```


## Links 

- #### **Audio Decoder**
    - [Morsecode](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)

- #### **Password Decoder**
    - [Check Psychobreak](https://www.cachesleuth.com/vanity.html)

- #### Reverse Shell `These will give you ROOT` 
    - [GTFOBINS](https://gtfobins.github.io/)
    - [PentestMonkey](https://github.com/pentestmonkey)



## Brute Forcing

- #### Hydra for SSH password bruteforce
```sh
hydra -l <ssh name> -P <passwordlist> -t 6 ssh://target
```


