#include <algorithm>
#include <iostream>

#define var_in(type, var) type var; cin >> var;
#define iin(var) var_in(int, var)
#define lin(var) var_in(ll, var)
#define strin(var) var_in(string, var)
#define rep(n) for (int i=0; i<(n); i++)
#define pb push_back

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

using namespace std;

int main(){
    strin(input);
    transform(input.begin(), input.end(), input.begin(), ::tolower);
    string output = "";
    for(auto c : input){
        switch(c){
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'y':
                break;
            default:
                output.pb('.');
                output.pb(c);
                break;
        }
    }
    cout << output << endl;
    return 0;
}