import re

def extract_course_times():
    """Write a regular expression that returns a list of timestamps:
        ['01:47', '32:03', '41:51', '27:48', '05:02']"""
    flask_course = ('Introduction 1 Lecture 01:47'
                    'The Basics 4 Lectures 32:03'
                    'Getting Technical!  4 Lectures 41:51'
                    'Challenge 2 Lectures 27:48'
                    'Afterword 1 Lecture 05:02')
    pattern = r'\d{2}:\d{2}'
    return re.findall(pattern, flask_course)

def get_all_hashtags_and_links():
    """Write a regular expression that returns this list:
       ['http://pybit.es/requests-cache.html', '#python', '#APIs']"""

    tweet = ('New PyBites article: Module of the Week - Requests-cache '
             'for Repeated API Calls - http://pybit.es/requests-cache.html '
             '#python #APIs')

    pattern = r'http[s]?:\/\/(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    url_hashes = re.findall(pattern, tweet)

    pattern = r'\B(\#[a-zA-Z]+\b)'
    return url_hashes + re.findall(pattern, tweet)


def match_first_paragraph():
    """Write a regular expression that returns  'pybites != greedy' """
    html = ('<p>pybites != greedy</p>'
            '<p>not the same can be said REgarding ...</p>')
    html2 = 'test'
    pattern = r'<p>(.*?)<\/p>'
    match_list = re.findall(pattern, html)

    if match_list:
        return(match_list[0])


# def main():
#     times = extract_course_times()
#     print(times)
#     hl = get_all_hashtags_and_links()
#     print(hl)
#     para = match_first_paragraph()
#     print(para)

# if __name__ == "__main__":
#     main()
