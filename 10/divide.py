def positive_divide(numerator, denominator):
    try:
        ret = numerator / denominator
        if ret > 0:
            return ret
        else:
            raise ValueError

    except ZeroDivisionError:
        print("Unexpected ZeroDivisionError!")
        return 0


# def main():
#     print(positive_divide(1, 2))
#     print(positive_divide(1, 0))
#     print(positive_divide(-1, -2))
#     print(positive_divide(1.5, 2))
#     # print(positive_divide(1, 's'))
#     # positive_divide([], 2)
#     # print(positive_divide(1, -2))
#     positive_divide(-1, 2)


# if __name__ == '__main__':
#     main()
