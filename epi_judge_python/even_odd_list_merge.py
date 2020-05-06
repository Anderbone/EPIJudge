from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode

def even_odd_merge(head):
    # def oddEvenList(self, head: ListNode) -> ListNode:
    if not head:
        return None
    if head.next is None or head.next.next is None:
        return head

    flag = 1
    head1 = pre = head
    l2 = ListNode(head.next.data)
    head2 = l2
    pre = pre.next.next

    while pre:
        if flag == 1:
            head1.next = pre
            pre = pre.next
            head1 = head1.next
            flag = 0

        elif flag == 0:
            head2.next = pre
            pre = pre.next
            head2 = head2.next
            flag = 1

    head1.next = l2
    head2.next = None

    return head

<<<<<<< HEAD
=======
def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
