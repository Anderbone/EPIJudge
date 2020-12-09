from test_framework import generic_test
import collections


# def can_form_palindrome(s):
#     sum = 0
#     for i in collections.Counter(s).values():
#         sum += i%2
#     if sum <=1:
#         return True
#     return False
def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    # counter = collections.defaultdict(lambda: 0)
    # s = "".join(s.split())
    # for i in s:
    #     counter[i] += 1

    counter = collections.Counter(s)
    single = 0
    for v in counter.values():
        if v % 2 == 1:
            single += 1
        if single > 1:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
