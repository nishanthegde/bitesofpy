import pprint
from typing import Any


def pretty_string(obj: Any) -> str:
    # TODO: your code
    return pprint.pprint(obj, depth=2, width=60)

