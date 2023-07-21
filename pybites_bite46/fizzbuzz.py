from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    ret = []

    if num % 3 == 0:
        ret.append("Fizz")

    if num % 5 == 0:
        ret.append("Buzz")

    if ret:
        return " ".join(ret)
    else:
        return num


# def main():
#     for i in range(1, 17):
#         print(fizzbuzz(i))


# if __name__ == "__main__":
#     main()
