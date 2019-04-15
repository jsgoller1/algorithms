"""
Implement next permutation, which rearranges numbers into
the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it
as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples. Inputs are in the left-hand column
and its corresponding outputs are in the right-hand column:

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
-------------------------------------------------------
In: List[int]
Out: None, in-place modify

Constraints: None
  - Could be empty list, could be massive, values could be huge
  - How do we handle duplicates (per 115 -> 151, skip them)

- Brute force (not constant memory):
  - Sort all permutations and then change the array to the one directly after it in order. O(N!)

- Brute force: For each character, try swapping it with each other character and seeing if the
result is greater than the initial state. Set the array to the lowest of these. O(n^2)

- Recursive 'get min from remaining chars'?
- Does constant extra memory mean we can't use recursion because of stack frames?
- Lexicographic "next" can be achieved by just looking at each array as though
it's a single int.
- Look at each digit and ask "what's the next digit that should be here"?
- Can we do this without trying to convert to an int or string? Is
there a heuristics where we just compare int-to-int from right to left?
- How do we handle the 321->123 case where we wrap around?


1,2,3 → 1,3,2
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

3,2,1 → 1,2,3
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

1,1,5 → 1,5,1
[(1, 1, 5), (1, 5, 1), (5, 1, 1)]

- Per discussion titles, there is a linear time solution / one pass.

As a simpler problem, how do we get all permutations?
- We can recursively generate each one in O(N!) time by
selecting elements from the input set until the set is empty.

What does "next permutation" mean?
- characters are swapped such that the result is as close to the original
as possible but still greater

How do we know if we should swap characters in an array? How do we know when
we shouldn't?


"""
import itertools


class Solution:
    def nextPermutation(self, nums):
        perms = itertools.permutations(nums)
        print(sorted(perms))
        return


if __name__ == '__main__':
    s = Solution()
    tests = [
        ([1, 2, 3], [1, 3, 2]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 5], [1, 5, 1])
    ]
    for test in tests:
        s.nextPermutation(test[0])
        assert test[0] == test[1]
