#include <iostream>
#include <string>
#include <vector>

using namespace std;

// Leetcode: Elevator string writing
class Solution {
public:
    string convert(string s, int numRows) {
        
        if (numRows >= s.size() or numRows == 1) {
            return s;
        }
        
        vector<string> rows(numRows);
        int curRow = 0;
        bool forth = false;
        
        for (char c: s) {
            rows[curRow] += c;
            
            if (curRow == 0 or curRow == numRows - 1) {
                forth = !forth;
            }
            curRow += forth ? 1 : -1;
        }
        
        string res;
        for (string row: rows) { res += row; }
        return res;
    }
};

int main() {

    Solution s;

    string st = "abcabacbc";
    int r = 3;

    string output = s.convert(st, 3);
    cout << output << endl;
    
    return 0;
}