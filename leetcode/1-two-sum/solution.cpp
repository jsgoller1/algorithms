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

// The more efficient way of doing this (O(N)) is to use a map and look for
complements:
- Initialize a std::map
- At each element, map the value to the index it is found at.
- If the target - current is in the dict, return current index and
map[target-current]

This is actually technically slower, interestingly! My less efficient approach
completed 4ms faster and used less memory; it might be due to using a std::map.
*/

#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using std::cin;
using std::cout;
using std::endl;
using std::map;
using std::string;
using std::vector;

class Solution {
 public:
  vector<int> twoSum(vector<int>& nums, int target) {
    map<int, size_t> indices;
    vector<int> solution;

    // Look for complements if they exist; if so, push into solution and return
    for (size_t i = 0; i < nums.size(); i++) {
      if (indices.find(target - nums[i]) != indices.end()) {
        int comp_i = static_cast<int>(indices[target - nums[i]]);
        solution.push_back(comp_i);
        int curr_i = static_cast<int>(i);
        solution.push_back(curr_i);
        break;
      } else {
        // otherwise note we find this number here
        indices[nums[i]] = i;
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
