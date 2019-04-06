"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.

    50
   / \
  1   100
     / \
    45  110
False (45 < 50)

    50
   / \
  1   100
     / \
    75  110
True
-----------------
- Did this in Golang already but redoing for mock interview

Recursive function with current, parent:
  assert left < current
  assert right > current
  if parent and current > parent:
    left and right must be greater than parent
  if parent and current < parent
    left and right must be less than parent

- We don't need to check and higher than parent;
  - This was actually false and the one edge case that failed;
  - How do we determine if all grand children are valid?
  - Each time we go left and right, the min/max value allowed decreases;
    if we keep track of the allowed range we should catch out-of-range
    no matter how far down they go.
  - Got nailed on this the night before an interview; feels bad man :(
- How do we handle duplicates? Will they come up?
  - They did; use a set.
-------------------------

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def validate(self, curr, parent, seen, lowest, highest):
        # Base case
        if not curr:
            return True

        # Ensure no duplicates
        if curr.val in seen:
            return False
        else:
            seen.add(curr.val)

        # Validate left child relationship
        if curr.left and curr.left.val >= curr.val:
            return False

        # Validate right child relationship
        if curr.right and curr.right.val <= curr.val:
            return False

        # Validate right relationship with parent
        if not (lowest < curr.val < highest):
            return False

        return self.validate(curr.left, curr, seen, lowest, curr.val) and self.validate(curr.right, curr, seen, curr.val, highest)

    def isValidBST(self, root):
        return self.validate(root, None, set(), -float('inf'), float('inf'))
