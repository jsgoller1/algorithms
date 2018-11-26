"""
If we have [1,1,2,3], we can either increment
one of the 1s, the 2, and the 3, or we can incrememnt
one of the 1s 3 times.

We must modify every non-unique integer in the array.

What if we loop through the array, and for each non-unique
int we find, incremement it until it is unique and add the
number of total increments to a running sum? Any edge cases?
  - [1,1,2,3,4,5,6,7...n] is probably the worst case
  - [1,1,1,1,1,1,1,1,1...n] is worse
- What kind of suboptimal moves exist? Are there any incrementing cases where
we do more work than necessary?

- If I am looking at a value in the array and it is non-unique, can I find out in
O(c) time what the minimum number of moves to make it unique is?
"""

class Solution:
    def minIncrementForUnique(self, A):
        total = 0
        uniques = set()
        for val in A:
            while val in uniques:
              val += 1
              total +=1
            uniques.add(val)
        return total

if __name__ == '__main__':
  s = Solution()
  assert s.minIncrementForUnique([4,3,2,1,0,0]) == 5
  assert s.minIncrementForUnique([1,2,2]) == 1
  assert s.minIncrementForUnique([3,2,1,2,1,7]) == 6
  assert s.minIncrementForUnique([1,1,1]) == 3
  assert s.minIncrementForUnique([]) == 0
