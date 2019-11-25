def round_even(number: float) -> int:
    """Takes a number and returns it rounded even"""
    mid = False
    if round(number) - number == 0.5:
        mid = True

    if mid and round(number) % 2 != 0:
        return int(number)
    else:
        return round(number)


# def main():
#     print('thank you for everything...')
#     print(round_even(1.6))


# if __name__ == '__main__':
#     main()
