# ffuf
**ffuf stands for `Fuzz Faster U Fool`. It's a tool used for web enumeration, fuzzing, and directory brute forcing.**

## Web-content
```sh
ffuf -u https://domain.hack/FUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/big.txt:FUZZ
```

## Web-Extension
```sh
ffuf -u https://domain.hack/indexFUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Co
ntent/web-extensions.txt
```
## By Extension
```sh
ffuf -u https://domain.hack/indexFUZZ -w /usr/share/wordlists/seclists/Discovery/Web-Content/raft-medium-words-lowercase.txt -e .php,.txt
```

**Sometimes We had a lot of output but not much was useful.For that we can filter out things. Like all 400 errors can be filter out cause we don't need them**
## Filtering Error Codes
```sh
ffuf -u http://https://daffodilvarsity.edu.bd/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt:FUZZ -fc 403
```
## Matching Specific Codes
```sh
 ffuf -u http://https://daffodilvarsity.edu.bd/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-directories-lowercase.txt:FUZZ -mc 200
```
**For more matcher you can use `ffuf -h | grep -A 10 "MATCHER"`**
**For more filters you can use `ffuf -h | grep -A 8 "FILTER"`**

## Filtering the extensions through `regex`
```sh
ffuf -u http://domain.hack/FUZZ -w /usr/share/seclists/Discovery/Web-Content/raft-medium-files-lowercase.txt -fr '/\..*'
```
## Fuzzing Parameters

### Using burp-param
```sh
ffuf -u 'http://hello.hacked?idx=&qFUZZ=1&weight_search=1' -c -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt -fw 39
```

- If it gives 200 ok it means we can input Integers.

### Using generated Wordlist
```sh
seq 0 255 | ffuf -u 'happyhacking.hack?idx=&FUZZ=0&weight_search=1' -c -w - -fw 33
```
- Replace this `seq 0 255 ` to your wordlist generator and pipe the `ffuf` command.
-  `-w -` which tells `ffuf` to read a wordlist from `stdout`.

### Wordlist-based brute-force attacks
```sh
ffuf -u http://happyhacking.com/sqli-labs/Less-11/ -c -w /usr/share/seclists/Passwords/Leaked-Databases/hak5.txt -X POST -d 'uname=Dummy&passwd=FUZZ&submit=Submit' -fs 1435 -H 'Content-Type: application/x-www-form-urlencoded' 
```
- `-H 'Content-Type: application/x-www-form-urlencoded' ` this is for http request. Here `Content-Type:` is a http request header.
- We  have to specify a custom header ` -H 'Content-Type: application/x-www-form-urlencoded'` because `ffuf` doesn't set this content-type header automatically as curl does.

## Finding VHOST and Subdomains

### Subdomains
```sh
ffuf -u http://FUZZ.mydomain.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

- **In bug bounty hunting, VHost (Virtual Host) refers to a method where multiple domains or websites are hosted on the same server, each one identified by a unique domain name. VHost misconfigurations can lead to vulnerabilities in the web application that allow attackers to access unauthorized content or gain unintended access to other domains hosted on the same server.**

- **virtual hosts (vhosts) is the name used by Apache httpd but for Nginx the right term is Server Blocks.**

### VHOST
```sh
ffuf -u http://mydomain.com -c -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H 'Host: FUZZ.mydomain.com' -fs 0
```

### Proxifying FFUF Traffic
```sh
ffuf -u http://hackeme.com/FUZZ -c -w /usr/share/seclists/Discovery/Web-Content/common.txt -x http://127.0.0.1:8080
```


# Common Commands
```sh
ffuf -u http://ffuf.me/cd/basic/FUZZ -w common.txt
ffuf -w common.txt -e .log -u http://ffuf.me/cd/ext/logs/FUZZ
ffuf -u http://ffuf.me/cd/recursion/FUZZ -w common.txt -recursion
ffuf -w common.txt -u http://ffuf.me/cd/no404/FUZZ -mc 204,301,302,307,401,403,405,500,200 -fs 669 // this has been filtered by file size and status code
ffuf -w common.txt -u http://ffuf.me/cd/no404/FUZZ -mc 204,301,302,307,401,403,405,500,200 -ac // this will filterout all its own
```
