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
    int findBottomLeftValue(TreeNode* root) {
        if (!root) return 0;
        int value = root->val, valLevel = 0;
        dfs(root, 0, value, valLevel);
        return value;
    }
private:
    void dfs(TreeNode* node, int level, int& value, int& valLevel) {
        if (!node) return;
        dfs(node->left, level+1, value, valLevel);
        dfs(node->right, level+1, value, valLevel);
        if (level > valLevel) {
            valLevel = level;
            value = node->val;
        }
        return;
    }
};