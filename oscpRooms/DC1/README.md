# DC 1 
The last battle between good and evil 

## Enumeration:
    - Ports opened: 22 SSH, 80 HTTP, and 111 RPC 
    - From the NMAP scan, I found that it is a drupal site.

### Website Enumeration: 
    - Looking at the source code, I found that it was a Drupal 7 site 

## Foot hold:
    - I took a chance on a Drupal 7 RCE vulnerability and turns out it was vulnerable to CVE-2014-3704 
    - The python file allows me to create an administrator account on the website 
    - I wrote a post with PHP injection on it to give me a reverse shell into www-data 

## Privilege Escalation:

### Enumeration: 
    - Searching for SUID binaries that are exploitable through this command `find / -perm -u=s -type f 2>/dev/null`
    - This gave a list of binaries I could use. 
    - Cross referencing GTFO bins with the list gave me this command for escalation 
    - `./find . -exec /bin/sh -p \; -quit`
