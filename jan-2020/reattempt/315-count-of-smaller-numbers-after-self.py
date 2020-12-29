"""
You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number of smaller
elements to the right of nums[i].

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Constraints:
    0 <= nums.length <= 10^5 (up to 100,000 numbers)
    -10^4 <= nums[i] <= 10^4 (each number between -10,000 and 10,000)
-------------------------------------------------------------------------------
Possible cases:
  - Every element after is smaller
  - No elements after are smaller
  - Mixed

Brute force:
  Compare every element in the array to every other (n^2) - with up to 100k elements,
  would be 10b steps (10s according to skeina); would prefer to do better.

In:     [ 5,  2,  6,   1 ]
sorted: [ 1,  2,  5,   6 ]
diff:   ['X', 2, 'X', 'X']
ans:    [ 2   1   1    0 ]

Val   sorted idx    unsorted idx  
 1       0              3
 6       3              2
 2       1              1
 5       2              0

sorted idx: how many overall values are less than this one (e.g. for 0th element, there will be 0 elements less than it)
len(in) - 1 - unsorted idx: how many values are after this one in the original array; there are no more than this many less than it to the right of it

Val | vals less than this |    vals after this    | correct out value
 1            0                    0                  0  (0 vals after in unsorted, 0 of 3 others in sorted are less)
 6            3                1  (4 - 1 - 2)         1  (1 vals after in unsorted, 3 of 3 others in sorted are less)
 2            1                2  (4 - 1 - 1)         1  (2 vals after in unsorted, 1 of 3 others in sorted are less)
 5            2                3  (4 - 1 - 1)         2  (3 vals after in unsorted, 2 of 3 others in sorted are less)

- We do know that if for some n, if there are 3 vals after it in the unsorted but 2 after it in the sorted, it means at least one of them was less than it
in the unsorted.
- We can't go by the number of values after n in either array though: [5, 2, 6, 1] sorts to [1,2,5,6]; 2 doesn't
change position but has 1 value less than it in unsorted
- Number of diffs after doesn't help either; 2 elements after 2 are swapped, but only 1 element in the unsorted is less than it 

- Is there a way to re-use information?
  in:  [n, m, ...]
  out: [j, k, ...]
  - If we go L-R, we should have some way of knowing what we've seen already. 
  - if n > m:
    - j > k, but we don't know how much greater
    - j is between k+1 and however many elements are between m and then end:
      - Example where j (4) is more than k+1 (2):
        [10, 5, 7, 6, 1]
        [    1, ......]
  - if n < m:
    - j < k, but again, we don't know by how much.
        [ 2, 15, 4, 6, 1]
        [     3, .......]

- Could we use a tree or dictionary or some other structure (up to n memory) so that at each step we do O(1) operations
  to determine how many elements we've seen before?

BST approach that will be nlogn on average but n^2 for lists as they get closer to perfectly descending (i.e. 5,4,3,2,1):

create an empty BST
for each val in nums from right to left:
  insert val into tree; as we insert, keep track of how many right-turns we make in the tree
  store in tree as (val, count of right turns)

-------------------------
Looked at leetcode, worked through solution on board, need to re-attempt this one later. 

"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0 for num in nums]
        sorted_in = sorted(nums)  # O(nlogn)

        return ans


if __name__ == '__main__':
    s = Solution()
    cases = [
        ([5, 2, 6, 1], [2, 1, 1, 0]),
    ]
    for input_args, expected in cases:
        actual = s.countSmaller(input_args)
        assert expected == actual, f"{input_args}, {expected} != {actual}"
