# Metasploit
----


- **The Metasploit Framework is a set of tools that allow information gathering, scanning, exploitation, exploit development, post-exploitation, and more. While the primary usage of the Metasploit Framework focuses on the penetration testing domain, it is also useful for vulnerability research and exploit development.**


- **Auxiliary:Any supporting module, such as scanners, crawlers and fuzzers, can be found here.**
- **Encoders: Encoders will allow you to encode the exploit and payload in the hope that a signature-based antivirus solution may miss them.**
    - **Signature-based antivirus and security solutions have a database of known threats. They detect threats by comparing suspicious files to this database and raise an alert if there is a match. Thus encoders can have a limited success rate as antivirus solutions can perform additional checks.**

- **Evasion: While encoders will encode the payload, they should not be considered a direct attempt to evade antivirus software. On the other hand, “evasion” modules will try that, with more or less success.**

- **Exploits: Exploits, neatly organized by target system.**
- **Payloads: Payloads are codes that will run on the target system.**

### Adapters
An adapter wraps single payloads to convert them into different formats. For example, a normal single payload can be wrapped inside a Powershell adapter, which will make a single PowerShell command that will execute the payload.

### Singles
Self-contained payloads (e.g., add user, launch notepad.exe) that do not need to download an additional component to run.

### Stagers
Responsible for setting up a connection channel between Metasploit and the target system. Useful when working with staged payloads. "Staged payloads" will first upload a stager on the target system, then download the rest of the payload (stage). This provides some advantages, as the initial size of the payload will be relatively small compared to the full payload sent at once.

### Stages
Downloaded by the stager. This will allow you to use larger-sized payloads.

### Metasploit Payload Identification

Metasploit has a subtle way to help you identify single (also called "inline") payloads and staged payloads:

- `generic/shell_reverse_tcp`
- `windows/x64/shell/reverse_tcp`

Both are reverse Windows shells. The former is an inline (or single) payload, as indicated by the "_" between "shell" and "reverse". The latter is a staged payload, as indicated by the "/" between "shell" and "reverse".

### Commands
```sh
help
use /path

show options
 
show payloads

msf6 exploit(windows/smb/ms17_010_eternalblue) > back
msf6 > 

msf6 exploit(windows/smb/ms17_010_eternalblue) > info

msf6 > search wordpress

msf6 > use 41
 // using numbers instead of path

msf6 > search type:auxiliary telnet

msf6 > set rport

msf6 > set rhosts

msf6 > unset all

/ it will unset them

exploit -z
```
- **The exploit command can be used without any parameters or using the “-z” parameter.The exploit -z command will run the exploit and background the session as soon as it opens.**

```sh
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions

Active sessions
===============

  Id  Name  Type                     Information                 Connection
  --  ----  ----                     -----------                 ----------
  1         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ JON-  10.14.86.101:4444 -> 10.10.
                                     PC                          41.232:49267 (10.10.41.232)


msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > background
[*] Backgrounding session 1...
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions -i 1
[*] Starting interaction with 1...

meterpreter > 

```