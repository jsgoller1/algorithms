from collections import Counter, defaultdict


class Solution:
    def threeSum(self, nums):
        nums = [val for val, count in Counter(
            nums).items() for _ in range(min(3, count))]

        solutions = set()
        cache = {num: k for k, num in enumerate(nums)}
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                delta = -nums[i]-nums[j]
                if delta in cache and len(set((i, j, cache[delta]))) == 3:
                    solutions.add(
                        tuple(sorted((nums[i], nums[j], delta))))
        return [list(sol) for sol in solutions]


class SolutionCubic:
    def threeSum(self, nums):
        solutions = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    if (nums[i] + nums[j] + nums[k] == 0) and len(set([i, j, k])) == 3:
                        solutions.add(
                            tuple(sorted((nums[i], nums[j], nums[k]))))
        return [list(sol) for sol in solutions]


class SolutionSlow:
    def threeSum(self, nums):
        solutions = set()
        nums = Counter(nums)
        for i in nums.keys():
            for j in nums.keys():
                k = ((0 - i) - j)
                if k in nums:
                    possible = Counter([i, j, k])
                    if nums[i] >= possible[i] and nums[j] >= possible[j] and nums[j] >= possible[k]:
                        solutions.add(tuple(sorted([i, j, k])))
        return [list(solution) for solution in solutions]


s = Solution()
for case, expected in [
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]])
]:
    actual = s.threeSum(case)
    assert sorted(actual) == sorted(
        expected), f"{case}: {sorted(actual)} != {sorted(expected)}"
