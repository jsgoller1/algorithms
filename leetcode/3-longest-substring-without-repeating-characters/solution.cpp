/*
Given a string, find the length of the longest substring without repeating
characters.

Example 1:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.

Input: string
Output: int

- No constraints
--------------------
- We are looking to return the length of the longest string, not the string
itself.
- This feels like a "two pointers / sliding window" problem.
- We can store repeating characters with a set or dict
- If we take a two-pointers approach, we can:
  - Start with both pointers at 0
  - Move 2nd pointer and add letters at indices to dictionary
  - When we come to a letter we've seen already, we have to move the first
pointer to that letter's index or no other letters past the second index can be
added.
----------------------
lengthOfLongestSubstring(str s)
  - set longest to 1
  - create map of letter -> index
  - have two indices, start and end
  - while last isn't len(s)-1:
    - advance end
    - if s[end] in map:
      - set start to s[map[s[end]+1]]
    - longest = max(longest, end-start)
  - return longest

- "abcabcbb"
  - max = 1, start = 0, end = 0, map{"a":0}
  - max = 2, end = 1, map{"a":1, b:1}
  - max = 3, end = 2, map{a:0,b:1,c:2}
  - max = 3, start = 1, end = 3, map{a:3, b:2, c:2}
*/

#include <iostream>
#include <map>
#include <string>

// Don't do this irl
using namespace std;

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    if (s.empty()) {
      return 0;
    }

    map<char, size_t> locations;
    size_t start = 0, end = 0;
    size_t longest = 1;
    while (end < s.size()) {
      if (locations.find(s[end]) != locations.end()) {
        start = max(locations[s[end]] + 1, start);
      }
      locations[s[end]] = end;
      longest = max(longest, end - start + 1);

      /*
            cout << s << " | "
                 << "start: " << start << ", end: " << end << ", longest: " <<
         longest
                 << endl;
      */
      end++;
    }

    return static_cast<int>(longest);
  }
};

int main() {
  Solution s;
  cout << (s.lengthOfLongestSubstring("aa") == 1) << endl;
  cout << (s.lengthOfLongestSubstring("abba") == 2) << endl;
  cout << (s.lengthOfLongestSubstring("abcabcbb") == 3) << endl;
  cout << (s.lengthOfLongestSubstring("bcadcefg") == 6) << endl;
  cout << (s.lengthOfLongestSubstring("bbbbb") == 1) << endl;
  cout << (s.lengthOfLongestSubstring("pwwkew") == 3) << endl;
  cout << (s.lengthOfLongestSubstring("abcdef") == 6) << endl;
  cout << (s.lengthOfLongestSubstring(string{}) == 0) << endl;
}
