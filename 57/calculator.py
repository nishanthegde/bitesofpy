import argparse

class InvalidArgType(Exception):
    """Raised when the user is not in USERS"""
    pass

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimals"""

    if operation == 'add':
      return round(sum(numbers),2)

    if operation == 'sub':
      return round(numbers[0] - sum(numbers[1:]),2)

    if operation == 'mul':
      prod = 1
      for i in numbers:
        prod *= i
      return round(prod,2)

    if operation == 'div':
      div = numbers[0]
      if len(numbers) > 1:
        for i in numbers[1:]:
          div /= i
      return round(div,2)

def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""

    parser = argparse.ArgumentParser(description='A simple calculator')
    parser.add_argument('-a','--add', nargs="+", help='Sums numbers', required=False)
    parser.add_argument('-s','--sub', nargs="+", help='Subtracts numbers', required=False)
    parser.add_argument('-m','--mul', nargs="+", help='Multiplies numbers', required=False)
    parser.add_argument('-d','--div', nargs="+", help='Divides numbers', required=False)

    return parser

def call_calculator(args=None, stdout=False):
    """
       Calls calculator with provided args object.
       If args are not provided get them via create_parser, (note: function is never called with args so it is always parsed from input)
       if stdout is True print the result
    """

    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # print(vars(args))

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():

        if numbers is None:
            continue

        # print(operation, numbers)
        # print(type(operation), type(numbers))

        try:
            num_list = [float(i) for i in list(numbers)]

        except:
           raise InvalidArgType("arg list to be operated on should only have numbers ")

        try:
            res = calculator(operation, num_list)

        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res

# def main():
#   """
#     $ python calculator.py -h
#       usage: calculator.py [-h] [-a ADD [ADD ...]] [-s SUB [SUB ...]]
#                            [-m MUL [MUL ...]] [-d DIV [DIV ...]]

#       A simple calculator

#       optional arguments:
#         -h, --help            show this help message and exit
#         -a ADD [ADD ...], --add ADD [ADD ...]
#                               Sums numbers
#         -s SUB [SUB ...], --sub SUB [SUB ...]
#                               Subtracts numbers
#         -m MUL [MUL ...], --mul MUL [MUL ...]
#                               Multiplies numbers
#         -d DIV [DIV ...], --div DIV [DIV ...]
#                               Divides numbers


#       $ python calculator.py --add 1 2 3
#       6.0
#       $ python calculator.py --sub 10 6 2
#       2.0
#       $ python calculator.py --mul 3 3 3
#       27.0
#       $ python calculator.py --div 8 5 7
#       0.23
#   """
#   call_calculator(stdout=True)

if __name__ == '__main__':
    call_calculator(stdout=True)
    # main()
