# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from math import isclose


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best_so_far = float('inf')
        best_delta = abs(target - best_so_far)

        def find_best(node):
            if not node:
                return

            node_delta = abs(target - node.val)
            nonlocal best_so_far
            nonlocal best_delta
            if isclose(node_delta, best_delta):
                best_so_far = min(node.val, best_so_far)
                best_delta = abs(target-best_so_far)
            elif node_delta < best_delta:
                best_so_far = node.val
                best_delta = node_delta

            if node.left and not (node.left.val < node.val < target):
                find_best(node.left)
            if node.right and not (target < node.val < node.right.val):
                find_best(node.right)

        find_best(root)
        return best_so_far
