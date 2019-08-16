# from string import ascii_lowercase

# PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
# ALPHABET = list(ascii_lowercase)
# test_list = ['n', 'c', 'g', 'b', 'k']
# test_list1 = ['n', 'b', 'g', 'd']
# test_list2 = [100]
# test_list3 = [2, 3]


def binary_search(sequence, target):

    sequence = sorted(sequence)

    start = 0
    end = len(sequence) - 1

    cntr = 0

    while start <= end:

        # print(sequence[start:end + 1])

        # print("start is {}".format(start))
        # print("end is {}".format(end))

        # print(start + (end - start) / 2)
        mid = (start + (end - start) / 2)
        # print(mid % 2)

        # if mid % 2 != 0:
        #     mid -= .5

        mid = int(mid)
        # print(mid)

        # print("mid is {}\n".format(mid))

        if target == sequence[mid]:
            return mid

        if target < sequence[mid]:
            end = mid - 1

        if target > sequence[mid]:
            start = mid + 1

        cntr += 1

        # if cntr == 5:
        #     break


# def main():
#     print("dance")

#     # ret = binary_search(PRIMES, 3)

#     # ret = binary_search(test_list1, 'z')

#     # ret = binary_search(test_list3, 1000)

#     # ret = binary_search(test_list1)

#     # ret = binary_search(test_list2)

#     # ret = binary_search(test_list2, 1001)

#     # print(ret)

#     assert binary_search(PRIMES, 2) == 0
#     assert binary_search(PRIMES, 59) == 16
#     assert binary_search(PRIMES, 5) == 2
#     assert binary_search(PRIMES, 61) == 17
#     assert binary_search(PRIMES, 18) == None

#     # ret = binary_search(ALPHABET, 'aaaa')
#     # print(ret)

#     assert binary_search(ALPHABET, 'u') == 20
#     assert binary_search(ALPHABET, 'a') == 0
#     assert binary_search(ALPHABET, 'z') == 25


# if __name__ == '__main__':
#     main()
