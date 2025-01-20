# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def getAncestors(node, target):
            if not node:
                return None
            if node == target:
                return deque([target])
            left = getAncestors(node.left, target)
            right = getAncestors(node.right, target)
            if not (left or right):
                return None
            (left or right).appendleft(node)
            return (left or right)

        pAncestors = getAncestors(root, p)
        qAncestors = getAncestors(root, q)
        if not (pAncestors and qAncestors):
            return None

        lca = root
        for p, q in zip(pAncestors, qAncestors):
            if p != q:
                break
            lca = p
        return lca
