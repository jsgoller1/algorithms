#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
vector<int> PlusOneFirstAttempt(vector<int> A) {
  vector<int> result;
  bool carry = true;

  for (int i = A.size() - 1; i >= 0; i--) {
    int val = carry ? (A[i] + 1) % 10 : A[i];
    result.push_back(val);
    carry = (carry && (A[i] == 9));
  }
  if (carry) {
    result.push_back(1);
  }
  std::reverse(result.begin(), result.end());
  return result;
}

vector<int> PlusOne(vector<int> A) {
  int i = A.size() - 1;
  bool carry = true;

  while (i >= 0) {
    A[i] = (A[i] + (carry ? 1 : 0)) % 10;
    carry = carry && (A[i] == 0);
    i--;
  }
  if (carry) {
    A[0] = 1;
    A.push_back(0);
  }
  return A;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"A"};
  return GenericTestMain(args, "int_as_array_increment.cc",
                         "int_as_array_increment.tsv", &PlusOne,
                         DefaultComparator{}, param_names);
}
