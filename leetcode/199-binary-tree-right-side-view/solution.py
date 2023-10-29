# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    """
    This is the obvious solution that I missed (thanks Adderall). Just do a level-order traversal / BFS

    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = []
        q = deque([(root, 0)])
        while q:
            curr, depth = q.popleft()
            if len(nodes) < depth+1:
                nodes.append(curr.val)
            else:
                nodes[depth] = curr.val
            if curr.left:
                q.append((curr.left, depth+1))
            if curr.right:
                q.append((curr.right, depth+1))
        return nodes
