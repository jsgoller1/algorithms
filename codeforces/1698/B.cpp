#include <iostream>

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
    iin(cases_n);
    ll vals, k;
    rep(i, cases_n){
        cin >> vals >> k;
        if (k == 1){
            output(((vals%2) ? (vals/2) : ((vals-1)/2))) ;
            while(vals-- > 0){cin >> k;}
        }
        else {
            ull too_tall = 0, l, m, r;
            cin >> m >> r; vals-=2;
            while (vals > 0){
                l = m;
                m = r;
                cin >> r;
                vals--;
                if (m > l+r){too_tall++;}
            }
            output(too_tall);
        }
    }

    return 0;
}