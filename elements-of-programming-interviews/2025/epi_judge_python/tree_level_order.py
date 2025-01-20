from typing import List

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

from collections import deque, defaultdict


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    # This version uses the fact that level order traversal will 
    # implicitly sort the nodes to achieve linear time. 
    if not tree:
        return []
    solution = []
    curr_level = 0
    curr_level_nodes = []
    q = deque([(curr_level, tree)])
    while q:
        level, node = q.popleft()
        if level != curr_level:
            solution.append(curr_level_nodes)
            curr_level += 1
            curr_level_nodes = []
        curr_level_nodes.append(node.data)
        if node.left:
            q.append((level + 1, node.left))
        if node.right:
            q.append((level + 1, node.right))
    if curr_level_nodes:
        solution.append(curr_level_nodes)
    return solution

def binary_tree_depth_order_linearithmic(tree: BinaryTreeNode) -> List[List[int]]:
    if not tree:
        return []
    levels = defaultdict(list)
    q = deque([(0, tree)])
    while q:
        level, node = q.popleft()
        levels[level].append(node.data)
        if node.left:
            q.append((level + 1, node.left))
        if node.right:
            q.append((level + 1, node.right))
    return [nodes for level, nodes in sorted(levels.items())]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
