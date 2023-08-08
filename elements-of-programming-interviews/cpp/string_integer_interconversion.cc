#include <string>

#include "test_framework/generic_test.h"
#include "test_framework/test_failure.h"
using std::string;

#define ASCII_ZERO 48

string IntToString(int x) {
  if (!x) {
    return "0";
  }
  bool neg = (x < 0);
  string val;
  while (x) {
    int digit = abs(x % 10) + ASCII_ZERO;
    val += digit;
    x /= 10;
  }
  if (neg) {
    val += "-";
  }
  reverse(val.begin(), val.end());
  return val;
}

int StringToInt(const string& s) {
  bool neg = (s[0] == '-');
  bool skipFirstChar = neg || (s[0] == '+');
  unsigned place = 1;
  int total = 0;
  for (int i = s.length() - 1; i >= (skipFirstChar ? 1 : 0); i--) {
    char digit = s[i] - ASCII_ZERO;
    total += (digit * place);
    place *= 10;
  }
  return total * (neg ? -1 : 1);
}

void Wrapper(int x, const string& s) {
  if (stoi(IntToString(x)) != x) {
    throw TestFailure("Int to string conversion failed");
  }

  if (StringToInt(s) != x) {
    throw TestFailure("String to int conversion failed");
  }
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "s"};
  return GenericTestMain(args, "string_integer_interconversion.cc",
                         "string_integer_interconversion.tsv", &Wrapper,
                         DefaultComparator{}, param_names);
}
