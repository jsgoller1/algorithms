"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list. You may assume the two numbers
do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [0], l2 = [0]
Output: [0]

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints
    - Each list has 1 - 100 nodes
        - 0 to 99...99.
    - Each node stores 0 - 9 (no negatives)
    - No leading zeroes (except a list storing the value 0)

Cases:
    - 0 (single element list with 0)
    - Two lists of different length
    - Addition resulting in carrying and new nodes (2 2-node lists in, one 3-node out)
    - Output should never be shorter than input (no negatives allowed)
---------------------------------
Approach 1:
    - Convert both input lists to int, sequentially
        - Will involve multiplying by powers of 10 for each node
    - Add values
    - Convert sum to list, return it

Approach 2:
    - Start at heads of both lists
    - Go node-by-node in each, summing values and storing carry
        - If one list is exhausted, copy remaining values
    - Create new node, append to output
    - Return 
"""

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = curr = ListNode()
        prev = None
        carry = 0
        while l1 or l2:
            # Get values from input lists
            l1_val = l1.val if l1 else 0
            l1 = l1.next if l1 else None
            l2_val = l2.val if l2 else 0
            l2 = l2.next if l2 else None

            # Compute new element's value
            new_val, carry = (l1_val+l2_val+carry) % 10, (l1_val+l2_val+carry) // 10

            # Insert new element to list and advance
            curr.val = new_val
            curr.next = ListNode()
            prev = curr
            curr = curr.next

        # If we had carry from final addition, use last
        # node for it; otherwise, last node is a leading
        # zero and should be removed.
        if carry:
            curr.val = carry
        else:
            prev.next = None

        return head
