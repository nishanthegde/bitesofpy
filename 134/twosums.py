from random import sample, seed

NUMBERS = [2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440, 1538, 7994, 465,
           6387, 7091, 9953, 35, 7298, 4364, 3749, 9686, 1675, 5201, 502, 366, 417,
           8871, 151, 6246, 3549, 6916, 476, 8645, 3633, 7175, 8124, 9059, 3819, 5664,
           3783, 3585, 7531, 4748, 353, 6819, 9117, 1639, 3046, 4857, 1981]


def two_sums(numbers, target):
    """Finds the indexes of the two numbers that add up to target.

    :param numbers: list - random unique numbers
    :param target: int - sum of two values from numbers list
    :return: tuple - (index1, index2) or None
    """
    candidate_values = []

    numbers_sorted = sorted(numbers)

    # print(numbers_sorted)

    for i, item in enumerate(numbers_sorted):
        for j in range(i + 1, len(numbers_sorted)):
            # print(i, item, j, numbers_sorted[j])
            if item + numbers_sorted[j] == target:
                # print(item, numbers_sorted[j])
                candidate_values.append((numbers.index(item), numbers.index(numbers_sorted[j])))
                # print(candidate_values)

    if candidate_values:
        return list(candidate_values)[0]

# 502 476

# def main():
#     """
#         assuming we have two indices pointing to two of the values in the numbers list, i and j.
#         the sum of i and j could only fall into one of these three possibilities:
#         i + j > target - increasing i ins't going to help us, as it makes the sum even bigger. Therefore we should decrease j
#         i + j < target - decreasing j isn't going to help us, as it makes the sum even smaller. Therefore we should increase i
#         i + j == target - We have found the answer
#     """

#     # print("dance")
#     numbers = [3, 10, 14, 8, 15, 5, 16, 13, 9, 2]
#     expected = (2, 6)
#     target = 30
#     result = two_sums(numbers, target)
#     assert result == expected

#     ret = two_sums(NUMBERS, 2934785974)
#     # print(ret)
#     # print(NUMBERS[ret[0]], NUMBERS[return[1]])
#     # print(NUMBERS[31], NUMBERS[42])

#     seed(1)
#     numbers = sample(range(1, 1_000_000), 1_000)
#     # print(numbers)
#     picked = sample(numbers, 2)
#     # print(picked)

#     index1 = numbers.index(picked[0])
#     index2 = numbers.index(picked[1])
#     # print(index1, index2)
#     ordered = sorted([index1, index2])
#     # print(ordered)
#     expected = ordered[0], ordered[1]
#     # print(expected)
#     target = sum(picked)
#     # print(target)

#     result = two_sums(numbers, target)

#     assert result == expected

#     result = two_sums(NUMBERS, 7000)
#     assert result is None


# if __name__ == "__main__":
#     main()
