from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        print(UPPER_SLICE)
        result = func(*args, **kwargs)
        print(LOWER_SLICE)
        return result

    return wrapped


@sandwich
def add_ingredients(ingredients):
    print(' / '.join(ingredients))


# def main():
#     """
#         >>> from sandwich import sandwich
#         >>> @sandwich
#         ... def add_ingredients(ingredients):
#         ...     print(' / '.join(ingredients))
#         ...
#         >>> ingredients = ['bacon', 'lettuce', 'tomato']
#         >>> add_ingredients(ingredients)
#         === Upper bread slice ===
#         bacon / lettuce / tomato
#         === Lower bread slice ===
#     """

#     print('here...')

#     ingredients = ['bacon', 'lettuce', 'tomato']
#     add_ingredients(ingredients)

#     ingredients = ['fried egg', 'tomato', 'cucumber']
#     add_ingredients(ingredients)


# if __name__ == '__main__':
#     main()
