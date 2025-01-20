from typing import Optional

from list_node import ListNode
from test_framework import generic_test


"""
O(n) space: keep track of the first node and last node not meant to be reversed, push nodes for reversal
into a deque, do reversal

O(c) space can also be done, carefully 
"""

def reverse_linked_list(start_node, end_node):
    if not (start_node and end_node and start_node != end_node):
        return start_node

    prev, curr = end_node.next, start_node
    while curr != end_node:
        new_next = curr.next 
        curr.next = prev 
        prev = curr
        curr = new_next
    curr.next = prev 
    return curr 


def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not (L and 0 < start < finish): 
        return L 
    dummy_head = sublist_head = L = ListNode(None, L)
    start_node = end_node = None 
    i = 0
    while i <= finish:
        if i == start-1:
            sublist_head = L 
        elif i == start:
            start_node = L
        elif i == finish:
            end_node = L 
        L = L.next
        i += 1
    sublist_head.next = reverse_linked_list(start_node, end_node)
    return dummy_head.next

  
"""
for start, finish in [
    (1,5),
    (1,3),
    (2,5),
    (2,4),
]:
    ll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, None)))))
    ll = reverse_sublist(ll, start, finish)
    print(ll)
    print("-----")
"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_sublist.py',
                                       'reverse_sublist.tsv', reverse_sublist))
