"""
Given the root of a binary tree, return all duplicate subtrees. For each kind of duplicate
subtrees, you only need to return the root node of any one of them. Two trees are duplicate
if they have the same structure with the same node values.

(Examples given on page; they use a custom Treenode type)

Constraints 
    - between 1 and 10000 nodes
    - Node values will be between -200 and 200
------------
I failed this question during an interviewing.io mock interview. I wasn't able to
figure out the correct way to solve it without help; probably just need more practice with binary trees.

One critical mistake I made was understanding what "subtree" means; I need to be more careful about
fully understanding a problem's statement (even before thinking about how to solve it). A subtree
here is when from a given node down, the entire child structure has been replicated somewhere else 
in the tree. Examples:
    1
   / \
  4   4
4 (with no children) is a trivial subtree occurring twice.

      1
     / \
    2   3
   /   /  \
  4   2    4
     /
    4
4 occurs 3 times as a trivial subtree, and "2 with 4 as only left child" occurs twice.

      1
     / \
    2   3
   /   /  \
  4   2    4
     / \
    4   5

Here, only "4" is a recurring subtree; by adding the new node, the original other subtree is now no
longer duplicated (only one has a 5 right child from 2).
-----------------------------------------------------------------------------------------------------
An important insight here is that for any two nodes, they can only have equal subtrees if their values
are the same, and their children's values are the same. We can leverage this in our solution. 

The solution I was able to come up with (via significant help from my interviewer) basically involves
DFSing the tree, and then keeping track of subtrees with a bottom-up serialization method allowing us
to easily cache previously seen subtrees. 
    - Start with two sets; one as the solution, and one for unique subtrees. 
    - Depth first search the tree; we want to visit each node's children before the node itself, 
      so this is a post-order walk (my interviewer mistakenly called it a pre-order walk)
    - At each step, if the node is a leaf, the subtree is "{val}##"; this represents that the node of that value has no children.
    - If the node isn't a leaf, the subtree is "{val}{dfs left subtree)}{(dfs right subtree)}"
    - If the subtree isn't in the unique subtree set, add it. If it is, it's a duplicate so add it to the solution
    - Return the solution as a list.

This solution will be O(N) for runtime complexity; we have to look at every node in the tree once. 
Leetcode says this approach is O(N^2), as at each of N nodes we wind up looking at at most N nodes in 
the subtree. I don't know if this is the lowest bound (since we definitely will not look at n-many nodes
at each step), but the approach above is technically O(N^2). Here's a more in-depth explanation I wasted 
several hours on justifying O(N^2) (though it was actually helpful since I needed to review properties of 
binary trees):

How much space is required to store every subtree of a binary tree?
- Any binary tree (complete or not) has one subtree for each node in the tree, as each of its nodes is a possible root of a subtree. 
- Any binary tree of height > 1 has at most 2^(h+1)-1 nodes. 
- In a complete binary tree of height h, there will be:
    - 1 subtree of size (2^h+1)-1 (the whole tree)
    - 2 subtrees of size (2^h)-1
    - 4 subtrees of size ((2^(h-1))-1)
    ...
    - 2^h subtrees of height 1 (all the leaf nodes)
- The above can be rewritten as: 
    - 2^0 subtrees of size (2^h+1)-1 
    - 2^1 subtrees of size (2^h)-1
    - 2^2 subtrees of size (2^(h-1))-1
    ...
    - 2^h subtrees of size 2^(h-h)-1
- So the total size of storing all subtrees is the summation from i=0 to i=h of (2^i * ((2^(h+1-i))-1). Not
sure how to explicitly calculate this. 
- After some playing with it on a whiteboard:
    - Both the number of subtrees and the size of the subtrees are bounded by 2^h
    - There are h terms in the summation
    - So h(2^h * 2^h) bounds the size of storing all subtrees. 
    - 2^h is approximately n
    - h(2^h * 2^h) = h((2^h)^2) = h(n^2) (approximately) which is O(n^2)


This question has a few differences requiring accounting for:
    - We don't want # symbols in the answer; we want lists of lists. 
        - We can use the same strategy with a delimiter character that we split on
------------------
Approach:
    Keep two sets: seen subtrees, duplicate subtrees
    DFS the tree (node, current_path)
        If node is none, return "#"
        path = "{current node},{dfs of left child},{dfs of right child}"
        if path not in seen, add it
        if path in seen, add to duplicates
        return path
    dfs(root, "")
    for each path in duplicates:
        split on commas, remove "#", and cast all vals to int
    return processed duplicates 

Mild goofup in the above - we just need to return the root, not the paths; modified
strategy to use a Counter to keep track of how many times we've seen a path. If it's 2,
(first time seeing a duplicate), add the root. 
"""
from collections import Counter
from typing import List, Union


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(node: Union[TreeNode, None], subtrees: Counter, duplicates: List) -> str:
    if not node:
        return "#"
    path = f"{node.val},{dfs(node.left, subtrees, duplicates)},{dfs(node.right, subtrees, duplicates)}"
    subtrees[path] += 1
    duplicates.append(node) if subtrees[path] == 2 else None
    return path


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        subtrees = Counter()
        solution = []
        dfs(root, subtrees, solution)
        return solution
