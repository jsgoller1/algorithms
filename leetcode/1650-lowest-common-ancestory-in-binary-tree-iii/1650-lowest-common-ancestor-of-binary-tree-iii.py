"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

globally:
    Keep track of current best CA and its depth

At each node:
    if the current node is an ancestor of both, compare to best and replace
        can return, don't need to dive deeper if we already found both 
    if we don't know yet, check the left and right subtrees:
        if current node is p or q, set found to true 

"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        def getAncestors(node):
            ancestors = []
            while node:
                ancestors.append(node)
                node = node.parent
            return ancestors[::-1]

        pAns = getAncestors(p)
        qAns = getAncestors(q)

        lca = pAns[0]
        for p, q in zip(pAns, qAns):
            if p != q:
                break
            lca = p
        return lca
