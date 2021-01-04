import re
from urllib import parse

class DomainException(Exception):
    """Raised when an invalid is created."""


class Domain:

    def __init__(self, name):
        # validate a current domain (r'.*\.[a-z]{2,3}$' is fine)
        # if not valid, raise a DomainException
        p = re.compile(r'.*\.[a-z]{2,3}$')
        m = p.match(name)
        if m:
            self.name = name
        else:
            raise DomainException('Invalid Domain')

    # next add a __str__ method and write 2 class methods
    # called parse_from_url and parse_from_email to construct domains
    # from an URL and email respectively
    @classmethod
    def parse_url(cls, url):
        return cls(parse.urlsplit(url).netloc)

    @classmethod
    def parse_email(cls, email):
        return cls(email.split('@')[1])

    def __str__(self):
        return '{}'.format(self.name)
