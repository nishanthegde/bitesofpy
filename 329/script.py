import re

def snake_case_keys(data):
    data2 = data.copy()

    if not data or len(data)==0:
        return {}

    for k in data.keys():
        pattern = re.compile(r'(?=[A-Z-0-9])')
        new_k = pattern.sub('_', k).lower().strip('_').replace('-','')
        if new_k != k:
            data2[new_k] = data2[k]
            del data2[k]

    return data2


def main():
    print('thank you for looking after mama!')
    # data = {"star": "wars"}
    # data = {"DarthVader": "James Earl Jones"}
    data = {"darth-vader": "James Earl Jones"}
    print(snake_case_keys(data))


if __name__ == '__main__':
    main()
