from typing import Optional

from list_node import ListNode
from test_framework import generic_test

"""
Last node is k = 1.
Other constraints a bit unclear; can't use more than a few words
of storage regardless of list len, and we cannot assume we can get the length of the list
- Does this mean we cannot do multiple passes?

Some approaches:
- Do one pass to count list length, and then do deletion on second pass. 
    - Linear time, constant space. 
    - Presumably not allowed?
- recurse to end of list and return how many nodes follow the current one; on the kth
one, delete it. 
    - O(n) time, and O(n) space for recursive frames.
- Reverse list, delete the kth node (with the head being the 1st) and re-reverse
    - Linear time, contstant space
    - But this allows us to get the list length?
- allocate k units of storage deque([None for None in range(k)]). Enqueue each node we find
  and dequeue last. each time we do a dequeue of a node, save it as a deletion candidate. When we reach
  the end of the list, delete the deletion candidate with "candidate.data = next.data, candidate.next = candidate.next.next"
    - This is linear time/space if k is the length of the list, but maybe it's the "few words" if k is small? 
- Same as above, but use two pointers
"""

# Assumes L has at least k nodes, deletes the k-th last node in L.
def remove_kth_last(L: ListNode, k: int) -> Optional[ListNode]:
    head = ListNode(None, L)
    curr = prev_to_kth = head
    for i in range(k+1):
        curr = curr.next
    while curr: 
        curr = curr.next 
        prev_to_kth = prev_to_kth.next 
    prev_to_kth.next = prev_to_kth.next.next    
    return head.next


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('delete_kth_last_from_list.py',
                                       'delete_kth_last_from_list.tsv',
                                       remove_kth_last))
