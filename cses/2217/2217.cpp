// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

// Includes all standard headers (no need for <vector>, <list>, etc).
#include <bits/stdc++.h>

using namespace std;

// --- I/O ---
/*
sync_with_stdio(): do not sync C++ streams (e.g. std::cin) with C streams
(e.g. stdin) after each output; adds unnecessary time.

tie(): untie cin from cout (tied by default); if tied, each read from cin
flushes cout, adds unnecessary time. Unclear from Stroustrup if both need to be
untied, doing it to be safe.
*/
#define sanic_io()                  \
  ios_base::sync_with_stdio(false); \
  cin.tie(NULL);                    \
  cout.tie(NULL);
#define endl "\n"  // std::endl causes a flush, adds unnecessary time
#define read_from_files(in_path, out_path) \
  freopen(in_path, "r", stdin);            \
  freopen(out_path, "w", stdout);
#define output(val) cout << val << endl;
#define var_in(type, var) \
  type var;               \
  cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)

// --- Abbreviations --
#define rep(i, n) for (int i = 0; i < (n); i++)
#define rep1(i, n) for (int i = 1; i <= (n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()  // reverse iterator
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define mp make_pair

// -- Types --
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<pii> vii;
typedef vector<pll> vll;

// -- Testing --
#ifdef LOCAL
#define eprintf(...)              \
  {                               \
    fprintf(stderr, __VA_ARGS__); \
    fflush(stderr);               \
  }

#else
#define eprintf(...) 0
#endif

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

ll calculateSwap(vl& nums, ll oldIdx, ll newIdx) {
  bool beforePredecessorLeft = false;
  bool beforeSuccessorRight = false;

  bool afterPredecessorLeft = false;
  bool afterSuccessorRight = false;

  ll sweepModifier = 0;
  if (beforePredecessorLeft != afterPredecessorLeft) {
    sweepModifier += (afterPredecessorLeft) ? -1 : 1;
  }
  if (beforeSuccessorRight != afterSuccessorRight) {
    sweepModifier += (afterSuccessorRight) ? -1 : 1;
  }
  return sweepModifier;
}

void swap(vl& nums, ll left, ll right) {
  ll temp = nums[left];
  nums[left] = nums[right];
  nums[right] = temp;
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
  lin(count);
  lin(swaps);

  vector<ll> sortedNums;
  map<ll, size_t> sortedPlaces;
  vector<ll> nums;
  map<ll, size_t> places;

  rep(i, count) {
    lin(num);
    nums.pb(num);
    sortedNums.pb(num);

    places[num] = i;
  }
  sort(sortedNums.begin(), sortedNums.end());
  rep(i, count) { sortedPlaces[sortedNums[i]] = i; }

  // First, determine the number of passes needed for the initial array
  ll passes = 1;
  rep(i, int(sortedNums.size() - 1)) {
    ll first = sortedNums[i];
    ll second = sortedNums[i + 1];
    if (places[first] > places[second]) {
      passes++;
    }
  }

  /*
  Then handle the swaps. For both numbers we are swapping:
  - if the swap moved its predecessor from its left to its right, add one pass.
  - if the swap moved its predecessor from its right to its left, remove one
  pass.
  - if the swap didn't change the side its predecessor was on (correct or not),
  no change.
  - then do the same but opposite thing for the successor.

  Note: if the two numbers are successors of each other make sure we don't
  double count; if we swapped 3 and 4, we still need to account for 4's
  successor and 3's predecessor, but we only need to account for 4's predecessor
  xor 3's successor.

  */
  rep(i, swaps) {
    lin(j);
    j--;
    lin(k);
    k--;
    passes += calculateSwap(nums, j, k);
    passes += calculateSwap(nums, k, j);

    // Don't double count reorderings
    if (sortedPlaces[nums[j]] + 1 == sortedNums[j + 1]) {
      passes--;
    }

    swap(nums, j, k);
    places[nums[j]] = k;
    places[nums[k]] = j;
  }

  return 0;
}
