#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Longest Common Prefix C++

class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        
        string first_word = strs[0];
        
        if (first_word.size() == 0) {
            return prefix;
        }
        
        for (char letter: first_word) {
            for (string word: strs) {
                if (prefix.size() > word.size() || word.rfind(prefix + letter, 0) != 0) {
                    return prefix;
                }
            }
            prefix += letter;
        }
        
        return prefix;
    }
};

int main() {

    Solution s;

    vector<string> strs = {"flower", "flow", "flies"};

    string output = s.longestCommonPrefix(strs);

    cout << output;
    
    return 0;
}