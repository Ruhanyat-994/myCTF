# Ninja Skills
----

## List of file
```sh
    8V2L
    bny0
    c4ZX
    D8B3
    FHl1
    oiMO
    PFbD
    rmfX
    SRSq
    uqyw
    v2Vb
    X1Uy
```
- This is totally a linux `find` based challenge


1. **Which of the above files are owned by the best-group group(enter the answer separated by spaces in alphabetical order)**

```sh
$ find / -type f -group best-group 2>/dev/null

/mnt/D8B3
/home/v2Vb

```
2. **Which of these files contain an IP address?**

```sh
$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec grep -E -o '[0-9][0-9]*[.][0-9][0-9]*[.][0-9][0-9]*[.][0-9][0-9]*' * {} \; 2>/dev/null

/opt/oiMO:1.1.1.1

```

3. **Which file has the SHA1 hash of 9d54da7584015647ba052173b84d45e8007eba94**
```sh
$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec sha1sum {} \; 2>/dev/null  | grep  9d54da7584015647ba052173b84d45e8007eba94
9d54da7584015647ba052173b84d45e8007eba94  /mnt/c4ZX

```
4. **Which file contains 230 lines?**
```sh
$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec wc -l {} \; 2>/dev/null 
209 /mnt/D8B3
209 /mnt/c4ZX
209 /var/FHl1
209 /var/log/uqyw
209 /opt/PFbD
209 /opt/oiMO
209 /media/rmfX
209 /etc/8V2L
209 /etc/ssh/SRSq
209 /home/v2Vb
209 /X1Uy

```
- **Here one file is missing it probably have the 230 line in it**
- **The file is `bny0`**

5. **Which file's owner has an ID of 502?**

```sh
$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -ln {} \; 2>/dev/null | grep 502
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /mnt/D8B3
-rw-rw-r-- 1 501 502 13545 Oct 23  2019 /home/v2Vb
-rw-rw-r-- 1 502 501 13545 Oct 23  2019 /X1Uy

```
- **Here the answer is `X1Uy`**

6. **Which file is executable by everyone?**
```sh
$ find / -type f \( -name 8V2L -o -name bny0 -o -name c4ZX -o -name D8B3 -o -name FHl1 -o -name oiMO -o -name PFbD -o -name rmfX -o -name SRSq -o -name uqyw -o -name v2Vb -o -name X1Uy \) -exec ls -l {} \; 2>/dev/null | grep rwxrwx
-rwxrwxr-x 1 new-user new-user 13545 Oct 23  2019 /etc/8V2L
```
- **The file is `8V2L`**