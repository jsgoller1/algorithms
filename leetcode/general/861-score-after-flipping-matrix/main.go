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
	"math"
)

// TODO: Each of these functions that crunch matrix values
// can be done in parallel with goroutines, I think
func printMatrix(pMatrix *[][]int) {
	for _, row := range *pMatrix {
		fmt.Println(row)
	}
}

func calculateScore(pMatrix *[][]int) int {
	var score int
	matrix := *pMatrix
	for _, row := range matrix {
		for i, col := range row {
			if col == 1 {
				score += int(math.Exp2(float64(len(row) - i - 1)))
			}
		}
	}

	return score
}

func flipRow(pMatrix *[][]int, row int) {
	matrix := *pMatrix
	for col := range matrix[row] {
		matrix[row][col] = 1 - matrix[row][col]
	}
}

func shouldFlipRow(pMatrix *[][]int, row int) bool {
	// you can only increase a row's value if the first
	// bit is unset; otherwise you can never increase it by
	// flipping
	return (*pMatrix)[row][0] == 0
}

func flipCol(pMatrix *[][]int, col int) {
	matrix := *pMatrix
	for i := range matrix {
		matrix[i][col] = 1 - matrix[i][col]
	}
}

func shouldFlipCol(pMatrix *[][]int, col int) bool {
	score := 0
	for _, row := range *pMatrix {
		score += row[col]
	}
	return float64(score) < float64(len(*pMatrix))/float64(2) // make odd-len arrays return a half value instead of rounding down
}

func matrixScore(matrix [][]int) int {
	continueChecking := true
	for continueChecking {
		continueChecking = false

		// Attempt to optimize columns;
		// this will leave the columns
		// in an optimized state and we
		// are unconditionally checking rows after
		// so we needn't toggle continueChecking
		for i := range matrix[0] {
			if shouldFlipCol(&matrix, i) {
				flipCol(&matrix, i)
			}
		}

		// Attempt to optimize rows;
		// continue checking if we flip one
		for i := range matrix {
			if shouldFlipRow(&matrix, i) {
				flipRow(&matrix, i)
				continueChecking = true
			}
		}
	}

	return calculateScore(&matrix)
}

func main() {
	var matrix1 = [][]int{[]int{0, 0, 1, 1}, []int{1, 0, 1, 0}, []int{1, 1, 0, 0}}
	var matrix2 = [][]int{[]int{0}}
	var matrix3 = [][]int{[]int{0, 1, 1}, []int{1, 1, 1}, []int{0, 1, 0}}
	fmt.Printf("Matrix score: %d\n", matrixScore(matrix1))
	fmt.Printf("Matrix score: %d\n", matrixScore(matrix2))
	fmt.Printf("Matrix score: %d\n", matrixScore(matrix3))

}
