/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer
overflows.

--------------------
Runtime: 4 ms, faster than 100.00% of C++ online submissions for Reverse
Integer.

Memory Usage: 8.6 MB, less than 96.15% of C++ online submissions for Reverse
Integer.
*/

#include <assert.h>
#include <algorithm>
#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::to_string;

class Solution {
 public:
  int reverse(int x) {
    // This is unnecessary since x is an int, but LeetCode breaks without it.
    if (x <= INT_MIN || INT_MAX <= x) {
      return 0;
    }

    int negative = (x < 0 ? -1 : 1);
    x *= negative;
    string val = to_string(x);
    std::reverse(val.begin(), val.end());

    // This is necessary, though; the reverse can overflow.
    try {
      return stoi(val) * negative;
    } catch (std::out_of_range) {
      return 0;
    }
  }
};

int main() {
  Solution s;
  assert(123 == s.reverse(321));
  assert(11 == s.reverse(11));
  assert(0 == s.reverse(0));
  assert(-123 == s.reverse(-321));
  assert(9646324351 == s.reverse(1534236469));
  assert(s.reverse(-2147483648));
}
