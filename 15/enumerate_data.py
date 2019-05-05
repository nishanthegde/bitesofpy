names = 'Julian Bob PyBites Dante Martin Rodolfo test1'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()

def enumerate_names_countries(names, countries):
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    per = '.'
    l = zip(names, countries)
    for index, (n,c) in enumerate(l):
      print(f'{index+1}{per} {n: <{11}} {c}')

    pass


enumerate_names_countries(names, countries)
