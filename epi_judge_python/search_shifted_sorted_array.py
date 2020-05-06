from typing import List

from test_framework import generic_test


<<<<<<< HEAD
def search_smallest(A):

    left, right = 0, len(A) - 1
    while left < right:
        mid = left + (right - left) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left
=======
def search_smallest(A: List[int]) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_shifted_sorted_array.py',
                                       'search_shifted_sorted_array.tsv',
                                       search_smallest))
