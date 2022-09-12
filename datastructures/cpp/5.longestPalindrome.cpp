#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Leetcode: Longest substring palindrom in a string
class Solution {
public:
    bool isPalindrome(string s1) {
        string s2 = s1;
        reverse(s1.begin(),s1.end());
        return s2 == s1;
    }
public:
    string longestPalindrome(string s) {
        if (isPalindrome(s)) { return s; }
        
        int max_length = 1;
        int start = 0;
        bool test_two = false;
        
        for (int i=1; i<s.size(); i++) {
            string one_more_char = s.substr(i - max_length, max_length + 1);
            string two_more_char;
            test_two = false;
            
            if (i - max_length - 1 >= 0) {
                two_more_char = s.substr(i - max_length - 1, max_length + 2);
                if (isPalindrome(two_more_char)) {
                    start = i - max_length - 1;
                    max_length = max_length + 2;
                    test_two = true;
                }
            }
            if (isPalindrome(one_more_char) && !test_two) {
                start = i - max_length;
                max_length ++;
                test_two = false;
            }
            
        }
        
        return s.substr(start, max_length);
    }
};

int main() {

    Solution s;

    string st = "abcabacbc";

    string output = s.longestPalindrome(st);

    cout << output << endl;
    
    return 0;
}