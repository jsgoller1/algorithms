from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
Recursive solution:
    height of a tree is 1 plus each of its subtrees (unless they're both empty)
    recursively calculate the height and difference

"""


def display(node, prefix="", margin=0):
    print(f"{' '*margin}| {prefix + ':' if prefix else ''} {node.data}")
    if node.right:
        display(node.right, 'R', margin+2)
    if node.left:
        display(node.left, 'L', margin+2)


def is_balanced_binary_tree(tree: BinaryTreeNode) -> bool:
    def balance_height(node):
        if not node:
            return -1, True
        lheight, lbalance = balance_height(node.left)
        rheight, rbalance = balance_height(node.right)

        height = max(lheight, rheight) + 1
        balanced = lbalance and rbalance and abs(lheight - rheight) < 2
        return height, balanced

    _, balanced = balance_height(tree)

    return balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_balanced.py',
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))
