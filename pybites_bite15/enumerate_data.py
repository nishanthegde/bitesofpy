names = "Julian Bob PyBites Dante Martin Rodolfo".split()
countries = "Australia Spain Global Argentina USA Mexico".split()


def enumerate_names_countries():
    """Outputs:
    1. Julian     Australia
    2. Bob        Spain
    3. PyBites    Global
    4. Dante      Argentina
    5. Martin     USA
    6. Rodolfo    Mexico"""

    for i in range(1, len(names) + 1):
        print(f"{i}. {names[i-1]}{' '* (11-len(names[i-1]))}{countries[i-1]}")
