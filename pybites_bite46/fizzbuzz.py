from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    ret = []

    if num % 3 == 0:
        ret.append("Fizz")

    if num % 5 == 0:
        ret.append("Buzz")

    if num % 3 != 0 and num % 5 != 0:
        ret.append(num)

    return " ".join(map(str, ret))


def main():
    for i in range(1, 17):
        print(fizzbuzz(i))


if __name__ == "__main__":
    main()
