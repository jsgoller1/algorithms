"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        This one works by having the pointers switch paths so that if one was 
        further from the LCA than the other, we'll wind up with the pointers having
        switched places but then being equidistant from the LCA. I dislike how clever it is. 
        """
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1

    def lowestCommonAncestorFirst(self, p: 'Node', q: 'Node') -> 'Node':
        """
        This implements the common approach for finding the intersection point of two linked lists 
        (which is effectively what a path from node to parent is). 
        """
        def get_distance_to_root(node):
            distance = 0
            while node.parent:
                distance += 1
                node = node.parent
            return distance
        p_distance = get_distance_to_root(p)
        q_distance = get_distance_to_root(q)

        while p_distance != q_distance:
            if p_distance > q_distance:
                p = p.parent
                p_distance -= 1
            else:
                q = q.parent
                q_distance -= 1

        while p != q:
            p = p.parent
            q = q.parent
        return p
