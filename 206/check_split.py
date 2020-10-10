from decimal import *


def check_split(item_total, tax_rate, tip, people):
    """Calculate check value and evenly split.

       :param item_total: str (e.g. '$8.68')
       :param tax_rate: str (e.g. '4.75%)
       :param tip: str (e.g. '10%')
       :param people: int (e.g. 3)

       :return: tuple of (grand_total: str, splits: list)
                e.g. ('$10.00', [3.34, 3.33, 3.33])
    """

    TWOPLACES = Decimal(10) ** -2

    item_total_float = Decimal(item_total.strip('$'))
    tax_rate_float = Decimal(tax_rate.strip('%'))
    tip_float = Decimal(tip.strip('%'))

    tax = (item_total_float * (tax_rate_float / 100)).quantize(TWOPLACES)
    total = (item_total_float + tax).quantize(TWOPLACES)
    tip = (total * (tip_float / 100)).quantize(TWOPLACES)

    grand_total = (total + tip).quantize(TWOPLACES)

    splits = list()

    for i in range(0, people):
            splits.append((grand_total / people).quantize(TWOPLACES))

    remaining = grand_total - sum(splits)
    splits[-1] += remaining

    return f'${str(grand_total)}', splits

