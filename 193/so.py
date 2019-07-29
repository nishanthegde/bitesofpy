import requests
from bs4 import BeautifulSoup
import os

local = os.getcwd()
tmp = 'so.html'
so_file = os.path.join(local, tmp)

cached_so_url = 'https://bit.ly/2IMrXdp'

def top_python_questions(url=cached_so_url):
    """Use requests to retrieve the url / html,
       parse the questions out of the html with BeautifulSoup,
       filter them by >= 1m views ("..m views").
       Return a list of (question, num_votes) tuples ordered
       by num_votes descending (see tests for expected output).
    """
    r = requests.get(cached_so_url)
    # print(r.text)

    soup = BeautifulSoup(r.text, features="html.parser")

    ques_list = []
    view_list = []
    vote_list = []
    for question_summary in soup.find_all("div", {"id": "questions"}):
        for question in question_summary.find_all('h3'):
            ques_list.append(question.get_text())

        for views in question_summary.find_all('div', {"title": True}):
            view_list.append(views.get_text().strip())

        for votes in question_summary.find_all("span", {"class": "vote-count-post"}):
            vote_list.append(votes.get_text().strip())

    res = sorted([(ques_list[i],int(vote_list[i])) for i,v in enumerate(view_list) if 'm views' in v], key= lambda x:x[1], reverse=True)

    return res

# def main():
#     actual_return = top_python_questions()
#     expected_return = [
#                         ('What does the “yield” keyword do?', 9169),
#                         ('Does Python have a ternary conditional operator?', 5135),
#                         ('What does if __name__ == “__main__”: do?', 4927),
#                         ('Calling an external command in Python', 4190),
#                         ('How to merge two dictionaries in a single expression?', 3874),
#                         ('How do I sort a dictionary by value?', 3394),
#                         ('Using global variables in a function', 2768),
#                         ('Understanding slice notation', 2707),
#                         ('How to make a flat list out of list of lists', 2545),
#                         ('How do I install pip on Windows?', 2388),
#                         ('How do I pass a variable by reference?', 2295),
#                         ('How to clone or copy a list?', 2063),
#                         ('How to read a file line-by-line into a list?', 2000),
#                         ('Converting string into datetime', 1816),
#                         ('How to print without newline or space?', 1615),
#                         ('Select rows from a DataFrame based on '
#                          'values in a column in pandas', 1304),
#                         ("Why does comparing strings using either '==' or 'is' "
#                          'sometimes produce a different result?', 1008)
#                         ]
#     # print(actual_return)
#     # print(expected_return)
#     actual_return == expected_return

# if __name__ == "__main__":
#     main()
