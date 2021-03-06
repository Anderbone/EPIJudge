import collections
from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
# def is_valid_sudoku(partial_assignment):
#
#     def check(nine):
#         single = []
#         for i in nine:
#             if i != 0 and i in single:
#                 return False
#             single.append(i)
#         return True
#
#     # def cut(self, partial_assignment, (starti, endi), (startj, endj)):
#     def cut(partial_assignment, starti, endi, startj, endj):
#         small = []
#         for i in partial_assignment[starti:endi]:
#             small += i[startj:endj]
#         return small
#     for i in partial_assignment:
#         if check(i) is False:
#             return False
#     Trans = [[row[i] for row in partial_assignment] for i in range(len(partial_assignment[0]))]
#     for i in Trans:
#         if check(i) is False:
#             return False
#
#     for i in [[0, 3], [3, 6], [6, 9]]:
#         for j in [[0, 3], [3, 6], [6, 9]]:
#             small = cut(partial_assignment, i[0], i[1], j[0], j[1])
#             if check(small) is False:
#                 return False
#     return True
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:

    # TODO - you fill in here.
    def check_9num(list_9num):
        counter = collections.Counter(list_9num)
        for num in counter:
            if num != 0 and counter[num] > 1:
                return False
        return True

    for row in partial_assignment:
        if check_9num(row) is False:
            return False

    for i in range(9):
        col = list()
        for j in range(9):
            col.append(partial_assignment[j][i])
        if check_9num(col) is False:
            return False

    def cut(partial_assignment, starti, endi, startj, endj):
        small = []
        for i in partial_assignment[starti:endi]:
            small += i[startj:endj]
        return small

    for i in [[0,3],[3,6],[6,9]]:
        for j in [[0,3],[3,6],[6,9]]:
            small = cut(partial_assignment, i[0], i[1], j[0], j[1])
            if check_9num(small) is False:
                return False
    return True




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
