# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.subtrees = set()
        self.known_duplicates = set()
        self.duplicate_nodes = set()

        def dfs(node):
            if not node:
                return ""
            sig = f"{node.val},{dfs(node.left)},{dfs(node.right)}"
            if sig not in self.subtrees:
                self.subtrees.add(sig)
            elif sig not in self.known_duplicates:
                self.known_duplicates.add(sig)
                self.duplicate_nodes.add(node)
            return sig
        dfs(root)
        return list(self.duplicate_nodes)
