"""
https://www.geeksforgeeks.org/binary-tree-array-implementation/

It is possible to represent a binary tree as an array. If we
have a tree:

      A(0)
     /   \
    B(1)  C(2)
  /   \      \
 D(3)  E(4)   F(5)

then the array representation is
arr = [0,1,2,3,4, None, 5]

For each node, if the parent's index is i, then the left child's
index is (2*i)+1 and the right child's is (2*i)+2.

"""
import binary_tree


def bst_to_array(node_id, node, array):
    """
    Convert a (possibly unbalanced) binary tree to an array;
    tree_node_tuple is an (int, node) tuple,
    where the int is breadth-order index of the
    node. The array is the array into which we flatten the tree.
    We can extend the array as needed.
    """
    if not node:
        return

    if len(array) <= node_id:
        array.extend([None] * (node_id - len(array) + 1))

    array[node_id] = node.val
    bst_to_array(2*node_id+1, node.left, array)
    bst_to_array(2*node_id+2, node.right, array)


if __name__ == '__main__':
    tree_balanced = binary_tree.create_balanced_bst()
    array1 = []
    bst_to_array(0, tree_balanced, array1)
    print(array1)

    tree_unbalanced = binary_tree.create_unbalanced_bst(8)
    array2 = []
    bst_to_array(0, tree_unbalanced, array2)
    print(array2)
