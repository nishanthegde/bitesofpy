from collections import defaultdict


def group_anagrams(strings: list[str]) -> list[list[str]]:
    """Group anagrams together."""
    anagrams = defaultdict(list, {k: [] for k in strings})

    for k in anagrams.keys():
        anagrams[k] = [v for v in strings if sorted(v) == sorted(k)]

    ret = list(anagrams.values())

    uniq_ret = []

    for r in ret:
        if r not in uniq_ret:
            uniq_ret.append(r)

    return uniq_ret


if __name__ == "__main__":
    print(group_anagrams(words))
