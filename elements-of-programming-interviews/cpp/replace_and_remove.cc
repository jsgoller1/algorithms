#include <iterator>
#include <string>
#include <vector>

#include "test_framework/generic_test.h"
#include "test_framework/timed_executor.h"
using std::string;
using std::vector;

/*
- Replace every `a` with `d d`.
- Delete every b.
- Can assume s has enough space for final result
- Do not need to worry about values beyond size (e.g. array[0] to array[size]
must be represented in the final array)
- If we process it backwards, the dd overwrites will only overwrite chars we've
seen already. We know where it ends (or we can figure it out)
---
Trivial (o(n) on time and space): produce correct array, overwrite everything in
original

Cases:
  - empty
  - No replace (efgh)
  - all replace (aaaaaaaa)
  - all delete (bbbb)
*/

int ReplaceAndRemoveBruteForce(int size, char s[]) {
  vector<char> processed;
  for (int i = 0; i < size; i++) {
    switch (s[i]) {
      case 'b':
        break;
      case 'a':
        processed.push_back('d');
        processed.push_back('d');
        break;
      default:
        processed.push_back(s[i]);
        break;
    }
  }
  for (int i = 0; i < processed.size(); i++) {
    s[i] = processed[i];
  }
  return processed.size();
}

int calculateFinalSize(int size, char s[]) {
  int finalSize = 0;
  for (int i = 0; i < size; i++) {
    switch (s[i]) {
      case 'b':
        break;
      case 'a':
        finalSize += 2;
        break;
      default:
        finalSize++;
        break;
    }
  }
  return finalSize;
}

int removeB(int size, char s[]) {
  int j = 0;
  for (int i = 0; i < size; i++) {
    if (s[i] == 'b') {
      continue;
    }
    s[j++] = s[i];
  }
  return j;
}

void replaceA(int size, int finalSize, char s[]) {
  for (int i = finalSize - 1, j = size - 1; j >= 0; j--) {
    if (s[j] == 'a') {
      s[i--] = 'd';
      s[i--] = 'd';
    } else {
      s[i--] = s[j];
    }
  }
}

int ReplaceAndRemove(int size, char s[]) {
  int finalSize = calculateFinalSize(size, s);
  int newEnd = removeB(size, s);
  replaceA(newEnd, finalSize, s);
  return finalSize;
}

vector<string> ReplaceAndRemoveWrapper(TimedExecutor& executor, int size,
                                       const vector<string>& s) {
  std::vector<char> s_copy(s.size(), '\0');
  for (int i = 0; i < s.size(); ++i) {
    if (!s[i].empty()) {
      s_copy[i] = s[i][0];
    }
  }

  int res_size =
      executor.Run([&] { return ReplaceAndRemove(size, s_copy.data()); });

  vector<string> result;
  for (int i = 0; i < res_size; ++i) {
    result.emplace_back(string(1, s_copy[i]));
  }
  return result;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"executor", "size", "s"};
  return GenericTestMain(args, "replace_and_remove.cc",
                         "replace_and_remove.tsv", &ReplaceAndRemoveWrapper,
                         DefaultComparator{}, param_names);
}
