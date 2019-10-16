from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

another_text = """
Take the block of text provided and strip() off the whitespace at the ends.
Split the whole block up by newline (\n).
 if the first character is lowercase, split it into words and add the last word
of that line to the results list.
Strip the trailing dot (.) and exclamation mark (!) from the word first.
  finally return the results list!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []
    lines = [l.lstrip() for l in text.split('\n')]
    for l in lines:
        # print(l[:1], l[:1].islower())
        if l[:1].islower():
            words_lower = [word for word in l.split()]
            results.append(words_lower[-1].replace('.', '').replace('!', ''))
    # is_first_lower = [c for l in lines for c in l[:1]]
    return results


# def main():
#     print('here ..')

#     actual = slice_and_dice(text)
#     print(actual)

#     actual = slice_and_dice(another_text)
#     print(actual)


# if __name__ == '__main__':
#     main()
