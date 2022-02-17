# Alex Farley
# arf2846@rit.edu
# Server program to interact with client.py

import socket
import sys

# host = sys.argv[1]
# port = int(sys.argv[2])

host = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))
s.listen()
s.accept()

# msg_received = ""

# while msg_received != "exit":
#     msg_received = s.recv(4096)
#     s.send(b"Message received! Type 'exit' to close.")

print("Connection established!")

s.close()

