class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        second = head.next
        if not second:
            return head
        head.next = self.swapPairs(second.next)
        second.next = head
        return second
