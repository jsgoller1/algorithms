from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


"""
null, single node, all nodes greater, all nodes smaller, exact node in tree

When can we stop searching?
- we found a node m where m > k, but we know there's no n st m > n > k. 
 - if node < k, don't search right subtree
 - if node > k, don't search left subtree
- all vals less than m are in its left subtree. 
- can possibly do normal recursive search, but instead, keep track of values
greater than k and return the smallest one?
"""

def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    best = None 
    def search(node):
        if not node:
            return 
        if node.data > k:
            nonlocal best
            best = node if (not best) or (node.data < best.data) else best 
        search(node.right if k >= node.data else node.left)
    search(tree)
    return best


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
