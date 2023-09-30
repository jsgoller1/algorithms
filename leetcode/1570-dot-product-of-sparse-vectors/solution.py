from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vals = {i: v for i, v in enumerate(nums)}

    # Return the dotProduct of two sparse vectors

    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for k, v in self.vals.items():
            if k in vec.vals:
                total += (v * vec.vals[k])
        return total


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
cases = [
    (SparseVector([]), SparseVector([]), 0),
    (SparseVector([1, 0, 1]), SparseVector([0, 1, 0]), 0),
    (SparseVector([1, 1, 1]), SparseVector([0, 1, 0]), 1),
]
for v1, v2, expected in cases:
    actual = v1.dotProduct(v2)
    assert actual == expected, f"{v1.vals} dot {v2.vals}: {actual} != {expected}"
