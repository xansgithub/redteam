# Alex Farley
# arf2846@rit.edu
# Client program to interact with server.py

import socket
import sys

# host = sys.argv[1]
# port = int(sys.argv[2])

host = "127.0.0.1"
port = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except:
    print("Connection failed!")
    sys.exit()

print("Connection established!")

# msg_sent = ""

# while msg_sent != "exit":
#     msg_sent = input("Enter message: ")
#     s.send(msg_sent.encode)
#     print(s.recv(4096).decode())
# s.close()