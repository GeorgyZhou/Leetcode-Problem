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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (p == q) return p;
        if (!root) return root;
        TreeNode* ret = root;
        dfs(root, p, q, ret);
        return ret;
    }
private:
    int dfs(TreeNode* root, TreeNode* p, TreeNode* q, TreeNode*& ret) {
        if (!root) return 0;
        int rootVal = (root == p ? 1 : (root == q ? 2 : 0));
        int lp = dfs(root->left, p, q, ret);
        if (lp == 3) return 3;
        int rp = dfs(root->right, p, q, ret);
        if (rp == 3) return 3;
        if (rootVal + lp == 3 || lp + rp == 3 || rootVal + rp == 3) {
            ret = root;
            return 3;
        }
        return max(rootVal, max(lp, rp));
    }
};