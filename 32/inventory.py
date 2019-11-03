import copy

items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items: dict) -> dict:
    return copy.deepcopy(items)

#time to dial up

# def main():
#     print('thank you ...')
#     items_copy = duplicate_items(items)
#     assert items == items_copy

#     items_copy[0]['name'] = 'macbook'
#     items_copy[1]['id'] = 4
#     items_copy[2]['value'] = 30

#     assert items[0]['name'] == 'laptop'
#     assert items[1]['id'] == 2
#     assert items[2]['value'] == 20

#     # print(items)


# if __name__ == '__main__':
#     main()
