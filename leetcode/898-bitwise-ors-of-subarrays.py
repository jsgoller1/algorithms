"""
- number of contiguous subarrays of array N is N!
- If we have [1,2,3,4], what work is unnecessary?
            001, 010, 011, 100
  - 01 | 10 | 11 is unnecessary, as is (001 | 010 | 011 | 100) given (011 | 100)
"""
import itertools


class Solution(object):
    def subarrayBitwiseORs(self, A):
        ans = set()
        cur = {0}
        for x in A:
            #print("x:", bin(x))
            cur = {x | y for y in cur} | {x}
            #print("cur: ", [bin(val) for val in cur])
            ans |= cur
            #print("ans: ", [bin(val) for val in ans])
        return len(ans)


if __name__ == '__main__':
    s = Solution()
    assert s.subarrayBitwiseORs([1, 2, 4]) == 6
    #assert s.subarrayBitwiseORs([0]) == 1
    #assert s.subarrayBitwiseORs([1, 1, 2]) == 3
