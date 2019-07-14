from test_framework import generic_test


def generate_pascal_triangle(n):
    numRows = n
    if numRows == 0:
        return []
    n1 = [1]
    n2 = [1, 1]
    if numRows == 1:
        return [n1]
    if numRows == 2:
        return [n1, n2]

    last = generate_pascal_triangle(numRows - 1)
    lastline = last[-1]
    newline = [1]
    for i in range(len(lastline) - 1):
        newline.append(lastline[i] + lastline[i + 1])
    newline.append(1)
    last.append(newline)
    return last

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("pascal_triangle.py",
                                       'pascal_triangle.tsv',
                                       generate_pascal_triangle))
