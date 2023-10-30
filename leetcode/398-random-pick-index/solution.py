from collections import defaultdict
import random


class Solution:
    def __init__(self, nums: List[int]):
        self.vals = defaultdict(list)
        for idx, num in enumerate(nums):
            self.vals[num].append(idx)

    def pick(self, target: int) -> int:
        idx = random.randint(0, len(self.vals[target])-1)
        return self.vals[target][idx]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
