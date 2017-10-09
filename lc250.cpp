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
    int countUnivalSubtrees(TreeNode* root) {
        if (!root) return 0;
        int cnt = 0;
        dfs(root, cnt);
        return cnt;
    }
private:
    bool dfs(TreeNode* node, int& cnt) {
        bool isUni = true;
        if (node->left) isUni &= (dfs(node->left, cnt) && node->val == node->left->val);
        if (node->right) isUni &= (dfs(node->right, cnt) && node->val == node->right->val);
        if (isUni) cnt++;
        return isUni;
    }
};