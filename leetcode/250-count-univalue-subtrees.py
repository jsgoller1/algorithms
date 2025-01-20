# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
A subtree of treeName is a tree consisting of a node in treeName and all of its descendants.
- assumption: root is in the tree, so we can count it 

- a single node has 1 subtree (itself), so count it as 1
- if we ever have a mismatch between a parent and its left or right children, that breaks the tree, 

if not node:
    return 0, True

left_subtrees, unbroken_left = recurse(node.left)
right_subtrees, unbroken_right = recurse(node.right)

left_match = (node.left.val == node.val) if node.left else True
right_match = (node.right.val == node.val) if node.right else True

if (left_match and unbroken_left) and (right_match and unbroken_right):
    return left_subtrees + right_subtrees + 1, True 
return left_subtrees + right_subtrees, False 


"""
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if not node:
                return 0, True

            left_subtrees, unbroken_left = recurse(node.left)
            right_subtrees, unbroken_right = recurse(node.right)

            left_match = (node.left.val == node.val) if node.left else True
            right_match = (node.right.val == node.val) if node.right else True

            if (left_match and unbroken_left) and (right_match and unbroken_right):
                return left_subtrees + right_subtrees + 1, True 
            return left_subtrees + right_subtrees, False
        return recurse(root)[0] 
