import socket
import os

HOST = '127.0.0.1'
PORT = 5001

storage_folder = "fog_node/stored_data"

if not os.path.exists(storage_folder):
    os.makedirs(storage_folder)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Fog Server Running... Waiting for IoT Data")

while True:

    conn, addr = server.accept()

    print("Connected from:", addr)

    data = conn.recv(4096)

    if data:

        file_path = os.path.join(storage_folder, "encrypt_data.bin")

        with open(file_path, "wb") as f:
            f.write(data)

        print("Encrypted Data Stored in Fog Node")

    conn.close()