#include "test_framework/generic_test.h"
short Parity(unsigned long long x) {
  bool parity = false;
  int shifts = 0;
  while (x) {
    parity = (x & 1 ? !parity : parity);
    x >>= 1;
  }
  return parity ? 1 : 0;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "parity.cc", "parity.tsv", &Parity,
                         DefaultComparator{}, param_names);
}
