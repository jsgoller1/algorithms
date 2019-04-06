"""
Merge two sorted linked lists and return it as a new list. The
new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
------------------------------
In: ListNode object
Out: ListNode object

- Either list could be null
- Lists may not be the same length
- Can be accomplished with the merge step of mergesort
-------------------------------
- Do the last step of mergesort; pick the head from each list and put
it into the new list, depending on whichever head is lower; if either is
exhausted first, append the remaining list to the new list

pseudo(listA, listB):
  if both listA and listB aren't null:
    newHead = lesser of them, advance the one that was used
  else:
    if listA:
      return listA
    if listB:
      return listB
    else:
      return null

  curr = newHead
  while listA and listB aren't null:
    if listA.val <= listB.val:
      curr.next = listA
      listA = listA.next
    else:
       curr.next = listB
       listB = listB.next
    curr = curr.next
  if listA is null and listB isn't:
    curr.next = listB
  elif listB is null and listA isn't:
    curr.next = listA
  return newHead

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
    def mergeTwoLists(self, l1, l2):
        preHead = ListNode("foobar")

        # Merge
        curr = preHead
        while (l1 != None and l2 != None):
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next

        # Append remainder
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2

        return preHead.next


if __name__ == '__main__':
    s = Solution()
    l1 = createSortedList(5)
    l2 = createSortedList(5)
    print("List 1: {0}\nList 2: {1}".format(walkList(l1), walkList(l2)))
    l3 = s.mergeTwoLists(l1, l2)
    print("Merged: {0}".format(walkList(l3)))
