from collections import namedtuple
from datetime import datetime

Transaction = namedtuple('Transaction', 'giver points date')
Transaction.__new__.__defaults__ = (datetime.now(),)  # http://bit.ly/2rmiUrL




class User:

    def __init__(self, name):

        self.name = name
        self._transactions = []
        self.points = self._transactions
        self.karma = 0
        self.fans = 0

    def __add__(self, other):

        self.karma += other.points
        self._transactions.append(other.points)
        self.points = self._transactions

        if other.points > 0:
            self.fans += 1

    def __str__(self):

        if self.fans > 1:
            return '{} has a karma of {} and {} fans'.format(self.name, self.karma, self.fans)

        return '{} has a karma of {} and {} fan'.format(self.name, self.karma, self.fans)

def main():

    alice = User('alice')
    bob = User('bob')
    tim = User('tim')

    transactions = [
    Transaction(giver=alice, points=1),
    Transaction(giver=bob, points=2),
    Transaction(giver=tim, points=3),
    Transaction(giver=tim, points=4),
    Transaction(giver=alice, points=2),
    ]

    assert alice.name == 'alice'
    assert bob.name == 'bob'
    assert tim.name == 'tim'
    assert alice._transactions == []
    assert bob._transactions == []
    assert tim._transactions == []

    bob + transactions[0]
    assert bob.karma == 1
    alice + transactions[1]
    assert alice.karma == 2
    bob + transactions[2]
    assert bob.karma == 4
    alice + transactions[3]
    assert alice.karma == 6
    tim + transactions[4]
    assert tim.karma == 2

    assert bob.points == [1, 3]
    assert alice.points == [2, 4]
    assert tim.points == [2]

    assert tim.fans == 1
    assert bob.fans == 2
    assert alice.fans == 2

    assert str(tim) == 'tim has a karma of 2 and 1 fan'
    assert str(alice) == 'alice has a karma of 6 and 2 fans'
    assert str(bob) == 'bob has a karma of 4 and 2 fans'

if __name__ == "__main__":
    main()
