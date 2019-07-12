from test_framework import generic_test


def apply_permutation(perm, A):
    # TODO - you fill in here.
    B = [0] * len(A)
    for i in zip(A, perm):
        B[i[1]] = i[0]
    return B


def apply_permutation_wrapper(perm, A):
    # print(A)

    # print(A)
    return apply_permutation(perm, A)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))
