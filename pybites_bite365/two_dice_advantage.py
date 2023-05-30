def original_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die."""
    exp_value = 0

    for i in range(1, n + 1):
        exp_value += i * 1 / n

    return round(exp_value, 1)


def new_expected_value(n: int) -> float:
    """Calculate the expected value of an n-sided die when the player simultaneously rolls
    two dice and chooses the larger value.
    """
    pass


def main():
    print(original_expected_value(6))


if __name__ == "__main__":
    main()
