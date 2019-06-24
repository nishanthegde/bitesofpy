def get_profile(name, age, *args, **kwargs):
    """function that accepts required name, required age, one or more optional sports (args),
    one or more optional awards (keyword args) and returns a dict with all arguments
    get_profile('tim', 36) == {'name': 'tim', 'age': 36}  # some arg types
    {'name': 'tim', 'age': 36, 'sports': ['basketball', 'tennis'], 'awards': {'champ': 'helped out team in crisis'}}  # all arg types
    """
    d = {}
    if isinstance(age, int) == True: #age is validated
        d['name'] = name
        d['age'] = age

        if args:
            l=sorted(list(args))

            if len(l) > 5:
                raise ValueError("provide 5 or less teams ")
            else: #length of *args is validated
                d['sports'] = l

        if kwargs:
            d['awards'] = kwargs

        return d
    else: #age is not valid
        raise ValueError("age must be an int")

