def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [n for n in numbers if n % 2 == 0 and n > 0]


# def main():
#     print('here')

#     numbers = list(range(-10, 11))
#     assert filter_positive_even_numbers(numbers) == [2, 4, 6, 8, 10]

#     numbers = [2, 4, 51, 44, 47, 10]
#     assert filter_positive_even_numbers(numbers) == [2, 4, 44, 10]

#     numbers = [0, -1, -3, -5]
#     assert filter_positive_even_numbers(numbers) == []


# if __name__ == '__main__':
#     main()
