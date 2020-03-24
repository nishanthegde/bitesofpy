from math import floor
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)

# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""

    remainder = record % BASE
    result = CODEX[remainder]

    queue = floor(record / BASE)
    add_result = ''
    if queue >= BASE:
        add_result = str(floor(queue / BASE)) + ''

    # print('queue is {}'.format(queue))

    while queue:
        remainder = queue % BASE
        queue = floor(remainder / BASE)
        # print('queue is {}'.format(queue))
        result = CODEX[remainder] + result

    return add_result + result


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    value = 0
    for c in short_url:
        value = BASE * value + CODEX.find(c)

    return value


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)
    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    pass


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB
    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    LINKS[next_record] = url + '/' + encode(next_record)

    return LINKS[next_record]


def main():
    print('please help everyone be safe... ')
    print(encode(5000))
    print(encode(6000))
    print(encode(7000))
    print(encode(8000))
    print(encode(9000))
    print(encode(9999))
    print(decode('jnRFH'))
    print(shorten_url("https://google.com", 5000))
    print(LINKS)


if __name__ == "__main__":
    main()
