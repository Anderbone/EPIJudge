from test_framework import generic_test
import collections

<<<<<<< HEAD
def can_form_palindrome(s):
    sum = 0
    for i in collections.Counter(s).values():
        sum += i%2
    if sum <=1:
        return True
    return False
=======
def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
