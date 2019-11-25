from pathlib import PosixPath
import difflib
from difflib import get_close_matches
import os

local = os.getcwd()
tmp_path = PosixPath(local)

FILES1 = ('bite1 test output').split()
FILES = ('bite.html commands.sh out_grepped pytest_testrun.out '
         'pytest_timings.out test_timings.py timings-template.py '
         'timings.py').split()


def _create_test_files(directory: PosixPath, flag: int=1):

  if flag == 1:
    for fi in FILES1:
      open(directory / fi, 'a').close()
  else:
    for fi in FILES:
      open(directory / fi, 'a').close()


def get_matching_files(directory: PosixPath, filter_str: str) -> list:
  """Get all file names in "directory" and (case insensitive) match the ones
     that exactly match "filter_str"

     In case there is no exact match, return closely matching files.
     If there are no closely matching files either, return an empty list.
     (Return file names, not full paths).

     For example:

     d = Path('.')
     files in dir: bite1 test output

     get_matching_files(d, 'bite1') => ['bite1']
     get_matching_files(d, 'Bite') => ['bite1']
     get_matching_files(d, 'pybites') => ['bite1']
     get_matching_files(d, 'test') => ['test']
     get_matching_files(d, 'test2') => ['test']
     get_matching_files(d, 'output') => ['output']
     get_matching_files(d, 'o$tput') => ['output']
     get_matching_files(d, 'nonsense') => []
  """
  # _create_test_files(directory, 2)

  files = [f for f in os.listdir(directory) if os.path.isfile(f)]

  return get_close_matches(filter_str, files)


# def main():
#   print('thank you for everything...')
#   # print(type(tmp_path))
#   actual = get_matching_files(tmp_path, '_timing')
#   print(actual)


# if __name__ == '__main__':
#   main()
