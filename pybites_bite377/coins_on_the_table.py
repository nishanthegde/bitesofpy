PENNY = 0.01  # use this to represent the penny
NICKEL = 0.05  # use this to represent the nickel
DIME = 0.1  # use this to represent the dime
QUARTER = 0.25  # use this to represent the quarter


def coins_on_the_table():
    """Return a sequence of all 1001 coins on the table."""
    coins = [PENNY for _ in range(1001)]

    # replace every other penny with a nickle
    for i in range(1, len(coins), 2):
        coins[i] = NICKEL

    # replace every third coin with a dime
    for i in range(2, len(coins), 3):
        coins[i] = DIME

    # replace every fourth coin with a quarter
    for i in range(3, len(coins), 4):
        coins[i] = QUARTER

    return coins
