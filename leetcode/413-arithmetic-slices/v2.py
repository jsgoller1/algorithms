"""
A sequence of number is called arithmetic if it consists of at least three
elements and if the difference between any two consecutive elements is the same.
For example, these are arithmetic sequence:
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9

The following sequence is not arithmetic.
1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given. A slice of that
array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of array A is called arithmetic if the sequence:
A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means
that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.
----------------
Reattempting this problem because I saw someone working on it during Open Mat
and I don't understand how I did it the first time

In: list[int]
Out: int
Constraints:
  - List could be empty
  - List could be very large

- A recurrence definitely exists here, with overlapping subcases:
f([1,2,3]) -> [1,2,3]
f([2,3,4]) -> [2,3,4]
f([1,2,3,4]) -> [1,2,3], [2,3,4], [1,2,3,4]
f([2,3,4,5]) -> [2,3,4], [3,4,5], [2,3,4,5]
f([1,2,3,4,5]) -> [1,2,3], [2,3,4], [3,4,5], [1,2,3,4], [2,3,4,5], [1,2,3,4,5]

- We can explicitly how many arithmetic subarrays an array contains:
f(3) = 1
f(4) = 1 (of len 4) + 2 (of len 3) = 3
f(5) = 1 (of len 5) + 2 (of len 4) + 3 (of len 3) = 6
f(6) = 1 (of len 6) + 2 (of len 5) + 3 (of len 4) + 4 (of len 3) = 10
This basically is 1 + 2 + 3 + 4, where we start with f(n) and decrement n to
go to the next term until n = 3. The explicit solution is n(n+1)/2

So the algorithm here is:
  - Keep a running sum
  - Scan the array linearly, finding all arithmetic slices (do not look for subslices,
  just the overall slice).
  - Explicitly calculate the count of number of subslices based on the arithmetic progression above.
  E.g.
  [1,2,3,-2,5,8,11,14,-2,1,2,3]
  [1,2,3]  [5,8,11,14]  [1,2,3]
    1         3           1
          total = 5

Finding all slices is a trickier operation than it sounds like. Two cases:
[1, 2, 5, 8] -> [2,5,8]
  If we start looking at [1,2,5], we need to advance start and end by 1
[1, 2, 3, 4, 5, 8, 11] -> [1,2,3,4,5], [5,8,11]
  - here, start will be 0 and end will be 4, but since 8 won't fit in the first sequence, we need to set start to 5 and end to 7
-----------------------------------------------------------------------------
The above works, but can be greatly simplified; below implements the "formula" version (worked before I looked but simplified
how the pointers are modified)
"""


class Solution:
    def numberOfArithmeticSlices(self, A):
        if len(A) < 3:
            return 0
        total = 0
        start, end = 0, 2
        n = 0
        while (end < len(A)):
            if A[start + 1] - A[start] == A[end] - A[end-1]:
                n += 1
            else:
                total += (n * (n + 1)) // 2
                n = 0
            start += 1
            end += 1

        if n > 0:
            total += (n * (n + 1)) // 2
        return total


if __name__ == '__main__':
    s = Solution()
    #assert s.numberOfArithmeticSlices([]) == 0
    #assert s.numberOfArithmeticSlices([1, 2, 5, 8])
    #assert s.numberOfArithmeticSlices([1, 2, 3, 4, 5, 8, 11])
    assert s.numberOfArithmeticSlices([1, 2, 3, -2, 5, 8, 11, 14, -2, 1, 2, 3]) == 5
    assert s.numberOfArithmeticSlices([0, 2, 5, -1]) == 0
    assert s.numberOfArithmeticSlices([1, 2, 3, 4]) == 3
    assert s.numberOfArithmeticSlices([1, 1, 1, 1, 1]) == 6
