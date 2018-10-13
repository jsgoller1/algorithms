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

Iteration solution:
In some way, iteration and recursion here are the same solution,
except that with iteration we explicitly use a stack whereas recursion
implicitly uses a call stack.

For the iterative example:
  postorder(node):
    stack = []
    while(stack):

----
Execute

See below
----
Review

The recursive version of this was _super_ easy - I implemented it very quickly.
I chatted with a friend about why this would be "hard" and he asked
"can you use a stack?" I decided to give the stack solution a try.
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

    # Interative version
    def traverse(root):
        stack = []

    # "Trivial" (according to LC) recursive solution
    def traverse_recursive(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return

        self.traverse(root.left)
        self.traverse(root.right)
        self.traversal.append(root.val)
