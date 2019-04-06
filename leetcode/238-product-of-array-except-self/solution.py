"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is
equal to the product of all the elements of
nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for
the purpose of space complexity analysis.)

------------------------------------------------------------
Input: List[int]
Output: List[int]

Constraints:
  - Should be O(n) execution
  - Should not use division
  - Challenge: O(c) soace

- Brute force - O(n^2) time / O(n) space
  - Create new solution array
  - For each in input array, multiply all other elements
  and store result
  - Return result

- Division - O(n) space/time
  - Create solution array
  - Get product of all elements in input array
  - For each in input array, store total product / each in solution array
    - Note that this breaks when the item in the array is 0
  - Return solution

- Without division - O(n) space/time
  - Left products / right products combination
  - Keep two arrays; one of running products multiplied left to right, other r-to-l
  - solution arr[i]= rights[i-1] * lefts[i+i] or just lefts/rights of that if i is boundary

- No division - O(c) space
  - Repeat the above, but instead of lefts / rights arr, use solution:
    - initialize solution to size of nums, as Nones
    - store l-to-r pass in solution, only storing in solution[1] to solution[-2]
    - store final product at end of arr
    - do the r-to-l pass from r to l, multiplying running product against existing entry
    - store final product as first element of solution
"""


class Solution(object):
    def productExceptSelfLinear(self, nums):
        solution = []
        lefts = []
        current = 1
        for each in nums:
            current *= each
            lefts.append(current)

        rights = []
        current = 1
        for each in nums[::-1]:
            current *= each
            rights.append(current)
        rights = rights[::-1]

        solution.append(rights[1])
        for i in range(1, len(nums)-1):
            solution.append(lefts[i-1]*rights[i+1])
        solution.append(lefts[-2])
        return solution


if __name__ == '__main__':
    s = Solution()
    tests = [
        [10, 20],
        [0 for _ in range(20)],
        [i for i in range(1, 20)],
        [-i for i in range(1, 20)]
    ]
    for test in tests:
        expected = divisionSolution(test)
        actual = s.productExceptSelf(test)
        print("test: {0}\n actual: {1}\n expected: {2}".format(
            test, actual, expected))
        assert actual == expected
