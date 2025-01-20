from binary_tree_node import BinaryTreeNode
from test_framework import generic_test



def is_symmetric(tree: BinaryTreeNode) -> bool:
    if not tree:
        return True
    def compare_nodes(left, right):
        if not (left and right):
            return not (left or right)
        is_symmetric = left.data == right.data
        is_symmetric &= compare_nodes(left.left, right.right)
        is_symmetric &= compare_nodes(left.right, right.left)
        return is_symmetric
    return compare_nodes(tree.left, tree.right)

    
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_symmetric.py',
                                       'is_tree_symmetric.tsv', is_symmetric))
