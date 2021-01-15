"""
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

    Given target value is a floating point.
    You may assume k is always valid, that is: k ≤ total nodes.
    You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:

Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]

Follow up:
Assume that the BST is balanced, could you solve it in less than O(n) runtime (where n = total nodes)?
----------------------------------------------------------------------------------------
Brute force:
    - Look at every element of the tree, keeping track of closest in k-heap
        - Heap is a max-heap storing (-distance, val) pairs. if we exceed size, pop.

What are we actually looking for:
    - k nodes with val smallest distance from target; this is the same as searching in an array, so we
      can use a maxheap with inverted distance; this way, we can always evict the worst. 

What can given BST tell us about subsequent values?
    - We will never find val greater than current node in left subtree, or less in right subtree. 

If the heap is full, what remaining BST nodes do we care about?
    - The top element of the heap has the max distance from target; we only care about vals between -distance(heap_max), target, distance(heap_max)
    - If the distance of the current node exceeds max, we don't care about any of its children that will also exceed max:
        - E.g. top of full heap is (4, n), and current BST node would be (5, m).
            - If tgt + 4 <  m, we don't need to look at the right subtree of m. 
            - If tgt - 4 > m, we don't need to look at the left subtree of m. 

While traversing tree with queue (BFS), if len(minheap) < k, add every node we find to heap, queue children. 
If len(minheap) == k:
    - if current node's distance to tgt > max current distance in k:
        - Don't add it to heap
        - Otherwise do
    - Do we look at the left subtree (nodes less than val)?
        - Yes: val between min(tgt, current min in k) and max(tgt, current max in k)
        - No: val < min(tgt, current min in k) or val > max(tgt, current max in k)
    - Do we look at right subtree (nodes greater than val)?
        - Yes:  
-------------------------------------------------------------------------------
solution:
    heap = []
    queue = [root]
    while queue:
        pop top of queue
        if len(heap) < k:
            push (-dist(tg, node.val), node.val) onto heap
            queue both children
        else:
            largest_dist = -heap[0][0]
            if dist(tgt, node.val) < largest_dist, push it onto heap
            if tgt + largest > node.val, queue its right child
            if tgt - largest < node.val, queue its left child 
    return all vals in heap
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from heapq import heappop, heappush


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        if k == 0 or root is None:
            return []

        maxheap = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            val_dist = abs(node.val-target)
            if len(maxheap) < k:
                queue.append(node.left) if node.left else None
                queue.append(node.right) if node.right else None
                heappush(maxheap, (-val_dist, node.val))
            else:
                largest_dist = -maxheap[0][0]
                if val_dist < largest_dist:
                    heappush(maxheap, (-val_dist, node.val))
                    heappop(maxheap)
                queue.append(node.right) if node.right and (target + largest_dist > node.val) else None
                queue.append(node.left) if node.left and (target - largest_dist < node.val) else None
        return [val for _, val in maxheap]
