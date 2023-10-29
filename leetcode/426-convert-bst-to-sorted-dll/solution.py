"""
In-order traversal gives us sorted order. 
One option:
    - process step is to append each node to an array
    - then when traversal is done, we fix up the pointers and return the head
    - O(n) time and space 

Faster, possibly:
    - traversal, but do pointer fixups at process time
    - Need to keep track of global min and max
    - still O(n) space if we implement recursively, but O(c) space if iterative



# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        nodes = []

        def in_order(node):
            if not node:
                return
            in_order(node.left)
            nodes.append(node)
            in_order(node.right)
        in_order(root)

        i = 0
        while i < len(nodes)-1:
            nodes[i].right = nodes[i+1]
            i += 1

        i = len(nodes)-1
        while 0 < i:
            nodes[i].left = nodes[i-1]
            i -= 1

        nodes[0].left = nodes[-1]
        nodes[-1].right = nodes[0]
        return nodes[0]
