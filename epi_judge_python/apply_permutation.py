from typing import List

from test_framework import generic_test


def apply_permutation(perm: List[int], A: List[int]) -> None:
    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]
    return A
# def apply_permutation(perm: List[int], A: List[int]) -> None:
#     index_ele = list(zip(range(len(A)), A))
#     for i in range(len(perm)):
#         A[perm[i]] = index_ele[i][1]
#     return A

# def apply_permutation(perm: List[int], A: List[int]) -> None:
    # # TODO - you fill in here.
    # B = [0] * len(A)
    # for i in zip(A, perm):
    #     B[i[1]] = i[0]
    # return B


def apply_permutation_wrapper(perm, A):
    # print(A)

    # print(A)
    return apply_permutation(perm, A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('apply_permutation.py',
                                       'apply_permutation.tsv',
                                       apply_permutation_wrapper))
