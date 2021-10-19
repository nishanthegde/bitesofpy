from itertools import permutations
from operator import add, sub, mul
from typing import List, Union, Iterable


def find_all_solutions(
        operator_path: List[str], expected_result: int
) -> Union[List[List[int]], Iterable[List[int]]]:
    # check for valid input parameters
    for op in operator_path:
        if op not in ['+', '-', '*']:
            raise ValueError('Operator not supported')

    if not isinstance(expected_result, int):
        raise ValueError('Result type not supported')

    priority = {'*': 0, '+': 1, '-': 2}
    operator_path.sort(key=priority.get)

    operands = [i for i in range(1, 10)]

    for i in permutations(operands, len(operator_path)+1):
        print(i)


def main():
    print('thank you for looking after Naia and Mama')
    find_all_solutions(['+','*','*'], 6)


if __name__ == '__main__':
    main()
