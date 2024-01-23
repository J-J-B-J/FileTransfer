"""Receive a file over the socket"""
import socket
from tkinter.filedialog import askdirectory

code = input("Enter sender code to receive file: ").split("-")
HOST = code[0]
PORT = code[1]
del code

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect
    s.connect((HOST, int(PORT)))
    print(f"Connected to {HOST}")

    # Receive name
    name = s.recv(4096)

    # Receive data
    lines = []
    data = ""
    while data != b'':
        data = s.recv(4096)
        lines.append(data)

# Save the file
file_name = askdirectory() + "/" + name.decode()
with open(file_name, "wb") as f:
    f.writelines(lines)
