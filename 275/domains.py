from collections import Counter
import bs4
import requests
import re

COMMON_DOMAINS = ("https://bites-data.s3.us-east-2.amazonaws.com/"
                  "common-domains.html")
TARGET_DIV = {"class": "middle_info_noborder"}


def get_common_domains(url=COMMON_DOMAINS):
    """Scrape the url return the 100 most common domain names"""
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.text, 'html.parser')

    pattern = re.compile(r'[a-zA-Z0-9]*\.[a-zA-Z]{2,}\.*[a-zA-Z]*')

    domains = list()

    for header in soup.find_all('h2', text='Top 100'):
        nextNode = header
        while True:
            nextNode = nextNode.nextSibling
            if nextNode is None:
                break
            # if nextNode.name == "table":
            if isinstance(nextNode, bs4.element.Tag):
                # print(nextNode)
                all_td = nextNode.find_all("td")
                for td in all_td:
                    domain = pattern.search(td.text)
                    if domain:
                        domains.append(domain.group(0))

    return domains


def get_most_common_domains(emails, common_domains=None):
    """Given a list of emails return the most common domain names,
       ignoring the list (or set) of common_domains"""
    if common_domains is None:
        common_domains = get_common_domains()

    c = Counter([e.split('@')[1] for e in emails if e.split('@')[1] not in common_domains])

    return c.most_common()


def main():
    print('thank you for everything you have given me... ')
    print(len(get_common_domains()))
    print(get_most_common_domains(["a@gmail.com", "b@pybit.es", "c@pybit.es", "d@domain.de"]))


if __name__ == '__main__':
    main()
