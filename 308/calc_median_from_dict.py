from collections import OrderedDict


def calc_median_from_dict(d: dict) -> float:
    """
    :param d: dict of numbers and their occurrences
    :return: float: median
    Example:
    {1: 2, 3: 1, 4: 2} -> [1, 1, 3, 4, 4] --> 3 is median
    """
    if any(not isinstance(i, int) for i in d.values()):
        raise TypeError

    od = OrderedDict(sorted(d.items()))
    num = 0
    den = 0
    for k, v in od.items():
        num += k * v
        den += v

    if (num / den) % 1 < .5:
        return round((num / den), 0)
    else:
        return num / den

# def main():
#     print("thank you for looking after my family...")
#     # print(calc_median_from_dict({1: "a"}))
#     print(calc_median_from_dict({
#         0: 800_000_000,
#         1: 200_000_000,
#         2: 200_000_000,
#         3: 200_000_000,
#         4: 200_000_000,
#         5: 1_000_000_000,
#         6: 20_000_000_000,
#         7: 4_000_000_000,
#         8: 8_000_000_000,
#         9: 16_000_000_000,
#     }))
#
#
# if __name__ == "__main__":
#     main()
