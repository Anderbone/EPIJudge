from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.

    # 1,2,9  -> 1,3,0
    # if last is 9, change to 0, add 1 to the next.
    # if first is 9, change to 0, add 1 in the first.
    count0_right = 0
    # for i, v in enumerate(A[::-1]):
    for i, v in enumerate(reversed(A)):
        index = len(A) - 1 - i
        if v != 9:
            v += 1
            res = A[:index] + [v] + [0] * count0_right
            break
        count0_right += 1
    if count0_right == len(A):
        return [1] + [0] * len(A)
        return A
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
