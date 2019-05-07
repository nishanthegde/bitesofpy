def sum_numbers(numbers=None):

    """
        Function that accepts a list and returns the sum of the numbers in the list.
        If no argumet is provided it calculates the sum of 1 to 100.
    """

    s = 0

    if numbers != None:
        s = sum(numbers)
    else:
        for n in range(1,101):
            s += n

    return s



# r = sum_numbers(range(1, 11))
# r = sum_numbers([])
# r = sum_numbers()
# r = sum_numbers(None)
# r = sum_numbers(numbers=None)
# print(r)
