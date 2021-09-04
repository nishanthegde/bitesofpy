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
    for key, value in data.items():
        if isinstance(value, dict):
            data[key] = snake_case_keys(value)
        elif isinstance(value, list):
            data[key] = []
            for item in value:
                if isinstance(item, dict):
                    data[key].append(snake_case_keys(item))
                elif isinstance(item, list):
                    data[key].append(
                        [snake_case_keys(item_inner) if isinstance(item_inner, dict) else item_inner for item_inner in
                         item])
                else:
                    data[key].append(item)
    return get_snake(data)
