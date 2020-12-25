from typing import List

from test_framework import generic_test


# def generate_pascal_triangle(n):
#     numRows = n
#     if numRows == 0:
#         return []
#     n1 = [1]
#     n2 = [1, 1]
#     if numRows == 1:
#         return [n1]
#     if numRows == 2:
#         return [n1, n2]
#
# def generate_pascal_triangle(n: int) -> List[List[int]]:
#     # TODO - you fill in here.
#     last = generate_pascal_triangle(n - 1)
#     lastline = last[-1]
#     newline = [1]
#     for i in range(len(lastline) - 1):
#         newline.append(lastline[i] + lastline[i + 1])
#     newline.append(1)
#     last.append(newline)
#     return last
def generate_pascal_triangle(n: int) -> List[List[int]]:
    if n == 0:
        return []
    if n == 1:
        return [[1]]

    def getNextRow(lastRow):
        nextRow = [1]
        for i in range(len(lastRow) - 1):
            nextRow.append(lastRow[i] + lastRow[i+1])
        nextRow.append(1)
        return nextRow

    last_tri = generate_pascal_triangle(n - 1)
    last_tri.append(getNextRow(last_tri[-1]))
    return last_tri

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pascal_triangle.py',
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
