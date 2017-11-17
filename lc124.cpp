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
    int maxPathSum(TreeNode* root) {
        int sum = INT_MIN;
        dfs(root, sum);
        return sum;
    }
private:
    int dfs(TreeNode* root, int& sum) {
        if (!root) return 0;
        int left = max(0, dfs(root->left, sum));
        int right = max(0, dfs(root->right, sum));
        sum = max(left + right + root->val, sum);
        return max(left, right) + root->val;
    }
};