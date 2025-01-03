# PicoCtf

## Forensics
### 1. Blast from the past
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

### 2. Mob Psycho
- Don't get feared by `.apk` files !
- Some time its nothing to do with apks
- try to find if there is are `.txt` file or not
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ find * -name "*.txt"
res/color/flag.tx
```
### 3. endianness-v2
- check the file!
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ exiftool challengefile
ExifTool Version Number         : 12.76
File Name                       : challengefile
Directory                       : .
File Size                       : 3.4 kB
File Modification Date/Time     : 2024:03:12 06:36:50+06:00
File Access Date/Time           : 2024:10:27 16:18:46+06:00
File Inode Change Date/Time     : 2024:10:27 16:18:36+06:00
File Permissions                : -rw-r--r--
Warning                         : Processing JPEG-like data after unknown 1-byte header
```
- This is a jpeg file it seems to be
- `ghex challengefile` this command give us the hex which is `\E0\FF\D8\FF`
-  But if we see the actual hex of jpeg which is `ff d8 ff e0`
-  So it has been reversed!
-  We will reverse it as well
```sh
hexdump -v -e '1/4 "%08x"' -e '"\n"' challange | xxd -r -p > output_file
```
- The flag is `picoCTF(cert!f1Ed_iNd!4n_s0rrY_3nDian_6d3ad08e}`
- We went on this approach becasue it said about `endianness`

