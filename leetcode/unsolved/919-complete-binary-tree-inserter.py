"""
This problem was one of the questions for LC Weekly contest #105
--------------------
- Normal tree insertion just involves traversal to the right point and then inserting
- Complete means that every level except the last is completely full, and nodes are
shifted as far left as possible

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class CBTInserter:
    def __init__(self, root):
        """
        :type root: TreeNode
        """

    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """

    def get_root(self):
        """
        :rtype: TreeNode
        """
