from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:

    for i in range(len(A)):
<<<<<<< HEAD
        # Check if the element at index i has not been moved by checking if
        # perm[i] is nonnegative.
        next = i
        while perm[next] >= 0:
            A[i], A[perm[next]] = A[perm[next]], A[i]
            temp = perm[next]
            # Subtracts len(perm) from an entry in perm to make it negative,
            # which indicates the corresponding move has been performed.
            # perm[next] -= len(perm)
            perm[next] = -1
            next = temp
    # Restore perm.
    # perm[:] = [a + len(perm) for a in perm]
=======
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
>>>>>>> upstream/master


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
