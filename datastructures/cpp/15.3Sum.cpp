#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// Leetcode: 3Sum in array of integers
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res = {};
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size(); i++) {
            
            if (i>0 && nums[i] == nums[i-1]) { continue; }
            
            int l = i+1;
            int r = nums.size() - 1;
            
            while (l < r) {
                
                int sum = nums[i] + nums[l] + nums[r];
                
                if (sum > 0) {
                    r--;
                } else if (sum < 0) {
                    l++;
                } else if (sum == 0) {
                    res.push_back({nums[i], nums[l], nums[r]});
                    while (l<r && nums[l] == nums[l+1]) {
                        l++;
                    }
                    
                    while (l<r && nums[r] == nums[r-1]) {
                        r--;
                    }
                    l++;
                }
            }
        }
        return res;
    }
};


int main() {

    Solution s;

    vector<int> st = {1, 2, 7, -2, 3, 1, -4, -5, 0, 4, -3, -1};
    vector<vector<int>> output = s.threeSum(st);
    
    for (vector<int> v: output) {
        for (int r: v) {
            cout << r << ' ';
        }
        cout << endl;
    }
    
    return 0;
}