from test_framework import generic_test


def rabin_karp(t: str, s: str) -> int:
    # TODO - you fill in here.
    try:
        i = t.index(s)
    except:
        return -1
    return i


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('substring_match.py',
                                       'substring_match.tsv', rabin_karp))
