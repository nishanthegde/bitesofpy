from typing import Dict, List
import keyword
import sys as s
import builtins
import pkgutil

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str],
                  scores: Dict[str, int] = scores) -> int:
    score = 0
    modules = []

    for _, module, package in list(pkgutil.iter_modules()):
        modules.append(module)

    modules += list(s.builtin_module_names)

    for object in objects:

        if keyword.iskeyword(object):
            print('kw')
            score += scores["keyword"]

        if object in dir(builtins):
            print('bi')
            score += scores["builtin"]

        if object in modules:
            print('mod')
            score += scores["module"]

    return score



