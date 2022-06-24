from contextlib import suppress
from hashlib import sha256
from socket import socket, AF_INET, SOCK_STREAM
from typing import Tuple


def socket_client(address: Tuple[str, int], server_message_length: int):
    s = socket(AF_INET, SOCK_STREAM)
    s.connect(address)

    while True:
        data = s.recv(1024)
        if not data:
            break

    s.close()


def main():
    print("thank you for looking after mama and naia")


if __name__ == '__main__':
    main()
