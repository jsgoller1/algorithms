#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
// Brute force method. Given n return all primes up to and including n.
vector<int> GeneratePrimesBruteForce(int n) {
  int counter = 0;
  if (n == 0 || n == 1) {
    return {};
  }
  vector<int> primes{2};
  for (int i = 2; i <= n; i++) {
    int j = 0;
    for (; j < primes.size(); j++) {
      if (!(i % primes[j])) {
        break;
      }
    }
    if (j == primes.size()) {
      primes.push_back(i);
    }
  }
  return primes;
}

vector<int> GeneratePrimes(int n) {
  // Sieve of Eratosthenes
  vector<int> primes;
  vector<bool> table(n + 1, false);
  for (size_t i = 2; i <= n; i++) {
    if (table[i] == true) {
      continue;
    }
    primes.push_back(i);
    for (size_t j = 0; j <= n; j += i) {
      table[j] = true;
    }
  }
  return primes;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"n"};
  return GenericTestMain(args, "prime_sieve.cc", "prime_sieve.tsv",
                         &GeneratePrimes, DefaultComparator{}, param_names);
}
