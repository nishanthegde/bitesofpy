def uncommon_cities(my_cities: list, other_cities: list) -> int:
    """Compare my_cities and other_cities and return the number of different
       cities between the two"""
    return len(set(my_cities) ^ set(other_cities))


# def main():
#     print('thank you for the curiosity ...')

#     my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
#     other_cities = ['Paris', 'Boston', 'Sydney', 'Madrid', 'Moscow', 'Lima']

#     my_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']
#     other_cities = ['Rome', 'Paris', 'Madrid', 'Chicago', 'Seville', 'Berlin']

#     my_cities = ['Rome', 'Paris', 'Madrid']
#     other_cities = ['Chicago', 'Seville', 'Berlin']

#     print(uncommon_cities(my_cities, other_cities))


# if __name__ == '__main__':
#     main()
