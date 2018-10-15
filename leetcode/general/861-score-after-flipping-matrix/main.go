/*
Statement

We have a two dimensional matrix A where each
value is 0 or 1. A move consists of choosing any
row or column, and toggling each value in that
row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of
this matrix is interpreted as a binary number,
and the score of the matrix is the sum of
these numbers.

Return the highest possible score.

Example 1:

Input: [[0,0,1,1],
				[1,0,1,0],
				[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],
						[1,0,0,1],
						[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

How to get there:
- start
[0,0,1,1]
[1,0,1,0]
[1,1,0,0]
- flip all of row 0
[1,1,0,0]
[1,0,1,0]
[1,1,0,0]
- flip all of column 3
[1,1,0,1]
[1,0,1,1]
[1,1,0,1]
- flip all of column 2
[1,1,1,1]
[1,0,0,1]
[1,1,1,1]

Alternative path.
- start
[0,0,1,1]
[1,0,1,0]
[1,1,0,0]
- flip column 1
[0,1,1,1]
[1,1,1,0]
[1,0,0,0]
- flip column 3
[0,1,1,0]
[1,1,1,1]
[1,0,0,1]
- flip row 1
[1,0,0,1]
[1,1,1,1]
[1,0,0,1]
- flip column 1
[1,1,0,1]
[1,0,1,1]
[1,1,0,1]
- flip column 2
[1,1,1,1]
[1,0,0,1]
[1,1,1,1]

Constraints:
1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.

--------------------------------
Understand / Plan

- we want to set the highest possible bits
- are there moves we definitely don't want to do?
	- we don't want to set lower bits at the expense
	of unsetting higher bits
	- could we give each bit a "score"? Flipping a row [1 1 0 0]
		would unset the two high bits and set the low bits, so the score
		is b1 + b10 - b100 - b1000. We wouldn't want to take a move
		that results in a negative score.
- how do we know when we've found the highest?
	- we can't make any move that make the matrix a higher score
	- is there a case where we've deadlocked ourselves at a lower
	score that might not be the highest score, but no moves are possible?
		- (weak thought-proof) that would be contradictory: it would mean that across the matrix,
		we cannot make any values higher than they currently are, but there is
		some combination of values that is greater than what it is now. If it's
		column, then somehow we'd be able to set the bits higher without being able to set them,
		or a row that could be increased without being able to increase it
		- our flip operation means that if the current value of the row/column is less than its opposite,
		we can and must flip it

Plan:
	- for each row in the matrix, check if count(1) < count(0). If so, flip the row and continue.
	- for each column in the matrix, do the same check. If we flip, go back to the rows and do them
	again.
	- Repeat the above process until there are no possible ways to flip and get more set bits.

pseudocode:
	flipping = true
	while flipping:
		for row in matrix:
			if score(row) < score(!row):
				flip(row)
		for col in matrix:
			check_rows = false
			if score(col) < score(!col):
				flip(col)
				check_rows = true
		if not check_rows:
			flipping = false
	return score(matrix)

Not sure what the runtime for the above could be. Worse case might be a checkerboard matrix?
Seems like the worst case is neither lots of bits set or few bits set.
*/

package main

import (
	"fmt"
)

// TODO: Each of these functions that crunch matrix values
// can be done in parallel with goroutines, I think

func calculateScore(pMatrix *[][]int) int {
	var score int
	matrix := *pMatrix
	for _, row := range matrix {
		// fmt.Println(row)
		for i, col := range row {
			if col == 1 {
				score += 1 << uint(len(matrix[0])-i-1)
			}
		}
	}

	return score
}

func flipRow(pMatrix *[][]int, row int) {
	matrix := *pMatrix
	for col := range matrix[row] {
		if matrix[row][col] == 1 {
			matrix[row][col] = 0
		} else {
			matrix[row][col] = 1
		}
	}
}

func shouldFlipRow(pMatrix *[][]int, row int) bool {
	score, opposite := 0, 0
	matrix := *pMatrix
	for i, col := range matrix[row] {
		if col == 1 {
			score += ((len(matrix[row]) - 1) - i)
		} else {
			opposite += ((len(matrix[row]) - 1) - i)
		}
	}
	return score < opposite
}

func checkRows(pMatrix *[][]int) bool {
	flipped := false
	for i := range *pMatrix {
		if shouldFlipRow(pMatrix, i) {
			flipRow(pMatrix, i)
			flipped = true
		}
	}
	return flipped
}

func flipCol(pMatrix *[][]int, col int) {
	matrix := *pMatrix
	for i := range matrix {
		if matrix[i][col] == 1 {
			matrix[i][col] = 0
		} else {
			matrix[i][col] = 1
		}
	}
}

func shouldFlipCol(pMatrix *[][]int, col int) bool {
	score, opposite := 0, 0
	matrix := *pMatrix
	for i, row := range matrix {
		if row[col] == 1 {
			score += ((len(matrix) - 1) - i)
		} else {
			opposite += ((len(matrix) - 1) - i)
		}
	}
	return score < opposite
}

func checkCols(pA *[][]int) bool {
	flipped := false
	for i := range (*pA)[0] {
		if shouldFlipCol(pA, i) {
			flipCol(pA, i)
			flipped = true
		}
	}
	return flipped
}

func matrixScore(matrix [][]int) int {
	for checkRows(&matrix) || checkCols(&matrix) {
		// continue checking rows and columns
		// until no flips occur in either
	}
	return calculateScore(&matrix)
}

func main() {
	var matrix = [][]int{[]int{0, 0, 1, 1}, []int{1, 0, 1, 0}, []int{1, 1, 0, 0}}
	fmt.Printf("Matrix score: %d\n", matrixScore(matrix))
}
