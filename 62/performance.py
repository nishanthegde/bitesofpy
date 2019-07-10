from functools import wraps
from time import time
from typing import List, Set
from string import ascii_lowercase

def timing(f):
    """A simple timer decorator to print the elapsed time of
       the execution of the function it wraps.
       Returns (timing, result) tuple"""
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        duration = end - start
        print(f'Elapsed time {f.__name__}: {duration}')
        return duration, result
    return wrapper

@timing
def contains(sequence: List[int], num: int) -> bool:
    for n in sequence:
        if n == num:
            return True
    return False

@timing
def contains_fast(sequence: Set[int], num: int) -> bool:
    if num in sequence:
        return True
    return False

@timing
def ordered_list_max(sequence: List[int]) -> int:
    return max(sequence)

@timing
def ordered_list_max_fast(sequence: List[int]) -> int:
    return sequence[-1]

@timing
def list_concat(sequence: List[str]) -> str:
    bigstr = ''
    for i in sequence:
        bigstr += str(i)
    return bigstr

@timing
def list_concat_fast(sequence: List[str]) -> str:
    return ''.join(sequence)


@timing
def list_inserts(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.insert(0, i)
    return lst

@timing
def list_inserts_fast(n: int) -> List[int]:
    return [i for i in range(n)][::-1]

@timing
def list_creation(n: int) -> List[int]:
    lst = []
    for i in range(n):
        lst.append(i)
    return lst

@timing
def list_creation_fast(n: int) -> List[int]:
    return [i for i in range(n)]

# @timing
# def get_name(name: str):
#     return 'name is {}'.format(name)

# def main():
#     """
#     In this Bite we provide you with 5 functions which you have to try to make faster. Some require different data structures or tactics. Knowing about these techniques goes a long way specially when your data sets grow and performance becomes an issue.

#     Notice that:

#     you need to complete the 5 functions containing _fast
#     the timing decorator can be ignored, the tests use this to time each function
#     we added some type hinting to help you, but some functions might require a different return type (so change it or get rid of the typing)
#     bisect would be a candidate for contains_fast but we think set (or dict) is the best way so this is the only function with a different input argument type for the fast equivalent (type casting was too expensive)
#     The tests ensure that the fast functions A. return the same result, B. are indeed faster
#     """
#     # t, res = get_name('Nishant')
#     # print(t, res)

#     alist = list(range(1000000))
#     aset = set(alist)
#     listofstrings = list(ascii_lowercase) * 1000

#     # print(alist[-10:])
#     # print(len(listofstrings))

#     # t1, res1 = contains(alist, 500)
#     # t2, res2 = contains_fast(aset, 1000)

#     # t1, res1 = ordered_list_max(alist)
#     # t2, res2 = ordered_list_max_fast(alist)

#     # t1, res1 = list_concat(listofstrings)
#     # t2, res2 = list_concat_fast(listofstrings)

#     # t1, res1 = list_inserts(10000)
#     # t2, res2 = list_inserts_fast(10000)

#     t1, res1 = list_creation(10000)
#     t2, res2 = list_creation_fast(10000)

#     print(t1)
#     print(t2)

#     # print(t1, res1)
#     # print(t2, res2)

#     print(res1 == res2)
#     print(t1 > t2)

# if __name__ == "__main__":
#     main()
