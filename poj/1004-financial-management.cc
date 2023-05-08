/*
http://poj.org/problem?id=1004

In:
100.00
489.12
12454.12
1234.10
823.05
109.20
5.27
1542.25
839.18
83.99
1295.01
1.75

Out:
$1581.42
*/

// Author: Joshua Goller
// Email: joshua.goller@hey.com
// Website: https://jsgoller1.github.io

// Includes all standard headers (no need for <vector>, <list>, etc).
#include <iostream>

using namespace std;

int main (){
    double x;
    double sum = 0;
    for(int i = 0; i < 12; i++){
        cin >> x;
        sum += x;
    }
    cout << "$" << sum/12 << endl;
    return 0;
}
