num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds

    num_hundreds += sum(numbers) // 100
    print(num_hundreds)
    return sum(numbers)


def main():
    print('thank you for everything you have given me...')
    print(sum_numbers([]))
    print(sum_numbers([1, 2, 3]))
    print(sum_numbers([40, 50, 60]))
    print(sum_numbers([140, 50, 60]))
    print(sum_numbers([140, 150, 160]))
    print(sum_numbers([1140, 150, 160]))


if __name__ == '__main__':
    main()
