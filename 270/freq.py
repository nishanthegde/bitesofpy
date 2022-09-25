from collections import Counter


def freq_digit(num: int) -> int:
    num_str = str(num)
    digit_count = Counter(num_str)

    return int(digit_count.most_common(1)[0][0])
