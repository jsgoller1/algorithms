# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, defaultdict


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = defaultdict(list)
        q = deque([(root, 0)] if root else [])
        while q:
            node, x = q.popleft()
            levels[x].append(node.val)
            if node.left:
                q.append((node.left, x-1))
            if node.right:
                q.append((node.right, x+1))
        return [nodes for _, nodes in sorted(levels.items())]


class SolutionDFS:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = {}

        def traverse(node, y, x):
            if not node:
                return
            if x not in levels:
                levels[x] = {}
            if y not in levels[x]:
                levels[x][y] = []
            levels[x][y].append(node.val)

            if node.left:
                traverse(node.left, y+1, x-1)
            if node.right:
                traverse(node.right, y+1, x+1)

        traverse(root, 0, 0)

        ordering = []
        for _, horizontal in sorted(levels.items()):
            sweep = []
            for _, vertical in sorted(horizontal.items()):
                for val in vertical:
                    sweep.append(val)
            ordering.append(sweep)
        return ordering
