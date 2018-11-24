"""
Write a function to delete a node (except the tail) in a singly linked list,
given only access to that node. Given linked list -- head = [4,5,1,9], which
looks like following:
4 -> 5 -> 1 -> 9

Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list
             should become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list
             should become 4 -> 5 -> 9 after calling your function.
Note:
- The linked list will have at least two elements.
- All of the nodes' values will be unique.
- The given node will not be the tail and it will always be a valid node of the linked list.
- Do not return anything from your function.
---------------------------------------------
In: ListNode
Out: None (return nothing)

- This question has gotten a lot of hate in the comments. I learned today that "MDZZ" is apparently
a transliterated acronym from Mandarin for "you are a fucking idiot".
- Deleting a linked list node simply involves finding the node before it and settings its next
to next.next. It will be automatically GC'd in Python.
- We can do this for the tail, but not the head, so I'm confused about the prompt of the question. On
First attempt, let's assume they meant head.
--------------------------------------------
- I did not read the prompt closely enough; the question is "given access ONLY to that node"
- In this case, we just copy the next's value into our current node's value, then set its next to next.next
"""
import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def createList(size=None):
    if size == None:
        size = random.randint(1, 20)
    if size == 0:
        return None
    vals = [val for val in range(size)]
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
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    s = Solution()
    ll1 = createList(2)
    ll2 = createList(10)
    print(walkList(ll1))
    print(walkList(ll2))
