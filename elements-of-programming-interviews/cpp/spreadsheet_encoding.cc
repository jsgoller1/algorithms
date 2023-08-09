#include <cmath>
#include <string>

#include "test_framework/generic_test.h"
using std::string;

/*
A-Z = 1 to 26
AA = 27
ZZ = 702

- Not considering empty str
- This is a different kind of base 26; rightmost column is mod 26, next is mod
26*26.
- A to ZZ inclusive is 702 (26*26 + 26)
*/

#define ASCII_A 64  // so A = 1

int SSDecodeColIDWithExp(const string& col) {
  int total = 0;
  int exp = 0;
  for (auto it = col.rbegin(); it != col.rend(); it++, exp++) {
    total += ((*it - ASCII_A) * pow(26, exp));
  }
  return total;
}

int SSDecodeColID(const string& col) {
  int total = 0;
  for (auto it = col.begin(); it != col.end(); it++) {
    total = (total * 26) + *it - 'A' + 1;
  }
  return total;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"col"};
  return GenericTestMain(args, "spreadsheet_encoding.cc",
                         "spreadsheet_encoding.tsv", &SSDecodeColID,
                         DefaultComparator{}, param_names);
}
