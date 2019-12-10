import re


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """

    splits = []

    item_total_float = float(re.sub(r'(\$)([\d.]+)', r'\2', item_total))
    tax_rate_float = float(re.sub(r'([\d.]+)(%)', r'\1', tax_rate)) / 100
    tip_float = float(re.sub(r'([\d.]+)(%)', r'\1', tip)) / 100

    total_w_tax = round(item_total_float + (item_total_float * tax_rate_float), 2)
    total = total_w_tax + (total_w_tax * tip_float)

    for i in range(0, people):
        splits.append(round(round(total, 2) / people, 3))

    return (round(total, 2), splits)


def main():

    print('here ...')

    # grand_total, splits = check_split('$191.57', '6.75%', '15%', 6)
    grand_total, splits = check_split('$141.86', '2%', '18%', 9)
    # grand_total, splits = check_split('$16.99', '10%', '20%', 4)
    print(grand_total)
    print(splits)
    print(f'${sum(splits)}')
    # print(check_split('$141.86', '2%', '18%', 9))
    # print(check_split('$16.99', '10%', '20%', 1))
    # print(check_split('$16.99', '10%', '20%', 2))
    # print(check_split('$16.99', '10%', '20%', 3))
    # print(check_split('$16.99', '10%', '20%', 4))

    # print(divmod(235.18, 6))


if __name__ == '__main__':
    main()
