# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    """
    if empty, go to parent and process, then go to its right
    otherwise go left
    ----
    parents = [root]
    curr = root.left
    while parents:
        if curr:
            parents.push(curr)
            curr = curr.left
        else: 
            curr = parents.pop()
            process(curr)
            curr = curr.right
    """

    def __init__(self, root: Optional[TreeNode]):
        self.val = -float("inf")
        self.curr = root.left if root else None
        self.parents = [root] if root else []

    def next(self) -> int:
        if not self.parents:
            return None

        while self.curr:
            self.parents.append(self.curr.left)

        self.curr = self.parents.pop()
        ret = self.curr.val
        self.curr = self.curr.right
        return ret

    def hasNext(self) -> bool:
        return len(self.parents) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
