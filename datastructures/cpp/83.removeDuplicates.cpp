#include <iostream>

using namespace std;

// Leatcode: Delete duplicates values in sorted linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        
        ListNode* curr = head;
        
        while (curr != NULL && curr->next != NULL) {
            
            if (curr->val == curr->next->val) {
                curr->next = curr->next->next;
            } else {
                curr = curr->next;
            }
        }
        
        return head;
    }
};

int main() {

    Solution s;

    ListNode* list = new ListNode(3);
    list->next = new ListNode(3);
    list->next->next = new ListNode(4);
    list->next->next->next = new ListNode(5);

    ListNode* output = s.deleteDuplicates(list);
    
    ListNode* curr = output;
    while (curr != NULL) {
        cout << curr->val << endl;
        curr = curr->next;
    }
    
    return 0;
}