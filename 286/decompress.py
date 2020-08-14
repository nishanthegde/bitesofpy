from typing import Dict


def decompress(string: str, table: Dict[str, str]) -> str:
    sp_chars = '~@#$%^&*/?;:()+='
    ret_in = ''
    if string:
        for c in string:
            if c in sp_chars:
                c = table.get(c, '')
                # ret_in = ''
                # for c_in in c:
                #     if c_in in sp_chars:
                #         ret_in += decompress(c, table)
                # c = ret_in
            ret_in += c

    ret = ret_in
    if any(i in sp_chars for i in ret_in):
        ret = decompress(ret_in, table)

    return ret
