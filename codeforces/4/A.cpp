#include <iostream>

/*
For weight w:
    - can't divide into w and 0
    - 1 = no
    - 2 = no
    - 3 = no
    - 4 = yes (2 + 2)
    - 5 = no
    - 6 = yes (4 + 2)

if weight >= 4 and not weight % 0, print YES else print NO

*/

using namespace std;

int main(){
    int weight;
    cin >> weight;
    if (weight >= 4 && !(weight % 2)){
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }
    return 0;
}