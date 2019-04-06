"""
Given a non negative integer number num. For every numbers i
in the range 0 ≤ i ≤ num calculate the number of 1's in their
binary representation and return them as an array.

Example 1:
Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]

Follow up:
It is very easy to come up with a solution with run time O(n*sizeof(integer)).
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).

Can you do it like a boss? Do it without using any builtin function like
__builtin_popcount in c++ or in any other language.

Input: int
Output: array of int, number of set bits in [0,...,n-2, n-1, n]

Constraints:
  - O(N) space, O(N) for integers
-------------------------------------------------------------------------
Brute force (O(n)*O(int size)):
  - for each integer, count bits with Kernighan's method:
    count = 0
    while(n != 0):
      n &= n-1
      count++
  - cache results

DP method:
  - can we use the same method as above, but caching and depending on the result?
  - What does knowledge of a previous number's bit count tell us about the next
    number?
  - all powers of 2 have 1 bit set
  - We can initialize with 0,1,2
  - if the lowest bit of n is 1, n has as many bit set as n-1, plus 1. (thus we can set half of them starting with 1.)
  - if the lowest bit of n is 0,

- Start with base case 0 and 1. Write recursive method that appends 0 or 1 to given input. If the resultant number is larger
than n, return empty. Otherwise, assign to return value and recurse. At the end, return the retval

Cases:
  - Program starts bottom up with '', and either has a string of all 1s or a string of all 0s
  - input ranges from 0 to num and includes num and zero
"""


class Solution:
    def recurse(self, bitstr, count, num, solution):
        zerobitstr = bitstr + '0'
        zeroval = int(zerobitstr, 2)
        if 0 < zeroval <= num:
            solution[zeroval] = count
            self.recurse(zerobitstr, count, num, solution)

        onebitstr = bitstr + '1'
        oneval = int(onebitstr, 2)
        if oneval <= num:
            solution[oneval] = count+1
            self.recurse(onebitstr, count+1, num, solution)

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        solution = [0 for i in range(num + 1)]
        self.recurse('', 0, num, solution)
        return solution


if __name__ == '__main__':
    s = Solution()
    assert s.countBits(5) == [0, 1, 1, 2, 1, 2]
    assert s.countBits(2) == [0, 1, 1]
