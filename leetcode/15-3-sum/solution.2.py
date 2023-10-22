from collections import defaultdict


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = set()

        seen = defaultdict(set)
        for idx, num in enumerate(nums):
            seen[num].add(idx)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]
                c = -(a+b)
                count = (i in seen[c]) + (j in seen[c])
                if c in seen and count < len(seen[c]):
                    solutions.add(tuple(sorted((a, b, c))))
        return [list(solution) for solution in solutions]

    def threeSumCubic(self, nums: List[int]) -> List[List[int]]:
        solutions = set()
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for k in range(j, len(nums)):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0 and (i != j and i != k and j != k):
                        solutions.add(tuple(sorted((a, b, c))))
        return [list(solution) for solution in solutions]
