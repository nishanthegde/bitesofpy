import numbers

class RecordScore():
    """Class to track a game's maximum score"""

    def __init__(self):
        self.max_score = None

    def __call__(self, score):

        if not(isinstance(score, numbers.Number)):
            raise ValueError("score must be numeric")

        if isinstance(score, bool):
            raise ValueError("score must be numeric")

        if self.max_score == None:
            self.max_score = score
        else:
            if score > self.max_score:
                self.max_score = score

        return self.max_score


# def main():
#     record = RecordScore()
#     record(10)
#     print(record.max_score)
#     record(9)
#     print(record.max_score)
#     record(11)  # initial max
#     print(record.max_score)
#     record(5)
#     print(record.max_score)
#     print(record(9) == 11)
#     record(10)
#     record(2)
#     print(record(4) == 11)
#     record(1)

# if __name__ == "__main__":
#     main()
