from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        # print('here ...')

        for v in self.values():
            if birthday.day == v.day and birthday.month == v.month:
                print(MSG.format(name))

        super(BirthdayDict, self).__setitem__(str(name), birthday)


# def main():

#     # print('here ...')
#     # print(MSG.format(2))

#     bd = BirthdayDict()
#     bd['bob'] = date(1987, 6, 15)
#     bd['tim'] = date(1984, 7, 15)
#     # print(bd)
#     # bd.update({'sara': date(1978, 6, 14)})
#     bd['mary'] = date(1987, 6, 15)
#     # bd['sara'] = date(1987, 6, 14)
#     bd['mike'] = date(1981, 7, 15)
#     print(bd)


# if __name__ == '__main__':
#     main()
