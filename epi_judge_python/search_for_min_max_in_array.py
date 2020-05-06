import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


<<<<<<< HEAD
def find_min_max(A):
    mi, ma = A[0], A[0]

    for i in range(2, len(A)-1, 2):
        if A[i] > A[i+1]:
            A[i], A[i+1] = A[i+1], A[i]
        # if A[i] <= A[i+1]:
        mi = min(mi, A[i])
        ma = max(ma, A[i+1])

    if len(A) % 2:
        # when 1,2,3,4,5.  need to check 5 at last
        mi = min(mi, A[-1])
        ma = max(ma, A[-1])
    return MinMax(mi, ma)
=======
def find_min_max(A: List[int]) -> MinMax:
    # TODO - you fill in here.
    return MinMax(0, 0)
>>>>>>> upstream/master


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
