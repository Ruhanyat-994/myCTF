# Lab: DOM XSS in document.write sink using source location.search inside a select element

# ***[LAB LINK](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)***

### Approach:
```plaintext
1. We have to check the dropdown manu
2. In the dropdown we can find an extra parameter
3. Adding the param with the existing link we can add our payload
4. In a  DOM based xss  we have to find exactly where our inputs are getting stored in the DOM of js.
```