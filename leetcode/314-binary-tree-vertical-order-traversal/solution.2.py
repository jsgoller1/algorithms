class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ordering = {}
        q = deque([(root, 0)])
        while q:
            curr, x = q.popleft()
            if x not in ordering:
                ordering[x] = []
            ordering[x].append(curr.val)

            if curr.left:
                q.append((curr.left, x-1))
            if curr.right:
                q.append((curr.right, x+1))

        nodes = []
        for _, col in sorted(ordering.items()):
            nodes.append(col)
        return nodes
