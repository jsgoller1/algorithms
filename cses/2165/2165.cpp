// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

// Includes all standard headers (no need for <vector>, <list>, etc).
#include <bits/stdc++.h>

using namespace std;

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
#define rep(i, n) for (ll i = 0; i < (n); i++)
#define rep1(i, n) for (ll i = 1; i <= (n); i++)
#define all(x) (x).begin(), (x).end()
#define rall(x) (x).rbegin(), (x).rend()  // reverse iterator
#define fi first
#define se second
#define pb push_back
#define eb emplace_back
#define mp make_pair

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

void movePlate(vl& source, ll sourceID, vl& dest, ll destID, vl& moves) {
  moves.pb(sourceID);
  moves.pb(destID);
  ll val = source[0];
  dest.push_back(val);
  source.pop_back();
}

void solve(ll largestDisk, vl& source, ll sourceID, vl& dest, ll destID,
           vl& extra, ll extraID, vl& moves) {
  if (largestDisk == 1) {
    movePlate(source, sourceID, dest, destID, moves);
  } else {
    solve(largestDisk - 1, source, sourceID, extra, extraID, dest, destID,
          moves);
    movePlate(source, sourceID, dest, destID, moves);
    solve(largestDisk - 1, extra, extraID, dest, destID, source, sourceID,
          moves);
  }
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
  lin(disksN);
  vl left, center, right, moves;
  for (int i = disksN + 1; i > 0; i--) {
    left.pb(i);
  }

  solve(disksN, left, 1, right, 3, center, 2, moves);

  printf("%d\n", moves.size() / 2);
  rep(i, moves.size()) {
    printf("%d ", moves[i]);
    if (i % 2) {
      printf("\n");
    }
  }

  return 0;
}
