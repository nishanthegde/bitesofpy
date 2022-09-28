def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    else:
        if not numbers:
            numbers = list(range(1, 101))

    return sum(numbers)
