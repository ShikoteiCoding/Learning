#include <iostream>
#include <string>
#include <map>

using namespace std;

// Leetcode: Convert Integer to Roman notation
class Solution {
public:
    string intToRoman(int num) {
        string res = "";
        int i = 1;
        int d = 0;
        
        map<int, char> m = {
            {1, 'I'},
            {5, 'V'},
            {10, 'X'},
            {50, 'L'},
            {100, 'C'},
            {500, 'D'},
            {1000, 'M'}
        };
        
        while (num > 0) {
            d = num % 10;
            num = num / 10;
            
            if (d <= 3) {
                res = string(d, m[i]) + res;
            } else if (d == 4 || d == 9) {
                res = string(1, m[i]) + string(1, m[i*(d+1)]) + res;
            } else if (d > 4 && d < 9) {
                res = string(1, m[5*i]) + string(d - 5, m[i]) + res;
            }
            
            i *= 10;
        }
        
        return res;
    }
};

int main() {

    Solution s;
    
    int v = 1998;

    string output = s.intToRoman(v);
    cout << output << endl;
    
    return 0;
}