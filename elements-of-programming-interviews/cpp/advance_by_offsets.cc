#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
bool CanReachEnd(const vector<int>& arr) {
  int best = arr[0];
  for (int curr = 0; curr < arr.size(); curr++) {
    if (best >= arr.size() - 1) {
      return true;
    }
    if (curr > best) {
      return false;
    }
    best = (curr + arr[curr] > best) ? curr + arr[curr] : best;
  }
  return true;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"max_advance_steps"};
  return GenericTestMain(args, "advance_by_offsets.cc",
                         "advance_by_offsets.tsv", &CanReachEnd,
                         DefaultComparator{}, param_names);
}
