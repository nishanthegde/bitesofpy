def generate_affiliation_link(url: str) -> str:
    aff = url.split('dp')[-1:][0].strip().split('/')[1]
    return '{}{}{}'.format('http://www.amazon.com/dp/', aff, '/?tag=pyb0f-20')
    # return url.split('/')[len(url.split('/')) - 2]


# original_links = [
#     ('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
#      '?keywords=war+of+art'),
#     ('https://amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
#      'ref=sr_1_1'),
#     ('https://www.amazon.es/War-Art-Through-Creative-Battles/dp/1936891026/'
#      '?qid=1537226234'),
#     'https://www.amazon.co.uk/Pragmatic-Programmer-Andrew-Hunt/dp/020161622X',
#     ('https://www.amazon.com.au/Python-Cookbook-3e-David-Beazley/dp/'
#      '1449340377/'),
#     ('https://www.amazon.com/fake-book-with-longer-asin/dp/'
#      '1449340377000/'),
# ]


# def main():
#     print('thank you for the waves...')

#     for u in original_links:
#         print(generate_affiliation_link(u))

#     assert 'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20' == 'http://www.amazon.com/dp/1936891026/?tag=pyb0f-20'


# if __name__ == '__main__':
#     main()
