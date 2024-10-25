# PicoCtf

## Forensics
### Blast from the past
- Try to see the metadata from exiftool
- For changing timestamp use exiftool
```sh
exiftool -Alldates='1970:01:01 00:00:00.001+00:00' -CreateDate='1970:01:01 00:00:00.001+00:00' -ModifyDate='1970:01:01 00:00:00.001' -SubSecCreateDate='1970:01:01 00:00:00.001' -SubSecDateTimeOriginal='1970:01:01 00:00:00.001' -SubSecModifyDate='1970:01:01 00:00:00.001' original.jpg
```
- still samsung time zone is not set.
- We have to set it through hex code
- I use `ghex` for that
- I changed all the last hex to 0 and at the end I changed 30 to 31 because there is a 001 milisecond timestamp
- then upload the file and boom!

### Mob Psycho
- Don't get feared by `.apk` files !
- Some time its nothing to do with apks
- try to find if there is are `.txt` file or not
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ find * -name "*.txt"
res/color/flag.tx
``` 


## Cryptography
### endianness
- **The term endianness describes the order in which computer memory stores a sequence of bytes**
- Big-endian: The most significant byte (the "big end") is stored first. For example, if you had the number 0x12345678 (in hexadecimal), in big-endian it would be stored in memory as `12 34 56 78`.

- Little-endian: The least significant byte (the "little end") is stored first. So, the same number 0x12345678 would be stored as `78 56 34 12` in little-endian.
- Use `reverse by character` and `to hex` in CyberChef. 

### Commitment Issues
```sh

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf/drop-in]
└─$ git log
commit 144fdc44b09058d7ea7f224121dfa5babadddbb9 (HEAD -> master)
commit 7d3aa557ff7ba7d116badaf5307761efb3622249

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf/drop-in]
└─$ git checkout 144fdc44b09058d7ea7f224121dfa5babadddbb9

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf/drop-in]
└─$ git checkout 7d3aa557ff7ba7d116badaf5307761efb3622249

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf/drop-in]
└─$ cat message.txt
picoCTF{s@n1t1z3_be3dd3da}
```
### Blame Game
```sh
git log <file>.py
```

### repetitions
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ base64 -d enc_flag | base64 -d |  base64 -d | base64 -d |  base64 -d| base64 -d
```
- Sometime we need to repeat the sequence
### Big Zip
```sh
 grep -r big-zip-files -e pico
```
### Find First
```sh
strings files.zip| grep pico
```


## Web Exploitation
**Bookmarklet**   

![firefox-1](https://github.com/user-attachments/assets/f8b04772-781d-4eb2-a040-0245a8068ff8)


**Local Authority**
- Always check the get request and find if there any directory is in the response or not

**Scanvenger Hunt**
- Always try to find the directorys which has `.js`,`.css` extensions and `/robots.txt`,`/.htaccess`,`/.DS_Store`

**dont-use-client-side** 
- When you find parallelly same things are giving you different requests then try to check the response by `Changing the Header`


