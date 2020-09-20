"""Tax Bracket Calculator

Here is the break-down on how much a US citizen's income was
taxed in 2019

      $0 - $9,700   10%
  $9,701 - $39,475  12%
 $39,476 - $84,200  22%
 $84,201 - $160,725 24%
$160,726 - $204,100 32%
$204,101 - $510,300 35%
$510,301 +          37%

For example someone earning $40,000 would
pay $4,658.50, not $40,000 x 22% = $8,800!

    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50

More detail can be found here:
https://www.nerdwallet.com/blog/taxes/federal-income-tax-brackets/

Sample output from running the code in the if/main clause:

          Summary Report
==================================
 Taxable Income:        40,000.00
     Taxes Owed:         4,658.50
       Tax Rate:           11.65%

         Taxes Breakdown
==================================
    9,700.00 x 0.10 =       970.00
   29,775.00 x 0.12 =     3,573.00
      525.00 x 0.22 =       115.50
----------------------------------
              Total =     4,658.50
"""

from dataclasses import dataclass, field
from typing import List, NamedTuple

Bracket = NamedTuple("Bracket", [("end", int), ("rate", float)])
Taxed = NamedTuple("Taxed", [("amount", float), ("rate", float), ("tax", float)])

BRACKET = [
    Bracket(9_700, 0.1),
    Bracket(39_475, 0.12),
    Bracket(84_200, 0.22),
    Bracket(160_725, 0.24),
    Bracket(204_100, 0.32),
    Bracket(510_300, 0.35),
    Bracket(510_301, 0.37),
]

bracket_2020 = [
    Bracket(9_875, 0.1),
    Bracket(40_125, 0.12),
    Bracket(85_525, 0.22),
    Bracket(163_300, 0.24),
    Bracket(207_350, 0.32),
    Bracket(518_400, 0.35),
    Bracket(518_401, 0.37),
]


class Taxes:
    """Taxes class

    Given a taxable income and optional tax bracket, it will
    calculate how much taxes are owed to Uncle Sam.

    """

    def __init__(self, income: int, bracket: List[Bracket] = BRACKET, tax_amounts: List[Taxed] = []):
        self.income = income
        self.bracket = bracket
        self.tax_amounts = tax_amounts
        self.total

    def __str__(self) -> str:
        """Summary Report

        Returns:
            str -- Summary report

            Example:

                      Summary Report          
            ==================================
             Taxable Income:        40,000.00
                 Taxes Owed:         4,658.50
                   Tax Rate:           11.65%
        """
        taxable_income_str = "{0:,.2f}".format(self.income)
        taxes_owed_str = "{0:,.2f}".format(self.total)

        output = "           Summary Report\n"
        output += "==================================\n"
        output += " Taxable Income:{}{}\n".format(" " * (17 - len(taxable_income_str)), taxable_income_str)
        output += "     Taxes Owed:{}{}\n".format(" " * (17 - len(taxes_owed_str)), taxes_owed_str)
        output += "       Tax Rate:{}{}%".format(" " * (16 - len(str(self.tax_rate))), self.tax_rate)

        return output

    def report(self):
        """Prints taxes breakdown report"""

        print(str(self))
        total_str = "{0:,.2f}".format(self.total)

        print()
        report = "           Taxes Breakdown\n"
        report += "==================================\n"
        for i, t in enumerate(self.tax_amounts):
            t_amount_str = "{0:,.2f}".format(t.amount)
            t_rate_str = "{0:,.2f}".format(t.rate)
            t_tax_str = "{0:,.2f}".format(t.tax)
            report += "{}{} X {} ={}{}\n".format(" " * (12 - len(t_amount_str)), t_amount_str, t_rate_str,
                                               " " * (13 - len(t_tax_str)), t_tax_str)

        report += "----------------------------------\n"
        report += "              Total ={}{}".format(" " * (13 - len(total_str)), total_str)
        print(report)

    @property
    def taxes(self) -> float:
        """Calculates the taxes owed

        As it's calculating the taxes, it is also populating the tax_amounts list
        which stores the Taxed named tuples.

        Returns:
            float -- The amount of taxes owed
        """
        return self.total

    @property
    def total(self) -> float:
        """Calculates total taxes owed

        Returns:
            float -- Total taxes owed
        """

        remained_to_be_taxed = self.income
        # taxed = list()
        self.tax_amounts = []
        start_tax_range = 0
        end_tax_range = self.bracket

        for i, b in enumerate(self.bracket):

            amount_to_tax = b.end - start_tax_range
            t = Taxed(min(amount_to_tax, remained_to_be_taxed), b.rate,
                      min(amount_to_tax, remained_to_be_taxed) * b.rate)
            self.tax_amounts.append(t)
            # print(i, start_t      ax_range, b.end, amount_to_tax, b.rate)

            remained_to_be_taxed -= amount_to_tax
            # print(remained_to_be_taxed)

            if b.end > self.income:
                break

            start_tax_range = b.end

        # print(taxed)
        return sum([t.tax for t in self.tax_amounts])

    @property
    def tax_rate(self) -> float:
        """Calculates the actual tax rate

        Returns:
            float -- Tax rate
        """
        return round((self.total / self.income) * 100, 2)


# def main():
#     # print("thank you for looking after my mama...")
#     salary = 1_000_000
#     t = Taxes(salary,bracket_2020)
#     t.report()
#
#
# if __name__ == "__main__":
#     # print(len("=================================="))
#     # print(t.bracket)
#     # print(t.total)
#     # print(t.tax_amounts)
#     # t.report()
#     # income = 8_000
#     # t = Taxes(income, bracket_2020)
#     # print(t.total)
#     # print(t.tax_amounts)
#     main()
