/*
Given an array of integers, return indices of the two numbers such that they add
up to a specific target.

You may assume that each input would have exactly one solution, and you may not
use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
----------------------------------------------
In: array of ints and target int
Out: indices of ints that add to that value
- Solution always exists
- Can't use same elements twice
- Not necessarily sorted

- Can we sort elements, and then use the following procedure:
  - start with hi and lo
  - if arr[hi] + arr[lo] > target, decrease hi
  - if arr[hi] + arr[lo] < target, increase lo
  - theoretically (though not for this problem), if hi == lo, no solution.

- Note that we are returning the indices, so we have to somehow preserve the
original ordering.
- We could do faster lookups by sticking things in a map, but that's more mem
intensive
- Or at the end we can look up the element, but would be problematic on a case
like [0,4,4,9] and 8.
  - Maybe we can just do searches but skip if index is the same?
---------------------------------------------------------------------------

// this finds the actual elements
- sort elements
- create answer vector
- hi = len-1
- lo = 0
- while hi != lo (catches empty):
  - if arr[lo] + arr[hi] = target
    - push arr[hi]
    - push arr[lo]
  - elif arr[lo] + arr[hi] > target
    - hi--
  - else:
    - lo--

// then, passed back to the main method:
  - new solution vector
  - first = answer[0]
  - find answer[0] in original vector, return index
  - find answer[1] in original vector not equal to answer[0]
*/

#include <algorithm>
#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::string;
using std::vector;

class Solution {
 public:
  vector<int> getValues(vector<int>& nums, int target) {
    // Create a sorted copy of the vector; apparently you can do this in
    // C++11???
    vector<int> solution;
    vector<int> sorted = vector(nums);
    string temp;
    std::sort(sorted.begin(), sorted.end());
    for (auto num : sorted) {
      cout << num << endl;
    }

    auto left = sorted.begin();
    auto right = sorted.rbegin();

    while ((*left + *right) != target) {
      // find the matching elements; move the right inwards
      // if too high, otherwise move the left.
      if ((*left + *right) > target) {
        right++;
      } else {
        left++;
      }
    }
    solution.push_back(*left);
    solution.push_back(*right);

    return solution;
  }

  vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> solution = getValues(nums, target);
    cout << "Initial solution values: " << solution[0] << " " << solution[1]
         << endl;

    // Find index of second value, replace in values vector
    for (size_t i = 0; i < nums.size(); i++) {
      if (nums[i] == solution[0]) {
        cout << "Match: " << solution[0] << " " << static_cast<int>(i) << endl;
        solution[0] = static_cast<int>(i);
        break;
      }
    }
    cout << "Solution after first assign: " << solution[0] << " " << solution[1]
         << endl;

    // Find index of second value; replace in values vector
    for (size_t i = 0; i < nums.size(); i++) {
      if (nums[i] == solution[1] && static_cast<int>(i) != solution[0]) {
        solution[1] = static_cast<int>(i);
      }
    }

    return solution;
  }
};

int main() {
  Solution s;
  vector<int> nums{-18, 12, 3, 0};
  int target = -6;
  auto solution = s.twoSum(nums, target);
  cout << solution[0] << " " << solution[1] << endl;
  return 0;
}
