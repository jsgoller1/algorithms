#include <string>

#include "test_framework/generic_test.h"
using std::string;

/*
- two pointer palindrome test
- Can contain non-alphanumerics, spaces, etc. Can use isalnum
- possibly empty
- need to compare lowercase to lowercase for alphas, tolower()
- edge cases:
  - empty
  - 11111111 (is palindrome)
  - 11111aa (is not palindrome)
  - !!!!!aa is palindrome
*/

bool IsPalindrome(const string& s) {
  if (s.empty()) {
    return true;
  }

  int l = 0, r = s.size() - 1;
  while (l < r) {
    // Find next suitable lefts and rights
    if (!isalnum(s[l])) {
      l++;
      continue;
    }
    if (!isalnum(s[r])) {
      r--;
      continue;
    }

    char left = s[l], right = s[r];
    // left is a digit and the other isn't / vice versa.
    if ((isdigit(left) != isdigit(right)) ||
        // tolower() returns the arg if no lowercase is available, works for
        // digits.
        (tolower(left) != tolower(right))) {
      return false;
    }
    l++, r--;
  }
  return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_string_palindromic_punctuation.cc",
                         "is_string_palindromic_punctuation.tsv", &IsPalindrome,
                         DefaultComparator{}, param_names);
}
