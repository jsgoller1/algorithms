/*
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
-------------------------
In: tree struct
Out: int, max depth

Possible input cases:
  - null pointer
  - any variant of a tree
    - equal height / perfectly balanced
    - SLL (degenerate)
    - other
- Trivial recursion
--------------------------
- recursive function taking int and tree struct
- if no children, return depth
- otherwise, recurse children with depth+1; return max
- base case is 1
--------------------------
Runtime: 16 ms, faster than 98.97% of C++ online submissions for Maximum Depth
of Binary Tree.

Memory Usage: 19.5 MB, less than 46.63% of C++ online
submissions for Maximum Depth of Binary Tree.

*/

#include <algorithm>
#include <iostream>

using std::cout;
using std::endl;
using std::max;

// Definition for a binary tree node.
#pragma clang diagnostic ignored "-Wpadded"
typedef struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
 public:
  int recurse(TreeNode* root, int depth) {
    if (root == nullptr) {
      return depth;
    }
    return max(recurse(root->left, depth + 1), recurse(root->right, depth + 1));
  }
  int maxDepth(TreeNode* root) { return recurse(root, 0); }
};

int main() {
  Solution s;
  TreeNode node3(3), node9(9), node20(20), node15(15), node7(7);
  node3.left = &node9;
  node3.right = &node20;
  node20.left = &node15;
  node20.right = &node7;
  cout << s.maxDepth(&node3) << endl;
  cout << s.maxDepth(nullptr) << endl;
}
