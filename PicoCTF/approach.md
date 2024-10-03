# PicoCtf
## endianness
- **The term endianness describes the order in which computer memory stores a sequence of bytes**
- Big-endian: The most significant byte (the "big end") is stored first. For example, if you had the number 0x12345678 (in hexadecimal), in big-endian it would be stored in memory as `12 34 56 78`.

- Little-endian: The least significant byte (the "little end") is stored first. So, the same number 0x12345678 would be stored as `78 56 34 12` in little-endian.
- Use `reverse by character` and `to hex` in CyberChef. 

## Commitment Issues
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
## Blame Game
```sh
git log <file>.py
```
