import itertools


def running_mean(sequence: list) -> list:
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    it = iter(sequence)
    n = len(sequence)

    run_mean = []

    for i in range(1, n + 1):
        win = list(itertools.islice(sequence, 0, i, 1))
        run_mean.append(round(sum(win) / len(win), 2))

    return run_mean


# def main():
#     print('thank you...')
#     print(running_mean([1, 2, 3]))
#     assert [1.0, 1.5, 2.0] == [1, 1.5, 2]


# if __name__ == '__main__':
#     main()
