def combine_and_count(a: dict, b: dict) -> dict:
    """Combine two dictionaries.

    Return  new dictionary with the combined keys and values.
    For any key found in both dictionaries,
    return the sum of the values for that key.

    Args:
      a: The first dictionary.
      b: The second dictionary.

    Returns:
      A dictionary with the contents of both.
      Values of any shared keys are summed.
    """
    if not a:
        return b

    if not b:
        return a

    # check overlapping keys
    overlap_keys = [key for key in a if key in b]

    combined = a | b

    for key in overlap_keys:
        combined[key] += a[key]

    return combined
