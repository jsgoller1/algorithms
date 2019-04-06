"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:
Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
-------------------------------------------------
In: List[int], Int
Out: None; modification is in-place

- The method we learned at Bradfield for right shifting(which was attributed to Bentley) is to
reverse the array, then reverse arr[0:k] and reverse arr[k:] -
  - arr [0,1,2,3,4,5,6,7,8,9], k = 3
  - reversed arr: [9,8,7,6,5,4,3,2,1,0]
  - reversed arr[:k] (0-2): [7,8,9,6,5,6,3,2,1,0]
  - reversed arr[k:] (3-9): [7,8,9,0,1,2,3,4,5,6]
- How about left shifting? Do the split reverse at arr[:len(arr)-k]
  - arr [0,1,2,3,4,5,6,7,8,9], k = 3
  - reversed arr: [9,8,7,6,5,4,3,2,1,0]
  - reverse arr[len-k:]: [9,8,7,6,5,4,3,0,1,2]
  - reverse arr[:len-k]: [3,4,5,6,7,8,9,0,1,2]
"""


class Solution(object):
    def subarrReverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotate(self, nums, k):
        if not nums:
            return nums

        k = k % len(nums)
        self.subarrReverse(nums, 0, len(nums) - 1)
        self.subarrReverse(nums, 0, k-1)
        self.subarrReverse(nums, k, len(nums)-1)


if __name__ == '__main__':
    s = Solution()
    testCases = [
        [[], 3, []],
        [[1, 2, 3], 0, [1, 2, 3]],
        [[1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]],
        [[1, 2, 3, 4, 5, 6, 7], 1123, [5, 6, 7, 1, 2, 3, 4]],
        [[-1, -100, 3, 99], 2, [3, 99, -1, -100]]
    ]
    for case in testCases:
        initial = case[0]
        k = case[1]
        expected = case[2]
        print(case, k)
        s.rotate(initial, k)
        print(initial)
        print(expected)
        assert initial == expected
        print("-"*30)
