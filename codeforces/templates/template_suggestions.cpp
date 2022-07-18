#pragma GCC optimize("Ofast")
#pragma GCC optimization("unroll-loops")
#pragma GCC target("avx,avx2,fma")

#include <bits/stdc++.h>

#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/trie_policy.hpp>
#include <ext/rope>

using namespace __gnu_pbds;
using namespace __gnu_cxx;

mt19937 rng(chrono::steady_clock::now().time_since_epoch().count());

#define gcd __gcd

typedef vector<int> vi;
typedef vector<vector<int>> vvi;
typedef vector<ll> vll;
typedef vector<vector<ll>> vvll;
typedef vector<bool> vb;
typedef vector<vector<bool>> vvb;
template <typename T, typename cmp = less<T>>
using ordered_set =
    tree<T, null_type, cmp, rb_tree_tag, tree_order_statistics_node_update>;
typedef trie<string, null_type, trie_string_access_traits<>, pat_trie_tag,
             trie_prefix_search_node_update>
    pref_trie;

#define _USE_MATH_DEFINES

#define EPS 1e-9

#define vec_in(type, var, count) \
  vector<type> var(count);       \
  for (int i = 0; i < count; i++) cin >> var[i];
#define vec_2d(type, var, m, n, val) \
  vector<vector<type>> var(m, vector<type>(n, val));
