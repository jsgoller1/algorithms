class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, node: TreeNode, r_ancestor=None, l_ancestor=None) -> bool:
        return not node or \
            (not node.left or node.left.val < node.val) and \
            (not node.right or node.val < node.right.val) and \
            (not r_ancestor or r_ancestor < node.val) and \
            (not l_ancestor or node.val < l_ancestor) and \
            self.isValidBST(node.left, r_ancestor, node.val) and \
            self.isValidBST(node.right, node.val, l_ancestor)


class Solution:
    def isValidBST(self, node: TreeNode) -> bool:
        self.prev = -float('inf')

        def in_order(node):
            if not node:
                return True
            valid = in_order(node.left)
            valid &= self.prev < node.val
            self.prev = node.val
            valid &= in_order(node.right)
            return valid
        return in_order(node)
