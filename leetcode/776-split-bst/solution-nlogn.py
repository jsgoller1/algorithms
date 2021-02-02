from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(root, new_node):
    if not root:
        return new_node
    if new_node.val <= root.val:
        root.left = insert(root.left, new_node)
    else:
        root.right = insert(root.right, new_node)
    return root


class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        self.ans = [None, None]

        def preorder(root, V):
            if not root:
                return
            new_node = TreeNode(root.val)
            if root.val <= V:
                self.ans[0] = insert(self.ans[0], new_node)
            else:
                self.ans[1] = insert(self.ans[1], new_node)
            preorder(root.left, V)
            preorder(root.right, V)

        preorder(root, V)
        return self.ans
