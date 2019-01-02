"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
---------------
In: TreeNode
Out: list[list[int]]

- A normal level-order traversal can be done with a BFS
- A less-complicated option here is to do the BFS, generate
the normal level-order traversal, and then just reverse the odd number
lists; this will still be O(n) for n nodes in the tree though it may TLE.
- With the approach outlined below, we can also just append left or right
depending on the level number instead of reversing, but converting this to
a vanilla list will take time, as will dumping the list each time with a + operation
to use correct ordering
- Will go with reversal strategy first
-------------------------------------
zigzag(root):
  solution = []
  q = queue initialized with (0,root)
  while q:
    level, curr = q.pop()
    for child in curr.children:
      if solution doesn't have a list for level+1:
        append a list to solution
      else:
        solution[level].append((level+1,child))
  for level_no, level in solution:
    if level_no is even:
      level.reverse()
"""
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        traversal = collections.defaultdict(list)
        q = collections.deque([(0, root)])
        while q:
            level, curr = q.popleft()
            traversal[level].append(curr.val)
            if curr.left:
                q.append((level+1, curr.left))
            if curr.right:
                q.append((level + 1, curr.right))

        return [traversal[level] if level % 2 == 0 else [item for item in reversed(traversal[level])] for level in traversal]


def constructFixedTree():
    """
    Create a binary tree [3,9,20,null,null,15,7],
      3
     / \
    9  20
      /  \
     15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


if __name__ == '__main__':
    s = Solution()
    root = constructFixedTree()
    assert s.zigzagLevelOrder(root) == [[3], [20, 9], [15, 7]]
    assert s.zigzagLevelOrder(None) == []
