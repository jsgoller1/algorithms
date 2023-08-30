from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:
    def recurse(node, remaining):
        if not node:
            return False

        remaining -= node.data
        if not node.left and not node.right:
            return remaining == 0
        return recurse(node.left, remaining) or recurse(node.right, remaining)

    return recurse(tree, remaining_weight)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
