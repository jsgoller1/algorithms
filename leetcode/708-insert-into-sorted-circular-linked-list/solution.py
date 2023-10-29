"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

"""
Cases:
0: create new list
1: insert in correct order
many: search for insertion point

also:
input fits in middle of list
input is minimum or maximum
"""


class GPTSolution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        # Empty
        if not head:
            new_node.next = new_node
            return new_node

        # Initialize pointers
        l, r = head, head.next

        # Loop until we find the insertion point or we complete a full cycle
        while True:
            # Condition for inserting in the middle
            if l.val <= new_node.val <= r.val:
                break
            # Condition for inserting at the turning point where the list wraps around
            if l.val > r.val and (l.val <= new_node.val or new_node.val <= r.val):
                break
            # Completed a full cycle without finding an insertion point
            if r == head:
                break

            # Move to the next pair of nodes
            l, r = r, r.next

        # Insert the new node
        l.next = new_node
        new_node.next = r

        return head


class JoshuaSolution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        # Empty
        if not head:
            new_node.next = new_node
            return new_node

        # 1 or more nodes
        l, r = head, head.next
        while not (l.val <= new_node.val <= r.val):
            l, r = l.next, r.next
            if l.val > r.val and (l.val <= new_node.val or new_node.val <= r.val):
                # Turning point; node is minimal or maximal element.
                l.next = new_node
                new_node.next = r
                return head
            if (l == head):
                # Did full loop through list, node fits nowhere
                break
        # Either we found a where new_node is middle element, or we did a loop and found none
        l.next = new_node
        new_node.next = r
        return head
