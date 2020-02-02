from collections import Counter, defaultdict
import csv

import requests

import re
CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501

test = ("""
Season,Episode,Character,Line
2,1,Announcer 1,"Since the last South Park, you've waited four long weeks to find out who the father of Eric Cartman is. Now, finally, the shocking truth about Cartman's lineage... will not be seen tonight, so that we can bring you the following special presentation.
"
2,1,Announcer 2,"Now, get ready for Canada's hottest action stars,  Terrance and Phillip in HBC's Movie of the Week:  Not Without My Anus. Based on a true story.
"
2,1,Scott,"Ladies and gentlemen, the case before you today is of a murderer. On the night in question, this monster entered the home of Dr. Jeffrey O'Dwyer and struck him repeatedly on the head with his hammer.  That monster is sitting right over there, and his name is Terrance!
"
2,1,Phillip,"Oh, Terrance! You farted in court!
"
2,1,Terrance,"Yes, Phillip. I'm making a case for our defense.
"
2,1,Scott,"All of these things link Terrance to the murder: hair fibers, blood samples, nail clippings, a piece of his shirt,  a watch with his initials on it, a day planner with the murder scheduled, a haiku called, Time to Kill Dr. Jeffrey O'Dwyer.
""Dr. O'Dwyer
Time to have your head smashed in
with my new hammer""
Terrance, you may be a famous surgeon, but you're not God! J'accuse, Terrance!
"
2,1,Terrance,"Would you like a monkey claw, Phillip?
"
    """)


def _count_words(line: str) -> int:

    line = re.sub(r'[^A-Za-z0-9 ]+', '', line)

    return len(re.findall(r'\w+', line))


def _check_int(s):
    try:
        int(s)
        return True
    except:
        return False


def get_season_csv_file(season):
    """Receives a season int, and downloads loads in its
       corresponding CSV_URL"""
    with requests.Session() as s:
        download = s.get(CSV_URL.format(season))
        return download.content.decode('utf-8')


def get_num_words_spoken_by_character_per_episode(content: str) -> defaultdict():
    """Receives loaded csv content (str) and returns a dict of
       keys=characters and values=Counter object,
       which is a mapping of episode=>words spoken"""

    ret_dict = dict()  # return

    # lines = [l for l in content.strip().split("\n") if l != "\""]
    lines = [l for l in content.strip().split("\n")][1:]

    # concatenate " to previous element and drop "
    for i in range(len(lines) - 1, 0, -1):
        if lines[i] == '"':
            lines[i - 1] = lines[i - 1] + lines[i]
            lines.pop(i)

    # lines that are wrapped
    for i in range(len(lines) - 1, 0, -1):
        if not _check_int(lines[i].split(',', 3)[0].strip()):
            lines[i - 1] = lines[i - 1] + lines[i]
            lines.pop(i)

    # return lines

    # create list of tuples with (character, ep, line)
    t_list = [(l.split(',', 3)[2].strip(), l.split(',', 3)[1].strip(), _count_words(l.split(',', 3)[3].strip())) for l in lines]

    # sample t_list
    # [('Boys', '1', 7), ('Kyle', '1', 13), ('Ike', '1', 1), ('Kyle', '1', 8)('Agent 1', '2', 1),
    # ('Agent 1', '8', 22), ('Agent 1', '8', 9), ('Agent 1', '8', 7), ('Agent 1', '8', 10)]

    d_default = defaultdict(list)

    for name, *v in t_list:
        d_default[name].append(v)

    t_new_list = list(d_default.items())

    # sample t_new_list
    # [('Boys', [['1', 7]]), ('Kyle', [['1', 13], ['1', 8], ['1', 7], ['1', 11], ['1', 2], ['1', 10], ['1', 3], ['1', 3]]),
    # ('Ike', [['1', 1], ['1', 4]]), ('Cartman', [['1', 6], ['1', 5], ['1', 4], ['1', 10], ['1', 8], ['1', 71]]),
    # ('Stan', [['1', 3], ['1', 4], ['1', 4], ['1', 11]]), ('Kenny', [['1', 10]]),
    # ('Agent 1', [['2', 1], ['8', 22], ['8', 9], ['8', 7], ['8', 10]])]

    for elem in t_new_list:
        c_list = [tuple(l) for l in elem[1]]
        ret_dict[elem[0]] = Counter(key for key, num in c_list for idx in range(num))

    return ret_dict


def main():

    print("thank you for the waves...")

    # content = get_season_csv_file(season=1)
    content = test
    words_spoken_test = get_num_words_spoken_by_character_per_episode(content)

    print(words_spoken_test)
    # for l in words_spoken_test:
    #     print(l)

    # print(words_spoken_test['Agent 1'].most_common()[:2])
    # name_count = [
    #     ("Lucy", '2', 10),
    #     ("Bob", '3', 5),
    #     ("Jim", '9', 40),
    #     ("Susan", '2', 6),
    #     ("Lucy", '1', 2),
    #     ("Bob", '3', 30),
    #     ("Harold", '10', 6)
    # ]

    # ret = dict()
    # d = defaultdict(list)

    # for name, *v in name_count:
    #     d[name].append(v)

    # new_list = list(d.items())
    # # print(new_list)

    # for e in new_list:
    #     c_list = [tuple(l) for l in e[1]]
    #     ret[e[0]] = Counter(key for key, num in c_list for idx in range(num))

    # test_str = "Hm, let me see that.  Why, this is Anasazi writing! My God, this must be thousands of years old"
    # print(_count_words(test_str))


if __name__ == "__main__":
    main()
