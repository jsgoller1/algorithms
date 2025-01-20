# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
At each node, we have the following options, ordered from best to worst:
    - if root and left and right all agree, we can join them. 
    - if root agrees with left or with right, we can join them. 
    - if root doesn't agree with left or right, the best is 1 (just the root) or the best seen so far in the subtrees

- keep running max. 
- return the following: if you join this node to the parent with the left subtree, produces walk of length x (and the same for y)

"""
class Solution:
    def recurse(self, node):
        if not node:
            return 0,0
        left_max, left_extend = self.recurse(node.left)
        right_max, right_extend = self.recurse(node.right)
        left_extend = left_extend + 1 if node.left and node.left.val == node.val else 0 
        right_extend = right_extend + 1 if node.right and node.right.val == node.val else 0 
        return max(left_max, right_max, left_extend + right_extend), max(left_extend, right_extend)

    def longestUnivaluePath(self, root):
        return self.recurse(root)[0] if root else 0 


class SolutionStillComplex:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 

        def recurse(node):
            if not node:
                return 0, 0 
            
            left_max, left_extend = recurse(node.left) 
            right_max, right_extend = recurse(node.right)

            left_match = node.left and node.left.val == node.val
            right_match = node.right and node.right.val == node.val

            node_max = max(left_max, right_max, 1)
            extension = 1
            if left_match and right_match:
                joined = left_extend + right_extend + 1 
                node_max = max(node_max, joined)
                extension = max(left_extend+1, right_extend+1)
            elif left_match:
                extension = left_extend+1
                node_max = max(node_max, extension)
            elif right_match:
                extension = right_extend+1
                node_max = max(node_max, extension)
            return node_max, extension

        best, _ = recurse(root)
        return best-1

class SolutionComplex:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if not node:
                return 0, 0 
            left_subtree_max, use_left = recurse(node.left)
            right_subtree_max, use_right = recurse(node.right)

            choose_left = use_left + 1 if (node.left and node.left.val) == node.val else 1
            choose_right = use_right + 1 if (node.right and node.right.val) == node.val else 1

            joined = 0 
            if node.right and node.left and node.right.val == node.left.val == node.val:
                joined = use_left + use_right + 1
            
            return max(joined, left_subtree_max, right_subtree_max, choose_left, choose_right), max(choose_left, choose_right)

        best, _ = recurse(root)
        return best-1 if root else 0