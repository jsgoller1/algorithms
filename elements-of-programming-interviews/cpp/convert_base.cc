#include <cmath>
#include <string>

#include "test_framework/generic_test.h"
using std::string;

/*
- num can be between int max and min
- int can be negative, and may have prefixes
- 0 is valid in any base
- b1, b2 are 2-16
- converting bin string to dec int: multiply each digit by power of two, sum and
return
- converting dec int to bin string: left to right starting from closest pow of 2
less than num: # set bit and subtract value.
*/

#define ASCII_ZERO 48
#define ASCII_A_LOWER 97
#define ASCII_A_UPPER 65

int digitToInt(const char digit) {
  if ('0' <= digit && digit <= '9') {
    return digit - ASCII_ZERO;
  } else if ('A' <= digit && digit <= 'F') {
    return digit - ASCII_A_UPPER + 10;
  } else if ('a' <= digit && digit <= 'f') {
    return digit - ASCII_A_LOWER + 10;
  }
  return -1;
}

char intToDigit(const int val) {
  if (0 <= val && val <= 9) {
    return val + ASCII_ZERO;
  } else if (0xA <= val && val <= 0xF) {
    return val - 10 + ASCII_A_UPPER;
  }
  return '!';
}

int stringToInt(const string& val, int oldBase) {
  bool neg = val[0] == '-';
  int total = 0;
  int pow = 1;
  for (int i = val.size() - 1; i >= (neg ? 1 : 0); i--) {
    total += (digitToInt(val[i]) * pow);
    pow *= oldBase;
  }
  return total * (neg ? -1 : 1);
}
string intToString(int value, int newBase) {
  if (!value) {
    return "0";
  }
  bool neg = value < 0;
  value = abs(value);

  string representation = neg ? "-" : "";
  long exp = 0;
  long sym = 1;
  while ((sym * long(pow(newBase, exp))) <= value) {
    exp++;
  }
  exp--;

  while (value) {
    sym = newBase - 1;
    while ((sym * int(pow(newBase, exp))) > value && sym > 0) {
      sym--;
    }
    representation += intToDigit(sym);
    value -= (sym * int(pow(newBase, exp)));
    exp--;
  }
  while (exp >= 0) {
    representation += '0';
    exp--;
  }

  return representation;
}

string ConvertBase(const string& num_as_string, int b1, int b2) {
  int base10Val = stringToInt(num_as_string, b1);
  string newVal = intToString(base10Val, b2);
  return newVal;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"num_as_string", "b1", "b2"};
  return GenericTestMain(args, "convert_base.cc", "convert_base.tsv",
                         &ConvertBase, DefaultComparator{}, param_names);
}
