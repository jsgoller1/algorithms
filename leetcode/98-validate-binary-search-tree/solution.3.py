class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def recurse(node, lo, hi):
            if not (node.left or node.right):
                return lo < node.val < hi

            # valid_data = isinstance(node.data, int)
            curr = lo < node.val < hi
            left = recurse(node.left, lo, node.val) if node.left else True
            right = recurse(node.right, node.val, hi) if node.right else True
            return curr and left and right

        return recurse(root, -float('inf'), float('inf'))
