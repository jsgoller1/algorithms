#include "test_framework/generic_test.h"
double _helper(double x, int y, std::map<int, double>& dp) {
  if (dp.find(y) != dp.end()) {
    return dp[y];
  }
  double val = _helper(x, y / 2, dp);
  val *= val;
  if (y % 2) {
    val = (y < 0) ? val / x : val * x;
  }
  dp[y] = val;
  return dp[y];
}

double Power(double x, int y) {
  std::map<int, double> dp{{0, 1}, {1, x}, {-1, (1.0 / x)}};
  _helper(x, y, dp);
  return dp[y];
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"x", "y"};
  return GenericTestMain(args, "power_x_y.cc", "power_x_y.tsv", &Power,
                         DefaultComparator{}, param_names);
}
