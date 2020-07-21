import re


def is_valid_ip(ip: str) -> bool:
    ipreg = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

    return ipreg.search(ip) is not None


def flatten(data: list) -> list:
    for i in data:
        if isinstance(i, (list, tuple)):
            for j in flatten(i):
                yield j
        else:
            yield i


def extract_ipv4(data: list) -> list:
    """
    Given a nested list of data return a list of IPv4 address information that can be extracted
    """
    l1 = list()
    l2 = list()

    if len(list(flatten(data))) <= 3:
        return []

    for i, x in enumerate(list(flatten(data))):
        if x:
            if x.lower() == 'ip':
                l1.append(list(flatten(data))[i + 1])
            if x.lower() == 'mask':
                l2.append(list(flatten(data))[i + 1])

    return [(t[0].replace('\"', ''), t[1].replace('\"', '')) for t in list(zip(l1, l2)) if
            t[0] and t[1] and is_valid_ip(t[0])]


def main():
    print('thank you...')
    # print(extract_ipv4(['ip', ['"172.16.0.0"'], 'mask', ['12'], 'type', ['ip_mask']]))
    # print(extract_ipv4([['TEST', ['ip', ['"1.1.1.0"'], 'mask', [None], 'type', ['ip_mask']], 'id']]))
    # print(extract_ipv4([['TEST', ['parent', [], 'uuid', ['"khk-yyas4h-323223-wewe-343er-3434-www"'], 'display_name',
    #                               ['"services"'], 'IPV4', [[['ip', ['"1.1.1.0"'], 'mask', ['20'], 'type', ['ip_mask']],
    #                                                         ['ip', ['"2.2.2.2"'], 'mask', ['32'], 'type',
    #                                                          ['ip_mask']]]]]]]))
    # print(extract_ipv4([['TEST', ['ip', ['"not.an.ip.address"'], 'mask', ['24'], 'type', ['ip_mask']], 'id']]))
    # print(extract_ipv4(['ip']))


if __name__ == '__main__':
    main()
