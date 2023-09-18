# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # get parents for each
        stack = [root]
        parents = []
        p_parents = q_parents = None
        while stack and not (q_parents and p_parents):
            curr = stack.pop()
            while parents and curr is not parents[-1].left and curr is not parents[-1].right:
                parents.pop()

            parents.append(curr)
            if curr == p:
                p_parents = [node for node in parents]
            if curr == q:
                q_parents = [node for node in parents]

            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

            # TODO: figure out how to pop correctly to maintain parent stack

        # find common
        lca = root
        i = j = 0
        print([node.val for node in p_parents])
        print([node.val for node in q_parents])

        while i < len(p_parents) and j < len(q_parents) and p_parents[i] is q_parents[j]:
            lca = p_parents[i]
            i += 1
            j += 1
        return lca
