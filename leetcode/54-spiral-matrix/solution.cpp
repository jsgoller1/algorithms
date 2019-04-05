/*
Given a matrix of m x n elements (m rows, n columns), return
all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Input: List[List[Int]]
Output: List[Int]

Constraints:
  - None given
---------------------
We meet again, ancient foe (I still don't want to work at Asana). I'm
going to use the "cursor" approach here with the explicit movement
values; I remember the M X M approach offhand, but don't remember
how it generalizes to M X N.

N x N: Moving in Right->Down->Left->Up order, the pattern is:
N moves, N-1, N-1, N-2, N-2, ... , 1, 1, halt.

Example:
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
M x N (4 x 3): Moving in same order, the pattern is:
M, N-1, M-1, N-2, M-2, N-3 (N is 0)
4, 2, 3, 1, 2

- We could just keep track of "how many remaining moves", and
keep separate counts for M and N but I think there's a more
concise answer.
- Yes, once one of the move values hits zero, we have nowhere left to go,
so we halt then
--------------------------
- create constant pairs distances = { U / D / L / R }
- Set M and N based on matrix width and height
- Set i to zero
- While M and N are both nonzero:
  - Move M cells in direction[i]
  - i = i + 1 % 3, M--
  - print cell
  - Move N cells in direction[i]
  - i = i + 1 % 3, N--
  - print cell
*/

#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::pair;
using std::vector;

class Solution {
 public:
  vector<int> spiralOrder(vector<vector<int>>& matrix) {
    // R, D, L U
    vector<pair<int, int>> directions{pair{0, 1}, pair{1, 0}, pair{0, -1},
                                      pair{-1, 0}};
    vector<int> solution;
    size_t current_dir = 0;
    pair<int, int> current{0, -1};
    size_t cols = matrix[0].size();
    size_t rows = matrix.size() - 1;
    while (cols > 0 && rows > 0) {
      // move cols units
      for (size_t j = 0; j < cols; j++) {
        current.first += directions[current_dir].first;
        current.second += directions[current_dir].second;

        /* TODO: Remove this
        cout << static_cast<size_t>(current.first) << ", "
             << static_cast<size_t>(current.second) << ": " << endl;
        cout << matrix[static_cast<size_t>(current.first)]
                      [static_cast<size_t>(current.second)]
             << endl;
        */
        solution.push_back(matrix[static_cast<size_t>(current.first)]
                                 [static_cast<size_t>(current.second)]);
      }
      current_dir = (current_dir + 1) % 4;
      cols--;

      // move rows units
      for (size_t j = 0; j < rows; j++) {
        current.first += directions[current_dir].first;
        current.second += directions[current_dir].second;

        /* TODO: Remove this
        cout << static_cast<size_t>(current.first) << ", "
             << static_cast<size_t>(current.second) << ": " << endl;
        cout << matrix[static_cast<size_t>(current.first)]
                      [static_cast<size_t>(current.second)]
             << endl;
        */

        solution.push_back(matrix[static_cast<size_t>(current.first)]
                                 [static_cast<size_t>(current.second)]);
      }
      current_dir = (current_dir + 1) % 4;
      rows--;
    }

    return solution;
  }
};

int main() {
  /*
  1,  2,  3,  4
  5,  6,  7,  8,
  9,  10, 11, 12
  13, 14, 15, 16
  */
  vector<vector<int>> matrix{vector<int>{1, 2, 3, 4}, vector<int>{5, 6, 7, 8},
                             vector<int>{9, 10, 11, 12},
                             vector<int>{13, 14, 15, 16}};
  Solution s;
  for (auto val : s.spiralOrder(matrix)) {
    cout << val << " ";
  }
  cout << endl;
  return 0;
}
