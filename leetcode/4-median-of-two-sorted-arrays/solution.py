"""
There are two sorted arrays nums1 and nums2 of size m and n respectively. Find the
median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
---------------------------------------
Luke and I tried this problem a few months ago and neither of us could figure it out.
We looked at the solution, which I didn't try to read in depth. It was highly mathematical
and didn't seem intuitive at all.

"median" is the value that separates the upper and lower half of the data set;
this does not have to be a member of the set itself.

can we just get the min of the two arrays, the max, and get the midpoint value?
if the max element is 100 and the min is 0, is 50 always the median? No,
what if the set is [100,99,99,99,99,0]?

Brute force / linear time solution:
  - create a third list by merging the two, get median

What possible cases exist?
- lists overlap: [1,3], [2,4]
- one list "contains" another: [1,4], [2,3]
- lists do not overlap: [1,2], [3,4]
- any of the above, plus duplicates exist: [1,2,3], [3,4,5]

logarithmic time:
  - we do not need to look at every element; why is this possible?
    - is there a recurrence? is there some way we can solve subproblems by halving the problem size?
      - don't think so; not sure if there's a way to compute medians from subsets, especially given falsify()
  - since the arrays are sorted, we can binary search them for any element; what element do we want to find?
  - finding the median element of each list and then averaging them appears to work for my current test cases;
    - is there a case where this won't work?
    - start with a list with a median, divide it into two such that the medians do not average to the original median
    - say A = [1,2,...,100]; if B = [1...99] and C = [100], it will not work. See falsify()
  - solving a smaller problem; can we find the median of a single sorted list in logarithmic time?
  - does having the median of each array help us at all?
    - It definitely looks like the overall median will fall between the median of each array.
    - Not strictly in the middle though
  - Is there a way to treat the two arrays as one array without actually merging them?

- Looking at discussion titles
  - seems like O(log(min(m,n))) is the fastest / optimal solution

"""
import statistics
import random


def falsify():
    """
    This demonstrates that finding the median of each array
    and then averaging will not work.
    """
    A = [i for i in range(1, 100)]
    mA = statistics.median(A)
    B = A[:-1]
    mB = statistics.median(B)
    C = [A[-1]]
    mC = statistics.median(C)
    print(mA)  # 50.0
    print(mB)  # 49.5
    print(mC)  # 99
    print((mC+mB)/2)  # 74.25


def myMedian(arr):
    if len(arr) % 2 != 0:
        return arr[len(arr) // 2]
    else:
        right = len(arr) // 2
        left = right-1
        return (arr[left] + arr[right]) / 2


class BruteForceSolution:
    # This solved the problem, but is in O(N*log(N)) time
    def findMedianSortedArrays(self, nums1, nums2):
        arr = sorted(nums1+nums2)
        if len(arr) % 2 != 0:
            return arr[len(arr) // 2]
        else:
            right = len(arr) // 2
            left = right-1
            return (arr[left] + arr[right]) / 2


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([1, 2, 3], [3, 4, 5], 3.0),
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([100, 99, 99], [99, 99, 99, 0], 99),
        ([100], [99, 99, 99, 99, 99, 0], 99),
        ([100, 99, 99, 99, 99, 99], [0], 99),
    ]
    reallyBadLeft = []
    reallyBadRight = []
    for i in range(101):
        if random.randint(1, 100) % 2 == 1:
            reallyBadLeft.append(i)
        else:
            reallyBadRight.append(i)
    cases.append((reallyBadLeft, reallyBadRight, 50))

    for case in cases:
        print("--"*20)
        arr1, arr2, answer = case
        print("arr1: {0}".format(arr1))
        print("median: {0}".format(statistics.median(arr1)))
        print("arr2: {0}".format(arr2))
        print("median: {0}".format(statistics.median(arr2)))
        print("overall median: {0}".format(statistics.median(arr1+arr2)))
        assert s.findMedianSortedArrays(arr1, arr2) == answer
