# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Approach 1: O(n) time and space - get list of ancestors for each node, then pairwise compare them to find lowest.
Approach 2: Recursive, still O(n) for time if tree is LL and space due to stack frames, but possibly nicer:
    - base case: node is p or q
    - recursive case: node has p or q in its subtrees
"""


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (root in [None, p, q]) or (p.val < root.val < q.val) or (q.val < root.val < p.val):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)


class Solution2:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findNodes(node):
            if node in [None, p, q]:
                return node
            results = {findNodes(node.left), findNodes(node.right)} - {None}
            if results == {p, q}:
                return node
            elif results == {p}:
                return p
            elif results == {q}:
                return q
            elif results == set():
                return None
            else:
                return results.pop()

        return findNodes(root)


class Solution3:
    def getAncestors(self, root, target):
        ancestors = []
        node = root
        while node != target:
            ancestors.append(node)
            node = node.left if target.val < node.val else node.right
        ancestors.append(target)
        return ancestors

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        pAncestors = self.getAncestors(root, p)
        qAncestors = self.getAncestors(root, q)
        best = root
        for p, q in zip(pAncestors, qAncestors):
            if p != q:
                break
            best = p
        return best
