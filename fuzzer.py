#!/usr/bin/python3

import socket,time

IP = ""
PORT = 1234

count = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

while True:
    print("Iteration: ", count)
    sock.send("A".encode() * count)
    response = sock.recv(1024)
    if response:
        time.sleep(0.05)
        continue
    else:
        break