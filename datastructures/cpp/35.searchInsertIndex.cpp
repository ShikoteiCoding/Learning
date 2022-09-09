#include <iostream>
#include <vector>

using namespace std;

// Leetcode: Upsert index search
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        
        int pos = 0;
        
        for (int v: nums) {
            if (v >= target) { return pos; }
            pos++;
        }
        return pos;
    }
};

int main() {

    Solution s;

    vector<int> list = {1, 2, 3, 4, 5, 5, 5, 6};

    int output = s.searchInsert(list, 2);

    for (int c: list) {
        cout << c << '\t';
    }
    cout << '\n' << output << '\n';
    
    return 0;
}