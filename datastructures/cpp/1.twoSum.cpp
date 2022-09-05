#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Two Sum Problem C++

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int size = nums.size();
        
        for (int i = 0; i < size; i++) {
            if (abs(i) <= abs(target)) {
                for (int j = i + 1; j < size; j++) {
                    if (nums[j] + nums[i] == target) {
                        return {i, j};
                    }
                }
            }
        }
        return nums;
    }
};

int main() {

    vector<int> nums;
    nums.push_back(2);
    nums.push_back(7);
    nums.push_back(11);
    nums.push_back(15);

    Solution s;

    vector<int> output = s.twoSum(nums, 9);

    for (int i = 0; i < output.size() ; i++) {
        cout << output[i] << ' ';
    }

    return 0;
}