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
    int longestUnivaluePath(TreeNode* root) {
        if (!root) return 0;
        int maxValue = 0;
        dfs(root, maxValue);
        return maxValue;
    }
private:
    int dfs(TreeNode* node, int& maxValue) {
        if (!node->left && !node->right) return 0;
        int leftValue = 0, rightValue = 0;
        if (node->left) {
            leftValue = dfs(node->left, maxValue);
            if (node->left->val == node->val) {
                leftValue += 1;
            } else {
                leftValue = 0;
            }
        }
        if (node->right) {
            rightValue = dfs(node->right, maxValue);
            if (node->right->val == node->val) {
                rightValue += 1;
            } else {
                rightValue = 0;
            }
        }
        int curValue = rightValue + leftValue;
        maxValue = max(maxValue, curValue);
        return max(leftValue, rightValue);
    }
};