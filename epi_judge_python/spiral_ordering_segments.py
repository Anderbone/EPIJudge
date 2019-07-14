from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    n = len(square_matrix)
    if not square_matrix:
        return []
    direction_next = {'right':'down', 'down':'left', 'left':'up', 'up':'right'}
    res = [i for i in square_matrix[0]]
    i,j = 0,n-1
    direction = 'down'
    stride = n-1
    while stride != 0:
        for _ in range(2):
            for _ in range(stride):
                if direction is 'down':
                    i += 1
                    res.append(square_matrix[i][j])
                elif direction is 'up':
                    i -= 1
                    res.append(square_matrix[i][j])
                elif direction is 'right':
                    j += 1
                    res.append(square_matrix[i][j])
                elif direction is 'left':
                    j -= 1
                    res.append(square_matrix[i][j])
            direction = direction_next[direction]
        stride -= 1
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
