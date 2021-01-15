"""
Given head, the head of a linked list, determine if the linked 
list has a cycle in it. There is a cycle in a linked list if there
is some node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to denote the
index of the node that tail's next pointer is connected to. Note
that pos is not passed as a parameter. Return true if there is a
cycle in the linked list. Otherwise, return false.

Constraints:
    - 0 to 10000 nodes (head can be none, though not according to type sig?)
    - Each node's val can be between -/+100000
    - Lists may or may not have cycle
---------------------------------
O(1) space solution: "Tortise and hare"
    - Go through LL with two pointers, one that advances two at a time and the other one at a time
    - If hare reaches end of list, no cycle. 
    - If hare / tortise on same node, cycle exists. 
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = head
        fast = head.next if head and head.next else None
        while fast:
            fast = fast.next.next if fast.next and fast.next.next else None
            slow = slow.next
            if fast == slow:
                return True
        return False
