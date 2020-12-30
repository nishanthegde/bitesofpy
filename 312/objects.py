from typing import Dict, List
import keyword
import sys as s

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    score = 0

    for object in objects:

        if keyword.iskeyword(object):
            score += scores["keyword"]

        if object in dir(__builtins__):
            score += scores["builtin"]

        if object in list(s.modules.keys()):
            score += scores["module"]

    return score
