#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Add one to a list of integers (bigint simulation)
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        
        int i = 0;
        int n = digits.size();
        
        while (i < n) {
            if (digits[n-i-1] < 9) {
                digits[n-i-1] = digits[n-i-1]  + 1;
                return digits;
            }
            digits[n-i-1] = 0;
            i++;
        }
        
        digits.insert(digits.begin(), 1);
        return digits;
    }
};

int main() {

    Solution s;

    vector<int> vec= {1, 2, 3, 4};

    vector<int> output = s.plusOne(vec);
    
    for (int v: vec) {
        cout << v << endl;
    }
    return 0;
}