"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def deep_copy_list(self, head):
        new_head = Node(head.val)
        copy_mapping = {head: new_head}
        curr, new_curr = head, new_head
        while curr.next:
            new_curr.next = Node(curr.next.val)
            curr = curr.next
            new_curr = new_curr.next
            copy_mapping[curr] = new_curr
        return copy_mapping, new_head

    def fixup_random_pointers(self, old_head, new_head, copy_mapping):
        while old_head:
            if old_head.random:
                new_head.random = copy_mapping[old_head.random]
            old_head = old_head.next
            new_head = new_head.next

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        copy_mapping, new_head = self.deep_copy_list(head)
        self.fixup_random_pointers(head, new_head, copy_mapping)
        return new_head
