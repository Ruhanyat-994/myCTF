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