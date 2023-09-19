"""
- create an array called "compressed" with the same size as weights.
- init rsum = -1  
- for idx, weight in enum(weights):
     rsum += weight
     compressed[idx] = rsum
- pick a random k number between 0 and sum(weights)-1
- idx = len(compressed)-1
- while k < compressed[idx]:
      idx -= 1
- return idx
"""
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.weights = w
        self.upper_bound = sum(w)-1
        self.compressed = [0 for val in w]
        rsum = -1
        for idx, weight in enumerate(w):
            rsum += weight
            self.compressed[idx] = rsum

    def pickIndex(self) -> int:
        k = random.randint(0, self.upper_bound)
        idx = 0
        # print(f"weights: {self.weights}")
        # print(f"compressed: {self.compressed}")
        # print(f"k: {k}")
        while self.compressed[idx] < k:
            idx += 1
        # print(f"idx: {idx}")
        return idx


s = Solution([3, 14, 1, 7])
print(s.pickIndex())
