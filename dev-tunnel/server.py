from flask import Flask, request
import requests
import socket
import threading
import queue

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5432        # The port used by the server

app = Flask(__name__)
request_queue = queue.Queue()


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def handle_request(path):
    # Extract request data (e.g., URL, method, headers, body)
    request_data = {
        'url': request.url,
        'method': request.method,
        'headers': request.headers,
        'data': request.data,
        'path': path
        # ... other request details
    }

    # Forward request to Client application through socket
    response = forward_request_to_client(request_data)

    # Return response to browser
    return response


def forward_request_to_client(request_data):
    print(request_data)

    return 'demo response data'


def handle_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            print(f"Received from {client_address}: {data}")
            client_socket.sendall(data)
        except Exception as e:
            print(f"Error handling client {client_address}: {e}")
            break
    client_socket.close()
    print(f"Connection with {client_address} closed")


def socket_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("Server listening on port", PORT)
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            client_thread = threading.Thread(
                target=handle_client, args=(conn, addr))
            client_thread.start()


if __name__ == '__main__':
    # Start Flask app in a separate thread
    app_thread = threading.Thread(target=app.run)
    app_thread.start(debug=True)

    # Start socket listener in the main thread
    socket_listener()
