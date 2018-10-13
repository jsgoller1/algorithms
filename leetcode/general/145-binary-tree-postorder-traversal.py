"""
Statement

Given a binary tree, return the postorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [3,2,1]

Follow up: Recursive solution is trivial, could you do it iteratively?

Input: TreeNode type
Output: list of ints
-------
Understand / Plan

Post-order traversal of a binary tree means visiting the leftmost child first, then the rightmost
child, then the parent. In the example above, we traverse down to 3, then 2, then 1 (trivial because
the tree is a linked list).

We can handle this recursively:
postorder(node):
  - if children == none:
    return

  postorder(left)
  postorder(right)
  print(node.value)

Tree traversal is O(N) for a tree of N nodes.
----
"""

# Definition for a binary tree node.
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


class Solution(object):
    def __init__(self):
        self.traversal = []

    def postorderTraversal(self, root):
        self.traverse(root)
        return self.traversal

    # "Trivial" (according to LC) recursive solution
    def traverse(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.traversal.append(root.val)
