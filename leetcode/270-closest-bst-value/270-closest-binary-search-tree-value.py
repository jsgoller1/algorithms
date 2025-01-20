# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = root.val
        while root:
            best_diff = abs(target - best)
            curr_diff = abs(target - root.val)
            if best_diff == curr_diff:
                best = min(best, root.val)
            else:
                best = root.val if curr_diff < best_diff else best

            root = root.left if target < root.val else root.right

        return best
