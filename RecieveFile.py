"""Receive a file over the socket"""
import socket

code = input("Enter sender code to recieve file: ").split("-")
HOST = code[0]
PORT = code[1]
del code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, int(PORT)))
    s.sendall(b"Hello, world")
    data = s.recv(1024)

print(f"Received {data!r}")

