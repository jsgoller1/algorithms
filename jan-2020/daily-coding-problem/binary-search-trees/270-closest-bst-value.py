"""
Given a non-empty binary search tree and a target value, find the value in the BST that is 
closest to the target.

Note:
    - Given target value is a floating point.
    - You are guaranteed to have only one unique value in the BST that 
      is closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

Constraints given:
    - target is a floating point; not stated if there would be floats in tree though example is ints only
    - there will be only one value in the tree that's closest

Input cases:
    - Tree with a single node
    - Unbalanced tree (subtrees at same height may contain different numbers of children) 

Note:
    DCP 7.1 is very similar to this, but asks for floor and cieling instead of nearest value

----------------------------------
Brute force:
    - Look at every element in the tree; O(n)

Insight:
    - At each node in the tree, we will only find values greater than it in the right
      subtree and values less in the left subtree

Alternate approach:
    - Start with floor = -inf, cieling = inf
    - while the current node is not none:
        - if the current node is less than the current cieling but greater
          than the target, it becomes new cieling
        - if current is greater than floor but less than cieling, it becomes
          floor
        - If the current node is greater than the target, go left next
        - If current is less than target, go right
    - Return floor or cieling depending on which is closer to target
"""


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        floor = -float('inf')
        cieling = float('inf')
        while root:
            if root.val < target:
                floor = max(floor, root.val)
                root = root.right
            else:
                cieling = min(cieling, root.val)
                root = root.left
        return floor if abs(floor - target) < abs(cieling - target) else cieling
