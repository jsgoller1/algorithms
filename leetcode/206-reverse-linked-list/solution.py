"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL

Follow up:
A linked list can be reversed either iteratively or recursively. Could you implement both?
-----------------------------
In: ListNode
Out: ListNode

- I've done the iterative version before, so i'll do the recursive one here
-----------------------------------------
- take the next node, make its next the current node but don't lose the reference to its old next
- then next becomes the current, and old next becomes next
- do this until next is none

iterative:
  pseudo(head):
    prev = head
    curr = prev.next
    head.next = None

    while curr:
      newNext = curr.next
      curr.next = prev
      prev = curr
      curr = newNext
    return prev
"""
import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createSortedList(size=None):
    if size == None:
        size = random.randint(1, 20)
    if size == 0:
        return None
    vals = sorted([random.randint(-100, 100) for val in range(size)])
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        new = ListNode(val)
        curr.next = new
        curr = curr.next
    return head


def walkList(listHead):
    listOut = ""
    while listHead != None:
        listOut += str(listHead.val) + "->"
        listHead = listHead.next
    return listOut


class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev = head
        curr = prev.next
        head.next = None

        while curr:
            newNext = curr.next
            curr.next = prev
            prev = curr
            curr = newNext
        return prev


if __name__ == '__main__':
    s = Solution()
    ll = createSortedList(0)
    print(walkList(ll))
    print(walkList(s.reverseList(ll)))
