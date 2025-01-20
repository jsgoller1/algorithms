from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    balanced = True 
    def get_depths(node):
        if not node:
            return 0
        left_depth, right_depth = get_depths(node.left), get_depths(node.right)
        nonlocal balanced 
        if balanced:
            balanced = abs(left_depth - right_depth) < 2
        return max(left_depth, right_depth) + 1            
    get_depths(tree)
    return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
