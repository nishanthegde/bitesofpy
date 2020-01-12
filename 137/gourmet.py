#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pairs wines and cheeses by similarity of wine name and cheese name.
"""

from collections import Counter
import operator
import re

CHEESES = [
    "Red Leicester",
    "Tilsit",
    "Caerphilly",
    "Bel Paese",
    "Red Windsor",
    "Stilton",
    "Emmental",
    "Gruyère",
    "Norwegian Jarlsberg",
    "Liptauer",
    "Lancashire",
    "White Stilton",
    "Danish Blue",
    "Double Gloucester",
    "Cheshire",
    "Dorset Blue Vinney",
    "Brie",
    "Roquefort",
    "Pont l'Evêque",
    "Port Salut",
    "Savoyard",
    "Saint-Paulin",
    "Carré de l'Est",
    "Bresse-Bleu",
    "Boursin",
    "Camembert",
    "Gouda",
    "Edam",
    "Caithness",
    "Smoked Austrian",
    "Japanese Sage Derby",
    "Wensleydale",
    "Greek Feta",
    "Gorgonzola",
    "Parmesan",
    "Mozzarella",
    "Pipo Crème",
    "Danish Fynbo",
    "Czech sheep's milk",
    "Venezuelan Beaver Cheese",
    "Cheddar",
    "Ilchester",
    "Limburger",
]

RED_WINES = [
    "Châteauneuf-du-Pape",  # 95% of production is red
    "Syrah",
    "Merlot",
    "Cabernet sauvignon",
    "Malbec",
    "Pinot noir",
    "Zinfandel",
    "Sangiovese",
    "Barbera",
    "Barolo",
    "Rioja",
    "Garnacha",
]

WHITE_WINES = [
    "Chardonnay",
    "Sauvignon blanc",
    "Semillon",
    "Moscato",
    "Pinot grigio",
    "Gewürztraminer",
    "Riesling",
]

SPARKLING_WINES = [
    "Cava",
    "Champagne",
    "Crémant d’Alsace",
    "Moscato d’Asti",
    "Prosecco",
    "Franciacorta",
    "Lambrusco",
]


def _find_similarity(w1: str, w2: str) -> float:

    dict1 = Counter(w1.lower())
    dict2 = Counter(w2.lower())

    common_dict = dict1 & dict2

    # print('----')
    # print(common_dict)

    sim = sum(list(common_dict.values())) / (1 + pow(len(w1) - len(w2), 2))
    return sim


def best_match_per_wine(wine_type="all"):
    """ wine cheese pair with the highest match score
    returns a tuple which contains wine, cheese, score
    """
    if wine_type != 'white' and wine_type != 'all' and wine_type != 'red' and wine_type != 'sparkling':
        raise ValueError('Incorrect Wine Type!')

    matches = list()

    if wine_type == 'white' or wine_type == 'all':
        for w in WHITE_WINES:
            for c in CHEESES:
                matches.append((w, c, _find_similarity(w, c)))

    if wine_type == 'red' or wine_type == 'all':
        for w in RED_WINES:
            for c in CHEESES:
                matches.append((w, c, _find_similarity(w, c)))

    if wine_type == 'sparkling' or wine_type == 'all':
        for w in SPARKLING_WINES:
            for c in CHEESES:
                matches.append((w, c, _find_similarity(w, c)))

    return max(matches, key=operator.itemgetter(2))


def match_wine_5cheeses():
    """  pairs all types of wines with cheeses ; returns a sorted list of tuples,
    where each tuple contains: wine, list of 5 best matching cheeses.
    List of cheeses is sorted by score descending then alphabetically ascending.
    e.g: [
    ('Barbera', ['Cheddar', 'Gruyère', 'Boursin', 'Parmesan', 'Liptauer']),
    ...
    ...
    ('Zinfandel', ['Caithness', 'Bel Paese', 'Ilchester', 'Limburger', 'Lancashire'])
    ]
    """

    best_five = list()

    for w in RED_WINES:
        matches = list()
        for c in CHEESES:
            matches.append((w, c, _find_similarity(w, c)))
        best_five.append((w, [i[1] for i in sorted(matches, key=lambda x: (-x[2], x[1]))[:5]]))

    for w in WHITE_WINES:
        matches = list()
        for c in CHEESES:
            matches.append((w, c, _find_similarity(w, c)))
        best_five.append((w, [i[1] for i in sorted(matches, key=lambda x: (-x[2], x[1]))[:5]]))

    for w in SPARKLING_WINES:
        matches = list()
        for c in CHEESES:
            matches.append((w, c, _find_similarity(w, c)))
        best_five.append((w, [i[1] for i in sorted(matches, key=lambda x: (-x[2], x[1]))[:5]]))

    return sorted(best_five, key=lambda x: x[0])


def main():
    print('thank you for everything you have given me ...')

    # print(len(CHEESES))
    # print(len(RED_WINES))
    # print(len(WHITE_WINES))
    # print(len(SPARKLING_WINES))
    # # print(pow(5, 2))

    # print(_find_similarity('house', 'mouse'))
    # print(_find_similarity('parapraxis', 'explanation'))
    # print(_find_similarity('parapraxis', 'parallax'))
    # print(_find_similarity('roosters-do-sound', 'cocka-doodle-doo'))
    # print(_find_similarity('Cabernet sauvignon', 'Dorset Blue Vinney'))
    # print(best_match_per_wine('white'))
    # print(best_match_per_wine('red'))
    # print(best_match_per_wine('sparkling'))

    # print(best_match_per_wine())
    # print(len(match_wine_5cheeses()))
    mw5c = match_wine_5cheeses()
    print(mw5c[0][0])


if __name__ == '__main__':
    main()
