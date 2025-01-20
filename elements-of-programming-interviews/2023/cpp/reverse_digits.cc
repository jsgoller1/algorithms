#include "test_framework/generic_test.h"
long long Reverse(int x) {
  long long y = 0;
  long long neg = x < 0 ? -1 : 1;
  x *= neg;
  while (x) {
    y *= 10;
    y += x % 10;
    x /= 10;
  }
  return y * neg;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "reverse_digits.cc", "reverse_digits.tsv",
                         &Reverse, DefaultComparator{}, param_names);
}
