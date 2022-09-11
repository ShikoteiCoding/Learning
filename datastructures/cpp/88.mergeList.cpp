#include <iostream>
#include <vector>

using namespace std;

// Leatcode: Merge 2 list in-place
class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        
        int i= m-1, j=n-1, k=m+n-1;
        
        if (n == 0) { return; }
        
        while (j>=0 && i >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k] = nums1[i];
                i--;
                k--;
            } else {
                nums1[k] = nums2[j];
                j--;
                k--;
            }
        }
        
        while (j>=0) {
            nums1[k] = nums2[j];
            j--;
            k--;
        }
    }
};

int main() {

    Solution s;
    
    vector<int> list1 = {1, 2, 3, 4, 7, 0, 0, 0};
    vector<int> list2 = {4, 5, 6};

    s.merge(list1, 5, list2, 3);
    
    for (int v: list1) {
        cout << v << endl;
    }
    
    return 0;
}