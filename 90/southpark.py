from collections import Counter, defaultdict
import csv

import requests

import re
CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501

test = ("""
Season,Episode,Character,Line
1,12,Anthropologist,"How's it going, boys?
"
1,12,Anthropologist,"Hm, let me see that.  Why, this is Anasazi writing! My God, this must be thousands of years old!
"
1,12,Anthropologist,"...And so, these ancient arrowheads are buried deep down in the earth's crust. We dig them up, polish them off, and find over twelve new arrowheads every month.
"
1,12,Anthropologist,"Now, can anybody tell me, who left these arrowheads here?
"
1,12,Anthropologist,"Well... yes, but I want to see if you're learning anything.
"
1,12,Anthropologist,"Okay, I tell you what. Why don't we all grab our little anthropology pickaxes - that were handed out and we wuh dig for our very own Indian arrowheads.
"
    """)


def _count_words(line: str) -> int:
    # print(line)
    # line = line.replace("\'re", " are")
    # line = re.sub(r'[^A-Za-z0-9 ]+', '', line)
    # print(len(re.findall(r'\w+', line)))

    # return len(re.findall(r'\w+', line))

    stripped_lines = [l.strip() for l in line.split() if l.strip() != '"']
    # stripped_lines = line.split()

    # if character == 'Anthropologist':
    #     print(stripped_lines)

    return len(stripped_lines)


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

    ret_dict = defaultdict(lambda: Counter())  # return

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

    # content = test
    # words_spoken_test = get_num_words_spoken_by_character_per_episode(content)
    # print(words_spoken_test)
    content = get_season_csv_file(season=1)
    words_spoken_s1 = get_num_words_spoken_by_character_per_episode(content)
    print(words_spoken_s1['Stan'].most_common()[: 3])
    print(words_spoken_s1['Cartman'].most_common()[: 3])
    # print(words_spoken_s1['Anthropologist'].most_common()[:3])
    print(words_spoken_s1['Cartman'].most_common()[-3:])
    print(words_spoken_s1['bogus'].most_common())

    content = get_season_csv_file(season=5)
    words_spoken_s5 = get_num_words_spoken_by_character_per_episode(content)
    print(words_spoken_s5['Sheila'].most_common()[: 3])
    print(words_spoken_s5['Ms. Choksondik'].most_common()[:3])
    # print(words_spoken_s5['Cartman'].most_common()[: 3])


if __name__ == "__main__":
    main()
