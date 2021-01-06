"""
A binary tree is a tree where each node has no more than two children.

Example:
      A(0)
     /   \
    B(1)  C(2)
  /   \      \
 D(3)  E(4)   F(5)

A tree is a binary search tree if for every node, the search
property holds (the left child is less than or equal to the node,
and the right child is greater than the node)
"""

import random
import math
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create_random_bst(node_count):
    """
    Insert n random nodes into a tree
    """
    root = TreeNode(random.randint(-100, 100))
    print("Root: {0}".format(root.val))
    for i in range(node_count):
        new_node = TreeNode(random.randint(-100, 100))
        print("Inserting {0} into tree".format(new_node.val))
        bst_insert(root, new_node)
        print(make_list(root))
    return root


def create_balanced_bst():
    """
    Creates a 7-node bst where each node's val is equivalent to
    its index in a bst array
    """
    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def create_unbalanced_bst(node_count):
    """
    Creates a 7-node bst where each node's val
    is NOT equivalent to its index in a bst array
    """
    root = TreeNode(0)
    current = root
    i = 1
    while (i < node_count):
        current.left = TreeNode(i)
        i += 1
        current.right = TreeNode(i)
        i += 1
        current = current.left
    return root


def bst_insert(root, new_node):
    """
    Insert into the tree while adhering to
    the binary search property
    """
    if root.val >= new_node.val:
        if root.left == None:
            root.left = new_node
        else:
            bst_insert(root.left, new_node)
    else:
        if root.right == None:
            root.right = new_node
        else:
            bst_insert(root.right, new_node)


def bst_dfs(root):
    if root == None:
        return
    print(root.val)
    bst_dfs(root.left)
    bst_dfs(root.right)


def bst_bfs(root, process_node):
    q = collections.deque([root])
    while (q):
        current = q.popleft()
        process_node(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)


if __name__ == '__main__':
    #tree = create_random_bst(10)
    # bst_dfs(tree)
    #print("=" * 20)
    # bst_bfs(tree)
    # print("="*20)
    # print(make_list(tree))

    root = create_bst_arrayable()
    bst_bfs(root, print)
