from collections import OrderedDict

scores = [10, 50, 100, 175, 250, 400, 600, 800, 1000]
belts = 'white yellow orange green blue brown black paneled red'.split()
HONORS = OrderedDict(zip(scores, belts))
MIN_SCORE, MAX_SCORE = min(scores), max(scores)


def get_belt(user_score):

    high = [k for k in HONORS.keys() if k<=user_score]

    if high:
        return HONORS[max(high)]
    return None

# def main():
#     """
#         Complete the get_belt function below which receives a user_score which you can assume to be an int.

#         The function should return the corresponding belt name from the HONORS dict. For example with 162 points you would have the orange belt (not yet reached green), 401 = brown, 999 is paneled, etc.

#         Note that the scores are inclusive so if you have 10 points you have earned the white belt, ≥ 50 = yellow belt, etc. Also make sure you take the min and max boundaries into account (< 10 is no belt and > 1000 is the highest belt).
#     """
#     # print(HONORS[10])
#     # print(type(HONORS))

#     s = get_belt(1200)
#     print(s)


# if __name__ == "__main__":
#     main()
