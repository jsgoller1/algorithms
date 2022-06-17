/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 *
- node count and val both fit in int, whole tree in mem

recurse(node):
    if null: return
    recurse(node.left)
    print(node.val)
    recurse(node.right)

iterative(head):
    while stack nonempty or curr not null:
        if node not null:
            stack.push(node)
            node = node.left
        else
            node = stack.pop()
            print node.val
            node = node.right
*/
#include <stack>

class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> path = *(new vector<int>());
        std::stack<TreeNode*> node_stack = std::stack<TreeNode*>();
        while (!node_stack.empty() || root != nullptr){
            if (root != nullptr){
                node_stack.push(root);
                root = root->left;
            } else {
                root = node_stack.top();
                node_stack.pop();
                path.push_back(root->val);
                root = root->right;
            }
        }
        return path;
    }
};