from collections import Counter, defaultdict
import csv

import requests

import re
CSV_URL = 'https://raw.githubusercontent.com/pybites/SouthParkData/master/by-season/Season-{}.csv'  # noqa E501

test = ("""Season,Episode,Character,Line
1,1,Boys,"School day, school day, teacher's golden ru...
"
1,1,Kyle,"Ah, damn it! My little brother's trying to follow me to school again.
"
1,1,Ike,"Zeeponanner.
"
1,1,Kyle,"Ike, you can't come to school with me.
"
1,1,Cartman,"Yeah, go home you little dildo.
"
1,1,Kyle,"Dude, don't call my brother a dildo!
"
1,1,Stan,"What's a dildo?
"
1,1,Kyle,"Well, I don't know...  and I'll bet Cartman doesn't know either!
"
1,1,Cartman,"I know what it means!
"
1,1,Kyle,"Well, what?
"
1,1,Cartman,"I'm not telling you.
"
1,1,Stan,"What's a dildo, Kenny?
"
1,1,Kenny,"(It's a giant stick that goes inside the mom's vagina)
"
1,1,Cartman,"He-yeah, that's what Kyle's little brother is all right!  Ow!
"
1,1,Stan,"Dude, that kicks ass!
"
1,1,Kyle,"Yeah, check this one out. Ready, Ike? Kick the baby!
"
1,1,Ike,"Don't kick the baby.
"
1,1,Kyle,"Kick the baby.
"
1,1,Stan,"Whoa, Cartman! Looks like you didn't get much sleep last night.
"
1,1,Cartman,"That's 'cause I was having these... bogus nightmares.
"
1,1,Kyle,"Really? What about?
"
1,1,Cartman,"Well, I dreamt that I was lying in my bed...  in the dark, when all of a sudden this bright blue light filled the room.  Then slowly my bedroom door begin to open,  and the next thing I remember, I was being drug through a hallway.  Then I was lying on a table,  and these scary hands wanted to operate on me. And they had big heads and big black eyes...
"
1,2,Agent 1,"Gun!
"
1,8,Agent 1,"Hello there little boy, we're looking for a starving African child who was accidentally sent here instead of a Teiko sports watch.
"
1,8,Agent 1,"Here's your sports watch son, sorry for the mix-up.
"
1,8,Agent 1,"Have you seen anyone fitting this description.
"
1,8,Agent 1,"There you are. Are you ready to go home now?
"
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

    line = re.sub(r'[^A-Za-z0-9 ]+', '', line)

    return len(re.findall(r'\w+', line))


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

    print("thank you for everything you have given me...")

    # content = get_season_csv_file(season=1)
    content = test
    print(get_num_words_spoken_by_character_per_episode(content))

    name_count = [
        ("Lucy", '2', 10),
        ("Bob", '3', 5),
        ("Jim", '9', 40),
        ("Susan", '2', 6),
        ("Lucy", '1', 2),
        ("Bob", '3', 30),
        ("Harold", '10', 6)
    ]

    ret = dict()
    d = defaultdict(list)

    for name, *v in name_count:
        d[name].append(v)

    new_list = list(d.items())
    # print(new_list)

    for e in new_list:
        c_list = [tuple(l) for l in e[1]]
        ret[e[0]] = Counter(key for key, num in c_list for idx in range(num))

    test_str = "Hm, let me see that.  Why, this is Anasazi writing! My God, this must be thousands of years old"
    print(_count_words(test_str))


if __name__ == "__main__":
    main()
