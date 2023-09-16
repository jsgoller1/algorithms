# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
For y, going down is +1; root is 0.
For x, going left is -1, going right is +1. Root is 0.
Position is (y,x), which is (depth, combination of left and right relationships)

We want leftmost, followed by topmost
- We must visit every node at least once and produce ordering containing all: min O(N) space, O(N) time
- Within same columns, we must produce items in sorted order if we cannot find traversal, possibly nlogn

nlogn time and n space:
    - traverse entire tree; place nodes in default dict mapping depth -> (x, node val).
    - After tree is traversed, make a list of all lists in dict sorted from least to greatest by key, each of which is sorted
    - Could also just create list of tuples (y, x, val); sorted() should be stable and do tiebreaking correctly

can we do it in O(n) time and space? nlogn 
"""
from collections import defaultdict


class Solution:
    def _nlogn(self, root: Optional[TreeNode]) -> List[List[int]]:
        nodes = defaultdict(list)

        def traverse(node: TreeNode, y: int, x: int):
            if not node:
                return
            nodes[x].append((y, node.val))
            traverse(node.left, y+1, x-1)
            traverse(node.right, y+1, x+1)

        traverse(root, 0, 0)
        ret = []
        i = min(nodes)
        while i in nodes:
            ret.append([pair[1] for pair in sorted(nodes[i])])
            i += 1
        return ret

    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        return self._nlogn(root)
