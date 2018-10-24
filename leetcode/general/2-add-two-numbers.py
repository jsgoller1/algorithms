"""
You are given two non-empty linked lists representing two nonnegative
integers. The digits are stored in reverse order and each of their nodes
contains a single digit. Add the two numbers and return the result
as a linked list. You may assume the two numbers do not contain any
leading zeros, except for the number zero itself.

Example:
In: (2->4->3) + (5->6->4)
Out: 7->0->8
Explanation: 342 + 465 = 807

Constraints:
  - Zero or positive numbers
------------------------------------
- Since the lists are in reversed order, we get the lower magnitude digits first.
- To convert a list to an integer, we can write a routine that keeps a running sum
and adds each value it finds (multiplied by 10^n) as it walks the list.
- Once we have both values and sum them, we convert back to a list one of two ways:
  - by successively performing (x // 10^n) % 10 starting at n = 0. We could write a generator for this.
  - by converting it to a string, reversing the string, and then interating through each character, casting it back to an int
- Then we use each value to construct the list

The above approach is O(N) for the character lengths of the integer.

Cases:
  - Empty list (either) are not allowed per constraints
  - List representing zero
    - Reconstruction involves division; might be best to take string approach
  - List representing positive number
-------------------------
One alternative approach would be to do an in-place addition in one pass; we wouldn't
know beforehand how long either linked list is, but what we could do to account for this
is walk both lists simultaneously calculate a sum (and carryover, if necessary) at each place
and both nodes to it. Then, if we exhaust one list first, we can return the unexhausted one.
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def listToInt(node):
    val = 0
    place = 0
    while node != None:
        val += node.val * (10 ** place)
        place += 1
        node = node.next
    return val


def intToList(val):
    valString = str(val)[::-1]
    head = ListNode(int(valString[0]))
    curr = head
    place = 1
    for char in valString[1:]:
        newNode = ListNode(int(char))
        place += 1
        curr.next = newNode
        curr = curr.next
    return head


class Solution:
    def addTwoNumbers(self, node1, node2):
        return intToList(listToInt(node1) + listToInt(node2))


if __name__ == '__main__':
    s = Solution()
    n1 = intToList(0)
    n2 = intToList(411)
    n3 = s.addTwo(n1, n2)
    while n3 != None:
        print(n3.val)
        n3 = n3.next
