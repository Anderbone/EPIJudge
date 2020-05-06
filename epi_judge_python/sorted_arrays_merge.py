from typing import List

from test_framework import generic_test
import heapq

def merge_sorted_arrays(sorted_arrays: List[List[int]]) -> List[int]:
    # TODO - you fill in here.
    sorted_arrays_iters = [iter(x) for x in sorted_arrays]
    min_heap = []
    for i in sorted_arrays:
        min_heap.append(i[0])
    heapq.heapify(min_heap)

    res = []
    while min_heap:
        small = heapq.heappop(min_heap)
        res.append(small)



    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_arrays_merge.py',
                                       'sorted_arrays_merge.tsv',
                                       merge_sorted_arrays))
