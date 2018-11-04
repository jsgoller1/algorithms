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
Understand / Plan (first attempt)

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

----
Understand / Plan (second attempt)

Trying to encode the tree in an array like above didn't work; firstly, my
algorithm wasn't exhaustive (it is a depth-first search and doesn't catch
balanced tree cases). Second, the solution is expecting an array of nodes that
it will then decode into an array of arrays; their decoding algorithm is wrong,
but it is consistent so producing the correct trees will in fact solve the problem.

While I was confused, I looked at the solution for the problem; the posted solution
loops through all possible left trees combined with all possible right trees (from
that left node) while using a cache. This is implemented below.

--------------------
Execute
--------------------
Review
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    cache = {0: [], 1: [TreeNode(0)]}

    def allPossibleFBT(self, n):
        """
        Find all possible full binary trees of N
        nodes;
        """
        if n % 2 == 0 or n < 1:
            return []

        if n not in self.cache:
            answer = []
            for x in range(n):
                y = n - 1 - x
                for left in self.allPossibleFBT(x):
                    for right in self.allPossibleFBT(y):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        answer.append(root)
            Solution.cache[n] = answer
        return self.cache[n]


if __name__ == '__main__':
    s = Solution()
    print(s.allPossibleFBT(7))
