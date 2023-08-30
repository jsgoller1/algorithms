from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

N = BinaryTreeNode


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    if not tree:
        return 0
    total = 0

    def recurse(node, rsum):
        rsum *= 2
        rsum += node.data
        if node.left == node.right == None:
            nonlocal total
            total += rsum
            return

        if node.left:
            recurse(node.left, rsum)
        if node.right:
            recurse(node.right, rsum)

    recurse(tree, 0)
    return total


if __name__ == '__main__':
    cases = [
        (None, 0),
        (N(0), 0),
        (N(1), 1),
        (N(1, N(0), N(0)), 4),
        (N(1, N(1), N(1)), 6)
    ]
    for tree, expected in cases:
        actual = sum_root_to_leaf(tree)
        assert actual == expected, f"tree: {tree} | {actual} != {expected}"

    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
