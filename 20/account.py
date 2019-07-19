class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        if sum(self._transactions) < 0:
            raise Exception("text").with_traceback(None)
            return 0

        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        return True



# def main():
#     """
#         The purpose of the context manager is to roll back any transaction that will make the balance go below 0 (debt != cool). The rest of the class is already defined so you can focus on the context manager part.
#     """
#     # print("write a context manager")

#     account = Account()
#     print(account.balance)
#     # account + 10
#     # account - 5
#     # print(account._transactions)
#     # print(account.balance)

#     with account as acc:
#         acc - 5

#     print(account._transactions)
#     print(account.balance)

# if __name__ == "__main__":
#     main()

