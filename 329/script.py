import re


def get_keys(data, level=1):
    keys = []
    for key, value in data.items():
        keys.append((key, level))
        if isinstance(value, dict):
            level += 1
            keys.extend(get_keys(value, level))
    return keys


def get_snake(data):
    data2 = data.copy()

    if not data or len(data) == 0:
        return {}

    pattern = re.compile(r'(?=[A-Z-])')
    pattern2 = re.compile(r'(\D*)(\d+)')

    for k in data.keys():
        new_k = pattern.sub('_', k).lower().strip('_').replace('-', '')
        if new_k != k:
            new_k2 = ''
            for m in re.finditer(pattern2, new_k):
                new_k2 += m.group(1) + '_' + m.group(2)
            if new_k2:
                data2[new_k2] = data2[k]
            else:
                data2[new_k] = data2[k]
            del data2[k]

    return data2


def snake_case_keys(data):
    # print(data)
    for key, value in data.items():
        if isinstance(value, dict):
            # print(value)
            data[key] = snake_case_keys(value)
            # level += 1
            # keys.extend(get_keys(value, level))
        # else:
    return get_snake(data)

    # data2 = data.copy()
    #
    # if not data or len(data) == 0:
    #     return {}
    #
    # pattern = re.compile(r'(?=[A-Z-])')
    # pattern2 = re.compile(r'(\D*)(\d+)')
    #
    # print(get_keys(data))
    #
    # for k in get_keys(data):
    #     new_k = pattern.sub('_', k).lower().strip('_').replace('-', '')
    #     if new_k != k:
    #         new_k2 = ''
    #         for m in re.finditer(pattern2, new_k):
    #             new_k2 += m.group(1) + '_' + m.group(2)
    #         if new_k2:
    #             data2[new_k2] = data2[k]
    #         else:
    #             data2[new_k] = data2[k]
    #         del data2[k]
    #
    # return data2


def main():
    print('thank you for looking after mama!')
    # data = {"star": "wars"}
    # data = {"DarthVader": "James Earl Jones"}
    # data = {"executeOrder66": "yes sir!"}
    data = {"firstName": "Han", "lastName": "Solo"}
    # data = {
    #     "darthVader": {
    #         "firstName": "Anakin",
    #         "lastName": "Skywalker",
    #         "appearance": {
    #             "helmetColor": "black",
    #             "armorColor": "black",
    #             "capeColor": "black",
    #         },
    #     }
    # }
    print(snake_case_keys(data))


if __name__ == '__main__':
    main()
