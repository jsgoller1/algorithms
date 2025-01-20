import functools
from typing import Optional

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None, size=None):
        self.data = data
        self.left = left
        self.right = right
        self.size = size


"""
- Inorder traversal is LNR. So before we process the current node, we have to process the entire left subtree.
- going left means "we will process fewer nodes before reaching this node"
- going right mean "we commit to processing this many nodes."

At each node:
    if k == left subtree size + 1, current node is kth. 
    if k < left subtree size + 1, go left. 
    if k > left subtree's size + 1, go right and subtract left subtree's size plus one (for root) from k. 


edge cases: tree empty, k is larger than whole tree size (assume this won't happen for now)
"""


def find_kth_node_binary_tree(tree: BinaryTreeNode,
                              k: int) -> Optional[BinaryTreeNode]:
    if (not tree) or k > tree.size:
        return None

    def find_kth(root, remaining):
        traversable = (root.left.size+1 if root.left else 1)
        if remaining == traversable:
            return root
        if root.left and traversable > remaining:
            return find_kth(root.left, remaining)
        else:  # (not root.left) or traversable < remaining
            return find_kth(root.right, remaining-traversable)

    return find_kth(tree, k)


@enable_executor_hook
def find_kth_node_binary_tree_wrapper(executor, tree, k):
    def init_size(node):
        if not node:
            return 0
        node.size = 1 + init_size(node.left) + init_size(node.right)
        return node.size

    init_size(tree)

    result = executor.run(functools.partial(find_kth_node_binary_tree, tree,
                                            k))

    if not result:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_node_in_tree.py',
                                       'kth_node_in_tree.tsv',
                                       find_kth_node_binary_tree_wrapper))
