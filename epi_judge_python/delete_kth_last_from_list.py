from test_framework import generic_test
from list_node import ListNode

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(head, n):

    if head.next is None:
        return None

    count = 0
    pre = ListNode(0)
    pre.next = head
    while (pre.next is not None):
        pre = pre.next
        count += 1

    pre2 = head
    ans = pre2

    if n == 1:
        while (count != 2):
            count -= 1
            pre2 = pre2.next
        pre2.next = None

    else:
        while (count != n):
            count -= 1
            pre2 = pre2.next
        pre2.data = pre2.next.data
        # must data first, then next
        pre2.next = pre2.next.next
    return ans


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("delete_kth_last_from_list.py",
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
