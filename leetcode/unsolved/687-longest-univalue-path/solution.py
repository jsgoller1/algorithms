"""

cases (for any tree):
Longest path involves root (so it's in both subtrees):
    1
   / \
  1   1
 /\   /\
1  2 2  1
Longest path is entirely inside one subtree:
    3
   / \
  5   1
 /\   /\
1  2 2  1

    3
   / \
  5   1
 /\   /\
1  2 1  1

Some tough edge cases:
In this one, the longest path is at one point 1-1, but then further up
in the tree, we'll see that it's actually 0-0-0. This is tricky because
we could have a case where the longest path is way down a left subtree (say it's 5 nodes long),
but as we recurse back, the roots along the path we take eventually are longer than that. 
                 0
             /      \
           /          \
          0            0 
         /  \        /   \
        2    3      1     1
       /\    /\    /\    / \
      6  7  4  5  0  0  0   1
In this one, the longest path involves part of one subtree that itself doesn't contain any long path,
and another that does. At one point in recursion, we might think the longest path is in the rightmost
tree (1-1-1), but then as we return upwards, we'll see we actually need to discard the left portion of that
initial tree and instead consider the left leaf and root and right subtree for 1-1-1-1. 
                 0
             /      \
           /          \
          0            1 
         /  \        /   \
        2    3      1     1
       /\    /\    /\    / \
      6  7  4  5  0  0  1   1

Bottoum up recursive solution (not gonna work):
- longest path for a leaf node is 0 
- if the root node is not equal to either leaf, the longest path of the tree is whichever is found in its subtrees.
- if the root node is equal to single leaf, the longest path is either:
    - the longest path in the leaf rooted at that subtree, if the root of that tree isn't part of it
    - the longest path in the leaf rooted at that subtree, plus one. 
- if the root is equal to both its leaves, the longest path is:
    - the longest between the two subtrees if the leaves aren't part of that path
    - the sum of both longest plus 2 if only 
- if the root shares the value of a leaf, it could extend the path from the leaf's left or right subtree,
  so we need to know how long each is. We cannot have a 3-way path though.

Top-down recursive:
- longest path for a leaf node is 0 
- if root and leaf share value, longest is 1
- if root and both leaves share value, longest is 3. 
- Then dive into left/right subtrees with that knowledge; add longest path from parent
  if parent and root match

Preprocess, then DFS
- We can come up with a node class that includes parent pointers, and preprocess the tree into a different tree
- Then we can just DFS from each node in this new tree (caching can be used, but may not be needed since there's
  no cycles).
    - We can keep all nodes in this new tree in a set and remove them as we visit them. This way we mimick the
      same way we'd find a solution if the problem were in a grid. 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        pass
