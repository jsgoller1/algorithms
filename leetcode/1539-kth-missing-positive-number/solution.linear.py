class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = k
        for elem in arr:
            if elem <= missing:
                missing += 1
        return missing
