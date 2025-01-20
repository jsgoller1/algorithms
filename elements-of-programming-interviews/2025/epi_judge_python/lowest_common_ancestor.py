import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Node is LCA when:
- isn't node1 or node2, and it has node1 and node2 in separate subtrees 
- is node1 or node2 and has the other in either subtree 

Assume tree contains both node1 and node0
"""

from collections import namedtuple

ContainsNodes = namedtuple('ContainsNodes', ['has_0', 'has_1'])

def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    lowest = None
    def find_lowest(node) -> ContainsNodes:
        if not node: 
            return ContainsNodes(False, False)
        left_tree = find_lowest(node.left)
        right_tree = find_lowest(node.right)
        has_0 = (node == node0) or left_tree.has_0 or right_tree.has_0
        has_1 = (node == node1) or left_tree.has_1 or right_tree.has_1
        nonlocal lowest
        if not lowest:
            lowest = node if has_0 and has_1 else None
        return ContainsNodes(has_0, has_1)
    find_lowest(tree)
    return lowest


@enable_executor_hook
def lca_wrapper(executor, tree, key1, key2):
    strip_parent_link(tree)
    result = executor.run(
        functools.partial(lca, tree, must_find_node(tree, key1),
                          must_find_node(tree, key2)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
