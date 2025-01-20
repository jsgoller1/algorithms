import functools
from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from test_framework.binary_tree_utils import draw_tree

"""
Multiple passes:
- get leaves
- get first node in preorder and reverse preorder, then traverse each back to parent (actually no parent node)

Need recursive test for an "exterior node"
- is leaf: no children
- if we ever move "into" the tree, that is we take a right from a left edge or a left from a right edge
    - maybe we want a "biasing" parameter? 

cases:
- single node, left bias and right biased trees: all nodes
- complete tree: all leftmost, rightmost, and leaf nodes
- incomplete tree: leftside view, rightside view, and leaves
    - hang on, what about a level order traversal with minimal and maximal nodes at each level, plus leaves? 
"""
from collections import defaultdict, deque

def get_leaves(tree):
    ret = []
    def recurse(node):
        if not node:
            return 
        if not (node.left or node.right):
            ret.append(node)
        recurse(node.left)
        recurse(node.right)
    recurse(tree)
    return [node for node in ret if node != tree]

def get_left_side(tree):
    ret = []
    def recurse(node):
        if not node:
            return 
        if node.right or node.left:
            ret.append(node)
        if node.left:
            recurse(node.left)
        else:
            recurse(node.right)
    recurse(tree)
    return ret

def get_right_side(tree):
    ret = []
    def recurse(node):
        if not node:
            return 
        if node.right or node.left:
            ret.append(node)
        if node.right:
            recurse(node.right)
        else:
            recurse(node.left)
    recurse(tree)
    return ret

def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:
    if not tree:
        return []
    left_side = get_left_side(tree)[1:] if tree.left else []
    right_side = get_right_side(tree)[1:][::-1] if tree.right else []
    return [tree] + left_side + get_leaves(tree) + right_side


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_exterior.py', 'tree_exterior.tsv',
                                       create_output_list_wrapper))
