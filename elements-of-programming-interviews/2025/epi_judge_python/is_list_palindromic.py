from list_node import ListNode
from test_framework import generic_test

"""
Linear time/space:
    - Get length of list
    - Recurse to midpoint, keep two pointers
        if point is midpoint:
                compare node1 to node2
                return node2.next 
                (parent frame is with node1's predecessor)

- Can also reverse second half of list, but mutating may not be allowed. 
"""


def is_linked_list_a_palindrome(L: ListNode) -> bool:
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_list_palindromic.py',
                                       'is_list_palindromic.tsv',
                                       is_linked_list_a_palindrome))
