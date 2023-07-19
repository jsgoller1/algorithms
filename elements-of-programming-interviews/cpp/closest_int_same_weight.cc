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

bool sameWeight(unsigned long long left, unsigned long long right) {
  int leftWeight = 0;
  int rightWeight = 0;
  while (left > 0 || right > 0) {
    if (left & 1) {
      leftWeight++;
    }
    left >>= 1;
    if (right & 1) {
      rightWeight++;
    }
    right >>= 1;
  }
  return rightWeight == leftWeight;
}

unsigned long long ClosestIntSameBitCountBruteForce(unsigned long long x) {
  /*
    Approach 1: look for the best weight explicitly knowing the value
    If we have a constant time approach for measuring the weight of a number,
    we could just try repeatedly calculating x++ and x-- until we find a value
    of the same weight. This is a brute force approach that technically works
    here but can become quite inefficient.
  */
  unsigned long long nearestUp = x + 1;
  unsigned long long nearestDown = x - 1;

  while (true) {
    if (sameWeight(x, nearestUp)) {
      return nearestUp;
    }
    if (sameWeight(x, nearestDown)) {
      return nearestDown;
    }
    nearestUp++;
    nearestDown--;
  }
}

unsigned long long ClosestIntSameBitCount(unsigned long long x) {
  /*
  Approach 2: look for the best value by explicitly knowing the weight
  To create y, we need to unset one bit in x, and set one unset bit in x.
  Unsetting is subtracting, and setting is adding. We want the net change
  between y and x to be as small as possible, so we want these two bits to be as
  close as possible. If we flip the first set bit we find, then the optimal
  choice is to flip the first unset bit to its right; this may not exist though.
  Consider 0xff, 255. Although changing this to 0xfe = 254 subtracts the
  smallest amount possible, the difference after we set a new bit will be huge,
  e.g. 0x1fe = 510. So what we want is to flip two differing bits that are as
  close as possible, i.e. adjacent. The book phrases this as "look for the
  least significant pair of differing bits and swap them".
  */
  int i = 1, j = 0;
  while (((x >> i) & 1) == ((x >> j) & 1)) {
    i++;
    j++;
  }
  int mask = (1LL << i) | (1LL << j);
  return x ^ mask;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x"};
  return GenericTestMain(args, "closest_int_same_weight.cc",
                         "closest_int_same_weight.tsv", &ClosestIntSameBitCount,
                         DefaultComparator{}, param_names);
}
