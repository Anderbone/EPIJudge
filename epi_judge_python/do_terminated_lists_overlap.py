import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


# def overlapping_no_cycle_lists(l1, l2):
#     # Definition for singly-linked list.
#     # class ListNode(object):
#     #     def __init__(self, x):
#     #         self.val = x
#     #         self.next = None

def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    if not l0 or not l1:
        return None
    head0 = l0
    head1 = l1
    count0 = count1 = 0
    while head0.next:
        count0 += 1
        head0 = head0.next
    while head1.next:
        count1 += 1
        head1 = head1.next

    diff = abs(count1 - count0)
    if count0 < count1:
        find = l1
        another = l0
    else:
        find = l0
        another = l1

    while diff > 0:
        find = find.next
        diff -= 1
    while find and another:
        if find != another:
            find = find.next
            another = another.next
        else:
            return find

# def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
#     len1 = 0
#     len2 = 0
#     t1 = p1 = l1
#     t2 = p2 = l2
#     while (p1):
#         len1 += 1
#         p1 = p1.next#
#     while (p2):
#         len2 += 1
#         p2 = p2.next
#
#     if len1 > len2:
#         for _ in range(len1 - len2):
#             t1 = t1.next
#     elif len1 < len2:
#         for _ in range(len2 - len1):
#             t2 = t2.next
#
#     while (t1 is not None and t1.next is not t2.next):
#         t1 = t1.next
#         t2 = t2.next
#
#     if t1 is None:
#         return None
#     # the last one is same
#     if t1 is t2:
#         return t1
#     return t1.next

@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
