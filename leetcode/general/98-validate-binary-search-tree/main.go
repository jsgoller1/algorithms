/*
Statement

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
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
------------------------------------
Understand

Cases:
- null tree
	- return true
- no children
	- return true
- one child
	- true if value is valid given child's side, false if not
		- left child must be less than parent, but not less than global min
		- right child must be greater than the parent, but not greater than global max
- two children
	- repeat one-child procedure

	100 right 125 left 80 (invalid, less than grandparent)
	100 left 75 right 110 (invalid, greater than grandparent)
	100 left 75 left 50 left 25 right 30 (valid)
	100 left 75 left 50 left 25 right 49 (valid)
	100 left 75 left 50 left 25 right 50 (invalid)

global min begins as -inf and global max as inf
	- if we traverse left, parent becomes new global max
	- if we traverse right, parent becomes new global min


Constraints:
	- How are duplicate keys handled?

------------------------------------
Plan / Pseudocode

validate(node*, globalMin, globalMax):
	if node == null:
		return true

	leftValid := true
	if node.left:
		if node.left.val > node.val:
			return false
		else:
			leftValid = validate(node.left)

	rightValid := true
	if node.right:
		if node.right.val < node.val:
			return false
		else:
			rightValid = valdiate(node.right)

	return leftValid && rightValid

------------------------------------
Execute

See below
------------------------------------
Review

*/
package main

import (
	"fmt"
	"math"
)

// TreeNode defines a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func validate(root *TreeNode, gMin, gMax float64) bool {
	leftValid := true
	if root.Left != nil {
		if root.Left.Val >= root.Val || float64(root.Left.Val) <= gMin {
			return false
		}
		leftValid = validate(root.Left, gMin, float64(root.Val))
	}

	rightValid := true
	if root.Right != nil {
		if root.Right.Val <= root.Val || float64(root.Right.Val) >= gMax {
			return false
		}
		rightValid = validate(root.Right, float64(root.Val), gMax)
	}

	return leftValid && rightValid
}

func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return validate(root, math.Inf(-1), math.Inf(1))
}

func main() {
	// Full tree, valid
	node1 := &TreeNode{6, nil, nil}
	node1.Left = &TreeNode{4, nil, nil}
	node1.Left.Right = &TreeNode{5, nil, nil}
	node1.Left.Left = &TreeNode{3, nil, nil}
	node1.Right = &TreeNode{7, nil, nil}
	node1.Right.Right = &TreeNode{9, nil, nil}

	// Full tree, invalid
	node2 := &TreeNode{6, nil, nil}
	node2.Left = &TreeNode{4, nil, nil}
	node2.Left.Right = &TreeNode{5, nil, nil}
	node2.Left.Left = &TreeNode{3, nil, nil}
	node2.Right = &TreeNode{-1234, nil, nil}
	node2.Right.Right = &TreeNode{9, nil, nil}

	// Full tree, invalid
	node3 := &TreeNode{100, nil, nil}
	node3.Left = &TreeNode{50, nil, nil}
	node3.Left.Left = &TreeNode{25, nil, nil}
	node3.Left.Right = &TreeNode{120, nil, nil}
	node3.Right = &TreeNode{200, nil, nil}
	node3.Right.Left = &TreeNode{50, nil, nil}
	node3.Right.Right = &TreeNode{300, nil, nil}

	// Null tree, valid
	var node4 *TreeNode

	// One node tree, valid
	node5 := &TreeNode{0, nil, nil}

	testCases := []*TreeNode{node1, node2, node3, node4, node5}
	for i, root := range testCases {
		fmt.Println(i, isValidBST(root))
	}
}
