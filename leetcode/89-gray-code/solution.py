"""
The gray code is a binary numeral system where two successive values differ in only one bit. Given a non-negative
integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1

Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].

Example from Wikipedia:
Decimal	Binary	Gray
0	      0000	  0000
1	      0001	  0001
2	      0010	  0011
3	      0011	  0010
4	      0100	  0110
5	      0101	  0111
6	      0110	  0101
7	      0111	  0100
8	      1000	  1100
9	      1001	  1101
10	    1010	  1111
11	    1011	  1110
12	    1100	  1010
13	    1101	  1011
14	    1110	  1001
15	    1111	  1000

10

--------------------------------------------------------------------------
In: int (length of bit vector)
Out: list, integers who form the full gray encoding of n bits, but are interpreted in base two

- My math prof. Paul Young tried to teach me about Gray encoding during Discrete Math II at C of C but I was too much of
an arrogant ass at the time to value his teaching. Prof. Young, if you ever read this, I'm sorry I was such a prick.

- For this problem, the core question is "how do we decide which bit to flip for the next number". There are apparently many ways.
- We also need to make sure that the selection is cyclic; we should only have to flip one bit to go from the highest number representable with our
encoding to 0.
- We also need to make sure that as we do our unsetting, we never create a bit pattern we've already used before.
  - If this were a graph problem, this would mean there are no cycles (except between the largest element and 0)
- I remember Prof. Young drawing a graph of some kind but I don't remember what the nodes or edges were.

- Wikipedia says we can do the following:
  - start with 1-bit vectors [0,1]
  - created "reflected" the list by reading it backwards: [1, 0]
  - prefix old entries with 0 [00, 01] and old entries with 1 [11,10]
  - append: [00,01,11,10]
  - Repeat this procedure to go from any n-bit gray code to n+1 bit gray code.
------------------------------------------------------------------------------
- We have the above listed gray code procedure for generating n->n+1 bit gray codings
- To do this in code to solve the problem
  - start with [0,1] as strings
  - do the above procedure from 1 to i = n
  - finally, convert all strings to bin
"""
class Solution():
  def grayCode(self, bitlen):
    vals = ["0", "1"]
    if bitlen == 0:
      return [0]
    for i in range(1, bitlen):
      reflected = vals[::-1]
      for i, val in enumerate(vals):
        vals[i] = "0"+val
      for i, val in enumerate(reflected):
        reflected[i] = "1"+val
      vals += reflected

    return [int(val,2) for val in vals]

if __name__ == '__main__':
  s = Solution()
  assert s.grayCode(2) == [0,1,3,2]
  assert s.grayCode(0) == [0]
