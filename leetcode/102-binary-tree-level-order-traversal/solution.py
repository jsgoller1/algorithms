# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque, defaultdict


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        levels = defaultdict(list)
        q = [(root, 0)]
        while q:
            curr, level = q.pop()
            levels[level].append(curr.val)
            if curr.right:
                q.append((curr.right, level+1))
            if curr.left:
                q.append((curr.left, level+1))

        return [v for v in levels.values()]
