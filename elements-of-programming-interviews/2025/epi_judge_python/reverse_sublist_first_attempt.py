from typing import Optional

from list_node import ListNode
from test_framework import generic_test


"""
O(n) space: keep track of the first node and last node not meant to be reversed, push nodes for reversal
into a deque, do reversal

O(c) space can also be done, carefully 
"""

# Book's solution
def reverse_sublist(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not (L and L.next and start != finish):
        return L
    dummy_head = prev = ListNode(None, L)
    for _ in range(1, start):
        prev = prev.next 
    curr = prev.next
    for _ in range(finish-start):
        new_next = curr.next 
        curr.next = new_next.next
        new_next.next = prev.next
        prev.next = new_next
    return dummy_head.next



def reverse_linked_list(start_node, end_node=None):
    if (not start_node) or (start_node == end_node):
        return 
    prev, curr = None, start_node
    while curr != end_node:
        new_next = curr.next 
        curr.next = prev 
        prev = curr 
        curr = new_next
    if curr:
        curr.next = prev 

def reverse_sublist_first_attempt(L: ListNode, start: int,
                    finish: int) -> Optional[ListNode]:
    if not (L and L.next) or (start == finish):
        return L 
    head = L = ListNode(None, L)

    left_border_node = start_node = end_node = right_border_node = None
    i = 0
    while L != None:
        if i == start-1:
            left_border_node = L
            start_node = L.next 
        elif i == finish:
            end_node = L 
            right_border_node = L.next
        L = L.next 
        i += 1

    reverse_linked_list(start_node, end_node)
    left_border_node.next = end_node
    start_node.next = right_border_node
    return head.next

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
