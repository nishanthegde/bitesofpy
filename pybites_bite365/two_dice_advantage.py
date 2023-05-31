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
    outcomes = []
    exp_value = 0

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            outcomes.append((i, j))

    for i in range(1, n + 1):
        num_ways = 0
        for outcome in outcomes:
            if max(outcome) == i:
                num_ways += 1
        exp_value += i * num_ways / len(outcomes)

    return round(exp_value, 3)
