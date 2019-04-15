/*
My initial approach didn't work; instead,
we can just try the brute force approach of checking
for even and odd length palindromes with center at i,
then set i from 0 to len(str)-1.

Optimization: if the longest we've found so far is longer
than mid to nearest end, we can quit immediately.

----
Runtime: 32 ms, faster than 64.81% of C++ online submissions for Longest
Palindromic Substring.

Memory Usage: 24.4 MB, less than 33.11% of C++ online
submissions for Longest Palindromic Substring.
*/

#include <iostream>
#include <string>
#include <tuple>

// don't do this IRL
using namespace std;
// This program complains about int being used for comparisons and
// array indexing, and I'm too lazy to fix it.
#pragma clang diagnostic ignored "-Wsign-conversion"
#pragma clang diagnostic ignored "-Wsign-compare"

class Solution {
 public:
  string validate(string& s, int left, int right) {
    /*
    cout << "validate() | initial args: left - " << left << "; right: " << right
         << endl;
    */

    int validLeft = 0, validRight = 0;
    while (left >= 0 && right < s.size()) {
      /*
      cout << s << " | checking " << s[left] << " " << left << " and "
           << s[right] << " " << right << endl;
      */

      if (s[left] == s[right]) {
        validLeft = left;
        validRight = right;
        left--;
        right++;
      } else {
        break;
      }
    }

    /*
    cout << s << " | returning " << validLeft << " , " << validRight << ", "
         << s.substr(validLeft, validRight - validLeft + 1) << endl;
    */

    return s.substr(validLeft, validRight - validLeft + 1);
  }

  string longestPalindrome(string s) {
    string longest{}, oddLen{}, evenLen{};

    for (int i = 0; i < s.size(); i++) {
      oddLen = validate(s, i, i);
      longest = (oddLen.length() > longest.length() ? oddLen : longest);
      evenLen = validate(s, i, i + 1);
      longest = (evenLen.length() > longest.length() ? evenLen : longest);

      // TODO: optimization above; quit here based on what can be possibly found
    }

    // cout << s << " | " << longest << endl;
    return longest;
  }
};

int main() {
  Solution s;
  cout << (s.longestPalindrome("aba") == "aba") << endl;
  cout << (s.longestPalindrome("") == "") << endl;
  cout << (s.longestPalindrome("cbbd") == "bb") << endl;
  cout << (s.longestPalindrome("catqg") == "c") << endl;
  cout << (s.longestPalindrome("qerezzaaaaaaprfgr") == "aaaaaa") << endl;
  cout << (s.longestPalindrome(
               "abcdefghiklmnoqerezzaaaaaaprfgrabcdefghiklmno") == "aaaaaa")
       << endl;
  return 0;
}
