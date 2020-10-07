from typing import List
import re


def split_once(text: str, separators: str = None) -> List[str]:
    return_value = list()

    if not separators:
        ws = ' \t\n\v\f\r'
        for s in ws:
            if len(text.split(s, 1)) > 1:
                if len(return_value) > 1:
                    return_value = return_value[:-1]
                return_value.append(text.split(s, 1)[0])
                return_value.append(text.split(s, 1)[1])
                text = text.split(s, 1)[1]

    if not return_value:
        return_value.append(text)

    return return_value


def main():
    print("please look after my mama...")
    print(split_once(''))
    print(split_once('abc'))
    print(split_once('abc def'))
    print(split_once('abc\tdef'))
    print(split_once('abc def ghi'))
    print(split_once('abc def\tghi'))
    print(split_once('abc def\tghi jkl\tmno'))


if __name__ == "__main__":
    main()
