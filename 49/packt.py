from collections import namedtuple

from bs4 import BeautifulSoup as Soup
import requests

CONTENT = requests.get('http://bit.ly/2EN2Ntv').text

Book = namedtuple('Book', 'title description image link')

def get_book():
    """make a Soup object, parse the relevant html sections, and return a Book namedtuple"""
    soup = Soup(CONTENT, 'html.parser')

    # list to hold descriptions
    desc = []
    # get title and desc tags
    for div in soup.find_all('div', attrs={'class': 'dotd-main-book-summary float-left'}):
        div_descendants = div.descendants
        for d in div_descendants:
            if d.name == 'div':
                # print(type(d.get('class', '')))
                if d.get('class', '') == ['dotd-title']:
                    title = d.text.strip()
                if d.get('class', '') == '':
                    desc.append(d.text.strip())

    # list to hold images
    img_src = []
    # get image and link
    for div in soup.find_all('div', attrs={'class': 'dotd-main-book-image float-left'}):
        div_descendants = div.descendants
        for d in div_descendants:
            if d.name == 'a':
                link = d.get('href').strip()
            if d.name == 'img':
                img_src.append(d.get('src').strip())

    #return first element in desc and img_src lists
    book = Book(title=title, description=desc[0], image =img_src[0], link=link)

    return book

# def main():

#     book = get_book()
#     # print(type(book))
#     print(book)

#     # get text of first h2 tag. this is the title of the free e book
#     # print(book.find_all('h2')[0].text.strip())

#     #free_book = book.find_all("div", class_="dotd-title")


#     # for bk in free_book:
#     #     temp = bk.find('h2')
#     #     if temp:
#     #         print(temp.text.strip())


#     # get title
#     # for div in book.findAll('div', attrs={'class':'dotd-title'}):
#     #     print(div.text.strip())


#     # get desc
#     # for outer_div in book.findAll('div', attrs={'class': 'dotd-main-book-summary float-left'}):
#     #     for inner_div in book.findAll('div', attrs={'class': None}):
#     #         print(inner_div.text)
#     # print(' '.join(book.find('div', {'class': 'dotd-main-book-summary float-left'}).stripped_strings))

#     # for s in book.find('div', {'class': 'dotd-main-book-summary float-left'}).stripped_strings:
#     #     print(s)
#     # write contents of the html file for checking
#     # with open("packt.html", "w") as file:
#     #     file.write(str(book))

# if __name__ == "__main__":
#     main()
