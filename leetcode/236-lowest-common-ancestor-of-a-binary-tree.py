"""
Given a binary tree, find the lowest common ancestor (LCA)
of two given nodes in the tree. According to the definition of
LCA on Wikipedia: “The lowest common ancestor is defined between
two nodes p and q as the lowest node in T that has both p and q
 as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:
root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself
             according to the LCA definition.
Note:
- All of the nodes' values will be unique.
- p and q are different and both values will exist in the binary tree.
-------------------------------------------------------------------------
Input: TreeNode (root of tree), TreeNode (p), TreeNode (q)
Ouput: TreeNote (LCA)

Constraints:
  - P != Q != root
  - P and Q are always in the tree

- We can find both P and Q with a
DFS
- We cannot assume the BT is a BST; finding a node is O(n), but
the algorithm itself could be O(log(n)) if it were a search tree
- We can keep track of the parents of P and Q using a child->parent
dict
- Once we know the path from root to p and to q, we can walk these forward
from the root, and return the last common node before they diverge

-----------------------------------------------------------
- use BFS to find both nodes
- while finding, keep a dict of
pseudocode
"""
