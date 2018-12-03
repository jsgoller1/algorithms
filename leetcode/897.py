"""
Contest 100 problem
---------
In: TreeNode
Out: TreeNode, as LL

- Create a dummy head
- In-order walk the tree
- our "process()" function takes the node and sets it to the right of head
- return head->next

- Cases: empty tree, unbalanced / LL tree
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def createTree():
  head = TreeNode(1)
  head.left = TreeNode(2)
  head.right = TreeNode(3)
  head.left.left = TreeNode(4)
  head.left.right = TreeNode(6)
  head.right.left = TreeNode(7)
  head.right.right = TreeNode(8)
  return head

def walkRight(node):
  while node:
    print(node.val)
    node = node.right

class Solution(object):
    def inOrder(self, root):
      if root:
        self.inOrder(root.left)
        self.curr.right = root
        self.curr = self.curr.right
        self.curr.left = None
        self.inOrder(root.right)

    def increasingBST(self, root):
      self.newRoot = TreeNode("derp")
      self.curr = self.newRoot
      self.inOrder(root)
      return self.newRoot.right

if __name__ == '__main__':
  s = Solution()
  n = createTree()
  nn = s.increasingBST(n)
  walkRight(nn)
