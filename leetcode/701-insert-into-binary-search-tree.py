"""
Statement

Given the root node of a binary search tree (BST) and
a value to be inserted into the tree, insert the
value into the BST. Return the root node of the
BST after the insertion. It is guaranteed that
the new value does not exist in the original BST.

Note that there may exist multiple valid ways for
the insertion, as long as the tree remains a BST
after insertion. You can return any of them.

For example, given the tree:
        4
       / \
      2   7
     / \
    1   3
And the value to insert: 5
You can return this binary search tree:

         4
       /   \
      2     7
     / \   /
    1   3 5
This tree is also valid:

         5
       /   \
      2     7
     / \
    1   3
         \
          4

Given: a root node and a value to insert into the tree
Return: root node, after value has been inserted
Constraints:
  - Value not already in tree
  - If several valid inserts are possible, any are acceptable
-----------------------
Understand / Plan

- to insert into the tree, walk until we find an appropriate parent
and add the new value there

pseudocode:
  func insert(root, value):
    while(root.val != value):
      if val <= root.val:
        if not root.left:
          root.left = Node(value)
        root = root.left
      else:
        if not root.right:
          root.right = Node(value)
        root = root.right
    return root
-----------------------
Execute
-----------------------
Review
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def dfs(root):
    if root == None:
        return
    dfs(root.left)
    print(root.val)
    dfs(root.right)


class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return
        node = root
        while(node.val != val):
            if val <= node.val:
                if not node.left:
                    node.left = TreeNode(val)
                node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                node = node.right
        return root


if __name__ == '__main__':
    s = Solution()
    tree = TreeNode(10)
    s.insertIntoBST(tree, 15)
    s.insertIntoBST(tree, 9)
    dfs(tree)
