#!/usr/bin/python3

import socket,time

IP = "192.168.192.167"
PORT = 2223

count = 1
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP, PORT))

print("Fuzzing the server...")
while True:
    print("\nIteration: ", count)
    sock.send("INC ".encode() * "1"*count.encode())
    response = sock.recv(1024)
    print(response)
    count += 1
    if response:
        time.sleep(0.05)
        continue
    else:
        break
print("Fuzzing crashed at iteration", count)