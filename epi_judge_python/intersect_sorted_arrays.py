from typing import List

from test_framework import generic_test
import bisect

def intersect_two_sorted_arrays0(A, B):
    def present(A, k):
        index = bisect.bisect_left(A, k)
        return index < len(A) and A[index] == k

    res = []
    for i,e in enumerate(B):
        if present(A, e) and (i == 0 or e != B[i-1]):
           res.append(e)
    return res

def intersect_two_sorted_arrays(A: List[int], B: List[int]) -> List[int]:
    i = j = 0
    ans = []
    while i < len(A) and j < len(B):
        # both jump to the next that not equal to A[i]
        if A[i] == B[j]:
            e = A[i]
            ans.append(e)
            i += 1
            while A[i] == e:
                i += 1
            j += 1
            while A[j] == e:
                j += 1
        elif A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
    return ans

def intersect_two_sorted_arrays(A, B):
    i, j, res = 0, 0, []
    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i-1]:
                res.append(A[i])
            i, j = i+1, j+1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('intersect_sorted_arrays.py',
                                       'intersect_sorted_arrays.tsv',
                                       intersect_two_sorted_arrays))
