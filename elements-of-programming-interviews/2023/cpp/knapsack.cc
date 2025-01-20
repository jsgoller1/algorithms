#include <unordered_map>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/serialization_traits.h"

#define MAX(a, b) (a > b ? a : b);

using std::pair;
using std::unordered_map;
using std::vector;

struct Item {
  int weight, value;
};

int OptimumSubjectToCapacity(const vector<Item>& items, int capacity) {
  int cap_to_maxval[items.size() + 1][capacity + 1];
  for (int j = 0; j <= capacity; j++) {
    cap_to_maxval[0][j] = 0;
  }

  for (int i = 1; i <= items.size(); i++) {
    int cweight = items[i - 1].weight, cval = items[i - 1].value;
    for (int j = 0; j <= capacity; j++) {
      int prev_val = cap_to_maxval[i - 1][j];
      int use_curr =
          (j >= cweight) ? cap_to_maxval[i - 1][j - cweight] + cval : 0;
      cap_to_maxval[i][j] = MAX(prev_val, use_curr);
    }
  }
  return cap_to_maxval[items.size()][capacity];
}

namespace test_framework {
template <>
struct SerializationTrait<Item> : UserSerTrait<Item, int, int> {};
}  // namespace test_framework

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"items", "capacity"};
  return GenericTestMain(args, "knapsack.cc", "knapsack.tsv",
                         &OptimumSubjectToCapacity, DefaultComparator{},
                         param_names);
}
