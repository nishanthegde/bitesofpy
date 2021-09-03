import re

def snake_case_keys(data):
    data2 = data.copy()

    if not data or len(data)==0:
        return {}

    pattern = re.compile(r'(?=[A-Z-])')
    pattern2 = re.compile(r'(\D*)(\d+)')

    for k in data.keys():
        new_k = pattern.sub('_', k).lower().strip('_').replace('-','')
        if new_k != k:
            new_k2 = ''
            for m in re.finditer(pattern2, new_k):
                new_k2 += m.group(1)+'_'+m.group(2)
            if new_k2:
                data2[new_k2] = data2[k]
            else:
                data2[new_k] = data2[k]
            del data2[k]

    return data2


def main():
    print('thank you for looking after mama!')
    # data = {"star": "wars"}
    # data = {"DarthVader": "James Earl Jones"}
    # data = {"executeOrder66": "yes sir!"}
    data = {"firstName": "Han", "lastName": "Solo"}
    print(snake_case_keys(data))


if __name__ == '__main__':
    main()
