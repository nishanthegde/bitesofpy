from typing import Dict, Any
import copy
from datetime import datetime
from collections import OrderedDict


def fb(value):
    return str(value)


def rename_keys(data: Dict[Any, Any]) -> Dict[Any, Any]:
    d = OrderedDict(copy.deepcopy(data))

    for key, value in d.items():
        if isinstance(value, dict):
            d[key] = rename_keys(value)
        if isinstance(value, list):
            for i, ele in enumerate(value):
                value[i] = rename_keys(ele)
        if isinstance(key, str) and key.strip().startswith('@'):
            d = OrderedDict([(key[1:], v) if k == key else (k, v) for k, v in d.items()])

    return dict(d)