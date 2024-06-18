# Level 0
## Command
```plaintext

ssh bandit0@bandit.labs.overthewire.org -p 2220

```

```plaintext
password : bandit0

```

# Level 0-1

## Command

```plaintext
cat filename
```
#### password :
```plaintext
 ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If
```
```plaintext
ssh bandit1@bandit.labs.overthewire.org -p 2220

```

# Level 1-2

## Commands


```plaintext
cat ./-
```

#### password :
```plaintext
 263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```
```plaintext
ssh bandit2@bandit.labs.overthewire.org -p 2220

```

# Level 2-3

## Command

```plaintext 
bandit2@bandit:~$ cat "spaces in this filename"

MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```
#### password :
```plaintext
 MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```
```plaintext
ssh bandit3@bandit.labs.overthewire.org -p 2220

```

# Level 3-4

## Commands


```plaintext
bandit3@bandit:~$ ls
inhere
bandit3@bandit:~$ ls -al
total 24
drwxr-xr-x  3 root root 4096 Jun 11 04:49 .
drwxr-xr-x 70 root root 4096 Jun 11 04:50 ..
-rw-r--r--  1 root root  220 Mar 31 08:41 .bash_logout
-rw-r--r--  1 root root 3771 Mar 31 08:41 .bashrc
drwxr-xr-x  2 root root 4096 Jun 11 04:49 inhere
-rw-r--r--  1 root root  807 Mar 31 08:41 .profile
bandit3@bandit:~$ cd inhere/
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls
bandit3@bandit:~/inhere$ ls -l
total 0
bandit3@bandit:~/inhere$ ls -a
.  ..  ...Hiding-From-You
bandit3@bandit:~/inhere$ cat "...Hiding-From-You"
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ

```

#### password :
```plaintext
 2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```
```plaintext
ssh bandit4@bandit.labs.overthewire.org -p 2220
```

# Level 4-5

## Commands

> ##### **The file command in Kali Linux is used to determine the type of a file. It performs tests to classify files into categories like text, executable, directory, etc.**

```plaintext
bandit4@bandit:~/inhere$ ls
-file00  -file02  -file04  -file06  -file08
-file01  -file03  -file05  -file07  -file09
bandit4@bandit:~/inhere$ file ./*
./-file00: data
./-file01: data
./-file02: data
./-file03: data
./-file04: data
./-file05: data
./-file06: data
./-file07: ASCII text
./-file08: data
./-file09: data
bandit4@bandit:~/inhere$ cat ./-file07 
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw

```
#### password :
```plaintext
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```
```plaintext
ssh bandit5@bandit.labs.overthewire.org -p 2220
```
# Level 5-6

## Commands
```plaintext
bandit5@bandit:~$ ls -l
total 4
drwxr-x--- 22 root bandit5 4096 Jun 11 21:30 inhere
bandit5@bandit:~$ cd inhere/
bandit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
bandit5@bandit:~/inhere$ cd maybehere00
bandit5@bandit:~/inhere/maybehere00$ ls
-file1  -file2  -file3  spaces file1  spaces file2  spaces file3
bandit5@bandit:~/inhere/maybehere00$ ls -al
total 72
drwxr-x---  2 root bandit5 4096 Jun 11 21:30 .
drwxr-x--- 22 root bandit5 4096 Jun 11 21:30 ..
-rwxr-x---  1 root bandit5 1039 Jun 11 21:30 -file1
-rwxr-x---  1 root bandit5  551 Jun 11 21:30 .file1
-rw-r-----  1 root bandit5 9388 Jun 11 21:30 -file2
-rw-r-----  1 root bandit5 7836 Jun 11 21:30 .file2
-rwxr-x---  1 root bandit5 7378 Jun 11 21:30 -file3
-rwxr-x---  1 root bandit5 4802 Jun 11 21:30 .file3
-rwxr-x---  1 root bandit5 6118 Jun 11 21:30 spaces file1
-rw-r-----  1 root bandit5 6850 Jun 11 21:30 spaces file2
-rwxr-x---  1 root bandit5 1915 Jun 11 21:30 spaces file3

``` 
- We can see there are many hidden files in the maybehere00 directory so there could be much more in the other directories
- We can't just find in every directories like this.
- There are many methods of finding it .

> **We can use grep along with  find or we can use 'du' which will tell use the file size in bytes**

