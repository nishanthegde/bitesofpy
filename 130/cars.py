from collections import Counter

import requests

CAR_DATA = 'https://bit.ly/2Ov65SJ'

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


def most_prolific_automaker(year: int) -> str:
    """Given year 'year' return the automaker that released
       the highest number of new car models"""
    year_models = [d['automaker'] for d in data if d['year'] == year]
    c = Counter(year_models)
    return c.most_common(1)[0][0]


def get_models(automaker: str, year: int) -> set:
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    models = set([d['model'] for d in data if d['automaker'] == automaker and d['year'] == year])

    return models


# def main():
#     print('focus ...')
#     # print(len(data))
#     print(most_prolific_automaker(1999))
#     print(most_prolific_automaker(2008))
#     print(most_prolific_automaker(2013))

#     models = get_models('Volkswagen', 2008)
#     print(models)

#     print(get_models('Nissan', 2000))
#     print(get_models('Opel', 2008))
#     print(get_models('Mercedes-Benz', 2007))


# if __name__ == '__main__':
#     main()
