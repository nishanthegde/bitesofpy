from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""

data2 = """last_name,first_name,country_code
Poxton,Sydney,CZ
Kynman,Bryant,NL
Mockler,Leese,AF
Gillicuddy,Raffaello,IR
Renyard,Carlo,CO
Beadham,Evonne,CZ
Tunstall,Allissa,IR
Kamenar,Augy,IR
Insko,Ave,NL
Pigney,Gavrielle,ID"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)

    entries = data.split('\n')[1:]
    for e in entries:
        countries[e.split(',')[-1]].append('{} {}'.format(e.split(',')[1], e.split(',')[0]))

    return countries


# def main():
#     print('here ...')
#     grouping1 = group_names_by_country(data)
#     assert type(grouping1) == defaultdict
#     assert len(grouping1) == 7
#     print(sorted(grouping1['CN']))

#     grouping2 = group_names_by_country(data2)
#     assert len(grouping2) == 6
#     print(sorted(grouping2['IR']))


# if __name__ == '__main__':
#     main()
