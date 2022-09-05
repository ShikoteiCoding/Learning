#include <iostream>
#include <vector>

using namespace std;

class Solution {

public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // 
        vector<int> seenIndices;
        return seenIndices;
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

    for (int i = 0; i < 4; i++) {
        cout << nums[i] << ' ';
    }

    return 0;
}