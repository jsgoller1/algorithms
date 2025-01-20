# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minVal, maxVal):
            valid = True
            if node.left:
                valid &= minVal < node.left.val < node.val
                valid &= isValid(node.left, minVal, node.val)
            if node.right:
                valid &= node.val < node.right.val < maxVal
                valid &= isValid(node.right, node.val, maxVal)
            return valid
        return isValid(root, -float('inf'), float('inf'))
