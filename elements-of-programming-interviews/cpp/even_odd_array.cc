#include <set>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
#include "test_framework/timed_executor.h"
using std::vector;

bool cmp(const int& a, const int& b) {
  if ((a & 1) == 0 && (b & 1) != 0) return true;   // a is even, b is odd
  if ((a & 1) != 0 && (b & 1) == 0) return false;  // a is odd, b is even
  return false;  // either both are even or both are odd; maintain original
                 // order
}

void EvenOddSort(vector<int>* A_ptr) {
  // Start with l = 0, r = len-1
  // sort, but comparator is just "equal less than odd";
  // two odd numbers are sorted, and two even numbers are sorted
  std::sort(A_ptr->begin(), A_ptr->end(), cmp);
  return;
}

void printArr(vector<int>& A) {
  printf("\n[");
  for (auto val : A) {
    printf("%d ", val);
  }
  printf("]\n");
}

void EvenOdd(vector<int>* A_ptr) {
  vector<int>& A = *A_ptr;
  size_t l = 0, r = A.size() - 1;
  while (l < r) {
    if ((A[l] & 1) && !(A[r] & 1)) {
      int tmp = A[l];
      A[l] = A[r];
      A[r] = tmp;
    }
    if (!(A[l] & 1)) {
      l++;
    }
    if (A[r] & 1) {
      r--;
    }
  }
}

void EvenOddWrapper(TimedExecutor& executor, vector<int> A) {
  std::multiset<int> before(begin(A), end(A));

  executor.Run([&] { EvenOdd(&A); });

  bool in_odd = false;
  for (int a : A) {
    if (a % 2 == 0) {
      if (in_odd) {
        throw TestFailure("Even elements appear in odd part");
      }
    } else {
      in_odd = true;
    }
  }

  std::multiset<int> after(begin(A), end(A));
  if (before != after) {
    throw TestFailure("Elements mismatch");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "A"};
  return GenericTestMain(args, "even_odd_array.cc", "even_odd_array.tsv",
                         &EvenOddWrapper, DefaultComparator{}, param_names);
}
