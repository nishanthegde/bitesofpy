from itertools import groupby
from collections import defaultdict

cars = [
    # need mock data? -> https://www.mockaroo.com == awesome
    ('Mercedes-Benz', '300D'), ('Mercedes-Benz', '600SEL'),
    ('Toyota', 'Avalon'), ('Ford', 'Bronco'),
    ('Chevrolet', 'Cavalier'), ('Chevrolet', 'Corvette'),
    ('Mercedes-Benz', 'E-Class'), ('Hyundai', 'Elantra'),
    ('Volkswagen', 'GTI'), ('Toyota', 'Highlander'),
    ('Chevrolet', 'Impala'), ('Nissan', 'Maxima'),
    ('Ford', 'Mustang'), ('Kia', 'Optima'),
    ('Volkswagen', 'Passat'), ('Nissan', 'Pathfinder'),
    ('Volkswagen', 'Routan'), ('Hyundai', 'Sonata'),
    ('Kia', 'Sorento'), ('Kia', 'Sportage'),
    ('Ford', 'Taurus'), ('Nissan', 'Titan'),
    ('Toyota', 'Tundra'), ('Hyundai', 'Veracruz'),
]

expected_output = """
CHEVROLET
- Cavalier
- Corvette
- Impala

FORD
- Bronco
- Mustang
- Taurus

HYUNDAI
- Elantra
- Sonata
- Veracruz

KIA
- Optima
- Sorento
- Sportage

MERCEDES-BENZ
- 300D
- 600SEL
- E-Class

NISSAN
- Maxima
- Pathfinder
- Titan

TOYOTA
- Avalon
- Highlander
- Tundra

VOLKSWAGEN
- GTI
- Passat
- Routan
"""

actual = """
CHEVROLET
- Cavalier
- Corvette
- Impala

FORD
- Bronco
- Mustang
- Taurus

HYUNDAI
- Elantra
- Sonata
- Veracruz

KIA
- Optima
- Sorento
- Sportage

MERCEDES-BENZ
- 300D
- 600SEL
- E-Class

NISSAN
- Maxima
- Pathfinder
- Titan

TOYOTA
- Avalon
- Highlander
- Tundra

VOLKSWAGEN
- GTI
- Passat
- Routan
"""


def group_cars_by_manufacturer(cars: list):
    """Iterate though the list of (manufacturer, model) tuples
       of the cars list defined above and generate the output as described
       in the Bite description (see the tests for the full output).

       No return here, just print to the console. We use pytest > capfd to
       validate your output :)
    """
    models = defaultdict(list)
    for k, g in groupby(cars, lambda x: x[0]):
        for model in g:
            models[k].append(model[1])
        # print(k, [model[1] for model in g])
        # print(k, g)

    models = sorted(models.items())

    for i, line in enumerate(models):
        print('{}'.format(line[0].upper()))
        for c in line[1]:
            print('- {}'.format(c))
        if i < len(models) - 1:
            print()
    # print([i[0].upper() for i in models])
    # for m in models.items():
    #     print(m.upper())

    # for i, line in enumerate(models):
    #     print(i, line)


# def main():
#     # print('it is time to focus on machine learning...')
#     group_cars_by_manufacturer(cars)
#     assert expected_output == actual


# if __name__ == '__main__':
#     main()
