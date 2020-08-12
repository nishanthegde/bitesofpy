from typing import List


def jagged_list(lst_of_lst: List[List[int]], fillvalue: int = 0) -> List[List[int]]:

    ret = list()

    if lst_of_lst:
        max_len = max([len(li) for li in lst_of_lst])

        for li in lst_of_lst:
            if len(li) < max_len:
                li = li + [fillvalue] * (max_len - len(li))
            ret.append(li)

    return ret
