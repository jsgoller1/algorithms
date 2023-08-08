#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
void ApplyPermutationLinearSpace(vector<int> perm, vector<int>* A_ptr) {
  vector<int>& A = *A_ptr;
  vector<int> result(A.size(), 0);
  for (int i = 0; i < perm.size(); i++) {
    int idx = perm[i];
    result[idx] = A[i];
  }
  for (int i = 0; i < result.size(); i++) {
    A[i] = result[i];
  }
  return;
}

void ApplyPermutation(vector<int> perm, vector<int>* A_ptr) {
  vector<int>& A = *A_ptr;
  if (A.size() == 0) {
    return;
  }
  int idx = 0;
  int curr = A[idx];
  for (int i = 0; i < perm.size(); i++) {
    int newIdx = perm[i];
    if (newIdx == -1) {
      continue;
    }
    while (newIdx != -1) {
      int next = A[newIdx];
      A[newIdx] = curr;
      curr = next;
      perm[idx] = -1;
      idx = newIdx;
      newIdx = perm[newIdx];
    }
  }
  return;
}

vector<int> ApplyPermutationWrapper(const vector<int>& perm, vector<int> A) {
  ApplyPermutation(perm, &A);
  return A;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"perm", "A"};
  return GenericTestMain(args, "apply_permutation.cc", "apply_permutation.tsv",
                         &ApplyPermutationWrapper, DefaultComparator{},
                         param_names);
}
