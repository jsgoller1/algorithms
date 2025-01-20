#include "test_framework/generic_test.h"

short CountBits(unsigned int x) {
  short count = 0;
  for (int i = 0; i < sizeof(int) * 8; i++) {
    if (x & 1) {
      count++;
    }
    x >>= 1;
  }
  return count;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "count_bits.cc", "count_bits.tsv", &CountBits,
                         DefaultComparator{}, param_names);
}
