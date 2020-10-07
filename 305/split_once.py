from typing import List
import re
from textwrap import dedent

def split_once(text: str, separators: str = None) -> List[str]:
    return_value = list()

    if not separators:
        ws = ' \t\n\v\f\r'

        for s in ws:
            if len(text.split(s, 1)) > 1:
                if len(return_value) > 1:
                    return_value = return_value[:-1]
                return_value.append(text.split(s, 1)[0])
                return_value.append(text.split(s, 1)[1])
                text = text.split(s, 1)[1]
    else:

        for s in separators:
            if len(text.split(s, 1)) > 1:
                if not return_value:
                    return_value.append(text.split(s, 1)[0])
                    return_value.append(text.split(s, 1)[1])
                    # print(return_value)
                else:
                    for i, t in enumerate(return_value):
                        if len(t.split(s, 1)) > 1:
                            return_value[i] = t.split(s, 1)[0]
                            return_value.insert(i+1, t.split(s, 1)[1])
                            break

    if not return_value:
        return_value.append(text)

    return return_value
