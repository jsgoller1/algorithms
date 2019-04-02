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
using namespace std;

class Solution {
 public:
  vector<int> getValues(vector<int>& nums, int target) {
    vector<int> solution = new vector();
    vector<int> sorted = vector(nums);
    sort(sorted.front, sorted.back);
    while (sorted.front != sorted.back) {
    }
  }

  vector<int> twoSum(vector<int>& nums, int target) {
    vector<int> solution = getValues(nums, target);

    // Find index of second value, replace in values vector
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == solution[0]) {
        solution[0] = nums[i];
      }
    }

    // Find index of second value; replace in values vector
    for (int i = 0; i < nums.size(); i++) {
      if (nums[i] == solution[1] && nums[i] != solution[0]) {
        solution[1] = nums[i];
      }
    }

    return solution;
  }
};

int main() {
  cout << "Hello, leetcode!" << endl;
  return 0;
}
