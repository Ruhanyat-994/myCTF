#  Level 0
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
# Level 10-11
## Commands
```sh
bandit10@bandit:~$ cat data.txt 
VGhlIHBhc3N3b3JkIGlzIGR0UjE3M2ZaS2IwUlJzREZTR3NnMlJXbnBOVmozcVJyCg==
bandit10@bandit:~$ base64 --help
Usage: base64 [OPTION]... [FILE]
Base64 encode or decode FILE, or standard input, to standard output.

With no FILE, or when FILE is -, read standard input.

Mandatory arguments to long options are mandatory for short options too.
  -d, --decode          decode data
  -i, --ignore-garbage  when decoding, ignore non-alphabet characters
  -w, --wrap=COLS       wrap encoded lines after COLS character (default 76).
                          Use 0 to disable line wrapping
      --help        display this help and exit
      --version     output version information and exit

The data are encoded as described for the base64 alphabet in RFC 4648.
When decoding, the input may contain newlines in addition to the bytes of
the formal base64 alphabet.  Use --ignore-garbage to attempt to recover
from any other non-alphabet bytes in the encoded stream.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Full documentation <https://www.gnu.org/software/coreutils/base64>
or available locally via: info '(coreutils) base64 invocation'
bandit10@bandit:~$ base64 -d data.txt 
The password is dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr

```
#### password :
```plaintext
dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr
```
```plaintext
ssh bandit11@bandit.labs.overthewire.org -p 2220
```

# Level 11-12
## Command
```sh
bandit11@bandit:~$ ls
data.txt
bandit11@bandit:~$ cat data.txt 
Gur cnffjbeq vf 7k16JArUVv5LxVuJfsSVdbbtaHGlw9D4
bandit11@bandit:~$ tr "A-Za-z" "N-ZA-Mn-za-m"
^C
bandit11@bandit:~$ cat data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"
The password is 7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4

```
#### Theory
```sh
The Linux tr command, which stands for ’translate’, allows replacing characters with others. The base command syntax looks like the following tr <old_chars> <new_chars>.
```
```sh
you can also use CyberChef web application.
```

#### password :
```plaintext
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```
```plaintext
ssh bandit12@bandit.labs.overthewire.org -p 2220
```




# Level 12-13

```markdown
# Hexdumps, File Types, Compression, and Archiving

Hexdumps are often used when we want to look at data that cannot be represented in strings and therefore is not readable, so it is easier to look at the hex values. A hexdump has three main columns:

1. The first shows the **address**.
2. The second shows the **hex representation** of the data at that address.
3. The last shows the **actual data as strings** (with ‘.’ representing hex values that cannot be represented as a string).

Many hex editors exist; just pick the one you like most.

## Using `xxd` for Hexdumps

For the command line, `xxd` can be used. The command:
```sh
xxd <input_file> <output_file>
```
creates hexdumps. When using the `-r` flag, it reverts the hexdump:
```sh
xxd -r <input_file> <output_file>
```

## Identifying File Types with Hexdumps

Hexdumps can be used to figure out the type of a file. Each file type has a **magic number/file signature**. You can find lists with collections of these different file signatures online. The `file` command, which was introduced in Level 5, also uses this method (and more beyond that). This is especially important to know because sometimes files might not have the correct or any file ending to identify its type.

## Compression Methods

Compression is a method of encoding that aims to reduce the original size of a file without losing information (or only losing as little as possible).

### `gzip`

- To compress a file:
    ```sh
    gzip <file>
    ```
- To decompress a file:
    ```sh
    gzip -d <file.gz>
    ```

### `bzip2`

- To compress a file:
    ```sh
    bzip2 <file>
    ```
- To decompress a file:
    ```sh
    bzip2 -d <file.bz2>
    ```

## Archive Files

An Archive File is a file that contains one or multiple files and their metadata. This can allow easier portability.

### `tar`

- To create an archive:
    ```sh
    tar -cf <archive.tar> <file1> <file2> ...
    ```
- To extract an archive:
    ```sh
    tar -xf <archive.tar>
    ```

---

Hexdumps, file type identification, compression, and archiving are essential skills for handling and inspecting files efficiently in various computing environments.

```sh
this solution is a lengthy process. We have to decompress and compress the file again and again so that we can get the actual decompressed value.
```

## Commands
```sh
.
.
.
.
.
.
compressed_data.tar  data5.bin  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ ls
compressed_data.tar  data5.bin  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ tar -xf da
tar: da: Cannot open: No such file or directory
tar: Error is not recoverable: exiting now
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ tar -xf data5.bin
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ ls
compressed_data.tar  data5.bin  data6.bin  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ bzip2 -d data6.bin
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ ls
compressed_data.tar  data5.bin  data6.bin.out  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ 
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ tar -xf data6.bin.out
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ ls
compressed_data.tar  data5.bin  data6.bin.out  data8.bin  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ mv data8.bin data8.gz
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ gzip data8.gz
gzip: data8.gz already has .gz suffix -- unchanged
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ gzip -d data8.gz
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ ls
compressed_data.tar  data5.bin  data6.bin.out  data8  hexdump_data
bandit12@bandit:/tmp/tmp.T6ddZmxbkJ$ cat data8
The password is FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn

```
## Commands
```sh
gzip -d <.gz file>
tar -xf
bzip2 -d <.bz2 file>
// .bin are the archieve file being created by tar 

```
#### password :
```plaintext
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
```
```plaintext
ssh bandit13@bandit.labs.overthewire.org -p 2220
```

# Level 13-14
## Commands
```sh
bandit13@bandit:~$ ls
sshkey.private

bandit13@bandit:~$ ssh -i sshkey.private -p 2220 bandit14@localhost
bandit14@bandit:~$ ls
bandit14@bandit:~$ cd /etc/bandit_pass/
bandit14@bandit:/etc/bandit_pass$ ls
bandit0   bandit13  bandit18  bandit22  bandit27  bandit31  bandit6
bandit1   bandit14  bandit19  bandit23  bandit28  bandit32  bandit7
bandit10  bandit15  bandit2   bandit24  bandit29  bandit33  bandit8
bandit11  bandit16  bandit20  bandit25  bandit3   bandit4   bandit9
bandit12  bandit17  bandit21  bandit26  bandit30  bandit5
bandit14@bandit:/etc/bandit_pass$ cat bandit14
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS

```
#### password :
```plaintext
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```
```plaintext
ssh bandit14@bandit.labs.overthewire.org -p 2220
```

# Level 14-15
**nc or netcat is a command that allows to read and write data over a network connection. It can be used for TCP and UDP connections. To connect to a service (as client) on a network the command syntax is the following: nc <host> <port>. To create a server that listens to incoming packets, the command looks like this: nc -l <port>.**
## Commands

```sh
bandit14@bandit:~$ nc localhost 30000
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
Correct!
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo

```
#### password :
```plaintext
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
```
```plaintext
ssh bandit15@bandit.labs.overthewire.org -p 2220
```

# Level 15-16
## Commands
```sh
openssl s_client -connect localhost:30001
```
- OpenSSL is a library for secure communication over networks. It implements the Transport Layer Security (TLS) and Secure Sockets Layer (SSL) cryptographic protocols that are, for example, used in HTTPS to secure the web traffic.`openssl s_client` is the implementation of a simple client that connects to a server using SSL/TLS.

```sh
read R BLOCK
8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo
Correct!
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx

closed

```

#### password :
```plaintext
kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx
```
```plaintext
ssh bandit16@bandit.labs.overthewire.org -p 2220
```


