import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
# def delete_duplicates(A: List[int]) -> int:
#     dic = collections.Counter(A)
#     for i,v in enumerate(dic.keys()):
#         A[i] = v
#     return len(dic)

# def delete_duplicates(A: List[int]) -> int:
#     if not A:
#         return 0
#     print(A)
#     last = A[0]
#     count = i = 1
#     end_add0_count = 0
#     while i < len(A):
#         cur = A[i]
#         if cur > last:
#             last = cur
#             i += 1
#             count += 1
#         elif cur == last:
#             if end_add0_count + count >= len(A):
#                 return count
#             end_add0_count += 1
#             j = i
#             while j+1 < len(A):
#                 A[j] = A[j+1]
#                 j += 1
#             # A[-end_add0_count] = 0
#         else:
#             return count
#     return count

def delete_duplicates(A: List[int]) -> int:
    if not A:
        return 0
    write_index = 1
    for i in range(1, len(A)):
        if A[i] > A[write_index-1]:
            A[write_index] = A[i]
            write_index += 1
    return write_index








# def delete_duplicates(A: List[int]) -> int:
#     # TODO - you fill in here.
#     if not A:
#         return None
#     index = 0
#     for i in A:
#         if i != A[index]:
#             index += 1
#             A[index] = i
#
#     return index+1


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_array_remove_dups.py',
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))
