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
in the array, i.e [3,2,3,4]
- the array requires more than one change to make into a non-decreasing
array: [3,2,3,2]



*/
package main

import (
	"fmt"
	"math"
)

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
		if rToLNums[i-1] >= rToLNums[i] {
			rToLNums[i-1] = rToLNums[i] - 1
			rToLChanges++
		}
	}

	// fmt.Println(lToRChanges, rToLChanges)
	return math.Min(float64(rToLChanges), float64(lToRChanges)) <= 1.0
}

func main() {
	a := [3]int{4, 2, 3}
	b := [3]int{4, 2, 1}
	c := [4]int{3, 4, 2, 3}

	fmt.Println(checkPossibility(a[:]))
	fmt.Println(checkPossibility(b[:]))
	fmt.Println(checkPossibility(c[:]))
}
