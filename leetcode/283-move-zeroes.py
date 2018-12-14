"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

In: list[int]
Out: list[int]
--------------------------------------------
- Since deques are implemented as doubly linked
lists, we can be relatively confident that deletions
will occur in O(1) time if we have a pointer to a specific node.
- Append is also an O(1) operation
- As such, the following algorithm is O(n):
  - j = len
  - i = 0
  - while i <j:
    - if nums[i] == 0:
      - delete it from nums, append it to end of nums
      - j--
    - i++

- Actually lists should be at least singly-linked lists,
so the O(1) append and delete should be true too. Let's try
it with that first.

- Above didn't work; we wind up advancing i and skipping over zeroes
- Instead, let's try something like having a "partition" element, where if it's
zero, we delete and move to the tail of nums, else we advance the partition element

"""

class Solution:
    def moveZeroes(self, nums):
      nonzero = 0
      for i in range(len(nums)):
        if nums[nonzero] == 0:
          del nums[nonzero]
          nums.append(0)
        else:
          nonzero += 1

if __name__ == '__main__':
  s = Solution()
  tests = [
    ([0,1,0,3,12], [1,3,12,0,0]),
    ([0,0,1], [1,0,0])
  ]
  for test in tests:
    print("="*25)
    s.moveZeroes(test[0])
    print(test[0])
    assert test[0] == test[1]
