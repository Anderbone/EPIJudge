from test_framework import generic_test
import collections

<<<<<<< HEAD
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter_c = collections.Counter(letter_text)

    for c in magazine_text:
        if c in letter_c:
            letter_c[c] -= 1
            if letter_c[c] == 0:
                del letter_c[c]
                if not letter_c:
                    return True

    return not letter_c
=======
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    return True
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
