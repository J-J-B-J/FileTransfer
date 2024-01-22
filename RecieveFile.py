"""Receive a file over the socket"""
import socket
from tkinter.filedialog import asksaveasfile

code = input("Enter sender code to receive file: ").split("-")
HOST = code[0]
PORT = code[1]
del code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, int(PORT)))
    print(f"Connected to {HOST}")

    lines = []
    data = ""
    while data != b'':
        data = s.recv(4096)
        lines.append(data)

with asksaveasfile("wb") as f:
    f.writelines(lines)
