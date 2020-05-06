from list_node import ListNode
from test_framework import generic_test


<<<<<<< HEAD
def is_linked_list_a_palindrome(head):
    if head is None:
        return True
    hare = turtle = curr = head
    while hare and hare.next:
        hare = hare.next.next
        turtle = turtle.next
    stack = []
    while turtle:
        stack.append(turtle.data)
        turtle = turtle.next
    while stack:
        if curr.data != stack.pop():
            return False
        curr = curr.next
=======
def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
>>>>>>> upstream/master
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
