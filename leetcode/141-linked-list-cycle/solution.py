"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
-----------------------------------------------
I believe you can use a "tortise-and-hare" method for this:
- use two pointers, one traversing two at a time and one traversing one at a time
- they will eventually meet if the list contains a cycle

With this method, you have to be careful about lists that do not contain cycles; can't derference
next.next if next is null

pseudo(head):
  if not head:
    return False

  slow = head
  fast = head.next
  while (fast != slow):
    slow = slow.next
    if fast and fast.next:
      fast = fast.next.next
    else:
      return False
  return True
"""

import random

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createLinkedList(size, hasCycle=False):
    if size == 0:
        return None

    vals = [random.randint(-100, 100) for val in range(size)]
    head = ListNode(vals[0])
    curr = head
    for val in vals[1:]:
        new = ListNode(val)
        curr.next = new
        curr = curr.next
    if hasCycle:
        curr.next = head
    return head


def walkList(listHead):
    """
    Will loop infinitely if list is
    cyclical
    """
    listOut = ""
    while listHead != None:
        listOut += str(listHead.val) + "->"
        listHead = listHead.next
    return listOut


class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False

        slow = head
        fast = head.next
        while (fast != slow):
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    ll1 = createLinkedList(10)
    if not s.hasCycle(ll1):
        print(walkList(ll1))
    ll2 = createLinkedList(10, True)
    if not s.hasCycle(ll2):
        print(walkList(ll2))
    else:
        print("List has a cycle")
