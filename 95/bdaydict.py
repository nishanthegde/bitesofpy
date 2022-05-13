from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""

    def __setitem__(self, name, birthday):

        for key in self:
            if super(BirthdayDict, self).__getitem__(key).month == birthday.month \
                    and super(BirthdayDict, self).__getitem__(key).day == birthday.day:
                print(MSG.format(name))

        super(BirthdayDict, self).__setitem__(name, birthday)
