# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque, namedtuple

Node = namedtuple("Node", ["val", "left", "right", "y", "x"])


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ordering = {}
        q = deque([Node(root.val, root.left, root.right, 0, 0)])
        while q:
            val, left, right, y, x = q.popleft()
            if x not in ordering:
                ordering[x] = {}
            if y not in ordering[x]:
                ordering[x][y] = []
            ordering[x][y].append(val)

            if left:
                q.append(Node(left.val, left.left, left.right, y+1, x-1))
            if right:
                q.append(Node(right.val, right.left, right.right, y+1, x+1))

        nodes = []
        for col, depths in sorted(ordering.items()):
            row = []
            for node_list in depths.values():
                row += node_list
            nodes.append(row)
        return nodes
