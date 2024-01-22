"""Send a file over the socket"""
import socket
from tkinter.filedialog import askopenfile

# Ask for the file
with askopenfile(mode='rb') as f:
    lines = f.readlines()

# Send the file
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 0))

    print("Ready to send!")
    print(f"Your send code: {socket.gethostname()}-{s.getsockname()[1]}")

    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected to {addr}")
        for line in lines:
            conn.sendall(line)
