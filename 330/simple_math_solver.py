from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
        operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    if not isinstance(expected_result, int):
        raise ValueError("Result must be an integer type!")

    if len([o for o in operator_path if o not in ('+', '-', '*')]) >= 1:
        raise ValueError("Operators can only be one of +, -, *")

    digits = [d for d in range(1, 10)]
    solutions = []

    if len(operator_path) == 1:
        if operator_path[0] == '+':
            for values in permutations(digits, 2):
                if values[0] + values[1] == expected_result:
                    solutions.append(list(values))
        elif operator_path[0] == '-':
            for values in permutations(digits, 2):
                if values[0] - values[1] == expected_result:
                    solutions.append(list(values))
        elif operator_path[0] == '*':
            for values in permutations(digits, 2):
                if values[0] * values[1] == expected_result:
                    solutions.append(list(values))
    else:
        for values in permutations(digits, len(operator_path) + 1):
            formula = "".join(o + str(v) for o, v in zip([""] + operator_path, values))
            if eval(formula) == expected_result:
                solutions.append(list(values))

    return solutions
