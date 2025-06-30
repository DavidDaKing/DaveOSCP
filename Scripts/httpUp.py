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

# Global Host var
# May have to assign it to tun0 ip address or pass in target address
HOST = "127.0.0.1"

# Global port var
PORT = 9999

#  Creating the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Binding the socket to tun0 and port 
server.bind((HOST, PORT))

# Listening for connections * most likely me with NC! 
server.listen(0)
print(f"Listening on {HOST}:{PORT}")

# Accept the nc connection
client_socket, client_address = server.accept()
print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

# Data loop
while True:
    request = client_socket.recv(1024)
    request = request.decode("utf-8")

    if request.lower() == "close":
        client_socket.send("closed".encode("utf-8"))
        break

    print(f"Recieved: {request}")

    # Sending response 
    response = "Hello,attacker".encode("utf-8")
    client_socket.send(response)


print("Server shut down")

# Closing the server 
client_socket.close()
server.close()

def main():
    print("HTTP Server is up!") 

if __name__ == "__main__":
    main()
