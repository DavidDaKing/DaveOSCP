### Active Directory Basic Enumeration 

## Host Discovery
    - command: `fping -agq [target ip]/24`
    - results: .10, .20, .250 up
    - command: `nmap -T5 -p- -sV -sC -iL results`
    - The domain controller will often have ports 88 (kerberos), 389 (LDAP), and 445 (SMB) open

## SMB Enumeration: 
    - Try to connect to SMB anonymously. 
    - command: smbclient -L //target -N 
    - command: smbmap -H [target]
    - command: nmap -p445 --script smb-enum-shares [target]
    - to access share: smbclient //target/dir -N 

## LDAP Enumeration:
    - command: ldapsearch -x -H ldap://target -s base
    - command: ldapsearch -x -H ldap://target -b "dc" "object"
# enum4linux
    - command: enum4linux-ng -A [target] -oA resultsFile
    
