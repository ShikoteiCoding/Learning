#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Remove duplicated in ordered vector in C++
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        
        int c = nums[0];
        int k = 1;
        
        int i = 0;
        for (int v: nums) {
            if (v > c) {
                nums[k] = v;
                k += 1;
                c = v;
            }
            
            i++;
        }
        return k;
    }
};

int main() {

    Solution s;

    vector<int> list = {1, 2, 3, 4, 5, 5, 5, 6};

    int output = s.removeDuplicates(list);

    for (int c: list) {
        cout << c << '\t';
    } 
    
    return 0;
}