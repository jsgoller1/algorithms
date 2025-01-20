from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
def inorder(node):
    if not node:
        return 
    inorder(node.left)  # push curr node, set curr to curr.left
                        # implicit pop 
    process(node)       # add to array 
    inorder(node.right) # don't need to push curr node, just need to set to node.right

on a given node: 
  - push it onto the stack if it has a left child, go to left
  - if it has no left child, append it to array,
  - if it has no right child, next node is popped from stack 
"""

def inorder_recursive(root):
    out = []
    def inorder(node):
        if not node:
            return 
        inorder(node.left)  # push curr node, set curr to curr.left
                            # implicit pop 
        out.append(node.data)       # add to array 
        inorder(node.right) # don't need to push curr node, just need to set to node.right
    inorder(root)
    return out

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    if not tree:
        return []
    stack, out = [tree], []
    tree = tree.left
    while stack or tree: 
        if not tree:
            tree = stack.pop()
            out.append(tree.data)
            tree = tree.right
        else:
            stack.append(tree)
            tree = tree.left 
    return out 

tn = {i: BinaryTreeNode(i) for i in range(1,8)}
tn[1].left, tn[1].right = tn[2], tn[3]
tn[2].left, tn[2].right = tn[4], tn[5]
tn[3].left, tn[3].right = tn[6], tn[7]

expected = inorder_recursive(tn[1])
actual = inorder_traversal(tn[1])
assert actual == expected, f"{actual} != {expected}"

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
