from typing import List

from test_framework import generic_test


def rotate_matrix(square_matrix: List[List[int]]) -> None:
    width = len(square_matrix)
    new_square = []
    for i in range(width):
        last_row = square_matrix.pop(-1)
        for j, e in enumerate(last_row):
            if len(new_square) < width:
                new_square.append([e])
            else:
                new_square[j].append(e)
    square_matrix[:] = new_square
    # return new_square


# def rotate_matrix(square_matrix: List[List[int]]) -> None:
#     # TODO - you fill in here.
#     # return
#     if not square_matrix:
#         return []
#     trans = [[row[i] for row in square_matrix] for i in range(len(square_matrix[0]))]
#
#     for i in trans:
#         for j in range(len(trans[0]) // 2):
#             i[j], i[len(trans[0]) - 1 - j] = i[len(trans[0]) - 1 - j], i[j]
#     square_matrix[:] = trans


def rotate_matrix_wrapper(square_matrix):
    rotate_matrix(square_matrix)
    return square_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_rotation.py',
                                       'matrix_rotation.tsv',
                                       rotate_matrix_wrapper))
