"""
Given a binary tree, find its maximum depth. The maximum depth is the number of nodes
along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
-------------------------
In: TreeNode
Out: Int

We can solve this with a DFS; the base case occurs if the root has no children, in
which case we return 1. If the root has children, return 1 + max of recursed value from
children.

If node is None, return 0.
"""


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        elif not (root.left or root.right):
            return 1
        else:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
