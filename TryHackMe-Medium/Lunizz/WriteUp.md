![alt text](image.png) 

----

## Initial Foothold
**PortScanning**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/lunizz]
└─$ sudo python3 pymap.py -t luni.thm --all >> ports.txt

[+] Port scanning...
80/tcp   open  http
3306/tcp open  mysql
4444/tcp open  krb524
5000/tcp open  upnp
```
- Here we found some ports but the mysql seems very suspicious to me
- And the other two unknown ports `krb524` & `upnp` are also interesting. I will use them with the webserver



**Directory Enumeration**
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/lunizz]
└─$ feroxbuster -u http://luni.thm/ >> ferox.txt

http://luni.thm/hidden 

http://luni.thm/hidden/uploads

http://luni.thm/whatever/

```
```sh
┌──(bc-here㉿BC-Here)-[~/CTF/THM/lunizz]
└─$ cat directory.txt
/instructions.txt     (Status: 200) [Size: 339]
/hidden               (Status: 301) [Size: 305] [--> http://luni.thm/hidden/]
/whatever             (Status: 301) [Size: 307] [--> http://luni.thm/whatever/]

```

## Web Server Enumeration
**Looking for File Upload Vuln**
- At `http://luni.thm/hidden/` 

![alt text](image-1.png)

- I thought There will be a file upload vulnerability , I might have but I couldn't break the validation

**Try to Break Command Executer Validation**

- At `http://luni.thm/whatever/` I found a command executer, I thought My command may work but its only reflecting the command I might be for the validation. It may restricted the command executer in its DataBase. And Look we also found that there is a mysql server is up and running.

![alt text](image-2.png)


****

- At `http://luni.thm:4444/` I found a hash code , Lets break it
