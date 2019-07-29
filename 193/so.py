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

    res = sorted([(ques_list[i],vote_list[i]) for i,v in enumerate(view_list) if 'm views' in v], key= lambda x:x[1], reverse=True)

    return res

# def main():
#     actual_ret = top_python_questions()
#     print(actual_ret)
#     print(len(actual_ret))
#     # print(len(actual_return))

# if __name__ == "__main__":
#     main()
