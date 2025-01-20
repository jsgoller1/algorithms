from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def remove_duplicates(L: ListNode) -> Optional[ListNode]:
    if not L:
        return L
    head, curr, next_node = L, L, L.next
    while curr:
        while next_node and curr.data == next_node.data: 
            next_node = next_node.next 
        curr.next = next_node
        curr, next_node = next_node, (next_node.next if next_node else None)
    return head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'remove_duplicates_from_sorted_list.py',
            'remove_duplicates_from_sorted_list.tsv', remove_duplicates))
