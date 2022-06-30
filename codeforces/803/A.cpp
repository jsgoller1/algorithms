#include <iostream>
#include <string>
#include <unordered_set>

#define io_optimize() ios_base::sync_with_stdio(false); cin.tie(NULL);
#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(i, n) for (int i=0; i<(n); i++)
#define endl "\n"
#define output(val) cout << val << endl;
#define fi first
#define se second
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    io_optimize();
    iin(cases_n);
    int vals; unordered_set<int> line; int total; int curr;
    rep(i, cases_n){
        cin >> vals;
        total = 0; line.clear();
        rep(j, vals){
            cin >> curr;
            total ^= curr;
            line.insert(curr);
        }
        for (int k: line){
            if (line.find(k^total) != line.end()){
                output(k);
                break;
            }
        }
    }
    return 0;
}