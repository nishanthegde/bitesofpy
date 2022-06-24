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
        else:
            s.sendall(sha256(data).digest())

    s.close()
