"""
Statement

A full binary tree is a binary tree where
each node has exactly 0 or 2 children.

Return a list of all possible full binary
trees with N nodes.  Each element of the
answer is the root node of one possible tree.

Each node of each tree in the answer must
have node.val = 0.

You may return the final list of trees in any order.

(see problem for an example involving pictures)
--------------------
Understand / Plan

- if N is even, return an empty list
- we need to try all possible combinations of trees, so this is
almost like a DFS through different graphs
- We can use backtracking; starting with the root, begin by adding children and decrementing
N for each one; if we get to a case where N is 0, deep copy the list into a solution array and return.
- per the online judge's expected answer format, we are going to need return the tree as a list,
adding it to the solution array. We can do the backtracking directly with the array
- The deepest a fully balanced tree of N nodes can be is (N/2 - 1); since N is always
less than 20, the tree should be no deeper than 10, which means that the array should
never need to be larger than 2**10

pseudocode:
  - if N < 1, return []
  - initialize solutions to []
  - initialize current_arr to [0]
  - call get_all_trees(current_arr, 0, n, solutions)
  - return solutions

  get_all_trees(current_arr, i, remaining nodes, solutions):
    if remaining_nodes = 0:
      solutions.append([x for x in current_arr])
      return

    # extend current_arr id needed
    if len(current_arr) <= 2*i+2:
        array.extend([None] * (2*i+2 - len(array) + 1))

    # Add both nodes; must be full, can't add individuals
    current_arr[2*i+1] = 0
    current_arr[2*i+2] = 0
    remaining_nodes -= 2

    # Try left subtree
    get_all_trees(current_arr, 2*i+1, remaining_nodes, solutions)

    # Try right subtree
    get_all_trees(current_arr, 2*i+2, remaining_nodes, solutions)

    # Uncommit and exit
    current_arr[2*i+1] = None
    current_arr[2*i+2] = None
    remaining_nodes += 2
    return




--------------------
Execute
--------------------
Review
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def get_all_trees(current_arr, i, remaining_nodes, solutions):
    if remaining_nodes == 0:
        solutions.append([x for x in current_arr])
        return

    # extend current_arr id needed
    if len(current_arr) <= 2*i+2:
        array.extend([None] * (2*i+2 - len(array) + 1))

    # Add both nodes; must be full, can't add individuals
    current_arr[2*i+1] = 0
    current_arr[2*i+2] = 0
    remaining_nodes -= 2

    # Try left subtree
    get_all_trees(current_arr, 2*i+1, remaining_nodes, solutions)

    # Try right subtree
    get_all_trees(current_arr, 2*i+2, remaining_nodes, solutions)

    # Uncommit and exit
    current_arr[2*i+1] = None
    current_arr[2*i+2] = None
    remaining_nodes += 2
    return


class Solution(object):
    def allPossibleFBT(self, n):
        if n % 2 == 0 or n < 1:
            return []
        solutions = []
        current_arr = [0]
        get_all_trees(current_arr, 0, n, solutions)
        return solutions


if __name__ == '__main__':
    s = Solution()
    assert s.allPossibleFBT(self, 7) == [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0], [0, 0, 0, 0,
                                                                                                                            0, 0, 0], [0, 0, 0, 0, 0, None, None, None, None, 0, 0], [0, 0, 0, 0, 0, None, None, 0, 0]]
