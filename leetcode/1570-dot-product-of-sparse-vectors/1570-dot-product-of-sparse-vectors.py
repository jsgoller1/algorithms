class SparseVector:
    def __init__(self, nums: List[int]):
        self._nums = nums
        self._idxs = set([i for i, val in enumerate(nums) if val != 0])

    def dotProduct(self, vec: 'SparseVector') -> int:
        shared_idxs = self._idxs & vec._idxs
        dp = 0
        for idx in shared_idxs:
            dp += (self._nums[idx] * vec._nums[idx])
        return dp

        # Your SparseVector object will be instantiated and called as such:
        # v1 = SparseVector(nums1)
        # v2 = SparseVector(nums2)
        # ans = v1.dotProduct(v2)
