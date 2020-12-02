from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode


def merge_two_sorted_lists(l1, l2):
    # res = ListNode(0, None)
    pre = ListNode(0)
    ans = pre
    while (l1 != None or l2 != None):
        if l1 == None or (l2 != None and l2.data <= l1.data):
            pre.next = l2
            l2 = l2.next
            pre = pre.next
        else:
            pre.next = l1
            l1 = l1.next
            pre = pre.next
    return ans.next

def merge_two_sorted_lists(L1: Optional[ListNode],
                           L2: Optional[ListNode]) -> Optional[ListNode]:
    # TODO - you fill in here.
    res = pre = ListNode(0)
    while L1 and L2:
        if L1.data < L2.data:
            pre.next = L1
            L1 = L1.next
            pre = pre.next
        elif L1.data >= L2.data:
            pre.next = L2
            L2 = L2.next
            pre = pre.next
    if L1:
        pre.next = L1
    elif L2:
        pre.next = L2
    return res.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sorted_lists_merge.py',
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
