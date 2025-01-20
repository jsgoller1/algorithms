from typing import List

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import draw_tree

def inorder_recursive(tree):
    out = []
    def recurse(node):
        if not node: 
            return 
        recurse(node.left)    # push current onto stack, curr = curr.left 
                              # implicit pop 
        out.append(node.data) # now curr is popped item 
        recurse(node.right)   # then curr becomes curr.right, no repushing 
    recurse(tree)
    return out

def get_successor(node):
    if not node and (node.parent or node.right):
        return None 
    if node.right: 
        node = node.right
        while node.left:
            node = node.left 
    else:
        while node.parent and node == node.parent.right:
            node = node.parent 
        node = node.parent  
    return node

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:
    out = []
    if not tree:
        return out 
    node = tree
    while node.left:
        node = node.left 
    while node:
        out.append(node.data)
        node = get_successor(node)
    return out 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_with_parent_inorder.py',
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
