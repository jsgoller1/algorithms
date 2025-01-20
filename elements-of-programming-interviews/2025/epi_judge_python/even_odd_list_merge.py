from typing import Optional

from list_node import ListNode
from test_framework import generic_test


def even_odd_merge(L: ListNode) -> Optional[ListNode]:
    if not (L and L.next):
        return L
    even_head = even = L 
    odd_head  = odd = L.next 
    L = L.next.next
    i = 2
    while L: 
        if i % 2:
            odd.next = L
            odd = odd.next
        else:
            even.next = L 
            even = even.next
        i += 1
        L = L.next
    odd.next = None 
    even.next = odd_head
    return even_head


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_list_merge.py',
                                       'even_odd_list_merge.tsv',
                                       even_odd_merge))
