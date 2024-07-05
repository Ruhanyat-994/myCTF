# Jeopardy-style CTFs

## Recon

### Port Scanning
- #### **nmap: For normal port scan**
```sh
nmap -sS -sV -O <ip> >> ports.txt
```
- **For aggressive port scan we will use**
```sh
nmap -A -p <ports that we found from normal scan> >> ports.txt
```

### Directory Enumeration

- #### **Gobuster**
```sh
gobuster dir -u http://targetIp -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o directory.txt
```


### Some Important commands

- #### **Finding file Type**
```sh
file <filename>
```

- #### **Running Python Server**
```sh
python3 -m http.server 80
```

- #### **Basic Stegnography**
```sh
steghide extract -sf <PictureName>
```




### FTP Commands
```sh
mget <filename>
mget *
mget *.fileextention
```
- `mget` will download file from the ftp to your local machine


## Scripts

