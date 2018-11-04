/*
Statement

Given an array with n integers, your task is to check if it could
become non-decreasing (increasing) by modifying at most 1 element. We define
an array is non-decreasing (increasing) if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Example 3:
Input: [3, 4, 2, 3]
Output: False

Example 4:
Input: [1, 2, 0]
Output: True

Note: The n belongs to [1, 10,000].
---
Understand / plan

We will assume that if the array is already non-decreasing,
the correct output is True

There are three possibilities:
- the most efficient number of changes involves increasing one value
in the array, i.e [1,2,3,0]
- the most efficient number of changes involves decreasing one value
in the array, i.e [7,2,3,4]
- the array requires more than one change to make into a non-decreasing
array: [3,2,3,2]

We can catch the first case by going L-to-R and setting R to L if
R < L, and the second case by going R-to-L and setting L to R if
L is greater than R; we have to do both though - if nums[0] is max(nums),
the L to R run will try to set every value to the right of R when all we need
to do is lower nums[0]; the same occurs for the R to L approach. Then, having
kept track of how many changes we made, return whether either of them were 1 or less.

There is a more complicated constant-space solution, but this one beats 97% of other
Golang solutions.
*/
package main

import (
	"fmt"
)

// O(n) space and time solution
func checkPossibility(nums []int) bool {
	var rToLChanges int
	var lToRChanges int
	rToLNums := make([]int, len(nums))
	copy(rToLNums, nums)

	for i := 0; i < len(nums)-1; i++ {
		if nums[i] > nums[i+1] {
			nums[i+1] = nums[i] + 1
			lToRChanges++
		}
	}

	for i := len(rToLNums) - 1; i > 0; i-- {
		if rToLNums[i-1] > rToLNums[i] {
			rToLNums[i-1] = rToLNums[i]
			rToLChanges++
		}
	}

	return rToLChanges <= 1 || lToRChanges <= 1
}

func main() {
	a := [3]int{4, 2, 3}
	b := [3]int{4, 2, 1}
	c := [4]int{3, 4, 2, 3}
	d := [5]int{1, 2, 5, 3, 3}

	fmt.Println(checkPossibility(a[:]) == true)
	fmt.Println(checkPossibility(b[:]) == false)
	fmt.Println(checkPossibility(c[:]) == false)
	fmt.Println(checkPossibility(d[:]) == true)

}
