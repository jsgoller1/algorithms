#include <limits>
#include <vector>

#include "test_framework/generic_test.h"
using std::vector;
double BuyAndSellStockTwice(const vector<double>& prices) {
  double negative_infinity = -std::numeric_limits<double>::infinity();
  double firstBuy = negative_infinity;
  double firstSell = 0.0;
  double secondBuy = negative_infinity;
  double secondSell = 0.0;
  for (auto price : prices) {
    firstBuy = (firstBuy > -price) ? firstBuy : -price;
    firstSell = (firstSell > (price + firstBuy)) ? firstSell : price + firstBuy;
    secondBuy =
        (secondBuy > (firstSell - price)) ? secondBuy : firstSell - price;
    secondSell =
        (secondSell > (secondBuy + price)) ? secondSell : secondBuy + price;
  }
  return secondSell;
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"prices"};
  return GenericTestMain(args, "buy_and_sell_stock_twice.cc",
                         "buy_and_sell_stock_twice.tsv", &BuyAndSellStockTwice,
                         DefaultComparator{}, param_names);
}
