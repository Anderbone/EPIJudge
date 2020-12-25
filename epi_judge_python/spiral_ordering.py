from typing import List

from test_framework import generic_test


#
# def matrix_in_spiral_order(square_matrix):
#     n = len(square_matrix)
#     if not square_matrix:
#         return []
#     direction_next = {'right':'down', 'down':'left', 'left':'up', 'up':'right'}
#     res = [i for i in square_matrix[0]]
#     i,j = 0,n-1
#     direction = 'down'
#     stride = n-1
#     while stride != 0:
#         for _ in range(2):
#             for _ in range(stride):
#                 if direction is 'down':
#                     i += 1
#                     res.append(square_matrix[i][j])
#                 elif direction is 'up':
#                     i -= 1
#                     res.append(square_matrix[i][j])
#                 elif direction is 'right':
#                     j += 1
#                     res.append(square_matrix[i][j])
#                 elif direction is 'left':
#                     j -= 1
#                     res.append(square_matrix[i][j])
#             direction = direction_next[direction]
#         stride -= 1
#     return res

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    res = []

    def right(square_in):
        if not square_in:
            return None
        nonlocal res
        res.extend(square_in.pop(0))
        return square_in

    def down(square_in):
        if not square_in:
            return None
        nonlocal res
        for row in square_in:
            res.append(row.pop(-1))
        return square_in

    def left(square_in):
        if not square_in:
            return None
        nonlocal res
        res.extend(list(reversed(square_in.pop(-1))))
        return square_in

    def up(square_in):
        if not square_in:
            return None
        nonlocal res
        for row in reversed(square_in):
            res.append(row.pop(0))
        return square_in

    while square_matrix:
        square_matrix = right(square_matrix)
        square_matrix = down(square_matrix)
        square_matrix = left(square_matrix)
        square_matrix = up(square_matrix)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
