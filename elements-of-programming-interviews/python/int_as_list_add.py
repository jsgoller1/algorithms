from typing import Optional

from list_node import ListNode
from test_framework import generic_test

# TODO: Negatives


def add_two_numbers(L1: ListNode, L2: ListNode) -> Optional[ListNode]:
    # NOTE: Only works for nonnegatives
    if not L2 or not L1:
        return L1 if L1 else L2

    head = curr = ListNode(-1, None)
    carry = 0
    while L1 or L2 or carry:
        op1 = L1.data if L1 else 0
        op2 = L2.data if L2 else 0
        digit = (op1 + op2 + carry) % 10
        carry = (op1 + op2 + carry) // 10
        curr.next = ListNode(digit, None)
        curr = curr.next
        L1 = L1.next if L1 else L1
        L2 = L2.next if L2 else L2

    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_list_add.py',
                                       'int_as_list_add.tsv', add_two_numbers))
