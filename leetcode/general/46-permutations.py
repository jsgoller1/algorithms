"""
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Input: List
Output: List of lists

Constraints:
    - List might be very large
    - List contains integers
----------------------
- All permutations is going to be O(N!) for time and space;
we _have_ to examine every possible permutation.

- We might be able to write a clean recursive solution that takes a list of used
numbers and a list of unused numbers and recursively calls until there's no more
elements in the unused list.
- There is an edge case around a list containing duplicates - we can probably use a set for this
    - Can't use a set; lists are unhashable
    - use tuples instead of lists

Cases:
- Empty list; return empty
- Singleton; algorithm will run and return a list of the singleton contained in a list
- Multiple items in list; algorithm functions as expected
    - Each element is unique; ideal case
    - Nondistinct elements; will generate some duplicate cases that will be caught by the set
---------------
permutations(used, unused, permset)
    - if unused = []: // we could terminate this early with if len(unused) == 1
        permset[used] := true
        return
    - else:
        for each in unused:
            permutations(used+each, unused-each, permset)

Try: [1,2,3]
- permutations([], [1,2,3], {})
- permutations([1], [2,3], {}), permutations([2],
               [1,3], {}), permutations([3], [1,2], {})
- permutations([1,2], [3], {}), permutations([1,3], [2], {}), permutations([2,1], [3], {}), permutations([2,3], [1], {})...
*/
"""


class Solution:
    def generatePermutations(self, used, unused, permSet):
        if unused == []:
            print("Adding :", used)
            permSet.add(tuple(used))
            return

        for i in range(len(unused)):
            self.generatePermutations(
                used + [unused[i]], unused[:i] + unused[i+1:], permSet)
        return permSet

    def permute(self, nums):
        permSet = set()
        self.generatePermutations([], nums, permSet)
        return [list(perm) for perm in permSet]


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
    print(s.permute([1]))
    print(s.permute([]))
