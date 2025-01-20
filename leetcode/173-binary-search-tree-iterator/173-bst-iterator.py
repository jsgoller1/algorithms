class BSTIterator:
    def _leftSideExplore(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def __init__(self, root: Optional[TreeNode]):
        # Node in stack means we've already fully explored
        # its left subtree
        self.stack = []
        self._leftSideExplore(root)

    def next(self) -> int:
        node = self.stack.pop()
        ret = node.val
        self._leftSideExplore(node.right)
        return ret

    def hasNext(self) -> bool:
        return len(self.stack) > 0
