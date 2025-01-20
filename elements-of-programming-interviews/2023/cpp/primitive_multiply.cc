#include "test_framework/generic_test.h"

void printBin(unsigned long long val, size_t len, const std::string& suffix) {
  std::string binval;
  for (size_t i = 0; i < len; i++) {
    binval.append(val & 1 ? "1" : "0");
    val >>= 1;
  }
  reverse(binval.begin(), binval.end());
  printf("%s (%s)\n", binval.c_str(), suffix.c_str());
}

unsigned long long Add(unsigned long long a, unsigned long long b) {
  /*
    total = a^b
    carry = (a & b) << 1
    while carry:
        newTotal = total ^ carry
        newCarry = (total & carry) << 1
        total, carry = newTotal, newCarry
    return total
  */
  unsigned long long total = a ^ b;
  unsigned long long carry = (a & b) << 1;
  while (carry) {
    unsigned long long newTotal = total ^ carry;
    carry = (total & carry) << 1;
    total = newTotal;
  }
  return total;
}

unsigned long long Multiply(unsigned long long x, unsigned long long y) {
  /*
  - Can only use assignment, comparisons, and bitwise operations (&, |, ~, ^)
  - Lshift is a multiply by 2
  - Clearing the lowest bit and setting all to the right of it: subtract 1
  - Adding: bitwise xor with carry
    (3+3=6)
    11 +
    11 =
   110
  - Multiply can be iterative addition, but without subtraction this will be
    hard
  - Multiply: prod = 0. Until b=0, if lowest bit is set, add prod+=a. Right
    shift b, leftshift a. (3*3=9) 11 * 11 = 1001 (5*5=25) 101 * 101 = 11001
  */
  unsigned long long prod = 0;
  while (y) {
    if (y & 1) {
      prod = Add(x, prod);
    }
    y >>= 1;
    x <<= 1;
  }

  return prod;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "primitive_multiply.cc",
                         "primitive_multiply.tsv", &Multiply,
                         DefaultComparator{}, param_names);
}
