class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        total = 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        return root.val + self.rangeSumBST(root.right, low, high) + self.rangeSumBST(root.left, low, high)


class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = root.val if (low <= root.val <= high) else 0
        if root.left:
            total += self.rangeSumBST(root.left, low, high)
        if root.right:
            total += self.rangeSumBST(root.right, low, high)
        return total
