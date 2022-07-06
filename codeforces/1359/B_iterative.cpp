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
#define LINF numeric_limits<long long>::max()

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

static ll solve_line(char* line, ll w, ll cost1, ll cost2) {
  ll costs[w];
  costs[0] = (line[0] == '*' ? 0 : cost1);
  for (int i = 1; i < w; i++) {
    if (line[i] == '*') {
      costs[i] = costs[i - 1];
      continue;
    }
    ll c1 = costs[i - 1] + cost1;
    ll c2 = LINF;
    if (line[i - 1] == '.') {
      c2 = cost2 + (i - 1 == 0 ? 0 : costs[i - 2]);
    }
    costs[i] = (c1 < c2 ? c1 : c2);
  }
  return costs[w - 1];
}

static void solve() {
  lin(h);
  lin(w);
  lin(cost1);
  lin(cost2);
  ll total = 0;
  char line[w];
  while (h--) {
    rep(i, w) { cin >> line[i]; }
    total += solve_line(line, w, cost1, cost2);
  }
  output(total);
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  //  read_from_files();
  lin(cases);

#ifdef LOCAL
  start_time = getCurrentTime();
  rep(i, cases) {
    case_time = getCurrentTime();
    eprintf("Case %d: ", i);

    solve();
    eprintf("%f sec \n", getCurrentTime() - case_time);
  }
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#else
  rep(i, cases) { solve(); }
#endif

  return 0;
}
