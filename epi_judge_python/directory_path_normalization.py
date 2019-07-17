from test_framework import generic_test
import re

def shortest_equivalent_path(path):
    # TODO - you fill in here.
    path = re.sub(re.compile(r'/+'), '/', path)
    ele = path.split('/')
    stack = []
    for i in ele :
        if i == '.':
            continue
        elif i == '..':
            if not stack or not stack[-1].isalnum():
                stack.append('..')
            else:
                stack.pop()
        else:
            stack.append(i)

    while stack and stack[-1] == '':
        stack.pop()
    if not stack:
        return '/'
    else:
        return '/'.join(stack)


if __name__ == '__main__':
    print('start')
    shortest_equivalent_path('///')
    print('end')
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
