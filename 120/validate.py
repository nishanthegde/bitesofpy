from functools import wraps

def int_args(func):

    @wraps(func)

    def wrapper(*args):
        if not all(isinstance(arg, int) for arg in args):
            raise TypeError("all arguments must be int")

        if any(arg < 0 for arg in args):
            raise ValueError("int argument must be greater than 0")

        return func(*args)

    return wrapper

# @int_args
# def sum_numbers(*numbers):
#     """
#         Function to calculate sum of n numbers.
#         If one or more of the passed in args are not of type int, it throws a TypeError, if it is an int but < 0, it throws a ValueError.
#     """
#     return sum(numbers)

# def main():

#     print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, -9))
#     # print(tuple(list(range(1,10))))

# if __name__ == "__main__":
#     main()

