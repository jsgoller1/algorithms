#include <tuple>

#include "test_framework/fmt_print.h"
#include "test_framework/generic_test.h"
#include "test_framework/serialization_traits.h"
struct Rect {
  // x and y are bottom left corner
  int x, y, width, height;
};

bool operator==(const Rect& r1, const Rect& r2) {
  return std::tie(r1.x, r1.y, r1.width, r1.height) ==
         std::tie(r2.x, r2.y, r2.width, r2.height);
}

bool pointIntervalIntersect(const int p, const int l, const int r) {
  // p in [l,r]?
  return l <= p && p <= r;
}

bool cornerOverlap1D(const int aLeft, const int aRight, const int bLeft,
                     const int bRight) {
  return pointIntervalIntersect(bLeft, aLeft, aRight) ||
         pointIntervalIntersect(bRight, aLeft, aRight) ||
         pointIntervalIntersect(aLeft, bLeft, bRight) ||
         pointIntervalIntersect(aRight, bLeft, bRight);
}

Rect IntersectRectangle(const Rect& r1, const Rect& r2) {
  int r1Left = r1.x;
  int r1Down = r1.y;
  int r1Right = r1.x + r1.width;
  int r1Up = r1.y + r1.height;

  int r2Left = r2.x;
  int r2Down = r2.y;
  int r2Right = r2.x + r2.width;
  int r2Up = r2.y + r2.height;

  if (!(cornerOverlap1D(r1Left, r1Right, r2Left, r2Right) &&
        cornerOverlap1D(r1Down, r1Up, r2Down, r2Up))) {
    return {0, 0, -1, -1};
  }
  std::vector<int> yVals{r1Up, r1Down, r2Up, r2Down};
  std::sort(yVals.begin(), yVals.end());
  std::vector<int> xVals{r1Left, r1Right, r2Left, r2Right};
  std::sort(xVals.begin(), xVals.end());

  return {xVals[1], yVals[1], xVals[2] - xVals[1], yVals[2] - yVals[1]};
}

namespace test_framework {
template <>
struct SerializationTrait<Rect> : UserSerTrait<Rect, int, int, int, int> {
  static std::vector<std::string> GetMetricNames(const std::string& arg_name) {
    return {FmtStr("height({})", arg_name), FmtStr("width({})", arg_name)};
  }

  static std::vector<int> GetMetrics(const Rect& x) {
    return {x.height, x.width};
  }
};
}  // namespace test_framework

std::ostream& operator<<(std::ostream& out, const Rect& r) {
  return PrintTo(out, std::make_tuple(r.x, r.y, r.width, r.height));
}

int main(int argc, char* argv[]) {
  std::vector<std::string> args{argv + 1, argv + argc};
  std::vector<std::string> param_names{"r1", "r2"};
  return GenericTestMain(args, "rectangle_intersection.cc",
                         "rectangle_intersection.tsv", &IntersectRectangle,
                         DefaultComparator{}, param_names);
}
