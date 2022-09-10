#include <iostream>
#include <string>

using namespace std;

// Leetcode: Addition of binary strings
class Solution {
public:
    string addBinary(string a, string b) {
        int max_l = max(a.size(), b.size());
        int sum;
        
        a.insert(a.begin(), max_l - a.size(), '0');
        b.insert(b.begin(), max_l - b.size(), '0');
        
        int r = 0;
        string s = "";
        
        for (int i = max_l - 1; i >= 0; i--) {
            sum = (i>=0?a[i]-'0':0) + (i>=0?b[i]-'0':0) + r;
            
            if (sum%2 == 1) {
                s = "1" + s;
            } else {
                s = "0" + s;
            }
            
            if (sum<2) {
                r = 0;
            } else {
                r = 1;
            }
        }
        
        if (r > 0) {
            s = "1" + s;
        }
        
        return s;
    }
};

int main() {

    Solution s;

    string st = "i have some words to say";

    string output = s.addBinary("1111", "1101");

    for (char v: output) {
        cout << v << endl;
    }
    return 0;
}