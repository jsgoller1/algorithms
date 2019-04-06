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

------------------------------
Runtime: 4 ms, faster than 100.00% of C++ online submissions for Spiral Matrix.

Memory Usage: 8.5 MB, less than 100.00% of C++ online submissions for Spiral
Matrix.
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
    vector<int> solution;
    if (matrix.empty()) {
      return solution;
    }
    pair<int, int> position{0, -1};

    // R, D, L U
    vector<pair<int, int>> directions{pair{0, 1}, pair{1, 0}, pair{0, -1},
                                      pair{-1, 0}};
    size_t current_dir = 0;
    vector<size_t> distances{matrix[0].size(), matrix.size() - 1};
    size_t current_distance = 0;
    while (distances[current_distance] > 0) {
      for (size_t j = 0; j < distances[current_distance]; j++) {
        position.first += directions[current_dir].first;
        position.second += directions[current_dir].second;
        solution.push_back(matrix[static_cast<size_t>(position.first)]
                                 [static_cast<size_t>(position.second)]);
      }
      distances[current_distance]--;
      current_distance = (current_distance + 1) % 2;
      current_dir = (current_dir + 1) % 4;
    }

    return solution;
  }

  bool test(vector<vector<int>>& matrix, vector<int> solution) {
    vector<int> answer = spiralOrder(matrix);
    if (answer.size() != solution.size()) {
      return false;
    }
    for (size_t i = 0; i < solution.size(); i++) {
      if (answer[i] != solution[i]) {
        return false;
      }
    }

    return true;
  }
};

int main() {
  Solution s;

  /*
  1,  2,  3,  4
  5,  6,  7,  8,
  9,  10, 11, 12
  13, 14, 15, 16
  */
  vector<vector<int>> matrix1{vector<int>{1, 2, 3, 4}, vector<int>{5, 6, 7, 8},
                              vector<int>{9, 10, 11, 12},
                              vector<int>{13, 14, 15, 16}};
  vector<int> actual1{1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10};
  cout << s.test(matrix1, actual1) << endl;

  /*
  1,  2,
  5,  6,
  9,  10,
  13, 14
  */
  vector<vector<int>> matrix2{vector<int>{1, 2}, vector<int>{5, 6},
                              vector<int>{9, 10}, vector<int>{13, 14}};
  vector<int> actual2{1, 2, 6, 10, 14, 13, 9, 5};
  cout << s.test(matrix2, actual2) << endl;

  vector<vector<int>> matrix3{vector<int>{}};
  vector<int> actual3;
  cout << s.test(matrix3, actual3) << endl;

  cout << s.test(nullptr, vector<int>{}) << endl;

  return 0;
}
