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
    int findTilt(TreeNode* root) {
        if (!root) return 0;
        int tilt = 0;
        dfs(root, tilt);
        return tilt;
    }
private:
    int dfs(TreeNode* node, int& tilt) {
        int leftSum = 0, rightSum = 0;
        if (node->left) leftSum = dfs(node->left, tilt);
        if (node->right) rightSum = dfs(node->right, tilt);
        tilt += abs(leftSum - rightSum);
        return leftSum + rightSum + node->val;
    }
};