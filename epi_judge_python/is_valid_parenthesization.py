from test_framework import generic_test
import collections

# <<<<<<< HEAD
# def is_well_formed(s):
#     dic = {'(': ')', '[': ']', '{': '}'}
#     # stack = collections.deque()
#     stack = []
#     for i in s:
#         # if i is '(' or i is '{' or i is '[':
#         if i in dic:
#             stack.append(i)
#         # elif i is '}' or i is ')' or i is ']':
#         else:
#             if not stack or dic[stack.pop()] is not i:
#                 return False
#     return not stack
#
# =======
# def is_well_formed(s: str) -> bool:
#     # TODO - you fill in here.
#     inp = list(s)
#     stack = []
#     for i in inp:
#         if not stack:
#             stack.append(i)
#         else:
#             if (stack[-1] == '(' and i == ')') or (stack[-1] == '[' and i == ']') or stack[-1] == '{' and i == '}':
#                 stack.pop()
#             else:
#                 stack.append(i)
#     if not stack:
#         return True
#     return False

def is_well_formed(s):

    left_chars, LOOKUP = [], {'(': ')', '{': '}', '[': ']'}
    for c in s:
        if c in LOOKUP:
            left_chars.append(c)
        elif not left_chars or LOOKUP[left_chars.pop()] != c:
            # Unmatched right char or mismatched chars.
            return False
    return not left_chars

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
