from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
Suppose we went through the left and right trees together:
    root.left must equal root.right
    root.left.left must equal root.right.right
    root.left.right must equal root.right.left 

So we recursively implement this; base case is if one node is none, both must be.
"""


def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True

    def compare(left_subtree, right_subtree):
        if None in [left_subtree, right_subtree]:
            return left_subtree == right_subtree
        symmetric = left_subtree.data == right_subtree.data
        symmetric &= compare(left_subtree.left, right_subtree.right)
        symmetric &= compare(left_subtree.right, right_subtree.left)
        return symmetric

    return compare(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
