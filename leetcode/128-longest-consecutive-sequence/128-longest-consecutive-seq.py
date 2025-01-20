class SolutionVerbose:
    """
    This is similar to union-find, but instead tracks "ranges" and merges them. 
    """

    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0

        lcs = 1
        ranges = {}
        for val in set(nums):
            lo = val-1
            hi = val+1
            lo_range = ranges[lo] if lo in ranges else None
            hi_range = ranges[hi] if hi in ranges else None

            if not (lo_range or hi_range):
                ranges[val] = (val, val)

            elif lo_range and not hi_range:
                l, r = lo_range
                new_lo = (l, val)
                del ranges[r]
                ranges[l] = new_lo
                ranges[val] = new_lo
                lcs = max(lcs, abs(val - l) + 1)

            elif hi_range and not lo_range:
                l, r = hi_range
                new_hi = (val, r)
                del ranges[l]
                ranges[r] = new_hi
                ranges[val] = new_hi
                lcs = max(lcs, abs(r-val) + 1)

            else:  # hi_range and lo_range:
                new_range = (lo_range[0], hi_range[1])
                del ranges[lo_range[1]]
                del ranges[hi_range[0]]
                ranges[lo_range[0]] = new_range
                ranges[hi_range[1]] = new_range
                lcs = max(lcs, abs(new_range[1] - new_range[0]) + 1)

        return lcs


s = Solution()
for i, case in enumerate([
    ([4, 2, 2, -4, 0, -2, 4, -3, -4, -4, -5, 1, 4, -9, 5,
      0, 6, -8, -1, -3, 6, 5, -8, -1, -5, -1, 2, -9, 1], 8),
    ([100, 1, 200, 3, 2, 4], 4),
    ([1, 2, 3, 4, 5], 5),
    ([18, 19, 0, 12, 5, 4, 10, 3, 16, 6, 11, 15, 13, 14, 2, 17, 8, 9, 1, 7], 20),
    ([18, 19, 0, 12, 5, 4, 9, 3, 16, 6, 11, 15,
     13, 14, 2, 17, 8, 9, 1, 7], 10)  # 10 missing

]):
    arr, expected = case
    actual = s.longestConsecutive(arr)
    assert actual == expected, f"{i}, {arr}: {actual} != {expected}"
