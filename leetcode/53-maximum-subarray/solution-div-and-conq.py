def find_max_crossing_subarray(arr, lo, mid, hi):
    l_sum = r_sum = -float('inf')
    l_csum = r_csum = 0
    for l in range(mid, lo-1, -1):
        l_csum += arr[l]
        max_left = l if l_csum > l_sum else max_left
        l_sum = max(l_sum, l_csum)

    for r in range(mid+1, hi+1):
        r_csum += arr[r]
        max_right = r if r_csum > r_sum else max_right
        r_sum = max(r_sum, r_csum)
    return (max_left, max_right, l_sum + r_sum)


def find_maximum_subarray(arr, lo, hi):
    if hi == lo:
        return (lo, hi, arr[lo])

    mid = (hi + lo) // 2
    l_lo, l_hi, l_sum = find_maximum_subarray(arr, lo, mid)
    r_lo, r_hi, r_sum = find_maximum_subarray(arr, mid+1, hi)
    c_lo, c_hi, c_sum = find_max_crossing_subarray(arr, lo, mid, hi)

    best = max(l_sum, r_sum, c_sum)
    if best == l_sum:
        return (l_lo, l_hi, l_sum)
    elif best == r_sum:
        return (r_lo, r_hi, r_sum)
    return (c_lo, c_hi, c_sum)


class Solution:
    def maxSubArray(self, arr):
        return find_maximum_subarray(arr, 0, len(arr)-1)[2]


s = Solution()
cases = [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([0], 0),
    ([-1], -1),
    ([-2147483647], -2147483647),
    ([-3, -2, -1], -1),
    ([-3, -2, 1], 1)

]
for arr, expected in cases:
    actual = s.maxSubArray(arr)
    assert expected == actual, f"{arr}, {expected} != {actual}"
