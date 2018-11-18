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
- while finding, keep a dict of how we got to a node from
a node
- once we find both nodes, walk both backwards, adding nodes
to a set. we can walk p or q backwards totally first, but the first node we try
to add the set that is already present is our LCA.

---pseudocode--
bfs(tree, parents, node):
  q = queue(root)
  while q:
    curr = q.pop()
    if curr == target:
      return
    for child in curr.children: # no cycles, so don't need to check if already visited
      parents[child] = curr

main(tree, p, q):
  parents = {root: none}
  bfs(tree, parents, p)
  bfs(tree, parents, q)
  uncommon = set()

  currP = p
  currQ = q
  while currP != currQ != null:
    if currP in uncommon:
      return currP
    else:
      uncommon.add(currP)
      currP = parents[currP]
    if currQ in uncommon:
      return currQ
    else:
      uncommon.add(currQ)
      currQ = parents[currQ]
"""
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeInsert(root, new):
    if new.val < root.val:
        if root.left == None:
            root.left = new
        else:
            treeInsert(root.left, new)
    if new.val > root.val:
        if root.right == None:
            root.right = new
        else:
            treeInsert(root.right, new)


def treeFind(root, val):
    if root.val == val:
        return root
    if val < root.val:
        if root.left:
            return treeFind(root.left, val)
    if val > root.val:
        if root.right:
            return treeFind(root.right, val)


def treeConstruct():
    root = TreeNode(50)
    vals = [75, 25, 15, 30, 100, 65]
    for val in vals:
        treeInsert(root, TreeNode(val))
    return root


class Solution(object):
    def bfs(self, root, node, parents):
        q = collections.deque([root])
        while q:
            curr = q.pop()
            if curr == node:
                return node
            else:
                if curr.left:
                    parents[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                    parents[curr.right] = curr

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parents = {root: None}
        self.bfs(root, p, parents)
        self.bfs(root, q, parents)

        uncommon = set()
        currP = p
        currQ = q
        while currP != None:
            uncommon.add(currP)
            currP = parents[currP]

        while currQ != None:
            if currQ in uncommon:
                return currQ
            else:
                currQ = parents[currQ]

        return None


if __name__ == '__main__':
    s = Solution()
    t = treeConstruct()
    lca = s.lowestCommonAncestor(t, treeFind(t, 65), treeFind(t, 100))
    assert lca == treeFind(t, 75)
    assert s.lowestCommonAncestor(t, treeFind(
        t, 50), treeFind(t, 65)) == treeFind(t, 50)
