from test_framework import generic_test



def can_reach_end(A):


    k = 0
    for i in range(len(A)-2, -1, -1):
        if A[i] > k:
            k = 0
        else:
            k += 1

    if k == 0:
        return True
    return False

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
