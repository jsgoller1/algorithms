from random import random
from bisect import bisect_left

class Solution:
    def __init__(self, w: List[int]):
        self.data = []
        total = sum(w)
        rtotal = 0
        for val in w:
            rtotal += val / total
            self.data.append(rtotal)

    def pickIndex(self) -> int:
        return bisect_left(self.data, random.random())


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
