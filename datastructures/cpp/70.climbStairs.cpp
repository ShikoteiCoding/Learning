#include <iostream>
#include <string>

using namespace std;

// Leetcode: Count square with 2 possibilities (fibonacci)
class Solution {
public:
    int climbStairs(int n) {
        
        if (n <= 3) { return n; }
        
        int n1 = 1;
        int n2 = 1;
        int nth = 0;
        int i = 0;
        
        while (i < n - 1) {
            nth = n1 + n2;
            n1 = n2;
            n2 = nth;
            i++;
        }
        return nth;
    }
};


int main() {

    Solution s;

    int output = s.climbStairs(9);
    
    cout << output << endl;
    
    return 0;
}