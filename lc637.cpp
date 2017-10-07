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
    vector<double> averageOfLevels(TreeNode* root) {
        if (!root) return {};
        vector<double> avgs;
        vector<int> cnt;
        dfs(root, avgs, cnt, 0);
        for (int i = 0; i < avgs.size(); i++) {
            avgs[i] /= cnt[i];
        }
        return avgs;
    }
private:
    void dfs(TreeNode* node, vector<double>& avgs, vector<int>& cnt, int level) {
        if (level == cnt.size()) { 
            cnt.push_back(1);
        } else {
            cnt[level]++;
        }
        if (level == avgs.size()) {
            avgs.push_back((double)node->val);
        } else {
            avgs[level] += (double)node->val;
        }
        if (node->left) dfs(node->left, avgs, cnt, level+1);
        if (node->right) dfs(node->right, avgs, cnt, level+1);
        return;
    }
};