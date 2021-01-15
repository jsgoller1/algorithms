"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?

No constraints given.

Possible cases:
    - Node has a next
    - Node has no next
    - Node should never itself be null
-----------------------------------------------------------

1->2->3->4->5->NULL

Iterative:
    If we start with prev = next_node = none, and curr = node, then while node is not null:
        next_node = node.next
        node.next = prev
        prev = node
        node = next_node

    then we return prev

Recursive(prev, node):
    if node == null:
        return prev    
    next = node.next
    node.next = prev
    recurse(node, next)
recurse(null, node)
"""


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = next_node = None
        curr = head
        while head:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        return prev


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        def recurse(prev, node):
            if node == None:
                return prev
            next_node = node.next
            node.next = prev
            return recurse(node, next_node)
        return recurse(None, head)
