/*
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

(the problem statement had a picture here)

Note: You may not slant the container and n is at least 2.

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
-----------------------------------------------------------
Oh boy, this problem; I remember struggling with this twice. The solution is
something like "two pointers moving closer together", though.
- I remember also each iteration needing to pick one of the two walls and move
it one

- If we start with the outermost "walls", why would we choose one closer in?
- Could there be a circumstance where moving one inward is suboptimal, but
moving several inward is optimal?
  - Yes: [2,1,5,1,1,1,1,5]
  - How would we detect this?

- Start with left = 0, right = len(arr)-1, max = 0
- while (left != right)
  - pick whichever of the two walls we should move inward:
    - if current amount of water exceeds known max, record it and indices
    - if left + 1 > left, move left
    - if right -1 > right, move right
    - if neither, pick randomly.
- return indices
- Can we make this fail?
  - we would need to skip a pair of walls
  - [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]

*/

#include <assert.h>
#include <iostream>
#include <vector>

using namespace std;

class Solution {
 public:
  int maxArea(vector<int>& height) {
    size_t left = 0;
    size_t right = height.size();
    size_t maximum = 0;
    while (left != right) {
      size_t amount = min(left, right) * (right - left);
      cout << amount << " " << left << " " << right << endl;
      maximum = max(amount, maximum);
      if (height[left] < height[left + 1]) {
        left++;
      } else {
        right--;
      }
    }

    cout << maximum << endl;
    return static_cast<int>(maximum);
  }
};

int main() {
  Solution s;
  vector<int> heights{1, 8, 6, 2, 5, 4, 8, 3, 7};
  assert(s.maxArea(heights) == 49);
}
