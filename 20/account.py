class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    def __enter__(self):
        self._copy_transactions = list(self._transactions)
        return self

    def roll_back(self):
        self.balance

    def __exit__(self, exc_type, exc_value, exc_traceback):

        if self.balance < 0:
            self._transactions = self._copy_transactions
            self.roll_back()

        return True


# def main():
#     """
#         The purpose of the context manager is to roll back any transaction that will make the balance go below 0 (debt != cool). The rest of the class is already defined so you can focus on the context manager part.
#     """
#     # print("write a context manager")

#     account = Account()
#     # print(account.balance)
#     account + 10
#     # account - 20
#     # print(account._transactions)
#     # print(account.balance)

#     with account as acc:
#         acc - 9

#     print(account._transactions)
#     print(account.balance)

# if __name__ == "__main__":
#     main()

