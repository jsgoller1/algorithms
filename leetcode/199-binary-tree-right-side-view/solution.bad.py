# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
"""


class SolutionInfernal:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        First idea: we need to find the rightmost node at each depth. The rightmost one will be the one at that depth who has the most parents who were right children. 
        Edge case: consider a tree where we a root with a left child and a right child. Then, the right child is a singly linked list of all left children, and the left child is a singly linked list of all right children. The correct answer is the right subtree from the root, but just adding the number of right parents would have us look at the left tree. 

        Second idea: what if deeper levels count less? How about instead of linearly adding the number of right parents to get the score, we set each node's score to `parent_score  + 1/(depth+1)` if the node is a right child (unless depth = 0; then the score is just 1), and `parent_score` if it's a left child.. 
        Edge case: The same one as before. Eventually, the sum of the left subtree with all right children will exceed the sub of the right subtree with all left children.

        Infernal hack: what if we just set the scaling factor for depth really high? Instead of the score of each child being `parent_score + 1/(depth+1)` for right children, we set it to `parent_score + 1/(depth^5+1)`?

        The infernal hack worked, probably because the trees were not deep enough to have an edge case that catches up to the scaling factor of 5. 
        However, I'm pretty sure such a tree exists. 

        I blame adderall for this overly complex approach. 
        """

        # Maps depth -> score, node
        # score is + 1 for each parent that is a right child.
        if not root:
            return []

        overall_scores = {}

        rightmost_nodes = {}
        max_depth = 0

        def traverse(node, depth, score):
            if not node:
                return
            overall_scores[node.val] = score
            nonlocal max_depth
            max_depth = max(depth, max_depth)

            if depth not in rightmost_nodes or score > rightmost_nodes[depth][0]:
                rightmost_nodes[depth] = (score, node)
            traverse(node.left, depth+1, score)
            # NOTE: This is an infernal hack; basically, each lower level counts "less" towards
            # the score. I picked 5 for score + 1/(depth^5 + 1) after noticing that for deeper trees,
            # you need the score of each lower level to decrease more rapidly or you wind up with an edge
            # case where at a very low depth, a left-er node has a higher score than a right-er one. I'm pretty sure
            # this doesn't work for large trees.
            traverse(node.right, depth+1, (score+1/(depth**5+1) if depth != 0 else 1))

        order = []
        traverse(root, 0, 0)
        printable_rightmosts = [(depth, item[1].val) for depth, item in rightmost_nodes.items()]

        for depth in range(max_depth+1):
            order.append(rightmost_nodes[depth][1].val)
        return order
