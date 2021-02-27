from typing import Generator
import decimal

VALUES = "[0.1, 0.2, 0.3, 0.005, 0.005, 2.67]"



def calc_sums(values: str = VALUES) -> Generator[str, None, None]:
    """
    Process the above JSON-encoded string of values and calculate the sum of each adjacent pair.

    The output should be a generator that produces a string that recites the calculation for each pair, for example:

        'The sum of 0.1 and 0.2, rounded to two decimal places, is 0.3.'
    """
    context = decimal.getcontext()
    context.rounding = decimal.ROUND_HALF_UP

    values_list = [val.strip('[').strip(']') for val in values.split(', ')]

    for i in range(0, len(values_list) - 1):
        yield 'The sum of {} and {}, rounded to two decimal places, is {}.' \
            .format(values_list[i], values_list[i + 1],
                    decimal.Decimal(str(decimal.Decimal(values_list[i])+decimal.Decimal(values_list[i+1]))).quantize(decimal.Decimal("1.00")))