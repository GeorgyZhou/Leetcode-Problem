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
    int rob(TreeNode* root) {
        return max(dfs(root, true), dfs(root, false));
    }
private:
    int dfs(TreeNode* node, bool include) {
        if (!node) return 0;
        if (include) { 
            return node->val + dfs(node->left, false) + dfs(node->right, false);
        } else {
            return rob(node->left) + rob(node->right);
        }
    }
};