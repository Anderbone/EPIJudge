from typing import List

from test_framework import generic_test


<<<<<<< HEAD
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

=======
def search_first_of_k(A: List[int], k: int) -> int:
    # TODO - you fill in here.
    return 0
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_first_key.py',
                                       'search_first_key.tsv',
                                       search_first_of_k))
