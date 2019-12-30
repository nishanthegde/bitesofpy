import os
from pathlib import Path
from urllib.request import urlretrieve

test = '-------------------------------------------------------------------------------'

S3 = "https://bites-data.s3.us-east-2.amazonaws.com/{}"
FILE_NAME = "mutpy.out"

# local = os.getcwd()
local = "/tmp"
TMP = os.getenv("TMP", local)
# TMP = os.getenv("TMP", "/tmp")

PATH = Path(TMP, FILE_NAME)

if not PATH.exists():
  urlretrieve(S3.format(FILE_NAME), PATH)


EXPECTED_OUTPUT = """
[*] Start mutation process:
   - targets: account
   - tests: /tmp/test_account.py
[*] 9 tests passed:
   - test_account [0.12459 s]
[*] Start mutants generation and execution:
   - [#   1] AOR account:
[0.12042 s] killed by test_account.py::test_balance
   - [#   2] AOR account:
[0.10003 s] killed by test_account.py::test_merge_account
   - [#   3] AOR account:
[0.10011 s] incompetent
   - [#   4] COD account:
[0.11709 s] killed by test_account.py::test_balance
   - [#   5] COI account:
[0.11089 s] killed by test_account.py::test_balance
   - [#   6] CRP account:
[0.09470 s] killed by test_account.py::test_balance
   - [#   7] CRP account:
[0.09643 s] killed by test_account.py::test_repr
   - [#   8] CRP account:
[0.09736 s] killed by test_account.py::test_repr
   - [#   9] CRP account:
[0.09909 s] killed by test_account.py::test_str
   - [#  10] CRP account:
[0.09923 s] killed by test_account.py::test_str
   - [#  11] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('mutpy')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09799 s] survived
   - [#  12] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09931 s] survived
   - [#  13] CRP account:
[0.10067 s] killed by test_account.py::test_merge_account
   - [#  14] CRP account:
[0.10083 s] killed by test_account.py::test_merge_account
   - [#  15] DDL account:
[0.10240 s] killed by test_account.py::test_balance
   - [#  16] ROR account:
[0.09937 s] killed by test_account.py::test_comparison
   - [#  17] ROR account:
[0.09987 s] killed by test_account.py::test_comparison
   - [#  18] ROR account:
--------------------------------------------------------------------------------
  37:     def __eq__(self, other):
  38:         return self.balance == other.balance
  39:
  40:     def __lt__(self, other):
- 41:         return self.balance < other.balance
+ 41:         return self.balance <= other.balance
  42:
  43:     def __add__(self, other):
  44:         owner = '{}&{}'.format(self.owner, other.owner)
  45:         start_amount = self.amount + other.amount
--------------------------------------------------------------------------------
[0.10084 s] survived
[*] Mutation score [7.08526 s]: 82.4%
   - all: 18
   - killed: 14 (77.8%)
   - survived: 3 (16.7%)
   - incompetent: 1 (5.6%)
   - timeout: 0 (0.0%)
[*] Coverage: 240 of 240 AST nodes (100.0%)
"""

EXPECTED_OUTPUT_WITH_GAP = """
[*] Start mutation process:
   - targets: account
   - tests: /tmp/test_account.py
[*] 9 tests passed:
   - test_account [0.12459 s]
[*] Start mutants generation and execution:
   - [#   1] AOR account:
[0.12042 s] killed by test_account.py::test_balance
   - [#   2] AOR account:
[0.10003 s] killed by test_account.py::test_merge_account
   - [#   3] AOR account:
[0.10011 s] incompetent
   - [#   4] COD account:
[0.11709 s] killed by test_account.py::test_balance
   - [#   5] COI account:
[0.11089 s] killed by test_account.py::test_balance
   - [#   6] CRP account:
[0.09470 s] killed by test_account.py::test_balance
   - [#   7] CRP account:
[0.09643 s] killed by test_account.py::test_repr
   - [#   8] CRP account:
[0.09736 s] killed by test_account.py::test_repr
   - [#   9] CRP account:
[0.09909 s] killed by test_account.py::test_str
   - [#  12] CRP account:
--------------------------------------------------------------------------------
  20:             self.amount)
  21:
  22:     def add_transaction(self, amount):
  23:         if not (isinstance(amount, int)):
- 24:             raise ValueError('please use int for amount')
+ 24:             raise ValueError('')
  25:         self._transactions.append(amount)
  26:
  27:     @property
  28:     def balance(self):
--------------------------------------------------------------------------------
[0.09931 s] survived
   - [#  13] CRP account:
[0.10067 s] killed by test_account.py::test_merge_account
   - [#  14] CRP account:
[0.10083 s] killed by test_account.py::test_merge_account
   - [#  15] DDL account:
[0.10240 s] killed by test_account.py::test_balance
   - [#  16] ROR account:
[0.09937 s] killed by test_account.py::test_comparison
   - [#  17] ROR account:
[0.09987 s] killed by test_account.py::test_comparison
   - [#  18] ROR account:
--------------------------------------------------------------------------------
  37:     def __eq__(self, other):
  38:         return self.balance == other.balance
  39:
  40:     def __lt__(self, other):
- 41:         return self.balance < other.balance
+ 41:         return self.balance <= other.balance
  42:
  43:     def __add__(self, other):
  44:         owner = '{}&{}'.format(self.owner, other.owner)
  45:         start_amount = self.amount + other.amount
--------------------------------------------------------------------------------
[0.10084 s] survived
[*] Mutation score [7.08526 s]: 82.4%
   - all: 18
   - killed: 14 (77.8%)
   - survived: 3 (16.7%)
   - incompetent: 1 (5.6%)
   - timeout: 0 (0.0%)
[*] Coverage: 240 of 240 AST nodes (100.0%)
"""


