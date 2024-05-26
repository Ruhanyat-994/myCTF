# Psycho Break THM
> ### "This room is incane"
> -Ruhansec  

 
## 1. Do some normal nmap stuff.

 ```
 nmap -sS -sV -O 10.10.239.153 >> ports.txt
```
This will give you some info about the ports and OS. 

![alt text](image-4.png)

## 2. Now Check the target IP  
- Check the target ip in the browser
- Check the dev tool and you will find a directory there
- Search the directory then you will get the key  

![alt text](image-5.png)

## 3. The most important part

- The most important part is that we can't let the sabestian to die.
- We have to copy the key and paste it to the sadist room 
- then it will redirect us to another room and then we can find a key there .
- this key needs to be decrypted  

[Cipher Identifier](https://www.boxentriq.com/code-breaking/atbash-cipher)  

- This decoding system will decode the key and you will find the key there.  

![alt text](image-6.png)

- our key is  

![alt text](image-7.png)

> ### "Grant_me_access_to_the_map_please"

- Now it will redirect us to another rooms

![alt text](image-8.png)  

## 4. The SafeHaeven 

- In this room we will do some gobuster thing  

```
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt -u 10.10.178.204/SafeHeaven/
```
- Now we found a secret directory called keeper

```
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://10.10.178.204/SafeHeaven/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirbuster/directory-list-lowercase-2.3-medium.txt

===============================================================
2024/05/01 19:53:53 Starting gobuster
===============================================================
/imgs (Status: 301)
/keeper (Status: 301)
===============================================================
```

