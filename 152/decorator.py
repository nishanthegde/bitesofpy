from functools import wraps


DEFAULT_TEXT = ('Subscribe to our blog (sidebar) to periodically get '
                'new PyBites Code Challenges (PCCs) in your inbox')
DOT = '.'


TEXTS = ['Hello world', 'Welcome to PyBites',
         'Decorators for fun and profit']


def strip_range(start, end):

    if start < 0:
        start = 0

    def rep_decorator(func):
        def func_wrapper(text):
            replacement = min((end - start), (len(text) - len(text[:start]))) * DOT
            if len(text) <= start:
                s = text
            else:
                s = text[:start] + replacement + text[start + len(replacement):]
            return s
        return func_wrapper
    return rep_decorator


# @strip_range(0, -1)
# def gen_output(text):
#     return text


# def main():

#     # print(get_text("John"))

#     for arg in TEXTS:
#         print(gen_output(text=arg))


# if __name__ == '__main__':
#     main()
