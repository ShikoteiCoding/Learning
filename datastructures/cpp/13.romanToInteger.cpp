#include <iostream>
#include <map>

using namespace std;

// Leetcode: Roman Number to Integer C++

class Solution {
public:
    int romanToInt(string s) {
        
        map<char, int> c = {
            {'I', 1},
            {'V', 5},
            {'X', 10},
            {'L', 50},
            {'C', 100},
            {'D', 500},
            {'M', 1000}
        };
        
        int count = 0;
        int prev = 0;
        
        for (int i = 0; i < s.size(); i++) {
            
            int curr = c[s[i]];
            
            if (prev < curr) {
                count = count - 2 * prev + curr;
            } else {
                count += curr;
            }
            prev = curr;
        };
        
        return count;
    }
};

int main() {

    Solution s;

    int output = s.romanToInt("MCMXCIV");

    cout << output;
    
    return 0;
}