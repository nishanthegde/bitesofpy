from typing import List, Union


def join_lists(lst_of_lst: List[List[str]], sep: str) -> Union[List[str], None]:

    if lst_of_lst:
        ret  = lst_of_lst

        if all(isinstance(el, list) for el in lst_of_lst) and len(lst_of_lst) > 1:
            ret = sum([[ele, sep] for ele in lst_of_lst], [])[:-1]

        return [item for ele in ret for item in ele]