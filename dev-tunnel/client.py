from argparse import ArgumentParser
from dotenv import dotenv_values
import socket
import sys


def receive_requests():
    # Listen for incoming requests from Server application
    while True:
        request_data = receive_request()
        # Forward request to local web server
        response = forward_request_to_local_server(request_data)
        # Send response back to Server application
        send_response_to_server(response)


def forward_request_to_local_server(request_data):
    # Construct request object based on request_data
    response = requests.request(**request_data)
    return response


if __name__ == '__main__':
    config = dotenv_values('.env')
    parser = ArgumentParser()
    parser.add_argument("-s", "--server", dest="server_host", default=config['SERVER_HOST'],
                        help="Dev-tunnel server host name or IP address")
    parser.add_argument("-p", "--port", dest="server_port", default=config['SERVER_PORT'],
                        help="Dev-tunnel server port")
    args = parser.parse_args()

    print(args.server_host + ':' + args.server_port)
    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect((HOST, PORT))
    #     while True:
    #         message = input("Enter message: ")
    #         s.sendall(message.encode())
    #         data = s.recv(1024)
    #         print(f"Received from server: {data.decode()}")
