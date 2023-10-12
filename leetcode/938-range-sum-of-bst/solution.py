# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def getSum(node: TreeNode):
            if not node:
                return 0
            total = node.val if (low <= node.val <= high) else 0
            if low < node.val:
                total += getSum(node.left)
            if node.val < high:
                total += getSum(node.right)
            return total

        return getSum(root)
