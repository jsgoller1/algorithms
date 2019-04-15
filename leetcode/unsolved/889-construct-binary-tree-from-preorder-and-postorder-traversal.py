"""
- In the pre-order, a node can only come after its parent
- In the post order, it can only come before its parent
- Create an array of nodes based on the values in the postorder
- Root is first in pre, last in post, skip it
- For each node from [1:]:
  - set its parent to the first thing in the preorder that comes to the right
  of it in the postorder
  - which child is it?
    - right if adjacent in postorder, left if adjacent in preorder
return pre[0]
"""

# Definition for a binary tree node.
    class TreeNode(object):
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None


class Solution(object):
    def satisfy(self, parentI, childI, pre, post):
        return pre.index(parent.val) < pre.index(child.val) and post.index(parent.val) > post.index(child.val)

    def constructFromPrePost(self, pre, post):
        nodes = [TreeNode(val) for val in pre]
        for childI in range(1, len(nodes)):
            for parentI in range(len(nodes)):
                if childI != parentI and self.satisfy(parentI, childI, pre, post):
                    if nodes[parentI-1] == parentI:
                        nodes[parentI].left = nodes[childI]
                    else:
                        nodes[parentI].right = nodes[childI]
        return nodes[0]
