from binary_tree_node import BinaryTreeNode
from test_framework import generic_test

"""
sum of all numbers in root-to-leaf path
- We can just store the actual numbers as strings for linear storage, but there's a better way to do this
0b1 = 1
0b10 = 2
0b100 = 4 

0b11 = 3
0b110 = 6
so lshifting is * 2 
"""


def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    total = 0 
    def recurse(node, rtotal):
        if not node: 
            return
        rtotal += 1 if node.data == 1 else 0    
        if node and not (node.left or node.right):
            nonlocal total 
            total += rtotal 
        else: 
            recurse(node.left, rtotal*2)
            recurse(node.right, rtotal*2)
    recurse(tree, 0)
    return total 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sum_root_to_leaf.py',
                                       'sum_root_to_leaf.tsv',
                                       sum_root_to_leaf))
