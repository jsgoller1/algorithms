import collections
import math

"""
Statement - https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

----
Understand

In this problem, we are given a binary tree node, and told to find the minimum distance from the root to a leaf node (a node with no children). We do _not_ need to look at every node - just enough to find the minimum distance to a leaf. To do this, we should
look at each node on a given level, and test if they are leaves. We can accomplish this with a BFS. However, we need to keep track of the height as we do this, so we will need some way of saying "this node is at height h and it is a leaf, return h."

As we consider how to keep track of height, we have to consider:
- the tree may not be fully populated at each level
- we cannot access the parent node from a child

----
Plan

On my first approach of this problem, I misunderstood the implications of trees who had nodes with only one child. If every node in a tree is either a leaf or a parent of two child nodes, we could find the min height by BFSing the tree using a queue, and keeping track of how many nodes we have processed (initialized to 0) as we look for a leaf. When we find the first leaf, we return math.floor(math.log(node_number,2))+1.

However, this doesn't work for some cases - for instance, a tree of 5 nodes where each non-leaf node has one left child and no right child

Here is a different approach:

- Start with a queue containing the root, and a dictionary with the root mapped to 1.
- dequeue a node as current
- If current has children:
  - map the children to the current's depth + 1 in the dict.
  - enqueue the children
- If current is a leaf, return its value in the dict

----

Execute

See below.
----
Review

When I initially solved this problem, it became clear pretty quickly that math.floor(math.log(node_number,2))+1 would work for the height, but I couldn't figure out (and am still not perfectly sure) why. Even so, my approach didn't work for trees that weren't fully populated.

My current approach of mapping nodes to heights works - I think it's _probably_ ok to assume that the string representation is unique, since it maps to an address. I am wondering if there is a way to keep track of the current depth on each iteration of the loop without having to look it up each time, but at this point I do not think there is.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def is_leaf(node):
    return not (node.left or node.right)


class Solution:
    def minDepth(self, root):
        if root == None:
            return 0

        depths = {str(root): 1}
        q = collections.deque([root])
        while q:
            current = q.popleft()
            depth = depths[str(current)]
            if is_leaf(current):
                break
            else:
                if current.left:
                    depths[str(current.left)] = depth+1
                    q.append(current.left)
                if current.right:
                    depths[str(current.right)] = depth+1
                    q.append(current.right)

        return depth
