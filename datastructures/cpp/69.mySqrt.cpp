#include <iostream>
#include <string>

using namespace std;

// Leetcode: Integer part of square root
class Solution {
public:
    int mySqrt(int x) {
        
        if (x == 1) { return 1; }
        
        long int m = x / 2;
        int r = m;
        int l = 0;
        
        while (true) {
            if (r - l <= 1) { return m; }
            
            if (m*m > x) {
                r = m;
                m = (m + l) / 2;
            } else {
                l = m;
                m = (m + r) / 2;
            }
        }
        return m;
    }
};

int main() {

    Solution s;

    int output = s.mySqrt(16);
    
    cout << output << endl;
    
    return 0;
}