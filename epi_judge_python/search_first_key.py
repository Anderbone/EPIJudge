import bisect
from typing import List

from test_framework import generic_test


def search_first_of_k(A, k):

    left, right = 0, len(A)-1
    flag = 0
    while left<=right:
        mid = left + (right-left)//2
        if A[mid] > k:
            right = mid - 1
        elif A[mid] < k:
            left = mid + 1
        else:
            flag = 1
            right = mid - 1

    if flag:
        return left
    return -1
#
# def search_first_of_k(A: List[int], k: int) -> int:
#     res = bisect.bisect_left(A, k)
#     if res < 0 or res >= len(A) or A[res] != k:
#         return -1
#     return res



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
