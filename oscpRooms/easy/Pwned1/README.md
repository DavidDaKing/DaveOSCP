# Pwned 1 
This network has been attacked, I have to find what the advesary has done. 


## Information:
    - ** Credentials: ** ftpuser/B0ss_Pr!ncess 
    - ** Employee Names: ** ariana, selena

## Ports Opened:
    - 21, ftp 
    - 22, ssh 
    - 80, http 

## Enumeration:
    - FTP: With the given credentials to the ftp server, I found an ssh private key, a shell script, and a note.
    - Website:
        - Told to investigate the employees. 
        - Robots.txt -> /nothing, /hidden_text
        - /hidden_text -> found a secret directory list 
    - pwned.vuln -> hacked logon page

## Idea:
    - Use the list of employees thats given and the id_rsa file found through ftp enumeration to log into the ssh server. 
    - Able to log in as Ariana in ssh 

## Privilege Escalation (Ariana): 
    - sudo -l -> ability to run a script as selena w/ sudo 
    - Got a shell as selena (lateral movement within the network)

## Privilege Escalation (Selena): 
    - id -> Selena is assigned to the docker group 
    - GTFO bin provided the payload to take advantage of this vulnerability.
