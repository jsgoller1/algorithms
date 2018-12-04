"""
In: two lists
out: 2-element list

A: 1, 4, 5, 10 == 20
B: 2, 3, 5, 6 == 16

A -2, B +2

[4, 2]

A: 1,2,5 == 8
B: 2,4 == 6

A -1, B +1

- get totals of each list
- set big to bigger, small to smaller
- get abs(big-small)
- select larger element in big and smaller element in small where larger-smaller = abs(big-small)/2
- this is basically the two sum problem; find two values who add to a specific value, except here we're looking
for the absolute value between them
---------------
Suppose Sa = total candy for alice, Sb = total candy for bob; given that a solution
always exists per the description, alice has some x and bob has some y such that
sA - x + y = sB + x - y
sA + 2y = sB + 2x
sA - sB = 2x - 2y
2y + sA - sB = 2x
2y - sB = 2x - sA
2y = 2x - sA + sB
2y = 2x + sB - sA
y = x + (sB-sA)/2

So bob must have some y such that we can find an x alice has and add (Sb - Sa)/2 to it to get y.
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        sA = sum(A)
        sB = sum(B)
        bob = set(B)
        for x in A:
            y = (x + (sB - sA) // 2)
            if y in bob:
                return [x, y]


if __name__ == "__main__":
    s = Solution()
    assert s.fairCandySwap(A=[1, 1], B=[2, 2]) == [1, 2]
    assert s.fairCandySwap(A=[1, 2], B=[2, 3]) == [1, 2]
    assert s.fairCandySwap(A=[2], B=[1, 3]) == [2, 3]
    assert s.fairCandySwap(A=[1, 2, 5], B=[2, 4]) == [5, 4]
