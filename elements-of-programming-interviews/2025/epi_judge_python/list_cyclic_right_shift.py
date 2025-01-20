from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Right shifting is easier to think about if our list was ring shaped. Suppose we iterate
to the end of the list, then set tail.next to head. If we restart from a dummy head 
(its next is the 1th element), the kth element is the new head, and the k-1th is the new tail. 

So:
- create dummy head
- form list into circle 
- start at dummy head .next and 1
- count to k (with prev)
- set prev.next to none, and return kth 
"""


def cyclically_right_shift_list(L: ListNode, k: int) -> Optional[ListNode]:
    if not (L and L.next and k > 0):
        return L 
    head = curr = L 
    length = 1
    while curr.next:
        curr = curr.next
        length += 1 
    curr.next = head 
    tail = curr 
    k = k % length

    while length != k: 
        tail, head = tail.next, head.next 
        length -= 1 
    tail.next = None
    return head 

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('list_cyclic_right_shift.py',
                                       'list_cyclic_right_shift.tsv',
                                       cyclically_right_shift_list))
