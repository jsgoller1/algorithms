import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, binary_tree_height
from test_framework.test_utils import enable_executor_hook


"""
Inorder is LNR
The given node is either:
    - left child
    - root of whole tree
    - right child

And has:
    - left child
    - right child
    - both
    - neither 

Successor means "we just printed this node; which do we print next?"

cases:
    we have no parent, we are root:
        we have a right child, successor is right child's leftmost element. 
        we have no right child. We have no successor.
    we have parent, we're left child:
        we have a right child; successor is right child's leftmost element. 
        else, parent is successor. 
    we have parent, we're right child
        we have a right child; successor is right child's leftmost element. 
        we have no right child, successor is first ancestor who spun off a left child, or none (because we're last)     


"""


def get_root(node):
    while node.parent:
        node = node.parent
    return node


def display(node, child_type=None, margin=0):
    if not margin:
        print("")
    print(f"{' '*margin}|{child_type if child_type else 'root:'} {node.data}")
    if node.left:
        display(node.left, 'L', margin+2)
    if node.right:
        display(node.right, 'R', margin+2)


def find_successor(node: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    if node and node.right:
        node = node.right
        while node.left:
            node = node.left
        return node
    elif node and node.parent:
        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent


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