### Style - 1
```plaintext
andit5@bandit:~/inhere$ ls
maybehere00  maybehere04  maybehere08  maybehere12  maybehere16
maybehere01  maybehere05  maybehere09  maybehere13  maybehere17
maybehere02  maybehere06  maybehere10  maybehere14  maybehere18
maybehere03  maybehere07  maybehere11  maybehere15  maybehere19
bandit5@bandit:~/inhere$ du -b -a
251	./maybehere12/-file2
9678	./maybehere12/-file1
9076	./maybehere12/-file3
1639	./maybehere12/spaces file3
2460	./maybehere12/spaces file2
5815	./maybehere12/.file1
2157	./maybehere12/spaces file1
'
'
'
```
```plaintext
bandit5@bandit:~/inhere$ du -b -a | wc -l
201
```
**There comes 201 files for this command**
- we can filter it through "grep"


```plaintext
bandit5@bandit:~$ du -b -a | grep 1033
1033	./inhere/maybehere07/.file2
bandit5@bandit:~$ cd ./inhere/maybehere07/
bandit5@bandit:~/inhere/maybehere07$ cat ./.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

### Style - 2

```plaintext
bandit5@bandit:~/inhere$ find . -type f -size 1033c
./maybehere07/.file2
bandit5@bandit:~/inhere$ cd ./maybehere07/
bandit5@bandit:~/inhere/maybehere07$ cat ./.file2
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

#### password :
```plaintext
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```
```plaintext
ssh bandit6@bandit.labs.overthewire.org -p 2220
```

# Level 6-7

##### In this level, we are introduced to the big topic of Linux File Permissions. Specifically, to the area of ownership. Each file is owned by a user and a group. You can see what user and group owns a file with the ls command and its -l tag.

### Example:

```sh
1 bandit6@bandit:/var/lib/dpkg/info$ ls -l bandit7.password 
2 -rw-r----- 1 bandit7 bandit6 33 May  7  2020 bandit7.password
```
> #### The third column shows the user, the fourth shows the group that owns the file.As mentioned in a previous level, the find command can be used to find files on the server. It offers flags to look for files owned by a specific user (-user <username>) and a specific group (-group <groupname>)

- **We use the find command with the following options:**

    - type f, because we are looking for a file  
    - user bandit7, to find files owned by the ‘bandit7’ user  
    - group bandit6, to find files owned by the ‘bandit6’ group  
    - size 33c, to find files of size 33 bytes

## Commands
```sh
bandit6@bandit:~$ find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cd /var/lib/dpkg/info/
bandit6@bandit:/var/lib/dpkg/info$ cat bandit7.password 
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
bandit6@bandit:/var/lib/dpkg/info$ 
```
**2>/dev/null** is for error handling


#### password :
```plaintext
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```
```plaintext
ssh bandit7@bandit.labs.overthewire.org -p 2220
```
# Level 7-8
## Commands

```sh
bandit7@bandit:~$ cat data.txt | grep "millionth"
millionth	dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
bandit7@bandit:~$ du -b data.txt 
4184396	data.txt
```
#### password :
```plaintext
dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc
```
```plaintext
ssh bandit8@bandit.labs.overthewire.org -p 2220
```
# Level 8-9
## Commands
```sh
bandit8@bandit:~$ sort data.txt | uniq -u
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```
#### Theory
```plaintext
uniq is a command that filters input and writes to the output. Specifically, it filters based on identical lines. It has a flag -u, which filters for unique lines (lines that appear only ones). Another interesting functionality is, for example, that it can also count (-c) or only return duplicate lines (-d).The command is often used with sort. For uniq to filter for unique lines, the lines need to be sorted. sort sorts the lines of a text file. Furthermore, it has flags for sorting in reverse (-r) and sorting numerically (-n).
```
#### password :
```plaintext
4CKMh1JI91bUIZZPXDqGanal4xvAg0JM
```
```plaintext
ssh bandit9@bandit.labs.overthewire.org -p 2220
```
# Level 9-10
## Commands 
```sh
bandit9@bandit:~$ strings  data.txt | grep ===
*N========== the
========== password
========== is
w========== FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```
#### Theory
```sh
The strings command finds human-readable strings in files. Specifically, it prints sequences of printable characters. Its main use is for non-printable files like hex dumps or executables.
```
#### password :
```plaintext
FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey
```
```plaintext
ssh bandit10@bandit.labs.overthewire.org -p 2220
```