"""
Given a sorted integer array arr, two integers k and x, return the k 
closest integers to x in the array. The result should also be sorted
in ascending order.

An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b
-------
- Probably a linear time solution? Only need to look at every val once. 
- Can use a maxheap - push tuples in of (distance from x, val); heapify on first value, only 
push new elements when max distance from x is greater than current element's. 
- Input array is sorted, so can we do better?
- Could find index / insertion point for x in arr, then
 use two pointers to keep track of k nearest elements - O(log(N)) + K where N = len(arr)
-----------
ret = collections.deque()
insertion_point = bin_search(arr, x)
if arr[insertion_point] <= x:
    lower, higher = insertion_point, insertion_point+1
else:
    lower, higher = insertion_point-1, insertion_point
while len(ret) < k and (lower >= 0 or higher < len(arr)):
    if higher >= len(arr) or distance(x, arr[lower]) <= distance(x, arr[higher]):
        ret.appendleft(arr[lower])
        lower -= 1
    else:
        ret.append(arr[higher])
        higher+=1
return ret
"""
from collections import deque
from typing import List

def bin_search(arr, val):
    lo, hi = 0, len(arr)-1
    while lo <= hi:
        mid = (hi + lo) // 2
        if arr[mid] == val:
            return mid
        elif arr[mid] > val:
            lo, hi = lo, mid - 1
        else:
            lo, hi = mid+1, hi
    return lo 

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        ret = deque()
        insertion_point = bin_search(arr, x)
        if insertion_point < len(arr) and arr[insertion_point] <= x:
            lower, higher = insertion_point, insertion_point+1
        else:
            lower, higher = insertion_point-1, insertion_point
        while len(ret) < k and (lower >= 0 or higher < len(arr)):
            if higher >= len(arr) or abs(x - arr[lower]) <= abs(x - arr[higher]):
                ret.appendleft(arr[lower])
                lower -= 1
            else:
                ret.append(arr[higher])
                higher+=1
        return list(ret)

s = Solution()
for case in [
    # lower will go below 0
    ([1,2,3,4,5], 4, 0, [1,2,3,4]),
    # higher will go above last element
    ([1,2,3,4,5], 4, 6, [2,3,4,5]),
    # len(arr) == k
    ([1,2,3,4,5], 5, 9, [1,2,3,4,5]),
    # x not in arr
    ([1,2,3,4,5], 4, -1, [1,2,3,4]),
    # x in arr
    ([1,2,3,4,5], 4, 3, [1,2,3,4]),
    # previous failures
    ([1,1,2,2,2,2,2,3,3], 3, 3, [2,3,3])
]:
    arr, k, x, ans = case
    print(arr, k, x)
    actual = s.findClosestElements(arr, k, x)
    assert actual == ans, (arr, k, x, ans, actual)
