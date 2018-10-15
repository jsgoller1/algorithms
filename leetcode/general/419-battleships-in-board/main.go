/*
Statement

Given an 2D board, count how many battleships are in it. The battleships
 are represented with 'X's, empty slots are represented with '.'s. You
 may assume the following rules:

-  You receive a valid board, made of only battleships or empty slots.
- Battleships can only be placed horizontally or vertically. In other
words, they can only be made of the shape 1xN (1 row, N columns)
or Nx1 (N rows, 1 column), where N can be of any size.
- At least one horizontal or vertical cell separates
between two battleships - there are no adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive - as
battleships will always have a cell separating between them.

Followup: Can you do it in one pass with O(1) memory and
an immutable board?

Input: array of array of bytes representing battleships or water
Output: Int (battleship count)

Constraints / edge cases
- board is 1 x n / n x 1, so a 1x1 array is possible
-------
Understand / Plan

This problem can be solved with a graph search. Starting at (0,0),
we can traverse the array and DFS at every cell in which we find an
X. Either by modifying the board or keeping a visited set, we can
ensure that we don't revisit cells twice.

Not sure about the O(1) memory and O(N) pass. How would
we both ensure linear runtime AND not store which cells
we'd visited before (either with a mutable board or a visisted list)?

What if, as we traverse the array, we ONLY count the Xs that have no
X neighbors up or to the left? Each battle ship will be separated by
water per the problem statement, so we don't have to worry about edge
cases where two battleships are touching but actually separate.


*/
package main

import "fmt"

func cellInGrid(pBoard *[][]byte, y, x int) bool {
	if y < 0 || len(*pBoard) <= y {
		return false
	}

	if (x < 0) || len((*pBoard)[0]) <= x {
		return false
	}

	return true
}

func countBattleships(board [][]byte) int {
	battleshipCount := 0
	for y, row := range board {
		for x, col := range row {
			if col == 'X' {
				if cellInGrid(&board, y-1, x) && (board[y-1][x] == 'X') {
					continue
				}
				if cellInGrid(&board, y, x-1) && (board[y][x-1] == 'X') {
					continue
				}
				battleshipCount++
			}
		}
	}
	return battleshipCount
}

func main() {
	board := [][]byte{[]byte{'X', '.', '.', 'X'}, []byte{'.', '.', '.', 'X'}, []byte{'.', '.', '.', 'X'}}
	fmt.Println(countBattleships(board))
}
