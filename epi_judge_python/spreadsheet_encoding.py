import functools

from test_framework import generic_test


def ss_decode_col_id(col: str) -> int:
    to_num = lambda x: ord(x) - 64
    f = lambda x, y: x * 26 + y
    res = functools.reduce(f, map(to_num, col))
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
