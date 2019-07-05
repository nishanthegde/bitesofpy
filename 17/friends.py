from itertools import permutations, combinations

def friends_teams(friends, team_size=2, order_does_matter=False):
    """
        A function that takes a list of friends, a team_size (type int, default=2) and order_does_matter (type bool, default False),
        and returns all possible teams.
        If order matters (order_does_matter=True), the number of teams would be greater.
    """
    if order_does_matter:
        res = permutations(friends, team_size)
    else:
        res = combinations(friends, team_size)

    return (i for i in list(res))

# def main():
#     friends = 'Bob Dante Julian Martin'.split()
#     combos = list(friends_teams(friends, team_size=3, order_does_matter=True))
#     print(len(combos))
#     print(combos)

# if __name__ == "__main__":
#     main()
