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

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
  lin(customers);

  vl entrances;
  vl exits;
  rep(i, customers) {
    lin(enter);
    lin(exit);
    entrances.pb(enter);
    exits.pb(exit);
  }
  sort(entrances.begin(), entrances.end());
  sort(exits.begin(), exits.end());

  ll maxPeople = 0;
  ll currPeople = 0;
  size_t i = 0;
  size_t j = 0;
  while (i < entrances.size() && j < exits.size()) {
    if (entrances[i] == exits[j]) {
      i++;
      j++;
    } else if (entrances[i] < exits[j]) {
      currPeople++;
      i++;
    } else {  // entrances[i] > exits[j]
      currPeople--;
      j++;
    }
    maxPeople = (currPeople > maxPeople) ? currPeople : maxPeople;
  }

  // Don't need to test if any exits remain; can't lead to a new best.
  while (i < entrances.size()) {
    currPeople++;
    maxPeople = (currPeople > maxPeople) ? currPeople : maxPeople;
  }
  output(maxPeople);

  return 0;
}
