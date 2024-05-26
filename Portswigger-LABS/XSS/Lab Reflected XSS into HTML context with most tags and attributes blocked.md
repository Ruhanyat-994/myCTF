# Lab: Reflected XSS into HTML context with most tags and attributes blocked

# [Lab Link](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-html-context-with-most-tags-and-attributes-blocked)

## Endpoints
```plaintext
https://0a7300ea032c4309808162fe004f0065.web-security-academy.net/?search=
```

> #### 1. If we input  a payload on this endpoint it gives us a warning!
> #### 2. It means there is a firewall here.

## Payloads

```js
hello"onmouseover="<script>alert('1')</script>
```
> ##### This is the initial payload! This is giving us error. It means onmouseover is validated by the backend.

## Error

![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/error_image.png?raw=true)

## Arguments 

**1. Everything is not validated**
```js
<>
<body>
// This are not validated
```  

**2. We have to find out which tags are not validated or we have to craft a tag as its not seeming a tag which is validated**

> ##### We use The boss to check which are not validated 
# <span style="color: orange;">Burp Intruder</span>


![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder1.png?raw=true)

# [CheatSheet!](https://portswigger.net/web-security/cross-site-scripting/cheat-sheet)

```plaintext
Process
--------------------------------
1. We will clear all the bruteforce tags

2. Then we will add <> because we found that this is not validated.

3. We will use a $ tag here to bruteforce

4. Now we need a list of tags by which we can iterate the tags which are not validated

5. Here we can use the xss cheat sheet by web academy. We can directly copy that to the clipboard.

```

![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder2.png?raw=true)

```plaintext
Process
--------------------------------
6. We can paste them into the payload section

7. Start Attack

8. If we are getting a 200 response status code it means that tag is not validated
```  
![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder3.png?raw=true)  

![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder4.png?raw=true)  



## Payload

```js
<body onload="alert(1)">
```
```plaintext
Process
--------------------------------
9. Now if we use this payload at the   endpoint
it will give us "Attribute is not allowed"

10. It means that body is not validated but onload is validated

11. Now we will repeat the same thing.

12. Previously we copied the tags from the cheatsheet but now we will copy the attributes

``` 
![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder5.png?raw=true)


![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/intruder6.png?raw=true)


## Payload
```js
<body onresize="print()">
```
```plaintext
Process
--------------------------------
13. If we use this payload it won't give us an any WAF message.

14. But nothing happend 

15. But if we resize the webpage the xss will work and take us to print the page functionality

16. We can actually use an iframe on an attacker page to rendaring the page to use the onresize(this will be work onload) without having any user interection.
``` 


## Tips:
```Plaintext


If you find a XSS altime try to do it without having any user interection. 
It will become more vulnerable for that case.
```
## Payload
```js

<iframe src=https://0a17002f03a45e3e800df82b008400ed.web-security-academy.net/?search=%3Cbody+onresize%3D%22print%28%29%22%3E width='100px'>
```
