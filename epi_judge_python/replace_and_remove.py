import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    st = ''.join(s)
    st = st.replace('a','dd')
    st= st.replace('b','')
    s[:] = st
    return len(st)
# def replace_and_remove(size: int, s: List[str]) -> int:
#     res = []
#     for c in s:
#         if c == 'a':
#             res.append('d')
#             res.append('d')
#         else:
#             res.append(c)
#     # print(res)
#     s[:] = list(filter(lambda x: x != '' and x != 'b', res))
#     # s[:] = res
#     return len(s)


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
