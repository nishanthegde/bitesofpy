class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    def __len__(self):
        return len(self._transactions)

    def __add__(self, value):

        if not(isinstance(value, int)):
            raise ValueError("only int can be added to Account object")
        self._transactions.append(value)

    def __sub__(self, value):

        if not(isinstance(value, int)):
            raise ValueError("only int can be added to Account object")
        self._transactions.append(-value)

    def __getitem__(self, key):
        return self._transactions[key]

    def __gt__(self, acc2):
        return self.balance > acc2.balance

    def __lt__(self, acc2):
        return self.balance < acc2.balance

    def __le__(self, acc2):
        return self.balance <= acc2.balance

    def __ge__(self, acc2):
        return self.balance >= acc2.balance

    def __eq__(self, acc2):
        return self.balance == acc2.balance

    def __str__(self):
        return '{} account - balance: {}'.format(self.name.capitalize(), self.balance)

# def main():
#     """
#         Let's enrich an Account class by adding dunder (aka special) methods to support the following:

#         length of the object: len(acc) returns the number of transactions
#         account comparison: acc1 >,<,>=.<=,== acc2 returns a boolean comparing account balances
#         indexing: acc[n] shows the nth transaction onaccount (0 based)
#         iteration: list(acc) returns a sequence of account transactions
#         operator overloading: acc + int and acc - int can be used to add/subtract money
#         string representation: str(acc) returns NAME account - balance: INT
#     """
#     # checking = Account('Checking')
#     # saving = Account('Saving', 10)

#     # # print(type(checking))
#     # # print(checking.name, type(checking.name))
#     # # print(checking.start_balance, type(checking.start_balance))
#     # # print(checking._transactions, type(checking._transactions))
#     # checking + 10
#     # saving - 5
#     # print(checking > saving)
#     # print(checking >= saving)
#     # print(saving < checking)
#     # print(saving <= checking)
#     # print(saving == checking)
#     # saving + 5
#     # print(saving == checking)
#     # print(str(checking))
#     # saving + 5
#     # print(str(saving))
#     # print(checking.balance)
#     # print(len(checking))
#     # print(saving.balance)
#     # print(len(saving))
#     # print(sum(checking._transactions))
#     # # print(checking.balance)
#     # print(type(saving))
#     # print(saving.name, type(saving.name))
#     # print(saving.start_balance, type(saving.start_balance))
#     # print(saving._transactions, type(saving._transactions))

# if __name__ == "__main__":
#     main()
