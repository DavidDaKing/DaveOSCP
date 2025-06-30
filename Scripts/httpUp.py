'''
    Name: Python listener

    Desc:
        To run on target system 
'''

import socket
import subprocess
import os

# Global Host var
# May have to assign it to tun0 ip address
HOST = "0.0.0.0"

# Global port var
PORT = 9999



def main():
    print("HTTP Server is up!") 

if __name__ == "__main__":
    main()
