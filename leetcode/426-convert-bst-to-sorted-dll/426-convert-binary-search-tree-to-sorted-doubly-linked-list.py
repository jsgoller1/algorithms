"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

inorder walk gives us correct node ordering

left child in inorder should be prev, right child in inorder should be next 

not in place: store all nodes in arr. Then for each node, set node.left to prev (if possible) and prev.right to node, then fixups for min/max 
in place: node.left = prev processed (if any), prev.right = current 
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        min_node = max_node = root 
        previous_node = None 
        def walk(node): 
            if not node:
                return 
            nonlocal min_node, max_node, previous_node

            if node.val < min_node.val:
                min_node = node
            if max_node.val < node.val:
                max_node = node 

            walk(node.left)
            
            if previous_node:
                previous_node.right = node
                node.left = previous_node
            previous_node = node 

            walk(node.right)

        walk(root)
        min_node.left = max_node
        max_node.right = min_node 
        return min_node 