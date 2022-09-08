#include <iostream>
#include <vector>
#include <stack>

using namespace std;

// Leetcode: Merge two sorted linked list C++
// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode* dummy = new ListNode();
        ListNode* tail = dummy;
        
        while (true) {
            
            if (!list1) {
                tail->next = list2;
                break;
            }
            else if (!list2) {
                tail->next = list1;
                break;
            }
            
            if (list1->val <= list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            
            tail = tail->next;
        }
        return dummy->next;
    }
};

int main() {

    Solution s;

    ListNode* list1 = new ListNode(3);
    ListNode* list2 = new ListNode(2);

    ListNode* output = s.mergeTwoLists(list1, list2);

    cout << output->val;
    
    return 0;
}