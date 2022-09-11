#include <iostream>
#include <vector>

using namespace std;

// Leatcode: Binary Tree in-order traversal: left first
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
            _rec_inorder(node->left, res);
            res.push_back(node->val);
            _rec_inorder(node->right, res);
        }
    }
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        
        _rec_inorder(root, res);
        
        return res;
    }
};

int main() {

    Solution s;

    TreeNode* root = new TreeNode(0);
    root->left = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(4);

    vector<int> output = s.inorderTraversal(root);
    
    for (int i: output) {
        cout << i << endl;

    }
    
    return 0;
}