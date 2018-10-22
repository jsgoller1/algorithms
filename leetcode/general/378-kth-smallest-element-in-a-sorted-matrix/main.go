/*
Statement

Given a n x n matrix where each of the rows and columns
are sorted in ascending order, find the kth smallest
element in the matrix.

Note that it is the kth smallest element in the
sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8, return 13.

Constraints
- You may assume k is always valid, 1 ≤ k ≤ n2.
- Does NOT say every element will be distinct

----------------------------
Understand

- Matrix is sorted in ascending order; an entry will always be less than the entry below it and to the right
- The fact that entry below the current is greater than the current does not mean the one below is greater than the one to the right
- Is there any reason we can't just treat the array as a contiguous array of integers and then get contiguous[k]?
	- How are they finding 13 given the matrix above? What does "kth smallest element in the sorted order" mean?
	- It means that, assuming every element in the matrix was sorted into a contiguous array, you'd find
		the kth element
		- Contiguous ordering: 1, 5, 9, 10, 11, 13, 12, 13, 15
		- Sorted contiguous order: 1, 5, 9, 10, 11, 12, 13, 13, 15
			 k = 8 returns 13
- Do we need to examine every matrix entry?
	- We could come up with a trivial solution where we keep a sorted array of distinct elements and then return
	the k-1th element. O(nlogn) execution and O(n) space
- What if starting at the top left we walk each row from left to right and each row top to bottom; we start with j and the top left element
as the value. Each time we find a value greater than the current, we update the new val to this value and increment j. We halt when j = k
	- Doesn't work with given array, 1

Cases:
	- Empty matrix (nil, empty array, array containing empty array): return -1
	- Singleton (single row or single column)
	- n x m matrix where n and m are 2 or greater

----------------------------
Plan / Pseudocode
- Unclear based on statement what "kth smallest element in the sorted order" means short of ordering contiguously and
	counting backwards from the last element
- Will try the above to see if I can find an edge case that breaks it
----------------------------
Execute / Review
- I initially tried the approach above, found that it broke for the given case, and then fell back to brute force. After it worked,
I looked at a few solutions and decided to implement this one: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85177/Java-1ms-nlog(max-min)-solution
*/
package main

import (
	"fmt"
	"sort"
)

// Brute force
func kthSmallest(matrix [][]int, k int) int {
	contiguous := make([]int, len(matrix)*len(matrix[0]))
	i := 0
	for row := 0; row < len(matrix); row++ {
		for col := 0; col < len(matrix[0]); col++ {
			contiguous[i] = matrix[row][col]
			i++
		}
	}

	sort.Ints(contiguous)
	return contiguous[k-1]
}

func main() {
	matrix1 := [][]int{
		[]int{1, 5, 9},
		[]int{10, 11, 13},
		[]int{12, 13, 15}}
	fmt.Println(kthSmallest(matrix1, 8)) // 13
	matrix2 := [][]int{
		[]int{1, 2},
		[]int{1, 3}}
	fmt.Println(kthSmallest(matrix2, 2)) // 1 (what? Why isn't this 2?)
}
