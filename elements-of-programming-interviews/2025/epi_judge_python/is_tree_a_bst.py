from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    def recurse(node, lo=-float('inf'), hi=float('inf')):
        if not node:
            return True
        if not (lo <= node.data <= hi):
            return False 
        return recurse(node.left, lo, node.data) and recurse(node.right, node.data, hi)
    return recurse(tree)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
