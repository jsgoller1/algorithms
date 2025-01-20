#include <iterator>
#include <vector>

#include "test_framework/generic_test.h"
using std::pair;
using std::vector;

/*
Cases:
  - Every building equal/ gets taller than previous; only last can view
  - Every building gets shorter; all can see it
  - Any time a taller building comes in, any previous shorter one can no longer
see and nothing changes this
  - If  building is shorter than top, push it.
  - If a building is equal or taller than top, pop until empty or we reach one
that's taller, then push.
O(n) space, O(n) time (evaluate, push, and pop almost every element)
*/

vector<int> ExamineBuildingsWithSunset(
    vector<int>::const_iterator sequence_begin,
    const vector<int>::const_iterator& sequence_end) {
  vector<pair<int, int>> s;
  int i = 0;
  for (auto it = sequence_begin; it != sequence_end; i++, it++) {
    if (s.empty() || s.back().first > *it) {
      s.push_back({*it, i});
    } else {
      while (!s.empty() && s.back().first <= *it) {
        s.pop_back();
      }
      s.push_back({*it, i});
    }
  }
  vector<int> final;
  for (auto it = s.rbegin(); it != s.rend(); it++) {
    final.push_back(it->second);
  }
  return final;
}
vector<int> ExamineBuildingsWithSunsetWrapper(const vector<int>& sequence) {
  return ExamineBuildingsWithSunset(cbegin(sequence), cend(sequence));
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"sequence"};
  return GenericTestMain(args, "sunset_view.cc", "sunset_view.tsv",
                         &ExamineBuildingsWithSunsetWrapper,
                         DefaultComparator{}, param_names);
}
