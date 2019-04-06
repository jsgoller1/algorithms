/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's
key. The right subtree of a node contains only nodes with keys greater than the
node's key. Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
---------------------------------------------
I screwed this problem up right before my initial interview with the
perception team at Uber ATG. I WILL NOT BE DEFEATED TWICE.

In: TreeNode
Out: bool
Possible inputs:
  - any tree
  - nullptr

We can use a recursive function that takes three arguments - a treenode,
as lower bound and an upper bound. The base case is the root, -inf and inf.
When we recurse, if we go left, the current val becomes the new max. If we go
right, the current becomes the new min. At each step, we test if the children
are within the range; if they ever aren't, return false.
----------------------------------------------------------------
Runtime: 20 ms, faster than 99.15% of C++ online submissions for Validate Binary
Search Tree.

Memory Usage: 20.5 MB, less than 75.98% of C++ online submissions
for Validate Binary Search Tree.
*/
#include <iostream>
#include <limits>

using std::cout;
using std::endl;

// Definition for a binary tree node.
#pragma clang diagnostic ignored "-Wpadded"

typedef struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
} TreeNode;

class Solution {
 public:
  bool recurse(TreeNode *root, double min, double max) {
    if (root == nullptr) {
      return true;
    }
    double val = static_cast<double>(root->val);
    if (val >= max || val <= min) {
      return false;
    }
    return recurse(root->left, min, root->val) &&
           recurse(root->right, root->val, max);
  }

  bool isValidBST(TreeNode *root) {
    double inf = std::numeric_limits<double>::infinity();
    return recurse(root, -inf, inf);
  }
};

int main() {
  Solution s;
  TreeNode node200(200), node100(100), node300(300);
  node200.left = &node100;
  node200.right = &node300;
  cout << s.isValidBST(&node200) << endl;
  TreeNode node5(5), node4(4), node1(1), node3(3), node6(6);
  node5.left = &node1;
  node5.right = &node4;
  node4.left = &node3;
  node4.right = &node6;
  cout << s.isValidBST(&node5) << endl;
  cout << s.isValidBST(nullptr) << endl;
}
