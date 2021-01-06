import random

class bst_node():
  def __init__(self, val=None):
    self.left = None
    self.right = None
    self.val = val

def insert(root, val):
  if root < val:
    if root.right:
      insert(root.right, val)
    else:
      root.right = bst_node(val)
  if root > val:
    if root.left:
      insert(root.left,val)
    else:
      root.left = bst_node(val)

def random(node_count):
  vals = [random.randint(-100,100) for i in range(node_count)]
  root = bst_node(val)
  for val in vals[1:]:
    insert(root, val)
  return root

def preorder_traversal(root, level=0):
  if root:
    level += 1
    print
    preorder_traversal(root.left)
    preorder_traversal(root.right)
