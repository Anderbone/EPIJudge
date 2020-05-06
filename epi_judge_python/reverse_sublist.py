from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode

def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    # TODO - you fill in here.
    res = ListNode()
    res.next = L


    count = 1
    while count != start:
        L = L.next
        count += 1
    sub = L
    L = L.next
    while count != finish:
        L.next = sub

    return None


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
