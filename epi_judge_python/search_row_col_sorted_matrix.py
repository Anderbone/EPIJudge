from test_framework import generic_test


def matrix_search(A, x):
    # TODO - you fill in here.
    row = len(A)-1
    col = len(A[0]) - 1

    for i in range(row, -1, -1):
        if A[i][col] < x:
            return False
        for j in range(col, -1, -1):
            if A[i][j] < x:
                break
            elif A[i][j] == x:
                return True
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
