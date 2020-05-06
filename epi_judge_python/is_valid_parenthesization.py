from test_framework import generic_test
import collections

<<<<<<< HEAD
def is_well_formed(s):
    dic = {'(': ')', '[': ']', '{': '}'}
    # stack = collections.deque()
    stack = []
    for i in s:
        if i is '(' or i is '{' or i is '[':
            stack.append(i)
        elif i is '}' or i is ')' or i is ']':
            if not stack:
                return False
            if dic[stack.pop()] is not i:
                return False

    if not stack:
        return True
    return False

=======
def is_well_formed(s: str) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
