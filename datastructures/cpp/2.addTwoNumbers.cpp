#include <iostream>
#include <vector>

using namespace std;

// Leatcode: Linked list Numbers Addition
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* d = new ListNode(0);
        
        int r = 0;
        int t = 0;
        
        ListNode* tail = d;
        
        while (l1 != NULL || l2 != NULL || r != 0) {
            t = r;
            if (l1 != NULL) {
                t += l1->val;
                l1 = l1->next;
            }
            if (l2 != NULL) {
                t += l2->val;
                l2 = l2->next;
            }
            
            if (t >= 10) {
                tail->next = new ListNode(t % 10);
                r = 1;
            } else {
                tail->next = new ListNode(t);
                r = 0;
            }
            
            tail = tail->next;
        }
        
        return d->next;
    }
};


int main() {

    Solution s;

    ListNode* root1 = new ListNode(0);
    root1->next = new ListNode(1);
    root1->next->next = new ListNode(2);

    ListNode* root2 = new ListNode(1);
    root2->next = new ListNode(1);
    root2->next->next = new ListNode(2);

    ListNode* output = s.addTwoNumbers(root1, root2);
    
    return 0;
}