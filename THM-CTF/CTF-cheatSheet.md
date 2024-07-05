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