### 4. MSB
- The description and name of challenge suggests data may be hidden in the Most Significant Bit (MSB) of the RGB pixels values within the image.
- I will use a script which will do that for me
- [sigBits](https://github.com/Ruhanyat-994/myCTF/tree/master/my-materials/Scripts/sigBits)

### 5. Sleuthkit Apprentice
```sh
┌──(bc-here㉿BC-Here)-[/tmp]
└─$ mmls disk.flag.img
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000206847   0000204800   Linux (0x83)
003:  000:001   0000206848   0000360447   0000153600   Linux Swap / Solaris x86 (0x82)
004:  000:002   0000360448   0000614399   0000253952   Linux (0x83)

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ fls -o 0000360448 disk.flag.img
d/d 451:        home
d/d 11: lost+found
d/d 12: boot
d/d 1985:       etc
d/d 1986:       proc
d/d 1987:       dev
d/d 1988:       tmp
d/d 1989:       lib
d/d 1990:       var
d/d 3969:       usr
d/d 3970:       bin
d/d 1991:       sbin
d/d 1992:       media
d/d 1993:       mnt
d/d 1994:       opt
d/d 1995:       root
d/d 1996:       run
d/d 1997:       srv
d/d 1998:       sys
d/d 2358:       swap
V/V 31745:      $OrphanFiles

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ fls -o 0000360448 disk.flag.img 11

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ fls -o 0000360448 disk.flag.img 1995
r/r 2363:       .ash_history
d/d 3981:       my_folder

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ fls -o 0000360448 disk.flag.img 3981
r/r * 2082(realloc):    flag.txt
r/r 2371:       flag.uni.txt

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ icat -o 0000360448 disk.flag.img 2371
picoCTF{by73_5urf3r_3497ae6b}
```

### 6. Redaction gone wrong
- If anything given to you which says secured of redacted data on a pdf try to check the basic security flaw
- Here A pdf was given and There are some data which has been redacted through black ink
- I just tried to copy that with ctrl+A and ctrl+C
- Paste is to another file and Majic! there wasn't the redaction there

### 7.# OR
```sh

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ pdftotext Financial_Report_for_ABC_Labs.pdf

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ ls
Financial_Report_for_ABC_Labs.pdf  Financial_Report_for_ABC_Labs.txt

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ cat Financial_Report_for_ABC_Labs.txt
Financial Report for ABC Labs, Kigali, Rwanda for the year 2021.
Breakdown - Just painted over in MS word.

Cost Benefit Analysis
Credit Debit
This is not the flag, keep looking
Expenses from the
picoCTF{C4n_Y0u_S33_m3_fully}
Redacted document.

```

### 8. Operation Orchid
```sh

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ icat -o 0000411648 disk.flag.img 1782
Salted__0��!�-6V����0�U��l��&�:�pj_1�0�|�h
                                          �Ȥ7� ���؎$�'%

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ icat -o 0000411648 disk.flag.img 1782 > flag.txt.enc


┌──(bc-here㉿BC-Here)-[/tmp]
└─$ openssl aes256 -d -salt -in flag.txt.enc -out flag.txt -k unbreakablepassword1234567
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.
bad decrypt
80A67144627F0000:error:1C800064:Provider routines:ossl_cipher_unpadblock:bad decrypt:../providers/implementations/ciphers/ciphercommon_block.c:107:

┌──(bc-here㉿BC-Here)-[/tmp]
└─$ cat flag.txt
picoCTF{h4un71ng_p457_0a710765}

```

### 9. File Type
[Look Here](https://github.com/Ruhanyat-994/myCTF/blob/master/PicoCTF/File_Type(forensics_pico).md)

### 10. Evesdrop
- You need to save the file from wireshark
```sh
┌──(bc-here㉿BC-Here)-[~]
└─$ openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
*** WARNING : deprecated key derivation used.
Using -iter or -pbkdf2 would be better.

┌──(bc-here㉿BC-Here)-[~]
└─$ cat file.txt
picoCTF{nc_73115_411_5786acc3}
```
### 11. WPA-ing Out
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ aircrack-ng -w /usr/share/wordlists/rockyou.txt wpa-ing_out.pcap

                               Aircrack-ng 1.7

      Time left: 29 minutes, 19 seconds                          0.02%

                          KEY FOUND! [ mickeymouse ]


```
### 12. advanced-potion-making
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ ghex advanced-potion-making
```
- After checking the hex data it looks like it has some sort of data which a `.png` file has
- So I changed the hex to png format `89 50 4E 47 0D 0A 1A 0A 00 00 00 0D`
- After that I found a completely red picture so I decided to use `zsteg photo.png` for that but it gave me nothing
- There is another tool I found on a github page [stegsolve](https://github.com/zardus/ctf-tools/blob/master/stegsolve/install)

```sh
┌──(bc-here㉿BC-Here)-[~/TOOLS]
└─$ java -jar /opt/stegsolve.jar
```
- Nice I got the flag which is `picoCTF{w1z4rdry}`
### 13. Matryoshka doll
- Sometime when you won't get anything from a picture do `unzip file.ext`

### 14. Wireshark doo dooo do doo...
- find tcp.stream eq <1-5>
- follow tcp or http stream in ASCII mode

### 15. Wireshark twoo twooo two twoo...
- I have checked the pcap file in wireshark And found too many dns query in two servers `8.8.8.8` and another one
**Commands**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ tshark -nr shark2.pcapng -Y 'dns'

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ tshark -nr shark2.pcapng -Y 'dns' | grep -v '8.8.8.8' | grep -v response | grep -v local | awk -e '{print $13}' | sed -e 's/\..*//' | base64
-d
picoCTpicoCTF{dns_F{dns_3xf1l_3xf1l_ftw_deftw_deadbeefadbeef}}}}
```

### 16. Trivial Flag Transfer Protocol
- Here we will know about the TFTP protocol which is a kind of file transfer protocol
- At first open the pcap file and go to `file>Export objects>TFTP`
- Then you will find some files , download them all
- open the first file which is `instructions.txt` it gives us a hash to decode
**Encoded**
```sh
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```
- I tried to cyber chef and it was ROT13
**Decoded**
```sh
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```
**More specific**
```sh
TFTP DOESN’T ENCRYPT OUR TRAFFIC, SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG, AND I WILL CHECK BACK FOR THE PLAN.
```
- `PLAN` this is my thing to get into
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ cat plan
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```
- It is also a ROT13
**Decoded**
```sh
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```
- `DUEDILIGENCE` is highlighted here and its also saying to run the `program.deb`, lets do it
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ sudo apt-get install ./program.deb
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Note, selecting 'steghide' instead of './program.deb'
.
.
.
.
.

```
- There is a hint here which is `Note, selecting 'steghide' instead of './program.deb'`
- Lets use steghide with `DUEDILIGENCE` as a passphrase
- It didn't work for pic1 and 2 but worked perfectly for pic3
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ steghide extract -sf ./picture3.bmp -p "DUEDILIGENCE"
the file "flag.txt" does already exist. overwrite ? (y/n) y
wrote extracted data to "flag.txt".

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ ls
flag.txt  instructions.txt  picture1.bmp  picture2.bmp  picture3.bmp  plan  program.deb  tftp.pcapng

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ cat flag.txt
picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
```
### 17. Pitter, Patter, Platters
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ fls suspicious.dd.sda1
d/d 11: lost+found
d/d 2009:       boot
d/d 4017:       tce
r/r 12: suspicious-file.txt
V/V 8033:       $OrphanFiles

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ icat suspicious.dd.sda1 12
Nothing to see here! But you may want to look here -->

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ strings -e b suspicious.dd.sda1
61d907ec_3<_|Lm_111t5_3b{FTCocip
qQWTYUiIOPb
FGjJKLs
ZXvc
#+3;CScs
!1Aa
qQWTYUiIOPb
FGjJKLs
ZXvc
#+3;CScs
!1Aa
#+3;CScs
!1Aa
7777777777

┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ strings -e b suspicious.dd.sda1 | rev
picoCTF{b3_5t111_mL|_<3_ce709d16
```
### 18. shark on wire 2
**Filters**
```sh
udp.ports == 22
ipp.addr == 10.0.0.66
```
- It is indicating that same ip address is connecting with another one with many differect ports
- Its fishy
- So with the help of python I worte script which will give me all the ports in a single file and make them horizontal with spaces
**Script**
```sh
import pyshark

# Input pcap file
pcap_file = "capture.pcap"
# Output file to store source ports
output_file = "source_ports.txt"
# Target IP address to filter
target_ip = "10.0.0.66"

try:
    # Open the pcap file
    capture = pyshark.FileCapture(pcap_file, display_filter=f'ip.addr == {target_ip}')

    # Open the output file in write mode
    with open(output_file, "w") as file:
        print(f"Processing packets from {pcap_file}...")
        # Loop through packets and extract source ports
        for packet in capture:
            # Ensure packet has a transport layer (e.g., TCP/UDP)
            if hasattr(packet, 'transport_layer'):
                src_port = packet[packet.transport_layer].srcport
                file.write(f"{src_port}\n")

    print(f"Source ports written to {output_file}")
except Exception as e:
    print(f"Error occurred: {e}")
finally:
    # Release resources
    if 'capture' in locals():
        capture.close()
```
```sh
pip install pyshark
```
- Then I convert them from Decimal to ASCII
## Cryptography
### 17. endianness
- **The term endianness describes the order in which computer memory stores a sequence of bytes**
- Big-endian: The most significant byte (the "big end") is stored first. For example, if you had the number 0x12345678 (in hexadecimal), in big-endian it would be stored in memory as `12 34 56 78`.

- Little-endian: The least significant byte (the "little end") is stored first. So, the same number 0x12345678 would be stored as `78 56 34 12` in little-endian.
- Use `reverse by character` and `to hex` in CyberChef.

### 18. Commitment Issues
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
### 19. Blame Game
```sh
git log <file>.py
```

### 20. repetitions
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/PicoCtf]
└─$ base64 -d enc_flag | base64 -d |  base64 -d | base64 -d |  base64 -d| base64 -d
```
- Sometime we need to repeat the sequence
### 21. Big Zip
```sh
 grep -r big-zip-files -e pico
```
### 22. Find First
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
