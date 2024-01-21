"""Send a file over the socket"""
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("", 0))

    print("Ready to send!")
    print(f"Your send code: {socket.gethostname()}-{s.getsockname()[1]}")

    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
