![alt text](image.png)

# Wireshark

![alt text](image-1.png)

![alt text](image-2.png)

![alt text](image-3.png)

 



# Wireshark Filters
----
## For successful Handshake 
```pcap
tls.handshake.type eq 1
```

## This is for all http req and tls handshake but we are avoiding ssdp
```pcap
(http.request or tls.handshake.type eq 1) and !(ssdp)
```

![alt text](image-4.png)