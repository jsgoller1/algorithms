import functools
from typing import Optional

from binary_tree_with_parent_prototype import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Get depth of each node by tracing to root. Then advance the longer to meet the shorter's depth,
then go one by one until they reach the first common node, which is LCA.
"""


def get_depth(node):
    depth = -1
    while node is not None:
        node = node.parent
        depth += 1
    return depth


def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    n0_depth, n1_depth = get_depth(node0),  get_depth(node1)
    if n0_depth != n1_depth:
        node0, node1 = (node0, node1) if n0_depth > n1_depth else (node1, node0)
        n0_depth, n1_depth = (n0_depth, n1_depth) if n0_depth > n1_depth else (n1_depth, n0_depth)
        while n0_depth > n1_depth:
            node0 = node0.parent
            n0_depth -= 1

    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0


@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_with_parent.py',
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))
