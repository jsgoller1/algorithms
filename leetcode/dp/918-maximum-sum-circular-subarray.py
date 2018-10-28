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
        maxCache = {}
        minCache = {}
        total = 0
        nonnegCount = 0
        for i, val in enumerate(A):
            if val >= 0:
                nonnegCount += 1
            total += val
            minCache[i] = self.minSubarraySum(i, A, minCache)
            maxCache[i] = self.maxSubarraySum(i, A, maxCache)

        #print("nonnegCount: {0}".format(nonnegCount))
        if nonnegCount == 0:
            return max(A)
        else:
            maxVal = maxCache[max(maxCache, key=maxCache.get)]
            minVal = minCache[min(minCache, key=minCache.get)]
            #print("maxVal: {0}".format(maxVal))
            #print("minVal: {0}".format(minVal))
            #print("total: {0}".format(total))
            return max(maxVal, total - minVal)

    def maxSubarraySum(self, i, arr, cache):
        if i in cache:
            return cache[i]
        if i == 0:
            return arr[0]
        else:
            return max(self.maxSubarraySum(i - 1, arr, cache) + arr[i], arr[i])

    def minSubarraySum(self, i, arr, cache):
        if i in cache:
            return cache[i]
        if i == 0:
            return arr[0]
        else:
            return min(self.minSubarraySum(i - 1, arr, cache) + arr[i], arr[i])


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
