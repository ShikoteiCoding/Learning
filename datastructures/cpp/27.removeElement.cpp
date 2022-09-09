#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Remove element in-place in cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        
        int k = 0;
        
        for (int v: nums) {
            if (v != val) {
                nums[k] = v;
                k++;
            }
        }
        return k;
        
    }
};

int main() {

    Solution s;

    vector<int> list = {1, 2, 3, 4, 5, 5, 5, 6};

    int output = s.removeElement(list, 2);

    for (int c: list) {
        cout << c << '\t';
    } 
    
    return 0;
}