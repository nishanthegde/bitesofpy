from abc import ABC, abstractmethod


class Challenge(ABC):

    @abstractmethod
    def __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self):
        pass

    @property
    @abstractmethod
    def pretty_title(self):
        pass


class BlogChallenge(Challenge):

    pretty_title = 'PCC1 - Wordvalues'

    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merged_prs = merged_prs

    def verify(self, value):
        return value in self.merged_prs


class BiteChallenge(Challenge):

    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result

    def verify(self, value):
        return value == self.result

    @property
    def pretty_title(self):
        return 'Bite {}. {}'.format(self.number, self.title)


# def main():
#     """
#         You define one or more methods and/or properties as abstract in the base class, and if the subclass does not implement them it raises a TypeError. In this bite you will use this concept as follows:

#         Define a Challenge base class that inherits from ABC (given), its constructor receives a number and a title attribute.

#         On Challenge define an abstractmethod called verify and an property (< 3.3 it would be an abstractproperty) called pretty_title.
#         Create the BlogChallenge and BiteChallenge classes which both inherit from Challenge. Note that they would raise a TypeError at this point,
#         exactly what you want: enforcing the use of the abstract method/ property.

#         BlogChallenge and BiteChallenge's constructors call the parent constructor (don't worry it's supercool, remember: we use Python3 so adjust your syntax),
#         and both receive an extra argument in the constructor: merged_prs for BlogChallenge and result for BiteChallenge.

#         Implement the required methods and properties, refer to the tests what they need to return.

#         Get coding, learn more about classes, and have fun!

#     """
#     # ch = Challenge(0, 'Should not instantiate ABC')
#     # print(ch.number)

#     blog = BlogChallenge(1, 'Wordvalues', [41, 42, 44])
#     assert blog.verify(41)
#     assert not blog.verify(43)
#     assert blog.pretty_title == 'PCC1 - Wordvalues'

#     bite = BiteChallenge(24, 'ABC and class inheritance', 'my result')

#     assert bite.verify('my result')
#     assert not bite.verify('other result')
#     assert bite.pretty_title == 'Bite 24. ABC and class inheritance'


# if __name__ == "__main__":
#     main()
