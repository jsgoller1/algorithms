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
#define rep(i, n) for (ll i = 0; i < (n); i++)
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
#define eprintf(...) ;
#endif

clock_t start_time, case_time;
double getCurrentTime() { return ((double)clock()) / CLOCKS_PER_SEC; }

vl createStanding(ll duration, vl problems, ll idx) {
  sort(problems.begin(), problems.end());
  eprintf("Creating standing for: %lld, ", duration);
  rep(i, ll(problems.size())) { eprintf("%lld ", problems[i]); }
  eprintf("\n");

  ll score = 0;
  ll penalty = 0;
  ll currTime = 0;
  rep(i, ll(problems.size())) {
    if (problems[score] + currTime <= duration) {
      score++;
      currTime += problems[i];
      penalty += currTime;
      eprintf("%lld: currTime: %lld, penalty: %lld, score: %lld\n", i, currTime,
              penalty, score);
    }
  }

  eprintf("Final - currTime: %lld, penalty: %lld, score: %lld\n\n", currTime,
          penalty, score);
  vl standing(3, 0);
  standing[0] = score;
  standing[1] = penalty;
  standing[2] = idx;
  return standing;
}

bool standingsSort(vl& stand1, vl& stand2) {
  return (stand1[0] != stand2[0]) ? stand1[0] > stand2[0]
                                  : stand1[1] < stand2[1];
}

static void solve() {
  lin(participants);
  lin(problems);
  lin(duration);

  vl times(problems, 0);
  vector<vl> standings;
  rep(i, participants) {
    rep(j, problems) {
      lin(time);
      times[j] = time;
    }
    vl standing = createStanding(duration, times, i);
    standings.pb(standing);
  }
  sort(standings.begin(), standings.end(), standingsSort);
  rep(i, participants) {
    eprintf("%lld %lld %lld\n", standings[i][0], standings[i][1],
            standings[i][2]);
  }

  rep(i, ll(standings.size())) {
    if (standings[i][2] == ll(0)) {
      printf("%lld\n", i + 1);
    }
  }
}

int main() {
  sanic_io();
  // cout << setprecision(12);
  // read_from_files();
  lin(cases);

#ifdef LOCAL
  start_time = getCurrentTime();
  rep(i, cases) {
    case_time = getCurrentTime();
    solve();
    eprintf("Case %lld: %f sec \n", i, getCurrentTime() - case_time);
  }
  eprintf("Total time: %f sec \n", getCurrentTime() - start_time);
#else
  rep(i, cases) { solve(); }
#endif

  return 0;
}
