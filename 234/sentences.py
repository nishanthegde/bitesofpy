import re
lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor!
Pulvinar sapien et ligula ullamcorper malesuada proin libero nunc consequat?
Sed viverra tellus in hac habitasse platea dictumst vestibulum.
Morbi tempus iaculis urna id volutpat.
Enim blandit volutpat maecenas volutpat.
Morbi tristique senectus et netus!
Massa tincidunt nunc pulvinar sapien?
Nunc aliquet bibendum enim facilisis gravida neque convallis a.
Enim blandit volutpat maecenas volutpat blandit aliquam etiam erat velit.
Id diam maecenas ultricies mi eget mauris?
Diam quis enim lobortis scelerisque fermentum dui faucibus in ornare!
Gravida in fermentum et sollicitudin ac orci phasellus!
Ut diam quam nulla porttitor massa id neque aliquam.
Sit amet dictum sit amet justo donec enim diam vulputate.
Risus sed vulputate odio ut?
Justo eget magna fermentum iaculis eu non!
At auctor urna nunc id.
At erat pellentesque adipiscing commodo elit at imperdiet!
Molestie nunc non blandit massa enim nec dui?
Lorem donec massa sapien faucibus et molestie ac feugiat.
""".strip().splitlines()

text1, text2, text3 = lorem_ipsum[:5], lorem_ipsum[5:13], lorem_ipsum[13:]


def capitalize_sentences(text: str) -> str:
    """Return text capitalizing the sentences. Note that sentences can end
       in dot (.), question mark (?) and exclamation mark (!)"""

    ret = []

    sent_pattern = re.compile(r'([^!?.]+[!?.])($|\s)')

    for match in sent_pattern.finditer(text):
        ret.append(match.group(1).capitalize())
    # s = sent_pattern.search(text)
    # return s.group(1).capitalize()

    return " ".join(ret)


# def main():
#     print('thank you ...')
#     expected = " ".join(text1)
#     # print(expected)
#     arg = expected.lower()
#     # print(arg)
#     # capitalize_sentences(arg)
#     # print(capitalize_sentences(arg))
#     assert capitalize_sentences(arg) == expected
#     # print(lorem_ipsum[0].lower())
#     # print(capitalize_sentences(lorem_ipsum[0].lower()))
#     # print(" ".join(text1).lower())


# if __name__ == '__main__':
#     main()
