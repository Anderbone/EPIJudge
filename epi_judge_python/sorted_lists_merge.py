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



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_lists_merge.py",
                                       'sorted_lists_merge.tsv',
                                       merge_two_sorted_lists))
