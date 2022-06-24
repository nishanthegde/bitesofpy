from contextlib import suppress
from hashlib import sha256
from socket import socket, AF_INET, SOCK_STREAM
from typing import Tuple


def socket_client(address: Tuple[str, int], server_message_length: int):
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(address)


def main():
    print("thank you for looking after mama and naia")


if __name__ == '__main__':
    main()
