import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook

"""
Most straightforward way is just pre-order traverse until we reach the node and get the one after
But:
- if we have a right child, proceed with in-order traversal from ourselves
- if we have no right child, go to the parent. 
  - if we were the left child, parent is next. 
  - if we were the right child, traverse until we're not. 
- if we have no parent or right child, we are the root and the last node in the tree. 

cases:
- empty tree 
- one node tree
- left/right biased tree 
"""

def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if not node and (node.right or node.parent):
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


@enable_executor_hook
def find_successor_wrapper(executor, tree, node_idx):
    node = must_find_node(tree, node_idx)

    result = executor.run(functools.partial(find_successor, node))

    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('successor_in_tree.py',
                                       'successor_in_tree.tsv',
                                       find_successor_wrapper))
