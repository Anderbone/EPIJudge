from typing import List

from test_framework import generic_test


def find_nearest_repetition(paragraph: List[str]) -> int:
    # TODO - you fill in here.

    mind = float('inf')
    last_word_index = {}

    for i, word in enumerate(paragraph):

        if word not in last_word_index:
            last_word_index[word] = i

        else:
            word_dis = i - last_word_index[word]
            mind = min(mind, word_dis)
            last_word_index[word] = i

    return mind if mind != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('nearest_repeated_entries.py',
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
