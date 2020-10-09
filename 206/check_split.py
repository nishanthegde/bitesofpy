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



    total = (item_total_float * (1 + (tax_rate_float / 100))).quantize(TWOPLACES)
    grand_total = (total * (1 + (tip_float / 100))).quantize(TWOPLACES)

    # total1 = item_total_float * (1 + (tax_rate_float / 100))
    # grand_total1 = total1 * (1 + (tip_float / 100))

    s = [(grand_total / people) for i in range(0, people)]

    return f'${str(grand_total)}', s, sum(s)


def main():
    print("thank you for looking after my family...")
    print(check_split('$8.68', '4.75%', '10%', 3))
    print(check_split('$8.44', '6.75%', '11%', 3))
    print(check_split('$9.99', '3.25%', '10%', 2))
    print(check_split('$186.70', '6.75%', '18%', 6))
    print(check_split('$191.57', '6.75%', '15%', 6))
    print(check_split('$0.00', '0%', '0%', 1))
    print(check_split('$100.03', '0%', '0%', 4))
    print(check_split('$141.86', '2%', '18%', 9))
    print(check_split('$16.99', '10%', '20%', 1))
    print(check_split('$16.99', '10%', '20%', 2))
    print(check_split('$16.99', '10%', '20%', 3))
    print(check_split('$16.99', '10%', '20%', 4))


if __name__ == "__main__":
    main()
