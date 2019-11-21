import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        pos = bisect.bisect_left(self._numbers, num)
        self._numbers.insert(pos, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)


# def main():
#     print('thank you for everything...')
#     order = OrderedList()
#     order.add(10)
#     print(order)
#     order.add(1)
#     print(order)
#     order.add(16)
#     print(order)
#     order.add(5)
#     print(order)


# if __name__ == '__main__':
#     main()
