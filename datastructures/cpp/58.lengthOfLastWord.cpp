#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Get the length of the last word in a sentence
class Solution {
public:
    int lengthOfLastWord(string s) {
        
        int l = 0;
        
        // Remove traling spaces
        while (!s.empty() && s.back() == ' ') {
            s.pop_back();
        }
        
        // Remove + count letters till a space or empty
        while (!s.empty() && s.back() != ' ') {
            l++;
            s.pop_back();
        }
        
        return l;
    }
};

int main() {

    Solution s;

    string st = "i have some words to say";

    int output = s.lengthOfLastWord(st);
    cout << output << endl;
    
    return 0;
}