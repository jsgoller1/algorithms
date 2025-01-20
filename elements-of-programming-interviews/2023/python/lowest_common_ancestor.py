import functools
from typing import Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node, strip_parent_link
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def get_path(root, node, path):
    if not root:
        return False
    path.append(root)
    if root == node:
        return True

    if root.left:
        if get_path(root.left, node, path):
            return True
    if root.right:
        if get_path(root.right, node, path):
            return True
    path.pop()
    return False


def lca_Oh_space(tree: BinaryTreeNode, node0: BinaryTreeNode,
                 node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    node0_path = []
    get_path(tree, node0, node0_path)
    node1_path = []
    get_path(tree, node1, node1_path)

    solution = tree
    for n0, n1 in zip(node0_path, node1_path):
        if n0 is n1:
            solution = n0
        else:
            break

    return solution


def lca(tree: BinaryTreeNode, node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
    best_lca = tree
    best_lca_distance = 0

    def nodes_in_tree(root, depth):
        if not root:
            return False, False

        node0_left, node1_left = nodes_in_tree(root.left, depth+1)
        node0_right, node1_right = nodes_in_tree(root.right, depth+1)

        node0_exists = (root is node0) or node0_left or node0_right
        node1_exists = (root is node1) or node1_left or node1_right

        nonlocal best_lca_distance
        nonlocal best_lca
        if (node0_exists and node1_exists) and best_lca_distance < depth:
            best_lca_distance = depth
            best_lca = root

        return node0_exists, node1_exists

    node0_exists, node1_exists = nodes_in_tree(tree, 0)

    return best_lca if (node0_exists and node1_exists) else None


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
