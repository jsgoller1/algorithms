"""
This problem can probably be solved with prefix sums or an interval tree:
- prefix sums: we create a second array that stores the sum from 0 to that index, as well as the value
    - Updates require updating all values to the right of the index
    - range sum involves subtracting the left sum from the right. 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]
"""
from typing import List

class NumArrayPrefixSums:
    def __init__(self, nums: List[int]):
        self.arr = []
        rsum = 0 
        for num in nums: 
            rsum += num
            self.arr.append(rsum)

    def update(self, index: int, val: int) -> None:
        """
        O(n)
        """
        old_val = self.arr[index] - self.arr[index-1] if index > 0 else self.arr[index]
        delta = -old_val + val 
        for i in range(index, len(self.arr)):
            self.arr[i] += delta

    def sumRange(self, left: int, right: int) -> int:
        """
        O(c) 
        """
        return self.arr[right] - self.arr[left-1] if left-1 >= 0 else self.arr[right]
        

class SegmentTreeNode:
    def __init__(self, l, r, total):
        self.l, self.r, self.total = l, r, total 
        self.right, self.left = None, None
    
    def __repr__(self):
        return f"SegmentTreeNode(l={self.l}, r={self.r}, total={self.total})"


def calculate_total(nums, l, r):
    rsum = 0 
    for i in range(l, r+1):
        rsum += nums[i]
    return rsum 


def construct_segment_tree(nums, l, r):
    if l == r: 
        return SegmentTreeNode(l, r, nums[l])
    total = calculate_total(nums, l, r)
    head = SegmentTreeNode(l, r, total)
    m = (l + r) // 2
    head.left = construct_segment_tree(nums, l, m)
    head.right = construct_segment_tree(nums, m+1, r)
    return head 


def update_segment_tree(node, index, delta): 
    if not (node and node.l <= index <= node.r):
        return
    node.total += delta 
    update_segment_tree(node.left, index, delta)
    update_segment_tree(node.right, index, delta)


def sum_range(node, left, right):
    if not node: 
        return 0
    if (left <= node.l <= node.r <= right):
        return node.total 
    mid = (node.l + node.r) // 2
    total = 0 
    if left <= mid:
        total += sum_range(node.left, left, right)
    if mid <= right: 
        total += sum_range(node.right, left, right)
    return total 


class NumArraySegmentTree:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = construct_segment_tree(nums, 0, len(nums)-1)

    def update(self, index: int, val: int) -> None:
        delta = -self.nums[index] + val 
        self.nums[index] = val 
        update_segment_tree(self.root, index, delta)

    def sumRange(self, left: int, right: int) -> int:
        return sum_range(self.root, left, right)


na = NumArraySegmentTree([1,3,5])
assert na.sumRange(0,2) == 9, f"{na.sumRange(0,2)}" # total = 9
na.update(1,2)  # now [1,2,5]
assert na.sumRange(0,2) == 8, f"{na.sumRange(0,2)} ({na.arr})"


na = NumArraySegmentTree([9, -8])
na.update(0, 3)
assert na.sumRange(1, 1) == -8, f"{na.sumRange(1, 1)}"
assert na.sumRange(0, 1) == -5, f"{na.sumRange(0, 1)}"
na.update(1, -3)
assert na.sumRange(0, 1) == 0, f"{na.sumRange(0, 1)}"


["NumArray","update","sumRange","sumRange","update","sumRange"]
[[[9,-8]],[0,3],[1,1],[0,1],[1,-3],[0,1]]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
