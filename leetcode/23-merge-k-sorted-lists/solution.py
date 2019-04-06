"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
----------------------------------------
In: List[ListNodes]
Out: ListNode

- Can we repeat the same idea from the list merging problem, but extend it to multiple lists?
- We can determine what the correct head to use is by writing a custom min() function
  - We could use the Python min() with a key that extracts the node val, but we need it to skip Nones
  - Alternatively we can just pull Nones out of the list
-----------------------------------------
- For all the nodes in the list, get the min valued one; append that to the list
- Advance the node; if it becomes none, remove it from the list
- Once the list is exhausted, return the new head

minHead(lists):
  minVal = float('inf')
  nodei = None
  for i, head in enumerate(lists):
    if head.val < minVal
      minVal = head.val
      nodei = i
  return nodei

pseudopython(lists):
  head = minHead(lists)
  curr = head
  while(lists):
    i = minHead(lists)
    curr.next = lists[i]
    lists[i] = lists[i].next
    if lists[i] == None:
      lists.pop(i)
  return head
"""
import random


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


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getMinNodeIndex(self, lists):
        minVal = float('inf')
        nodei = None
        for i, head in enumerate(lists):
            if head.val <= minVal:
                minVal = head.val
                nodei = i
        return nodei

    def mergeKLists(self, lists):
        dummyHead = ListNode("You are wrong if you see this message.")
        curr = dummyHead
        lists = [head for head in lists if head is not None]
        while(lists):
            i = self.getMinNodeIndex(lists)
            curr.next = lists[i]
            lists[i] = lists[i].next
            if lists[i] == None:
                lists.pop(i)
            curr = curr.next
        return dummyHead.next


if __name__ == '__main__':
    s = Solution()
    normalHeads = [createSortedList(
        5), createSortedList(5), createSortedList(5)]
    mixedHeads = [createSortedList(
        8), createSortedList(2), createSortedList(5)]

    testCases = [normalHeads, mixedHeads]
    for case in testCases:
        for head in case:
            print(walkList(head))
        print(walkList(s.mergeKLists(case)))
        print("-"*20)
