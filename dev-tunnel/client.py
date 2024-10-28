from argparse import ArgumentParser
import requests
from dotenv import dotenv_values
import socket
import sys


if __name__ == '__main__':
    # fetch default arguments from .env file
    config = dotenv_values('.env')
    # setup arguments
    parser = ArgumentParser()
    if bool(config) and 'SERVER_HOST' in config:
        parser.add_argument("-s", "--server", dest="server_host", default=config['SERVER_HOST'],
                            help="Dev-tunnel server host name or IP address")
    else:
        parser.add_argument("-s", "--server", dest="server_host",
                            help="Dev-tunnel server host name or IP address")

    if bool(config) and 'SERVER_PORT' in config:
        parser.add_argument("-p", "--port", dest="server_port", default=config['SERVER_PORT'],
                            help="Dev-tunnel server port")
    else:
        parser.add_argument("-p", "--port", dest="server_port",
                            help="Dev-tunnel server port")

    args = parser.parse_args()

    if not bool(config) and len(sys.argv) <= 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    print(args.server_host + ':' + args.server_port)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((args.server_host, args.server_port))
        while True:
            message = input("Enter message: ")
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f"Received from server: {data.decode()}")
