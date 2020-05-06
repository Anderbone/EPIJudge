from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from list_node import ListNode

def add_two_numbers(l1, l2):

<<<<<<< HEAD
    def getnum(l1):
        number1 = 0
        count = 0
        while l1 is not None:
            digit = l1.data
            # number1 = number1*10 + digit
            number1 = 10 ** count * digit + number1
            l1 = l1.next
            count += 1
        return number1

    number1 = getnum(l1)
    number2 = getnum(l2)

    ans = number1 + number2

    head = ListNode(ans % 10)
    p = head
    ans = ans // 10
    while (ans != 0):
        digit = ans % 10
        ans = ans // 10
        p.next = ListNode(digit)
        p = p.next

    return head
    
=======
def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # TODO - you fill in here.
    return None
>>>>>>> upstream/master


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
