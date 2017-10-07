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
    vector<int> largestValues(TreeNode* root) {
        vector<int> maxVals;
        dfs(root, maxVals, 0);
        return maxVals;
    }
private:
    void dfs(TreeNode* node, vector<int>& maxVals, int level) {
        if (!node) return;
        if (level == maxVals.size()) maxVals.push_back(INT_MIN);
        maxVals[level] = max(maxVals[level], node->val);
        dfs(node->left, maxVals, level+1);
        dfs(node->right, maxVals, level+1);
        return;
    }
};