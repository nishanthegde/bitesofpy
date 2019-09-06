from contextlib import redirect_stdout
from io import StringIO
from types import BuiltinFunctionType
import inspect


def get_len_help_text(builtin: BuiltinFunctionType) -> int:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    s = StringIO()

    if isinstance(builtin, BuiltinFunctionType):

        with redirect_stdout(s):
            help(builtin)

        return len(s.getvalue())

    else:
        raise ValueError

    return None


# def main():

#     print(get_len_help_text(pow))

#     max1 = object()
#     print(get_len_help_text(max1))

#     print(get_len_help_text(max))

#     print(get_len_help_text(min))

#     print(get_len_help_text('string'))

#     src = inspect.getsource(get_len_help_text)
#     assert 'help' in src
#     assert 'redirect_stdout' in src


# if __name__ == '__main__':
#     main()
