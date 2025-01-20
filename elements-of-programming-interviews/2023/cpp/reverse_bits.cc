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

unsigned long long ReverseBits(unsigned long long x) {
  unsigned long long y = x & 1;
  for (int i = 0; i < (sizeof(x) * 8); i++) {
    y <<= 1;
    if (x & 1) {
      y |= 1;
    }
    x >>= 1;
  }
  return y;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "reverse_bits.cc", "reverse_bits.tsv",
                         &ReverseBits, DefaultComparator{}, param_names);
}

// 0000101101000100011001000110101010111001000000000000000000000000
// 000010110100010001100100011010101011100100000000000000000000000
