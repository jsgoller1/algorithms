# If we sort first, we can identify triplets via (l,m,r). Doing it this way,
# we have to try every element in the array for m (which takes O(n) time),
# and each iteration we can utilize an O(n) two-pointer technique, so the whole
# thing is O(n^2).

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solutions = []
        seen = set()
        for i, fixed_point in enumerate(nums):
            l, r = 0, len(nums)-1
            while l < i < r:
                a, b = nums[l], nums[r]
                total = a + fixed_point + b
                if total > 0:
                    r -= 1
                elif total == 0:
                    if (a, fixed_point, b) not in seen:
                        seen.add((a, fixed_point, b))
                        solutions.append([a, fixed_point, b])
                    l, r = l+1, r-1
                else:  # total < 0
                    l += 1
        return solutions
