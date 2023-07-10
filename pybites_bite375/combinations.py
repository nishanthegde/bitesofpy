import itertools
from collections import defaultdict

digits_dict = defaultdict(list)

digits_dict["2"] = ["a", "b", "c"]
digits_dict["3"] = ["d", "e", "f"]
digits_dict["4"] = ["g", "h", "i"]
digits_dict["5"] = ["j", "k", "l"]
digits_dict["6"] = ["m", "n", "o"]
digits_dict["7"] = ["p", "q", "r", "s"]
digits_dict["8"] = ["t", "u", "v"]
digits_dict["9"] = ["w", "x", "y", "z"]


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
    all_digits = []
    output = []

    if len(digits) > 4 or not digits.isnumeric():
        raise ValueError
    else:
        for d in digits:
            all_digits.append(digits_dict[d])

    for comb in list(itertools.product(*all_digits)):
        output.append("".join([ele for ele in comb]))

    return sorted(output)


if __name__ == "__main__":
    generate_letter_combinations()
