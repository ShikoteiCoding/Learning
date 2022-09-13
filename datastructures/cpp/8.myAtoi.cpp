#include <iostream>
#include <string>
#include <vector>
#include <cstdint>
#include <climits>
using namespace std;

// Leetcode: String to Integer
class Solution {
public:
    int myAtoi(string s) {
        int j = 0;
            
        while (j < s.size()) {
            if (s[j] == ' ') {
                j++;
            } else {
                break;
            }
        }
        
        int64_t r = 0;
        bool negative = false;
        
        int i = j;

        while (i < s.size()) {
            
            if ((s[i] == '-' || s[i] == '+') && i == j) {
                if (s[i] == '-') {
                    negative = true;
                }
            } else if (s[i] >= 48 && s[i] <= 57) {
                r = 10*r + s[i] - 48;
            } else {
                break;
            }
            
            if (r > INT_MAX) {
                r = negative ? INT_MIN : INT_MAX;
                break;
            }
            
            i++;
        }
        
        return negative ? (int32_t) (- r) : (int32_t) r;
    }
};

int main() {

    Solution s;

    string st = "-1261572";
    int r = 3;

    int output = s.myAtoi(st);
    cout << output << endl;
    
    return 0;
}