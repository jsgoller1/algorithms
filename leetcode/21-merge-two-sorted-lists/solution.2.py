class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 if not l2 else l2
        if l1.val <= l2.val:
            next_node = l1
            l1 = l1.next
        else:
            next_node = l2
            l2 = l2.next
        next_node.next = self.mergeTwoLists(l1, l2)
        return next_node
