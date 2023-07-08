def generate_letter_combinations(digits: str) -> list[str]:
    """
    Calculate all possible letter combinations of a very short phone number.
    Input: A string of up to four digits.
    Output: A list of strings where each string represents a valid combination of letters
        that can be formed from the input. The strings in the output list should be sorted
        in lexicographical order.
    Raises: `ValueError`: If the input `digits` string contains non-digit characters or
        has more than four digits.
    """
    if len(digits) > 4 or not digits.isnumeric():
        raise ValueError
    else:
        print(digits)


def main():
    print("thank you for everything")


if __name__ == "__main__":
    # main()
    generate_letter_combinations("97s9")
