"""
Suppose an array sorted in ascending order is rotated at
some pivot unknown to you beforehand. (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise
return -1.

You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
--------------------------------------------------
Input: List[int]
Output: int (index)

Constraints:
  - Always in ascending order
  - No duplicates exist
  - Runtime must be log(n)
    - No sorting; O(n*log(n))
    - Cannot examine every element; O(n)

Cases:
  - Empty array
  - Singleton array
  - Unshifted array, in correct order
  - Rotate-shifted any number of places

- Do we need to modify the array before searching?
  - can't rotate back to sorted, would be O(n)
- What _do_ we need to examine?
  - log(n) says binary search; how can we still correctly execute a binary search
  without knowing the shift?
  - log(n) means we can examine half as many elements as we did last iteration
  - if i < j but a[i] > a[j], we know that that particular subarray isn't in order
    - this will be true until we i,j are the boundaries of the section that is shifted out of order
- If we can find the "pivot's" index, then we can search the subarray with the pivot as the boundary; if pivot = i and arr[0] < val < arr[pivot],
we search that subarray, else we search arr[pivot:]
- We can find the pivot element using binsearch; see pseudocode below
--------------------------------------------------
Pseudocode
- find pivot element using modified binsearch
- compare the two subarrays of arr that pivot creates, binsearch the appropriate one and either return
index if found, or return -1

[3,4,5,6,7,8,9,0,1,2]
[7,8,9,0,1,2]

[7,8,9,0,1,2,3,4,5,6]

[6,7,8,9,0,1,2,3,4,5]
[6,7,8,9,0,1]
[8,9,0,1]
[9,0,1]
[9,0]

findPivot(arr):
  start = 0
  end = len(arr)-1
  while end-start > 1:
    mid = (end+start)//2
    if mid > start:
      start = mid
    else:
      end = mid

  if arr[start] > arr[end]
    return end
  else:
    return start

  return mid

binSearch(arr,val, start, end)
  while end-start > 1:
    mid = (end+start)//2
    if mid > val:
      end = mid
    else:
      start = mid
  if arr[start] == val:
    return start
  elif arr[end] == val:
    return end
  else:
    return -1
"""
import random


def lshift(arr, n):
    return (arr[:n][::-1] + arr[n:][::-1])[::-1]


class Solution(object):
    def findPivot(self, arr):
        start = 0
        end = len(arr)-1
        while arr[start] > arr[end] and end-start > 1:
            mid = (end+start)//2
            if arr[mid] > arr[start]:
                start = mid
            else:
                end = mid
            print("pivot subarr: {0}".format(arr[start:end+1]))

        if arr[start] < arr[end]:
            return end
        else:
            return start

        return mid

    def binSearch(self, arr, val, start, end):
        #print("binsearch: start = {0}, end = {1}".format(start, end))
        while end-start > 1:
            mid = (end+start)//2
            if arr[mid] > val:
                end = mid
            else:
                start = mid
            # print(arr[start:end+1])

        if arr[start] == val:
            return start
        elif arr[end] == val:
            return end
        else:
            return - 1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        pivot = self.findPivot(nums)
        #print("pivot: {0}".format(pivot))
        if nums[0] <= target <= nums[pivot]:
            return self.binSearch(nums, target, 0, pivot)
        else:
            return self.binSearch(nums, target, pivot, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.findPivot([5, 6, 7, 8, 9, 0, 1, 2, 3, 4]))
    assert s.search([5, 1, 3], 5) == 0
    assert s.search([5, 1, 3], 3) == 2
