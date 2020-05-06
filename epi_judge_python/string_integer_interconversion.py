from test_framework import generic_test
from test_framework.test_failure import TestFailure
import functools
import string

<<<<<<< HEAD
def int_to_string(x):
#    123- '123'

    return str(x)
def string_to_int(s):
    x = 123
    a = (chr(ord('0') + x % 10))
    print(a)
    print(type(a))
    flag = 0
    if s[0] is '-':
        flag = 1
        s = s[1:]
    num = 0
    # while :
    #     one = s % 10
    #     left = s // 10

    for digit in reversed(s):
        digit = ord(digit)
        digit = chr(digit)
        num += digit
        num *= 10
    num /= 10

    if flag:
        num = -num
    return num
=======
def int_to_string(x: int) -> str:
    # TODO - you fill in here.
    return '0'


def string_to_int(s: str) -> int:
    # TODO - you fill in here.
    return 0

>>>>>>> upstream/master

def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
