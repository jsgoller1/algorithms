"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]

Input:
      1
    2   3
  4  5 6  7

Output: [4, 2, 5, 1, 6, 3, 7]

Follow up: Recursive solution is trivial, could you do it iteratively?

Input: TreeNode
Output: List of ints representing in-order traversal
-------------------------------
Types of traversal:
  Pre-order: View node data, Exhaust left subtree, exhaust right subtree
  In order: Exhaust left subtree, view data, exhaust right subtree
  Post-order: Exhaust left subtree, exhaust right subtree, view data


Recursive:
  walk(node):
    if node == null:
      return
    walk(node.left)
    display(node.val)
    walk(node.right)

Iterative:
  q = stack()
  walk = []
  while q or node != null:
    if node != null:
      q.push(node)
      node = node.left
    else:
      node = q.pop()
      walk.append(node)
      node = node.right
"""
import random


class TreeNode(object):
    """
    Defines binary tree node
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def createTree():
    head = TreeNode(1)
    head.left = TreeNode(2)
    head.right = TreeNode(3)
    head.left.left = TreeNode(4)
    head.left.right = TreeNode(5)
    head.right.left = TreeNode(6)
    head.right.right = TreeNode(7)
    return head


class Solution(object):
    def inorderTraversal(self, root):
        walk = []
        q = []
        while q or root:
            if root:
                q.append(root)
                root = root.left
            else:
                root = q.pop()
                walk.append(root.val)
                root = root.right
        return walk


if __name__ == '__main__':
    s = Solution()
    assert s.inorderTraversal(createTree()) == [4, 2, 5, 1, 6, 3, 7]
    assert s.inorderTraversal(None) == []
    assert s.inorderTraversal(TreeNode(99)) == [99]
