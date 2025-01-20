"""
For m calls against n weights:
- Store sorted version of weights array (nlogn)
- For picking, select random number between 0 and sum(weights), then binsearch for candidate
  (mlogn)
O(n) for space
sorting 10,000 weights isn't hard to do, and binsearching them 10,000 times is probably fine

Is there a way to do lookups in constant time based on ranges?

"""
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        rsum = 0
        self.arr = []
        for val in w:
            rsum += val
            self.arr.append(rsum)
        self.weights_total = rsum

    def pickIndex(self):
        random_value = random.randint(1, self.total_sum)
        return bisect.bisect_left(self.prefix, random_value)


s = Solution([1, 5, 1, 3, 5])
s.pickIndex()
