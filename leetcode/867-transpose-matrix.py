"""
Statement

Given a matrix A, return the transpose of A. The transpose of a
matrix is the matrix flipped over it's main diagonal, switching
the row and column indices of the matrix.

Example 1:

Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000

Input: array of arrays of ints
Output: arrays of arrays of ints
- Can be at most 1 million ints
----
Understand / Plan
- we can compute a transpose T of a matrix A by setting T_ij to A_ji.
- For square matrices, we could simply do an in-place swap of A_ij and A_ji. However,
non-square matrices and their transposes will have a different number of rows and columns.
- A more straightforward way to handle this would be to create the transpose matrix with
values set to None, and then set the values in a loop. It would be O(N) for space and time.
- Matrices in python are accessed via matrix[row][column]
"""


class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # Row and column count are swapped in transpose
        T = [[None for row in A] for col in A[0]]
        for i, row in enumerate(A):
            for j, col in enumerate(row):
                T[j][i] = A[i][j]
        return T


if __name__ == '__main__':
    s = Solution()
    assert s.transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        [1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert s.transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
