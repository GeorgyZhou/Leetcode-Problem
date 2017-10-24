/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        TreeNode *left = root->left;
        TreeNode *right = root->right;
        root->left = NULL;
        flatten(left);
        root->right = left;
        TreeNode *tail = root;
        while (tail->right != NULL) tail = tail->right;
        flatten(right);
        tail->right = right;
    }
};