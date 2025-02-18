""" 
Recursive solution should work here: 
Base cases: single node (0), single node with one child (1), single node with 2 children (2)

Best we've seen is max(best, left height + right height) at every node 

Return deepest path at each node; 

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def recurse(node):
            if not node: 
                return 0, 0 
            
            left_best, left_deepest = recurse(node.left)
            right_best, right_deepest = recurse(node.right)

            best = max(left_best, right_best, left_deepest + right_deepest)
            deepest = max(left_deepest, right_deepest) + 1 
            return best, deepest 

        return recurse(root)[0]
        