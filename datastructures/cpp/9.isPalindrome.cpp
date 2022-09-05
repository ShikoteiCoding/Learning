#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Two Sum Problem C++

class Solution {
public:
    bool isPalindrome(int x) {
        
        if (x < 0) {
            return false;
        }
        
        string s = to_string(x);
        int size = s.size();
        int i = 0;
        int mid = int(size / 2);
        
        while (s[i] == s[size - 1 - i]) {
            if (i == mid) {
                return true;
            } 
            i = i + 1;
        }
        
        return false;
    }
};

int main() {

    Solution s;

    bool output = s.isPalindrome(121);

    cout << output;
    
    return 0;
}