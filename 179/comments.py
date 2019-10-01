import re

single_comment = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
# tmmmimi mimimm
'''

single_comment_after_strip = '''
def hello_world():
    print("Hello World")
'''

single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''

single_docstring_after_strip = '''
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")
'''

class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''
class_with_method_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')
'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

multiline_docstring_after_strip = '''
def __init__(self, name, sound, num_legs):
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''

code_bite_description_after_strip = '''
import re

def hello(name):
    return f'hello {name}'
'''

class_three_indents = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''
class_three_indents_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')

        def func_in_method(self):
            pass
'''


def strip_comments(code):

    # remove single line comments
    str_wo_single_comments = re.sub(re.compile(r'^\s*#.*\n', re.MULTILINE), '', code)

    # remove multiline comments/doc strings
    str_wo_doc_strings = re.sub(re.compile(r'^\s*"""[\s\S]*?"""\n', re.MULTILINE), '', str_wo_single_comments.strip())

    # regex for inline comments (take care of false positives)
    inline_regex = re.compile(r'(.+)(#.*)', re.MULTILINE)

    for match in inline_regex.finditer(str_wo_doc_strings.strip()):
        num_single_quotes = str(match.group(1)).count("'")
        # print(num_single_quotes % 2)
        if (num_single_quotes % 2) == 0:
            str_wo_inline_comments = re.sub(inline_regex, r'\1', str_wo_doc_strings.strip())
            return str_wo_inline_comments.strip()

    return str_wo_doc_strings.strip()


false_positive = '''
def foo():
    # this is a comment
    print('this is not a #comment')
'''

false_positive_after_strip = '''
def foo():
    print('this is not a #comment')
'''


# def main():

#     print('here ...')

#     assert strip_comments(single_comment).strip() == single_comment_after_strip.strip()
#     assert strip_comments(single_docstring).strip() == single_docstring_after_strip.strip()
#     assert strip_comments(class_with_method).strip() == class_with_method_after_strip.strip()
#     assert strip_comments(multiline_docstring).strip() == multiline_docstring_after_strip.strip()
#     assert strip_comments(code_bite_description).strip() == code_bite_description_after_strip.strip()
#     assert strip_comments(class_three_indents).strip() == class_three_indents_after_strip.strip()
#     assert strip_comments(false_positive).strip() == false_positive_after_strip.strip()


# if __name__ == '__main__':
#     main()
