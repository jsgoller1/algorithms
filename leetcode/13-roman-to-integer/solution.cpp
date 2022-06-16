/*
- numbers ordered L-R, greatest to least except for subtraction case
- 15 chars long, valid numeral
- val fits in int


greatest = 0
sum = 0
i = len-1
while i >= 0
    current = s[i]
    if current < max, sum -= current
    else sum += current
    greatest = max(current, greatest)

Note: the use of max() here is because I assumed 8 could be written as IIX; the problem rules this out though real roman numerals can look like this (https://en.wikipedia.org/wiki/Roman_numerals#Irregular_subtractive_notation); it causes an extra function call but also
lets us simplify the code by looking at one char at a time (other solutions do two at a time) with minimal runtime overhead.
*/

#include <algorithm>
#include <map>

class Solution {
public:
    int romanToInt(string s) {
        int sum = 0, greatest = 0;
        unordered_map<char, int> table = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        for (int i = s.length()-1; i >= 0; i--){
            table[s[i]] >= greatest ? sum += table[s[i]] : sum -= table[s[i]];
            greatest = std::max(table[s[i]], greatest);
        }
        return sum;
    }
};