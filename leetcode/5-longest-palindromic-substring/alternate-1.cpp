/*
Given a string s, find the longest palindromic substring in s. You may assume
that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
----------------------------------
- Once we find a palindrome, we don't need to check its substrings;
they cannot be longer.

- Recursive approach:
  - try string[start:end]
    - if this is a palindrome, return it
  - recurse with string[start+1:end]
  - recurse with string[start:end-1]

- The brute force approach to this is:
  - go character by character doing the following:
    - start with a middle character or middle two characters
    - try appending either a character or two characters to each
    end and see if it's a palindrome
    - store the longest result
- I've tried this before and it is error prone
-------------------------------------------
Unfortunately, the fully recursive approach is TLE; going to need to choose a
different one.
*/

#include <iostream>
#include <string>
#include <tuple>

// don't do this IRL
using namespace std;

class Solution {
 public:
  bool validate(string& s, size_t start, size_t end) {
    while (start < end) {
      if (s[start] != s[end]) {
        // cout << "Not palindrome, " << s[start] << " != " << s[end] << endl;
        return false;
      }
      start++;
      end--;
    }
    // cout << "Palindrome!" << endl;
    return true;
  }

  tuple<size_t, size_t> recurse(string& s, size_t start, size_t end,
                                size_t spaces = 0) {
    // Diagnostic; remove this
    /*
    for (size_t i = 0; i < spaces; i++) {
      cout << " ";
    }
    cout << " - " << start << ", " << end << " (" << end - start + 1 << ") ("
         << s.substr(start, end - start + 1) << ")" << endl;
    */

    // Empty or valid palindromes are the base case
    if (s.empty() || validate(s, start, end)) {
      return tuple<size_t, size_t>{start, end};
    }

    // recurse on one shorter from the left
    tuple<size_t, size_t> substr1 = recurse(s, start + 1, end, spaces + 2);
    size_t substr1Size = get<1>(substr1) - get<0>(substr1) + 1;

    // recurse on one shorter from the right
    tuple<size_t, size_t> substr2 = recurse(s, start, end - 1, spaces + 2);
    size_t substr2Size = get<1>(substr2) - get<0>(substr2) + 1;

    // return greater of the two
    return (substr1Size > substr2Size ? substr1 : substr2);
  }

  string longestPalindrome(string s) {
    tuple<size_t, size_t> longest = recurse(s, 0, s.size() - 1);
    size_t start = get<0>(longest);
    size_t end = get<1>(longest);

    // Diagnostic, remove this
    /*
    cout << s << " | "
         << "start: " << start << ", end: " << end
         << ", palindrome: " << s.substr(start, end - start + 1) << endl;
    */
    return s.substr(start, end - start + 1);
  }
};

int main() {
  Solution s;
  cout << (s.longestPalindrome("aba") == "aba") << endl;
  cout << (s.longestPalindrome("") == "") << endl;
  cout << (s.longestPalindrome("cbbd") == "bb") << endl;
  cout << (s.longestPalindrome("catqg") == "c") << endl;
  cout << (s.longestPalindrome("qerezzaaaaaaprfgr") == "aaaaaa") << endl;
  // cout <<
  // (s.longestPalindrome("abcdefghiklmnoqerezzaaaaaaprfgrabcdefghiklmno") ==
  // "aaaaaa") << endl;

  return 0;
}
