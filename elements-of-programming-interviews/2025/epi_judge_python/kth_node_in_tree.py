import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from test_framework.binary_tree_utils import draw_tree
"""
.size = number of nodes in tree rooted here (inc current node)
.size - .left.size = number of nodes in right subtree (.size if no left)

because in-order, choosing this node means we've traversed all nodes in the left subtree
suppose we keep a running count of nodes we've included, and traverse the tree. At each node:
- if we go right, we add node.left.size + 1 to our count. 
- if we choose this node, we add node.left.size + 1 to our count. 
- if we go left, we don't add anything to our count. 

So starting at the root:
- init running total to 1. 
- look at each child's size (or 0 if no child)
- if total + left.size + 1 = k, we found our node. 
- if less, go right and add left.size + 1 to total
- if more, go left. 
"""



class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size

def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    def traverse(node, total):
        if not node:
            return None 
        left_size = node.left.size if node.left else 0 
        if total + left_size + 1 == k:
            return node 
        elif total + left_size + 1 < k:
            return traverse(node.right, total + left_size + 1)
        else:
            return traverse(node.left, total)
    return traverse(tree, 0)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
