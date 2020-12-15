from typing import List

from test_framework import generic_test



def can_reach_end(A):
    if A == [0]:
        return True
    step_need = 1
    for i in reversed(range(len(A)-1)):
        if A[i] < step_need:
            step_need += 1
        else:
            step_need = 1
    if A[0] >= step_need:
        return True
    return False

# def can_reach_end(A: List[int]) -> bool:
#     k = 0
#     for i in range(len(A)-2, -1, -1):
#         if A[i] > k:
#             k = 0
#         else:
#             k += 1
#
#     if k == 0:
#         return True
#     return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
