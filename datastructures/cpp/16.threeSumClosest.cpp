#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Leetcode: 3Sum over target value
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = nums[0] + nums[1] + nums[2];
        
        for (int i = 0; i < nums.size(); i++) {
            int l = i+1;
            int r = nums.size() - 1;
            
            while (l < r) {
                int s = nums[i] + nums[l] + nums[r];
                
                
                if (abs(s - target) < abs(res - target)) {
                    res = s;
                } else if (s < target) {
                    l ++;
                } else if (s > target) {
                    r --;
                } else {
                    return res;
                }
            }
        }
        
        return res;
    }
};

int main() {

    Solution s;

    vector<int> st = {1, 2, 7, -2, 3, 1, -4, -5, 0, 4, -3, -1};
    int output = s.threeSumClosest(st, 3);
    
    cout << output << endl;
    
    return 0;
}