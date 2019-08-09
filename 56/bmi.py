import argparse


def calc_bmi(weight, length):
  """
     Calc BMI give a weight in kg and length in cm, return the BMI
     rounded on 2 decimals"""
  bmi = int(weight) / ((int(length) / 100) ** 2)
  return round(bmi, 2)


def create_parser():
  """
     Create an ArgumentParser adding the right arguments to pass the tests,
     returns a argparse.ArgumentParser object"""
  parser = argparse.ArgumentParser(description='Calculate your BMI.')
  parser.add_argument('-w', '--weight', help='Your weight in kg', required=False)
  parser.add_argument('-l', '--length', help='Your length in cm', required=False)

  return parser


def handle_args(args=None):
  """Call calc_bmi with provided args object.
     If args are not provided get them from create_parser
  """
  if args is None:
    parser = create_parser()
    args = parser.parse_args()

  if args.weight and args.length:
    bmi = calc_bmi(args.weight, args.length)
    print(f'Your BMI is: {bmi}')
  else:
    # could enforce SystemExit in create_parser/add_argument, but argparse
    # docs are not clear how to do it, so raising the exception here manually
    raise SystemExit


if __name__ == '__main__':
  """
    $ python bmi.py -h
    usage: bmi.py [-h] [-w WEIGHT] [-l LENGTH]

    Calculate your BMI.

    optional arguments:
      -h, --help            show this help message and exit
      -w WEIGHT, --weight WEIGHT
                            Your weight in kg
      -l LENGTH, --length LENGTH
                            Your length in cm

    $ python bmi.py -w 80 -l 187
    Your BMI is: 22.88
  """
  handle_args()
