#include <iostream>
#include <vector>

using namespace std;

// Leatcode: Length of longest substring
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        string r = "";
        int m = 0;
        int pos = 0;
        
        for (char c: s) {
            pos = r.find(c);
            
            if (pos != -1) {
                r = r.substr(pos+1, r.size() - pos) + c;
            } else {
                r += c;
                m = r.size() >= m ? r.size() : m;
            }
        }
        
        return m;
    }
};

int main() {

    Solution s;

    string st = "abcabcabc";

    int output = s.lengthOfLongestSubstring(st);

    cout << output << endl;
    
    return 0;
}