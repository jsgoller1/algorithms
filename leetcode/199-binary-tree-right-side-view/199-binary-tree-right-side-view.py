# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Second attempt, from scratch
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        nodes = {}

        def postorder(node, depth):
            if not node:
                return
            postorder(node.left, depth+1)
            postorder(node.right, depth+1)
            nodes[depth] = node
        postorder(root, 0)
        return [node.val for _, node in sorted(nodes.items())]


class SolutionOld:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        candidates = {}  # y: (node.val, x)

        def traverse(node, y):
            if not node:
                return
            traverse(node.left, y+1)
            traverse(node.right, y+1)
            candidates[y] = node.val

        traverse(root, 0)
        return [val for key, val in sorted(candidates.items())]
