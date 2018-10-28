"""
This problem was part of LeetCode Weekly Contest #105

- This is the same as the maximum subarray problem, except that we
must also account for subarrays that can be created by wrapping.
- If we reuse the solution from maximum subarrays, all we need to do
is generate the array that represents "wrapping", run the same routine on it,
and then pick the max of wrapped and regular arays.
- Above doesn't work for edge case #1

- Some facts:
    - Within every array, there is a maximum subarray and a minimum subarray,
    each of which may be 1 element.
    - The value of the maximum subarray is the sum of all the values not in the min subarray,
    and vice versa.
    - In a wrapping array, either the maximum subarray falls on the wrap point, or the minimum
    value does. It is not possible for both to be in the middle or both to wrap around. One edge
    case occurs where every value from 0 to n is in the max or min subarray, and every value
    from n+1 to len-1 is in the other.
    -

"""


class Solution:
    def maxSubarraySumCircular(self, A):
        total = 0
        currentMax = 0
        currentMin = 0
        maxVal = -float("inf")
        minVal = float("inf")
        for val in A:
            total += val
            currentMax = max(val, currentMax + val)
            currentMin = min(val, currentMin + val)
            maxVal = max(currentMax, maxVal)
            minVal = min(currentMin, minVal)

        if maxVal < 0:
            return maxVal
        else:
            return max(maxVal, total - minVal)


if __name__ == '__main__':
    s = Solution()
    assert s.maxSubarraySumCircular([1, -2, 3, -2]) == 3
    assert s.maxSubarraySumCircular([5, -3, 5]) == 10
    assert s.maxSubarraySumCircular([3, -1, 2, -1]) == 4
    assert s.maxSubarraySumCircular([3, -2, 2, -3]) == 3
    assert s.maxSubarraySumCircular([-2, -3, -1]) == -1

    # Edge case #1
    assert s.maxSubarraySumCircular([-2, 4, -5, 4, -5, 9, 4]) == 15

    # Edge case #2
    assert s.maxSubarraySumCircular([2, -2, 2, 7, 8, 0]) == 19
