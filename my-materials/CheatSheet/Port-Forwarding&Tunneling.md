## Dynamic Port Forwarding

```sh
sudo gedit /etc/proxychains4.conf

socks4 	127.0.0.1 9050

ssh -D 9050 target@<target-ip>

target@machine#
<we are in>
```
- If we know the password of the target machine , then we will be able to get into that machine.
- We can also do that in our network for connecting to a remote server from your local system .

```sh
proxychains nmap -v -p 22,21,44,448 <random-ip>
```
- **If we run this command from attacking machine while enabling the target machines ssh , the command will work as if its working from the target machine .**

- The proxychain will be maintained through port `9050`.


## Local Port Forwarding

```sh
ssh -L 1234:localhost:3000 target@<target-ip>

```

- If something is running on the `localhost:3000` of the target machine you can run that thing to you machines `localhost:1234`  

**Scenario:**
- Suppose we have two targets , target1 and target2
- Target2 is a subnet of target1
- Now we have the password of target1, and target2
- Now we will jump from target1 to target2 over the ssh tunnel and access target2 from our attacking machine.

```sh
ssh -J target1@<target1-ip> -D localhost:9050 target2@<target2-ip>
```
- We will connect through port 9050.