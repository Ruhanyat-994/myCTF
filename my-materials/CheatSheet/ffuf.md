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
