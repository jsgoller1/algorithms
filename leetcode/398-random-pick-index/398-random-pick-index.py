from random import randint
from collections import defaultdict


class Solution:

    def __init__(self, nums: List[int]):
        self.mapping = defaultdict(list)
        for idx, num in enumerate(nums):
            self.mapping[num].append(idx)

    def pick(self, target: int) -> int:
        idxs = self.mapping[target]
        choice = random.randint(0, len(idxs)-1)
        return idxs[choice]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
