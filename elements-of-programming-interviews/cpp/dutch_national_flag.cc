#include <array>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::vector;
enum class Color { kRed, kWhite, kBlue };

int pivotSort(int left, const Color& val, vector<Color>& A) {
  int curr = left;
  while (curr < A.size()) {
    if (A[curr] == val) {
      Color temp = A[curr];
      A[curr] = A[left];
      A[left] = temp;
      left++;
    }
    curr++;
  }
  return left;
}

void DutchFlagPartition(int pivot_index, vector<Color>* A_ptr) {
  /*
  This solution kind of sucks because the problem kind of sucks; as stated,
  we want to sort A into [less than pivot, equal to pivot, greater than pivot].
  However, The test cases here are based on the dutch flag, not arbitrary
  integers - so the end result is the Dutch flag no matter what, and this code
  directly solves that (with two passes) by hardcoding the given colors. This
  approach would not work for a more general Dutch Flag sort akin to quicksort's
  pivot. See my Python solution for a better approach.
  */
  vector<Color>& A = *A_ptr;
  int i = pivotSort(0, Color::kRed, A);
  pivotSort(i, Color::kWhite, A);
  return;
}

void DutchFlagPartitionWrapper(TimedExecutor& executor, const vector<int>& A,
                               int pivot_idx) {
  vector<Color> colors;
  colors.resize(A.size());
  std::array<int, 3> count = {0, 0, 0};
  for (size_t i = 0; i < A.size(); i++) {
    count[A[i]]++;
    colors[i] = static_cast<Color>(A[i]);
  }
  Color pivot = colors[pivot_idx];

  executor.Run([&] { DutchFlagPartition(pivot_idx, &colors); });

  int i = 0;
  while (i < colors.size() && colors[i] < pivot) {
    count[static_cast<int>(colors[i])]--;
    ++i;
  }

  while (i < colors.size() && colors[i] == pivot) {
    count[static_cast<int>(colors[i])]--;
    ++i;
  }

  while (i < colors.size() && colors[i] > pivot) {
    count[static_cast<int>(colors[i])]--;
    ++i;
  }

  if (i != colors.size()) {
    throw TestFailure("Not partitioned after " + std::to_string(i) +
                      "th element");
  } else if (count != std::array<int, 3>{0, 0, 0}) {
    throw TestFailure("Some elements are missing from original array");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "A", "pivot_idx"};
  return GenericTestMain(args, "dutch_national_flag.cc",
                         "dutch_national_flag.tsv", &DutchFlagPartitionWrapper,
                         DefaultComparator{}, param_names);
}
