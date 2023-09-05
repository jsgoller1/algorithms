from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def inorder_traversal(root: BinaryTreeNode) -> List[int]:
    traversal = []
    stack = [root] if root else []
    curr = root.left if root else None
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        if not curr:
            curr = stack.pop()
            traversal.append(curr.data)
            curr = curr.right
    return traversal


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_inorder.py', 'tree_inorder.tsv',
                                       inorder_traversal))
