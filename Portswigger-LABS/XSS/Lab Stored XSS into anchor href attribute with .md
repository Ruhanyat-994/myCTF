# Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

[https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-href-attribute-double-quotes-html-encoded)

[https://youtu.be/3jFVfS9BsDc](https://youtu.be/3jFVfS9BsDc)

# payload:

> ### javascript:alert("Hakced by RuhanSec")

![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/image.png?raw=true)

1. for doing this lab you have to check every endpoint where you can find stored xss
2. check if there is any unusual things or not
3. here we found if we type a website to the website section , after posting the comment it appends to the name and if we click the name it will redirect to the website
4. so we have to check the developers tool for that 
5. and as we know we can add javascript:payload to an endpoint where there is an existence of urls like href
6. and that all we can do PAWNED!