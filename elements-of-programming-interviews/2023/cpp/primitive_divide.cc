#include "test_framework/generic_test.h"
int Divide(int a, int b) {
  /*
  Divide x by y, using only subtraction, addition, and shifting.

  Brute force would be to iteratively subtract until a remainder occurs, but
  this could take up to 2^n (e.g. (2^31 - 1) / 1).

  Could we use the same strategy for multiply, but with subtraction?
  */
  if (a < b || b == 0) {
    return 0;
  }

  long long x = a;
  long long y = b;
  long long amount = 1;
  long long quotient = 0;
  while (x > y) {
    y <<= 1;
    amount <<= 1;
  }
  while (x) {
    if (x >= y) {
      x -= y;
      quotient += amount;
    } else {
      y >>= 1;
      amount >>= 1;
    }
  }
  return quotient;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "primitive_divide.cc", "primitive_divide.tsv",
                         &Divide, DefaultComparator{}, param_names);
  // Divide(2097428739, 186);
}
