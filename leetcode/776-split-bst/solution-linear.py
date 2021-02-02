from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:
            return [None, None]
        if V >= root.val:
            left = root
            sub_left, right = self.splitBST(root.right, V)
            left.right = sub_left
        else:
            right = root
            left, sub_right = self.splitBST(root.left, V)
            right.left = sub_right
        return [left, right]
