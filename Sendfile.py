"""Send a file over the socket"""
import socket
from tkinter.filedialog import askopenfilename

# Ask for the file
file_name = askopenfilename()
with open(file_name, 'rb') as f:
    lines = f.readlines()

# Send the file
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Bind
    s.bind(("", 0))

    print("Ready to send!")
    print(f"Your send code: {socket.gethostname()}-{s.getsockname()[1]}")

    # Listen and accept connection
    s.listen()
    conn, addr = s.accept()

    # Send the name
    conn.sendall(file_name.split("/")[-1].encode())

    # Send the data
    with conn:
        print(f"Connected to {addr}")
        for line in lines:
            conn.sendall(line)
