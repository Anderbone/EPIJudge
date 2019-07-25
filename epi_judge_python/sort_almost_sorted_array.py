from test_framework import generic_test
import heapq, itertools

def sort_approximately_sorted_array(sequence, k):
    h = []
    for i in  itertools.islice(sequence, k):
        heapq.heappush(h, i)

    res = []

    # for i in sequence[k:]:
    for i in sequence:
        small = heapq.heappushpop(h, i)
        res.append(small)

    while h:
        small = heapq.heappop(h)
        res.append(small)

    return res

def sort_approximately_sorted_array_wrapper(sequence, k):
    return sort_approximately_sorted_array(iter(sequence), k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "sort_almost_sorted_array.py", 'sort_almost_sorted_array.tsv',
            sort_approximately_sorted_array_wrapper))
