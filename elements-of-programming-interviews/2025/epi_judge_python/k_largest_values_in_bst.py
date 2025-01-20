from typing import List

from bst_node import BstNode
from test_framework import generic_test, test_utils

"""
brute force is O(n log (k)): full walk, push to k heap; pruning could be used to make this approach better, but 
edge cases where the root is the largest element can still cause issues. 

for BST, larger elements are always in right subtree. We need to pick elements starting with the rightmost until we have
enough.Reverse inorder walk: inorder walk for BSTs prints nodes in ascending order (traverse all nodes less than current,
print current, then all nodes greater). Append to arr if we have fewer than k; don't explore further if we have k. O(n) for
time and space (e.g. right-biased tree where k <<< n). Average space and time closer to O(h) for height of rightmost leaf node.
"""

def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    out = []
    def rev_inorder(node):
        if (not node) or len(out) == k:
            return
        rev_inorder(node.right)
        if len(out) < k:
            out.append(node.data)
        rev_inorder(node.left)

    rev_inorder(tree)
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('k_largest_values_in_bst.py',
                                       'k_largest_values_in_bst.tsv',
                                       find_k_largest_in_bst,
                                       test_utils.unordered_compare))
