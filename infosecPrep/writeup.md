# Enumeration: 
## Open Ports:
### 22 - SSH - 8.2p1 Ubuntu 
### 80 - HTTP - Word Press Site
#### username found: oscp
## Directories:
### /secret.txt
#### notes: found ssh private key encoded in base64 

# Privilege Escalation: 
## Enumeration:
### command used: `find / -perm -4000 -type f -ls 2>/dev/null`
### notes: /usr/bin/bash -> -rwsr-sr-x root root 
