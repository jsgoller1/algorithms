/*
Statement

Given two binary trees and imagine that when you put one
of them to cover the other, some nodes of the two trees
are overlapped while the others are not.

You need to merge them into a new binary tree.
The merge rule is that if two nodes overlap,
then sum node values up as the new value of the
merged node. Otherwise, the NOT null node will be
used as the node of new tree.

Example 1:
Input:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
Output:
Merged tree:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7


Note: The merging process must start from the
root nodes of both trees.
----------------------------------------------
Understand
- What optimal cases exist?
	- both trees are exactly the same shape so we can
	DFS for great justice
- What typical but tricky cases exist?
	- tree A has an entire branch that tree B lacks; doing
	a DFS could be hazardous if we try to dereference a nil
- What possible degenerate cases exist?
	- one tree is empty; return the nonempty one
	- both are empty, return nil

----------------------------------------------
Plan / Pseudocode
- if both trees have at least one node, we can
create a third tree and then call a helper function
that takes three nodes:
	- to avoid creating children in the new tree
	that shouldn't be there, we should only create a left
	or right child if at least one of the parent trees has a child in that
	position. As such, the function will be called on created nodes whose
	values are set and will fix up correct children before recursively subcalling
	- the function is not recursed if nodeA.Left && nodeB.Left are nil (same for
	nodeA.Right and nodeB.Right)
	- our DFS helper function CAN NOT assume that nodeA and nodeB are not nil. newTree should never be nil
	- at every node, if nodeA.left or nodeB.left, create newNode.left and copy the value, then recurse.
	- same for right


----------------------------------------------
Execute

See below.
----------------------------------------------
Review
*/
package main

import (
	"fmt"
)

// TreeNode is a node in a binary tree
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

func dfsMerge(t1, t2, newTree *TreeNode) {
	var newLeft *TreeNode
	var newRight *TreeNode

	var t1Left *TreeNode
	var t2Left *TreeNode
	var t1Right *TreeNode
	var t2Right *TreeNode

	// copy left / right values from t1 if it exists
	if t1 != nil {
		if t1.Left != nil {
			t1Left = t1.Left
			newLeft = &TreeNode{t1.Left.Val, nil, nil}
		}
		if t1.Right != nil {
			t1Right = t1.Right
			newRight = &TreeNode{t1.Right.Val, nil, nil}
		}
	}

	// copy left/right values from t2, or
	// add them if we already created the new node
	if t2 != nil {
		if t2.Left != nil {
			t2Left = t2.Left
			if newLeft == nil {
				newLeft = &TreeNode{t2.Left.Val, nil, nil}
			} else {
				newLeft.Val += t2.Left.Val
			}
		}
		if t2.Right != nil {
			t2Right = t2.Right
			if newRight == nil {
				newRight = &TreeNode{t2.Right.Val, nil, nil}
			} else {
				newRight.Val += t2.Right.Val
			}
		}
	}

	// Traverse if we created left or right nodes
	if newLeft != nil {
		newTree.Left = newLeft
		dfsMerge(t1Left, t2Left, newTree.Left)
	}
	if newRight != nil {
		newTree.Right = newRight
		dfsMerge(t1Right, t2Right, newTree.Right)
	}
}

func mergeTrees(t1, t2 *TreeNode) *TreeNode {
	if t1 == nil {
		return t2
	}
	if t2 == nil {
		return t1
	}

	newTree := TreeNode{t1.Val + t2.Val, nil, nil}
	dfsMerge(t1, t2, &newTree)
	return &newTree
}

func main() {
	/*
		nodeA := TreeNode{1, nil, nil}
		nodeA.Left = &TreeNode{4, nil, nil}
		nodeB := TreeNode{2, nil, nil}
		nodeB.Right = &TreeNode{5, nil, nil}
	*/
	// [1,2,null,3]
	nodeA := TreeNode{1, nil, nil}
	nodeA.Left = &TreeNode{2, nil, nil}
	nodeA.Left.Left = &TreeNode{3, nil, nil}

	// [1,null,2,null,3]
	nodeB := TreeNode{1, nil, nil}
	nodeB.Right = &TreeNode{2, nil, nil}
	nodeB.Right.Right = &TreeNode{3, nil, nil}

	newTree := mergeTrees(&nodeA, &nodeB)
	dfs(newTree)
}
