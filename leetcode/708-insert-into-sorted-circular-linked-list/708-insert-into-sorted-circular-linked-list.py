"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

Viable: 
    Somewhere in the middle:
        curr <= val <= curr.next
    
    on the edge:
        curr > curr.next and curr < val > curr.next or curr > val < curr.next


[1,3,5,7]
    Min insert: 0
    Max insert: 8
    Middle insert: 4
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        node = Node(insertVal)

        if not head: 
            node.next = node
            return node 

        curr = head
        while True:
            if (curr.val <= insertVal <= curr.next.val):
                break
            elif (curr.val > curr.next.val) and (curr.val <= insertVal or insertVal <= curr.next.val):
                break
            elif curr.next == head:
                break 
            curr = curr.next

        node.next = curr.next 
        curr.next = node 
        return head

