from test_framework import generic_test


def remove_duplicates(A):
    # TODO - you fill in here.
    if not A:
        return None
    ans = dumb = A
    while dumb.next:
        if dumb.next.data == dumb.data:
            if dumb.next.next:
                dumb.next = dumb.next.next
            else:
                dumb.next = None
        else:
            dumb = dumb.next

    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "remove_duplicates_from_sorted_list.py",
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
