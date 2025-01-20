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

long long SwapBitsBruteForce(long long x, int i, int j) {
  // Not clever approach:
  // 1) Isolate the bit values:
  long long ival = x & (1LL << i);
  long long jval = x & (1LL << j);

  // 2) Clear them in the original string
  x &= ~(1LL << i);
  x &= ~(1LL << j);

  // 3) Now use the isolated values to set them in the swapped places
  if (ival) {
    x |= (1LL << j);
  }
  if (jval) {
    x |= (1LL << i);
  }
  return x;
}

long long SwapBits(long long x, int i, int j) {
  if (((x >> i) & 1) != ((x >> j) & 1)) {
    long long mask = (1LL << i) | (1LL << j);
    return x ^ mask;
  }
  return x;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "i", "j"};
  return GenericTestMain(args, "swap_bits.cc", "swap_bits.tsv", &SwapBits,
                         DefaultComparator{}, param_names);
}

// 0000000000000000000100010010101011010110100101010001100010101001
// 00000000000000000001000x0010101011010110100101010001100010101001
