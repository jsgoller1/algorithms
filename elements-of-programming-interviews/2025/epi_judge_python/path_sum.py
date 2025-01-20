from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def has_path_sum(tree: BinaryTreeNode, target_sum: int) -> bool:
    def recurse(node, rtotal):
        if (not node):
            return False 
        rtotal += node.data
        if (not (node.left or node.right)) and rtotal == target_sum:
            return True 
        return recurse(node.left, rtotal) or recurse(node.right, rtotal)
    return recurse(tree, 0)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('path_sum.py', 'path_sum.tsv',
                                       has_path_sum))
