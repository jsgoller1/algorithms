#include "test_framework/generic_test.h"
bool IsPalindromeNumber(int x) {
  if (x < 0) {
    return false;
  }

  int original = x;
  int revX = 0;
  while (x) {
    revX *= 10;
    revX += x % 10;
    x /= 10;
  }

  return original == revX;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "is_number_palindromic.cc",
                         "is_number_palindromic.tsv", &IsPalindromeNumber,
                         DefaultComparator{}, param_names);
}
