import base64
from cryptography.fernet import Fernet  # type: ignore
from cryptography.hazmat.backends import default_backend  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC  # type: ignore
from os import urandom
from typing import ByteString, Tuple, Optional
from random import choice
import os
from datetime import datetime

KEYS = (
    b"rvxePMSDUcZFowEaNxnFb8Pifn1KmhkF70Mz1ZQe2Bw=",
    b"2gODW4C4Lc7H9bjuuhPyn48HkVHriqa96P8lmstABo8=",
    b"mAbAfF5CW3EGlngOEEroDqtxlxVlJILzoUE4TJScMIw=",
)

MESSAGE = "This is my secret message"


class ClamyFernet:
    """Fernet implementation by clamytoe

    Takes a bytestring as a password and derives a Fernet
    key from it. If a key is provided, that key will be used.

    :param password: ByteString of the password to use
    :param key: ByteString of the key to use, else defaults to None

    Other class variables that you should implement that are hard set:

    salt, algorithm, length, iterations, backend, and generate a base64
    urlsafe_b64encoded key using self.clf().
    """

    def __init__(self, password=b"pybites", key=None):
        self.password = password
        if key is None:
            self.key = base64.urlsafe_b64encode(self.kdf.derive(password))
        else:
            self.key = key

    @property
    def kdf(self):
        """Derives the key from the password

        Uses PBKDF2HMAC to generate a secure key. This is where you will
        use the salt, algorithm, length, iterations, and backend variables.
        """
        backend = default_backend()
        salt = os.urandom(16)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=backend
        )

        return kdf

    @property
    def clf(self):
        """Generates a Fernet object
        Key that is derived from cryptogrophy's fernet.
        """
        # f = Fernet(base64.urlsafe_b64encode(self.key))
        # f = Fernet(Fernet.generate_key())
        f = Fernet(self.key)
        return f

    def encrypt(self, message: str) -> ByteString:
        """Encrypts the message passed to it"""

        what_b = message.encode("utf-8")
        # token = self.clf.encrypt(what_b)
        token = self.clf.encrypt(what_b)
        return token

    def decrypt(self, token: ByteString) -> str:
        """Decrypts the encrypted message passed to it"""
        return self.clf.decrypt(token).decode("utf-8")


def rcf():
    password = b"#clamybite"
    key = choice(KEYS)
    return ClamyFernet(password, key)


def cf():
    return ClamyFernet(key=KEYS[0])


def main():

    print('thank you for the wave')
    # r = rcf()
    # print(r.password)
    # print(r.key)
    # token = r.encrypt(MESSAGE)
    # og_message = r.decrypt(token)
    # print(og_message)
    # assert len(token) == 120
    # assert isinstance(token, bytes)
    # assert r.key in KEYS
    # assert og_message == MESSAGE
    # print(r.kdf)
    # print(type(r.clf))
    # token = r.encrypt("secret msg")
    # print(token)
    # ts = r.clf.extract_timestamp(token)
    # print(ts)
    # dt = datetime.fromtimestamp(ts)
    # print(dt.year)

    # word = "very secret thing"
    # c = cf()
    # print(c.password)
    # print(c.key)
    # token = c.encrypt(MESSAGE)
    # print(token)
    # print(len(token))
    # og_message = c.decrypt(token)
    # print(og_message)

if __name__ == '__main__':
    main()
