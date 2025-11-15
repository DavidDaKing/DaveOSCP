# DC2 
Back and Forth story 

## Enumeration:
    - Ports opened: 80 http, 7744 SSH
    - I found that it is a word press site.
    - The main page gave a hint for flag 1 
    - The WP version is 4.7.10
    - Users are: admin, tom, and jerry 
    - found users through this command `wpscan --url dc-2 --enumerate u`

## Password Bruteforcing: 
    - In this room, I've done bruteforcing through wpscan and hydra. 
    - The hint entailed that the usual word lists won't work.
    - I found online that the cewl command had to be used and since I didn't have any experience with it, I looked up how to execute it 
    - cewl dc-2 | tee list 

## Privilege escalation: 
    - Had to break out of restrictive bash first 
    - su - attempts with tom then jerry 
    - jerry worked, sudo -l led me to /usr/bin/git 
    - GTFO bins for git
