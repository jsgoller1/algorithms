# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        order = defaultdict(list)

        def traverse(node, y, x):
            if not node:
                return
            order[x].append((y, node.val))
            traverse(node.left, y+1, x-1)
            traverse(node.right, y+1, x+1)
        traverse(root, 0, 0)

        solution = []
        for key, pairs in sorted(order.items()):
            solution.append([val for _, val in sorted(pairs)])
        return solution
