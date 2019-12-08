from functools import wraps


# def make_html(element: str)-> str:
#     tag = '<{}>'.format(element)
#     return '{}{}{}'.format(tag, get_text(), tag)


# def make_html(element):
#     def real_decorator(func_to_decorate):

#         @wraps(func_to_decorate)
#         def new_func(*original_args, **original_kwargs):
#             print('Calling decorated function with {}'.format(element))
#             return func_to_decorate(*original_args, **original_kwargs)
#         return new_func
#     return make_html

def make_html(tag_name):
    def dec(func):
        def func_wrapper(*original_args, **original_kwargs):
            return '<{}>{}</{}>'.format(tag_name, func(*original_args, **original_kwargs), tag_name)
        return func_wrapper
    return dec


# @make_html('p')
# @make_html('strong')
# def get_text(text: str) -> str:
#     return text


# def main():
#     @make_html('p')
#     @make_html('strong')
#     def get_text(text='I code with PyBites'):
#         return text

#     # print(get_text())
#     assert get_text() == '<p><strong>I code with PyBites</strong></p>'


# if __name__ == '__main__':
#     main()
