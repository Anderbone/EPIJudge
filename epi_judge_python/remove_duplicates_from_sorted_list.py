from typing import Optional

from list_node import ListNode
from test_framework import generic_test


<<<<<<< HEAD
def remove_duplicates(A):
=======
def remove_duplicates(L: ListNode) -> Optional[ListNode]:
>>>>>>> upstream/master
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
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
