"""
- Need to look right and swap
- if array is perfectly reverse sorted, reverse it to get lowest
- Start from rightmost / least sig.
- Find first number to the left less than it. Swap it.
- then sort everything to the right of that number. 
- If no number less, just sort entire array. 
"""


class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, -1, -1):
            for j in range(len(nums)-1, i, -1):
                if nums[i] < nums[j]:
                    # print(f"original: {nums}")
                    # print(
                    #    f"Swapping nums[{i}] ({nums[i]}) < nums[{j}] ({nums[j]})")
                    nums[i], nums[j] = nums[j], nums[i]
                    # print(f"swapped: {nums}")
                    nums[i+1:] = sorted(nums[i+1:])
                    # print(f"sorted: {nums}")
                    return
        nums.sort()


s = Solution()
for i, case in enumerate([
    # ([1], [1]),
    # ([1, 2, 3], [1, 3, 2]),
    # ([3, 2, 1], [1, 2, 3]),
    # ([2, 3, 1], [3, 1, 2]),
    # ([1, 1, 5], [1, 5, 1]),
    # ([1, 2, 3, 4, 5], [1, 2, 3, 5, 4]),
    # ([1, 2, 3, 5, 4], [1, 2, 4, 3, 5]),
    # ([1, 2, 4, 3, 5], [1, 2, 4, 5, 3]),
    ([1, 2, 4, 5, 3], [1, 2, 5, 3, 4]),
    ([2, 3, 4, 5, 1], [2, 3, 5, 1, 4]),
    ([4, 2, 0, 2, 3, 2, 0], [4, 2, 0, 3, 0, 2, 2])
]):
    arr, expected = case
    s.nextPermutation(arr)
    assert arr == expected, f"{i}: {arr} != {expected}"
    print("------------")