def _get_data(path=PATH):
  with open(path) as f:
    return [line.rstrip() for line in f.readlines()]


def filter_killed_mutants(mutpy_output: list = None) -> list:
  """Read in the passed in mutpy output and filter out the code snippets of
     mutation tests that were killed. Surviving mutants should be shown in
     full, as well the surrounding output.

     For example, this is a killed mutant:

       - [#  15] DDL account:
    --------------------------------------------------------------------------------
      23:         if not (isinstance(amount, int)):
      24:             raise ValueError('please use int for amount')
      25:         self._transactions.append(amount)
      26:
    - 27:     @property
    - 28:     def balance(self):
    + 27:     def balance(\
    + 28:         self):
      29:         return self.amount + sum(self._transactions)
      30:
      31:     def __len__(self):
      32:         return len(self._transactions)
    --------------------------------------------------------------------------------
    [0.10240 s] killed by test_account.py::test_balance

    You should reduce this to:

       - [#  15] DDL account:
    [0.10240 s] killed by test_account.py::test_balance

    So you mute all that is in between the two dashed lines.

    You do the same for incompetent mutants, for example:
       - [#   3] AOR account:
    --------------------------------------------------------------------------------
      43:     def __add__(self, other):
      44:         owner = '{}&{}'.format(self.owner, other.owner)
      45:         start_amount = self.amount + other.amount
      46:         acc = Account(owner, start_amount)
    - 47:         for t in list(self) + list(other):
    + 47:         for t in list(self) - list(other):
      48:             acc.add_transaction(t)
      49:         return acc
    --------------------------------------------------------------------------------
    [0.10011 s] incompetent

    ... becomes:
       - [#   3] AOR account:
    [0.10011 s] incompetent

    Return the filtered output as a list of lines.
  """
  if mutpy_output is None:
    mutpy_output = _get_data()

  # return [l for l in mutpy_output if 'killed by' in l or 'incompetent\n' in l]
  # return '\n'.join(mutpy_output)

  remove_indices = list()

  for x in enumerate(mutpy_output):
    # print(x[0], x[1])
    if 'killed by' in x[1] or ('incompetent' in x[1] and ':' not in x[1]):
      remove_indices.append(x[0] - 1)
      i = x[0] - 2  # indice of line above dashes
      # print(x[0], x[1], i)
      # print(mutpy_output[i - 10] == '--------------------------------------------------------------------------------')
      while mutpy_output[i] != '--------------------------------------------------------------------------------':
        remove_indices.append(i)
        i -= 1
      remove_indices.append(i)

  mutpy_output = [i for j, i in enumerate(mutpy_output) if j not in remove_indices]

  return mutpy_output


# def main():
#   print('thank you for everything you have given me...')

#   actual = [line.rstrip() for line in filter_killed_mutants()]
#   print(len(actual))
#   expected = [line.rstrip() for line in EXPECTED_OUTPUT.strip().splitlines()]
#   print(len(expected))

#   print(actual == expected)

#   mutpy_output = _get_data()
#   test10 = mutpy_output.index('   - [#  10] CRP account:')
#   test12 = mutpy_output.index('   - [#  12] CRP account:')
#   output = mutpy_output[:test10] + mutpy_output[test12:]

#   actual = [line.rstrip() for line in filter_killed_mutants(output)]
#   print(len(actual))
#   expected = [line.rstrip() for line in EXPECTED_OUTPUT_WITH_GAP.strip().splitlines()]
#   print(len(expected))

#   print(actual == expected)


# if __name__ == '__main__':
#   main()
