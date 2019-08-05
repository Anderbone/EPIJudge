from test_framework import generic_test


def longest_subarray_with_distinct_entries(A):
    # TODO - you fill in here.
    # print(A)
    recent = {}
    for i, w in enumerate(A):
        if w not in recent:
            recent[w] = i



    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "longest_subarray_with_distinct_values.py",
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
