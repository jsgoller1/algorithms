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

ll updateSweepCount(const vl& nums, size_t idx) {
  ll modifier = 0;
  if (idx < nums.size() - 1 && nums[idx] < nums[idx + 1]) {
    modifier++;
  } else {
    modifier--;
  }

  if (0 < idx && nums[idx - 1] < nums[idx]) {
    modifier++;
  } else {
    modifier--;
  }
  return modifier;
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
  lin(count);
  lin(swaps);
  vector<ll> nums;
  map<ll, size_t> places;
  rep(i, count) {
    lin(num);
    nums.pb(num);
    places[num] = i;
  }
  sort(nums.begin(), nums.end());

  ll passes = 1;
  rep(i, int(nums.size() - 1)) {
    ll first = nums[i];
    ll second = nums[i + 1];
    if (places[first] > places[second]) {
      passes++;
    }
  }
  rep(i, swaps) {
    lin(j);
    lin(k);
    ll temp = nums[k];
    nums[k] = nums[j];
    nums[j] = temp;
    passes += updateSweepCount(nums, k);
    passes += updateSweepCount(nums, j);
    output(passes);
  }

  return 0;
}
