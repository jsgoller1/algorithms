import functools
from typing import List, Optional

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

"""
At each level (other than the root) we can add a left child, a right child, or both, and then traverse down any tree we create. 
"""
def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:
    trees = []
    if num_nodes == 0:
        return [None]
    for left_size in range(num_nodes):
        right_size = num_nodes - 1 - left_size
        right_subtrees = generate_all_binary_trees(right_size)
        left_subtrees = generate_all_binary_trees(left_size)
        for left_subtree in left_subtrees:
            for right_subtree in right_subtrees:
                trees.append(BinaryTreeNode(None, left=left_subtree, right=right_subtree))    
    return trees


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_trees.py',
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
