from datetime import timedelta
from typing import List

text1 = """
1
00:00:00,498 --> 00:00:02,827
Beautiful is better than ugly.

2
00:00:02,827 --> 00:00:06,383
Explicit is better than implicit.

3
00:00:06,383 --> 00:00:09,427
Simple is better than complex.
"""
text2 = """
18
00:01:12,100 --> 00:01:17,230
If you want a bit more minimalistic view, you can actually hide the sidebar.

19
00:01:18,200 --> 00:01:19,500
If you go to Settings

20
00:01:23,000 --> 00:01:26,150
scroll down to 'Focus Mode'.

21
00:01:28,200 --> 00:01:35,180
You can actually hide the sidebar and have only the description and the code editor.
"""  # noqa E501

text3 = '\n'.join(text1.splitlines()[:9])

text4 = '\n'.join(text2.splitlines()[5:])
# testing hours as well
text5 = """
32
00:59:45,000 --> 00:59:48,150
talking quite normal here

33
01:00:00,000 --> 01:00:07,000
he is talking slooooow

34
02:04:28,000 --> 02:04:30,000
she is talking super fast here!
"""


def get_secs(time_str: str) -> int:
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def is_int(s: str) -> bool:
    try:
        int(s)
        return True
    except ValueError:
        return False


def get_srt_section_ids(text: str) -> List[int]:
    results = []
    lines = text.split('\n')

    for i, ele in enumerate(lines):
        if is_int(ele):
            t = lines[i + 1]
            # start = get_secs(t.split(' --> ')[0].split(',')[0]) + (int(t.split(' --> ')[0].split(',')[1]) / 1000)
            start = get_secs(t.split(' --> ')[0].split(',')[0])
            # end = get_secs(t.split(' --> ')[1].split(',')[0]) + (int(t.split(' --> ')[1].split(',')[1]) / 1000)
            end = get_secs(t.split(' --> ')[1].split(',')[0])
            chars_per_sec = len(lines[i + 2])/(end-start)
            results.append((ele, start, end, chars_per_sec))

    # return [e[0] for e in sorted(results, key=lambda x: x[2] - x[1])]
    return [int(e[0]) for e in sorted(results, key=lambda x: x[3], reverse=True)]

# def main():
#     print(get_srt_section_ids(text1))
#     print(get_srt_section_ids(text2))
#     print(get_srt_section_ids(text3))
#     print(get_srt_section_ids(text4))
#     print(get_srt_section_ids(text5))
#
#
# if __name__ == '__main__':
#     main()
