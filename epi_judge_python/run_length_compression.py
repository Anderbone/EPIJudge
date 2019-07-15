from test_framework import generic_test
from test_framework.test_failure import TestFailure


def decoding(s):
    # TODO - you fill in here. 13e4f to eee
    res = []
    # for i in len(s):
    i = 0
    while i < len(s):
        num = int(s[i])
        while s[i+1].isdigit():
            num = num*10
            num += int(s[i+1])
            i += 1
        part = num * s[i+1]
        # print(part)
        res.append(part)
        i += 2
    return ''.join(res)
    # return ''.join(i for i in res)


def encoding(s):
    # TODO - you fill in here.  ee to 2e
    i = 0
    res = []
    while i<len(s):
        count = 1
        while i+1 < len(s) and s[i] == s[i+1]:
            count += 1
            i += 1
        res.append(str(count)+s[i])
        i += 1
    return ''.join(res)


def rle_tester(encoded, decoded):
    if decoding(encoded) != decoded:
        raise TestFailure('Decoding failed')
    if encoding(decoded) != encoded:
        raise TestFailure('Encoding failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("run_length_compression.py",
                                       'run_length_compression.tsv',
                                       rle_tester))
