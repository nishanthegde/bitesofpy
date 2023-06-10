def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
    returns a sequence of same length with the averages.
    You can assume all items in sequence are numeric."""

    running_means = []

    for i in range(1, len(sequence) + 1):
        running_means.append(round(sum(sequence[0:i]) / len(sequence[0:i]), 2))

    return running_means
