import functools
from typing import Optional

from bst_node import BstNode
from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

"""
Assumption: s and b are both actually in the tree, tree is actually BST

- BST is BT (no parent reference); recursive algorithm for normal BT works
- but also: pick left / right from s and b (compare them). Need to find node
  where s < node.data < b.data (unless s or b is ancestor of the other); will only be one.

return node where:
    - it's b, and s is a descendent 
    - it's s, and b is a descendent
    - s is in one subtree, b is in the other
otherwise recurse:
    - right if either greater than current
    - left if either less than current 
from left and right subtrees, return s status and b status
"""
from collections import namedtuple
ChildStatus = namedtuple("ChildStatus", ['has_l', 'has_r'])


# Input nodes are nonempty and the key at s is less than or equal to that at b.
# My version
def find_lca_joshua(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    lca = None
    left, right = (s,b) if s.data < b.data else (b,s) 

    def recurse(node) -> ChildStatus:
        if not node:
            return ChildStatus(False, False)
        is_l = node.data == left.data
        is_r = node.data == right.data 

        right_status = left_status = ChildStatus(False, False)
        if node.data < left.data or node.data < right.data:
            right_status = recurse(node.right)
        if left.data < node.data or right.data < node.data:
            left_status = recurse(node.left)
        
        if (left_status.has_l and right_status.has_r) or (is_l and right_status.has_r) or (left_status.has_l and is_r) or (is_l and is_r):
            nonlocal lca
            lca = node 
        return ChildStatus(is_l or left_status.has_l or right_status.has_l, is_r or left_status.has_r or right_status.has_r)

    recurse(tree)
    return lca

# ChatGPT's version after showing it mine
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:
    # Ensure that `s` is the smaller and `b` is the larger node
    smaller, larger = (s, b) if s.data < b.data else (b, s)

    def recurse(node: Optional[BstNode]) -> Optional[BstNode]:
        if not node:
            return None

        # If both nodes are smaller, the LCA must be in the left subtree
        if larger.data < node.data:
            return recurse(node.left)
        # If both nodes are larger, the LCA must be in the right subtree
        elif smaller.data > node.data:
            return recurse(node.right)
        # Otherwise, the current node is the LCA
        else:
            return node

    return recurse(tree)

@enable_executor_hook
def lca_wrapper(executor, tree, s, b):
    result = executor.run(
        functools.partial(find_lca, tree, must_find_node(tree, s),
                          must_find_node(tree, b)))
    if result is None:
        raise TestFailure('Result can\'t be None')
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('lowest_common_ancestor_in_bst.py',
                                       'lowest_common_ancestor_in_bst.tsv',
                                       lca_wrapper))
