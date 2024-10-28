import socket
import threading
import queue

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5432        # The port used by the server

# Dict of queues.
queue_dict = {}


def handle_socket_client(client_socket, client_address):
    print(f"New connection from {client_address}")
    # create a new queue
    request_queue = queue.Queue()
    queue_dict[client_address] = request_queue

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
                target=handle_socket_client, args=(conn, addr))
            client_thread.start()


if __name__ == '__main__':
    # Start socket listener in the main thread
    socket_listener()
