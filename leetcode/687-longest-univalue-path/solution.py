# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def traverse(node):
            if not node:
                return 0

            left_path = traverse(node.left)
            right_path = traverse(node.right)
            nonlocal longest

            if (node.left and node.right) and (node.val == node.left.val == node.right.val):
                longest = max(left_path + right_path + 2, longest)
                return max(left_path, right_path) + 1
            elif node.left and node.val == node.left.val:
                longest = max(left_path+1, longest)
                return left_path + 1
            elif node.right and node.val == node.right.val:
                longest = max(right_path+1, longest)
                return right_path+1
            else:
                return 0

        traverse(root)
        return longest
