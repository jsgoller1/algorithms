/*
Statement

We are given the head node root of a binary tree, where
additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given
tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X,
plus every node that is a descendant of X.)

Example 1:
Input: [1,null,0,0,1]
Output: [1,null,0,null,1]

Explanation:
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

Constraints:
The binary tree will have at most 100 nodes.
The value of each node will only be 0 or 1.

Input: Tree node, the root of the tree
Output: Tree node, the root of the tree
------------------------
Understand

- Possible cases
	- nil pointer
		- should be ignored / immediately returned
	- one-node tree
		- same rule applies to it as a many-node tree
	- multiple nodes
		- no zero subtree
			- return tree unmodified
		- some zero node subtrees
			- should be removed
		- all zero node subtrees
			- nil should be returned

- We do need to visit every node so we can determine
if a subtree contains all zeros or not; min runtime will be O(n)

------------------------
Plan / Pseudocode

We can handle the tree recursively by visiting a node, visiting its children
via assignment, and then returning nil if both children are nil or the node if
not

pruneTree(*node){
	if node && node->left {
		node->left = pruneTree(node->left)
	}
	if node && node->right {
		node->right = pruneTree(node->right)
	}

	if node && node->val == 0 && node->left == nil && node->right == nil {
		return nil
	}
	return node
}

------------------------
Execute
(see below)

------------------------
Review
*/
package main

import (
	"fmt"
)

// TreeNode defines a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func dfs(tree *TreeNode) {
	if tree == nil {
		return
	}
	fmt.Println(tree.Val)
	dfs(tree.Left)
	dfs(tree.Right)
}

func pruneTree(root *TreeNode) *TreeNode {
	if root != nil && root.Left != nil {
		root.Left = pruneTree(root.Left)
	}
	if root != nil && root.Right != nil {
		root.Right = pruneTree(root.Right)
	}

	if root != nil && root.Val == 0 && root.Left == nil && root.Right == nil {
		return nil
	}
	return root
}

func main() {
	node := &TreeNode{1, nil, nil}
	node.Left = &TreeNode{1, nil, nil}
	node.Left.Right = &TreeNode{0, nil, nil} // should be removed
	node.Left.Left = &TreeNode{1, nil, nil}
	node.Right = &TreeNode{0, nil, nil}       // should be removed
	node.Right.Right = &TreeNode{0, nil, nil} // should be removed
	dfs(node)
	pruneTree(node)
	fmt.Println("--------")
	dfs(node)

}
