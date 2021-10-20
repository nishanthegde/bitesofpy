from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
        operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    solutions = []
    # check for valid input parameters
    for op in operator_path:
        if op not in ['+', '-', '*']:
            raise ValueError('Operator not supported')

    if not isinstance(expected_result, int):
        raise ValueError('Result type not supported')

    priority = {'*': 0, '+': 1, '-': 2}
    operator_path.sort(key=priority.get)
    operations_map = {
        "+": add,
        "-": sub,
        "*": mul
    }
    operands = [i for i in range(1, 10)]

    for i in permutations(operands, len(operator_path) + 1):
        combined = [None] * (len(list(i)) + len(operator_path))
        combined[::2] = list(i)
        combined[1::2] = operator_path

        result = combined[0]
        for j in range(1, len(combined)):
            if combined[j - 1] in operations_map:
                result = operations_map[combined[j - 1]](result, combined[j])
        if result == expected_result:
            solutions.append(list(i))
            # print(combined, result, list(i))

    return solutions


def main():
    print('thank you for looking after Naia and Mama')
    print(find_all_solutions(['*', '-'], 16))


if __name__ == '__main__':
    main()
