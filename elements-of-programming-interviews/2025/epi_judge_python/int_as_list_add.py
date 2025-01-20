from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
- Problem statement says lists are of digits, so assuming no negatives 
"""


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    head = curr = ListNode(None, None)
    carry = 0 
    while L1 or L2 or carry:
        total = (L1.data if L1 else 0) + (L2.data if L2 else 0) + carry
        curr.next = ListNode(total % 10)
        carry = 1 if total > 9 else 0 
        curr, L1, L2 = curr.next, (L1.next if L1 else None), (L2.next if L2 else None)
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
