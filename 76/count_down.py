from functools import singledispatch

@singledispatch
def count_down(data_type):
    raise ValueError('Unsupported type')

@count_down.register(float)
@count_down.register(int)
def _(data):
    if isinstance(data, bool):
        raise ValueError('Unsupported type')

    data = str(data)
    print('{}'.format(data))

    for i in range(1, len(data), 1):
        print('{}'.format(data[:-i]))

@count_down.register(str)
def _(data):
    if data:
        print('{}'.format(data))

        for i in range(1, len(data), 1):
            print('{}'.format(data[:-i]))

@count_down.register(list)
@count_down.register(set)
@count_down.register(tuple)
@count_down.register(range)
def _(data):
    data = [str(e) for e in data]
    print('{}'.format(''.join(data)))

    for i in range(1, len(data), 1):
        print('{}'.format(''.join(data[:-i])))

@count_down.register(dict)
def _(data):
    data = [str(k) for k in data.keys()]
    print('{}'.format(''.join(data)))

    for i in range(1, len(data), 1):
        print('{}'.format(''.join(data[:-i])))


def main():

    # count_down('nishant')
    # count_down(9)
    # count_down(['a','b'])
    # count_down('1234')
    # count_down([1, 2, 3, 4])
    # count_down(['1', '2', '3', '4'])
    # count_down((1, 2, 3, 4))
    # count_down(('1', '2', '3', '4'))
    # count_down({1, 2, 3, 4})
    # count_down({1: 'one', 2: 'two', 3:'three', 4:'four'} )
    # count_down({'1': 'one', '2': 'two', '3':'three', '4':'four'})
    # count_down(12.34)
    count_down(range(1, 5))

if __name__ == "__main__":
    main()
