
### File Type
```sh
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ sh flag.sh
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ ar x flag
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag Flag

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ cpio -i < Flag
2 blocks

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: bzip2 compressed data, block size = 900k

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.bz2

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ bzip2 -dv flag.bz2
  flag.bz2: done

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: gzip compressed data, was "flag", last modified: Thu Mar 16 01:40:15 2023, from Unix, original size modulo 2^32 328

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.gz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ gunzip flag.gz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ lzip -d flag.lz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: LZ4 compressed data (v1.4+)

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.lz4

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ lz4 flag.lz4
Decoding file flag
flag.lz4             : decoded 266 bytes


┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: LZMA compressed data, non-streamed, size 255

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.lzma

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ lzma -d flag.lzma

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.lz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag.lz flag.lzo

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ lzop -d flag.lzo

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: lzip compressed data, version: 1

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.lz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ lzip -d flag.lz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: XZ compressed data, checksum CRC64
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mv flag flag.xz

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ xz -d flag.xz
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ file flag
flag: ASCII text

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ cat fi
cat: fi: No such file or directory

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f33633739633562617d0a
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ cat flag | xxd -r -p
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
```
