"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.

Follow up:
Could you do this in one pass?
------------------------------
- We don't know where the end of a list is until we actually find it
- If it were a doubly linked list, we could walk backwards and delete
the desired node.
- With O(n) additional space, we could enqueue n+1 additional nodes.
When the final node is found, we dequeue once and set its next to next.next.
- Can we do it with O(c) space?
  - starting with the head as prior and seen = 0, walk the list incrementing seen until seen == n. Then
  on every iteration, prior->next = prior->next->next.
  - Ignore n = 0 and n > list length, return list unmodified
  - n = 1 removes end of list, need to catch this
    - actually, last-1->next->next is None, so this should be caught
  - if n == length, the head should be removed; this algorithm cannot handle this case
  - if n == length - 1 or less, this should be ok.
"""
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(size):
    if size < 1:
        return None
    head = ListNode(1)
    curr = head
    for i in range(2, size - 1):
        newNode = ListNode(i)
        curr.next = newNode
        curr = newNode
    return head


def walkList(head):
    path = ""
    while head != None:
        path += "{0}->".format(head.val)
        head = head.next
    print(path)


class Solution:
    def removeNthFromEnd(self, head, n):
        if head == None or n < 1:
            return

        size = 0
        prev = head
        curr = head
        while curr != None:
            curr = curr.next
            size += 1
            if size > n+1:
                prev = prev.next

        if n < size:
            prev.next = prev.next.next
        elif n == size:
            head = head.next

        return head


if __name__ == '__main__':
    s = Solution()
    params = [(0, 10), (1, 0), (1, 1), (1, 4),
              (10, 5), (10, 1), (10, 10), (10, 15)]
    for param in params:
        print(
            "Remove {0}th element from end from {1}-list".format(param[1], param[0]))
        ll = createList(param[0])
        walkList(ll)
        ll = s.removeNthFromEnd(ll, param[1])
        walkList(ll)
        print("-"*15)
