#include <iostream>
#include <vector>
#include <stack>

using namespace std;

// Leetcode: Valid Parenthesis C++

class Solution {
public:
    bool isValid(string s) {
        
        vector<char> opens = {'(', '{', '['};
        vector<char> closes = {')', '}', ']'};
        vector<string> pairs = {"()", "{}", "[]"};
        
        stack<char> stack;
        for (char c: s) {
            
            if (find(opens.begin(), opens.end(), c) != opens.end()) {
                stack.push(c);
            }
            
            if (find(closes.begin(), closes.end(), c) != closes.end()) {
                
                if (stack.empty()) { return false; }
                
                char last = stack.top();
                stack.pop();
                
                string pair = string(1, last) + string(1, c);
                
                if (find(pairs.begin(), pairs.end(), pair) == pairs.end()) {
                    return false;
                }
            }
        }
        
        return stack.empty();
    }
};

int main() {

    Solution s;

    string strs = "()[]{}";

    bool output = s.isValid(strs);

    cout << output;
    
    return 0;
}