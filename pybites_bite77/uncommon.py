def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
      cities between the two"""
    set1 = set(my_cities)
    set2 = set(other_cities)
    intersection = set1 & set2
    not_intersection = (set1 | set2) - intersection

    return len(list(not_intersection))
