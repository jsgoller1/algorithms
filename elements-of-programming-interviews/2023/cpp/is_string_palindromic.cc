#include <string>

#include "test_framework/generic_test.h"
using std::string;

bool IsPalindromic(const string& s) {
  if (s.empty()) {
    return false;
  }
  int l = 0, r = s.size() - 1;
  while (l <= r) {
    if (s[l++] != s[r--]) {
      return false;
    }
  }

  return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"s"};
  return GenericTestMain(args, "is_string_palindromic.cc",
                         "is_string_palindromic.tsv", &IsPalindromic,
                         DefaultComparator{}, param_names);
}
