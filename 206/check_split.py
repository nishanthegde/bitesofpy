import re


class newfloat(float):

    def __str__(self):
        return "%.2f" % self

    # def __add__(self, other):
    #     return self.__class__(self + other)


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """

    splits = list()

    item_total_float = newfloat(re.sub(r'(\$)([\d.]+)', r'\2', item_total))
    tax_rate_float = newfloat(re.sub(r'([\d.]+)(%)', r'\1', tax_rate)) / 100
    tip_float = newfloat(re.sub(r'([\d.]+)(%)', r'\1', tip)) / 100

    # total_w_tax = round(item_total_float + (item_total_float * tax_rate_float), 2)
    total_w_tax = newfloat(round(item_total_float + (item_total_float * tax_rate_float), 2))
    # grand_total_pre = total_w_tax + (total_w_tax * tip_float)
    grand_total = newfloat(round(total_w_tax + (total_w_tax * tip_float), 2))

    for i in range(0, people):
        splits.append(newfloat(grand_total / people))

    # if len('${}'.format(grand_total).split('.')[-1]) < 2:
    #     ret = '${}0'.format(grand_total)
    #     # print('here')
    #     # splits[-1] = splits[-1] + .1
    # else:
    #     ret = '${}'.format(grand_total)

    ret = '${}'.format(grand_total)

    # if sum(splits) > grand_total:
    #     # print(sum(splits) - grand_total)
    #     splits[-1] = splits[-1] - (sum(splits) - grand_total)

    # if sum(splits) < grand_total:
    #     # print(grand_total - sum(splits))
    #     splits[-1] = splits[-1] + (grand_total - sum(splits))

    # print(type(sum(splits)))

    # for s in splits:
    #     print(s)
    s = sum(splits)
    ret1 = [newfloat(s)]
    return (ret, ret1)


def main():

    print('thank you for the waves and for all that you have given me...')

    # grand_total, splits = check_split('$191.57', '6.75% ', '15%', 6)
    # grand_total, splits = check_split('$100.03', '0%', '0%', 4)
    # grand_total, splits = check_split('$141.86', '2%', '18%', 9)
    # grand_total, splits = check_split('$191.57', '6.75% ', '15%', 6)
    grand_total, splits = check_split('$8.68', '4.75%', '10%', 3)
    print(grand_total, f'${sum(splits)}')

    grand_total, splits = check_split('$8.44', '6.75%', '11%', 3)
    print(grand_total, f'${sum(splits)}')

    grand_total, splits = check_split('$0.00', '0%', '0%', 1)
    print(grand_total, f'${sum(splits)}')


if __name__ == '__main__':
    main()
