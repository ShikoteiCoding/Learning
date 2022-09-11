#include <iostream>
#include <vector>

using namespace std;

// Leatcode: Same Binary Tree check
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
class Solution {
public:
    void _rec_inorder(TreeNode* node, vector<int>& res) {

        if (node != NULL) {
            res.push_back(node->val);
            _rec_inorder(node->left, res);
            _rec_inorder(node->right, res);
        } else {
            res.push_back(-1);
        }
    }
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<int> v1;
        vector<int> v2;
        _rec_inorder(p, v1);
        _rec_inorder(q, v2);
        
        if (v1.size() != v2.size()) { return false; }
        
        for (int i = 0; i<v1.size(); i++) {
            if (v1[i] != v2[i]) { return false; }
        }
        
        return true;
    }
};

int main() {

    Solution s;

    TreeNode* root1 = new TreeNode(0);
    root1->left = new TreeNode(1);
    root1->right = new TreeNode(2);
    root1->right->left = new TreeNode(3);
    root1->right->right = new TreeNode(4);

    TreeNode* root2 = new TreeNode(1);
    root2->left = new TreeNode(1);
    root2->right = new TreeNode(2);
    root2->right->left = new TreeNode(3);
    root2->right->right = new TreeNode(4);

    bool output = s.isSameTree(root1, root2);
    
    cout << output << endl;
    
    return 0;
}